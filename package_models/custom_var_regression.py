import os
import pandas as pd
import numpy as np
import statsmodels.api as sm

def custx_regression_analysis(segment_results='Y', segmentation_column='Generation', filter_column=None,
                              filter_values=None, pvalue_threshold=0.1, y_column='Yvar_USE_AI_Work',
                              x_column_prefixes=None, output_filename_template='Regression_Results_{segmentation_column}_Detailed.xlsx'):

    if x_column_prefixes is None:
        x_column_prefixes = ['VAR']
    
    # Define the path to your dataset
    current_directory = os.path.dirname(os.getcwd())
    excel_path = os.path.join(current_directory, '01-data', 'TAM_DEF.xlsx')
    summary_dir = os.path.join(current_directory, '04-summary')

    # Print paths for debugging
    print(f"Excel file path: {excel_path}")
    print(f"Summary directory: {summary_dir}")

    # Ensure the summary directory exists
    if not os.path.exists(summary_dir):
        os.makedirs(summary_dir)

    # Load the dataset
    try:
        df = pd.read_excel(excel_path)
        print("Dataset loaded successfully.")
    except FileNotFoundError:
        print(f"File not found. Please check the file path: {excel_path}")
        return
    except Exception as e:
        print(f"Error during dataset loading: {e}")
        return

    # Print columns for debugging
    print(f"Columns in the dataset: {df.columns.tolist()}")

    # Check if the filter_column exists
    if filter_column and filter_column not in df.columns:
        print(f"Filter column '{filter_column}' not found in the dataset.")
        return

    # Apply filtering if filter_column and filter_values are set
    if filter_column and filter_values:
        df = df[~df[filter_column].isin(filter_values)]
        print(f"Filtered dataset to exclude {filter_values} in {filter_column}")

    # Check if the segmentation_column exists
    if segmentation_column not in df.columns:
        print(f"Segmentation column '{segmentation_column}' not found in the dataset.")
        return

    if segment_results == 'Y':
        # Get unique values in the segmentation column
        segments = df[segmentation_column].unique()
        print(f"Found {segmentation_column} segments: {segments}")
    else:
        # If not segmenting, treat the entire dataset as a single segment
        segments = ['Entire Dataset']
        df['Entire Dataset'] = 'Entire Dataset'  # Add a dummy column to facilitate the loop

    # Loop through each segment and run the regression model
    all_results = []
    top_variables_set = set()

    for segment in segments:
        df_segment = df[df[segmentation_column] == segment] if segment != 'Entire Dataset' else df
        
        # Define X (independent variables) and y (dependent variable)
        X = pd.concat([df_segment.filter(regex=f'^{prefix}') for prefix in x_column_prefixes], axis=1)
        y = df_segment[y_column]
        
        # Check if there are any independent variables left after filtering
        if X.empty:
            print(f"No variables found for the prefixes {x_column_prefixes} in segment {segment}. Skipping this segment.")
            continue
        
        # Add a constant (intercept) to the model
        X = sm.add_constant(X)

        # Fit the OLS model
        try:
            model = sm.OLS(y, X).fit()
        except Exception as e:
            print(f"Error fitting the model for segment {segment}: {e}")
            continue

        # Extract the results, filtering by p-value threshold
        significant_results = model.summary2().tables[1]
        significant_results = significant_results[significant_results['P>|t|'] <= pvalue_threshold]
        
        # Exclude the constant from the top variables set
        top_variables_set.update(var for var in significant_results.index.tolist() if var != 'const')
        
        # Append results to the list for later export
        segment_results = significant_results.reset_index()
        segment_results.insert(0, 'Segment', segment)
        segment_results.insert(1, 'R2 Value', model.rsquared)
        all_results.append(segment_results)

    if not all_results:
        print("No significant results found. No output will be generated.")
        return

    # Combine the results from all segments into a DataFrame
    all_results_df = pd.concat(all_results)

    # Run overall regression with combined top variables
    combined_X = df[list(top_variables_set)]
    combined_X = sm.add_constant(combined_X)
    combined_model = sm.OLS(df[y_column], combined_X).fit()

    # Prepare overall model results for export
    overall_results = combined_model.summary2().tables[1].reset_index()
    overall_results.insert(0, 'Segment', 'Overall')
    overall_results.insert(1, 'R2 Value', combined_model.rsquared)

    # Save the results to Excel, including the segmentation column name in the filename
    output_filename = output_filename_template.format(segmentation_column=segmentation_column)
    output_path = os.path.join(summary_dir, output_filename)

    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        # Write the overall hypothesis results
        all_results_df.to_excel(writer, sheet_name='Hypothesis Results', index=False)
        
        # Write the overall regression results
        overall_results.to_excel(writer, sheet_name='Overall Regression', index=False)

        # Apply formatting
        workbook = writer.book
        header_format = workbook.add_format({
            'bold': True, 'text_wrap': True, 'align': 'center', 'valign': 'center', 'bg_color': '#D9EAD3'
        })
        for sheet_name in writer.sheets:
            worksheet = writer.sheets[sheet_name]
            worksheet.set_row(0, None, header_format)
            worksheet.set_column('A:G', 20)  # Adjust column width for better readability

    print(f"Summary statistics and regression results saved to {output_path}.")
