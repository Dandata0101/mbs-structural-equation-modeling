import os
import pandas as pd
import numpy as np
import statsmodels.api as sm

def perform_regression_analysis(
    segment_results='Y',  # Set to 'Y' to segment results by a specific column
    segmentation_column='Generation',  # The column used for segmentation
    filter_column=None,  # The column used for filtering
    filter_values=None,  # List of values to exclude from the dataset
    pvalue_threshold=0.05,  # P-value threshold for significance
    y_column='Yvar_USE_AI_Work',  # Dependent variable
    x_column_prefix='VAR',  # Prefix for independent variables
    output_filename_template='Regression_Results_{segmentation_column}_Detailed.xlsx',  # Template for output filename
    excel_path=None,  # Define the path to your dataset
    summary_dir=None  # Define the path for saving the results
):
    # Set up directories if not provided
    current_directory = os.path.dirname(os.getcwd())
    if excel_path is None:
        excel_path = os.path.join(current_directory, '01-data', 'TAM_DEF.xlsx')
    if summary_dir is None:
        summary_dir = os.path.join(current_directory, '04-summary')

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

    # Apply filtering if filter_column and filter_values are set and the column exists
    if filter_column and filter_values:
        if filter_column in df.columns:
            df = df[~df[filter_column].isin(filter_values)]
            print(f"Filtered dataset to exclude {filter_values} in {filter_column}")
        else:
            print(f"Warning: {filter_column} column not found. No filtering applied.")

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
        X = df_segment.filter(regex=f'^{x_column_prefix}')
        y = df_segment[y_column]
        
        # Add a constant (intercept) to the model
        X = sm.add_constant(X)

        # Fit the OLS model
        model = sm.OLS(y, X).fit()

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

# Example usage:
# perform_regression_analysis()
