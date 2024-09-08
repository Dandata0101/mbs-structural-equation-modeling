
# AI Ethics & Innovation: Data Analysis, Models, and Datasets

## Overview

This repository contains all the scripts, models, and datasets used in the research project titled **"The Balance Between AI Ethics & Innovation"**. The primary objective of this project is to explore the dynamic relationship between **AI ethics** and **innovation** within both the public and private sectors. It aims to provide a comprehensive framework to understand and address the concerns of **employees** and **consumers** while fostering the ethical adoption of AI technologies. 

The project specifically delves into how factors like **explainability**, **fairness**, **ethical AI development**, **training accessibility**, and **personalization** influence the trust and acceptance of AI across different generations. By examining these elements, the research offers insights into critical concerns such as **privacy**, **transparency**, and **bias reduction**, all of which play a pivotal role in the ethical integration of AI technologies into various industries.

### Key Findings:

- **Explainability and Fairness as Drivers of Trust**: The study found that **explainability** and **fairness** are major contributors to building trust, especially among **Generation X** and **Millennials**. These groups demand clarity in AI decision-making processes and expect AI systems to operate without bias, aligning with their broader ethical and social values.

- **Ethical AI Development**: The research highlights the importance of ethical AI development, particularly for **Boomers**, who place a high priority on AI systems being designed and used responsibly. While younger generations also value ethical AI, they tend to see it as a baseline expectation rather than a trust-building factor.

- **Training Accessibility and Career Growth**: Surprisingly, the availability of AI training and career growth opportunities had a minimal impact on influencing trust across all generations. While training remains important for skill development, it was not a decisive factor in driving AI adoption or increasing trust in AI technologies.

- **AI-Driven Personalization**: Although AI-driven personalization is appreciated by users, it was found not to be a significant factor in enhancing trust or AI adoption. This suggests that while personalization can improve user experiences, it is not sufficient on its own to drive widespread acceptance of AI.

These findings underscore the need for a multi-faceted approach to AI integration, one that prioritizes **transparency**, **fairness**, and **ethical considerations** while recognizing the diverse expectations and concerns of different generational groups.

## Repository Structure

The repository is organized into the following directories:

- **`/01-data/`**: Contains the datasets used for analysis. The data has been preprocessed and segmented to align with the research objectives.
- **`/02-Charts/`**: Contains visual representations of the data analysis, including charts and graphs that illustrate key findings and trends.
- **`/03-notebooks/`**: Jupyter notebooks that provide a step-by-step walkthrough of the analyses conducted.
- **`/04-summary/`**: Output files such as regression analysis results, figures, and tables used in the final report.
- **`/05-model-images/`**: Contains images of the models used, including regression and SEM models.
- **`/package_models/`**: This directory contains custom Python modules used in the analysis. These modules are imported into the notebooks for various data processing and model evaluation tasks.

## Datasets

The datasets used in this study are located in the `/01-data/` directory. Each dataset is accompanied by a README file that provides details on the data sources, preprocessing steps, and any transformations applied. These datasets are anonymized and comply with ethical guidelines for data usage.

### TAM_DEF.xlsx Dataset Overview

The dataset `TAM_DEF.xlsx` contains 870 responses from a survey aimed at assessing attitudes towards AI training, career growth opportunities, explainability, fairness, ethical considerations, and AI-driven personalization. Key variables include:

- **ResponseId:** Unique identifier for each survey respondent.
- **Wave:** Indicates the round of the survey, categorized into three distinct waves.
- **Region and Country:** Geographic information about the respondents, covering regions like North America and various countries, with the US being the most represented.
- **Generation:** Demographic segmentation, including groups such as Millennials, Gen X, etc.
- **CS_experience_rollup:** Experience level with customer service roles, categorized into "No Experience," "Some Experience," and "Extensive Experience."
- **Roles:** Job roles of respondents, categorized broadly into "Tech" and "Non-Tech" roles.
- **VAR01_CG_Training to VAR30_SAFETY_AI_protect_Cyber_Threats:** Columns representing various survey questions related to AI training, opportunities, accessibility, fairness, ethics, privacy, and safety.
- **Yvar_USE_AI_Work and Yvar_USE_AI_Personal:** Dependent variables representing the extent of AI use in work and personal contexts.
- **Yvar_Work_Personal, Yvar_TopBox_Work, Yvar_Topbox_personal:** Variables representing the combined use of AI in both personal and professional contexts and top-box scores indicating the highest level of agreement or satisfaction.

**Summary Statistics:**
- **Wave Distribution:** The majority of responses were collected in "Wave 1."
- **Regional Distribution:** The dataset has strong representation from North America, with the United States being the most common country of respondents.
- **Generational Insights:** Millennials represent the largest demographic group.
- **Customer Service Experience:** A significant portion of respondents reported having no experience in customer service roles.
- **AI Usage:** The dependent variables show moderate AI usage in both personal and work-related contexts, with a mean score around 3.5 on a 5-point scale.

This dataset provides a robust foundation for analyzing how different demographic factors and perceptions influence the adoption and usage of AI technologies.

## Models

The `Models.ipynb` notebook in this repository contains the key models used for analysis in this study. These models include:

### 1. Exploratory Regression Models

The exploratory regression models test different sets of independent variables (`X` variables) against the dependent variable (`Y` variable), which represents AI usage in different contexts. The general form of the regression model is:

![Regression Model](https://github.com/Dandata0101/mbs-structural-equation-modeling/blob/main/05-model-images/regression_model.png)

### 2. Structural Equation Models (SEM)

**Trust:**

![SEM Trust](https://github.com/Dandata0101/mbs-structural-equation-modeling/blob/main/05-model-images/sem_trust.png)

**Ease of Use:**

![SEM Ease of Use](https://github.com/Dandata0101/mbs-structural-equation-modeling/blob/main/05-model-images/sem_ease_of_use.png)

**Training:**

![SEM Training](https://github.com/Dandata0101/mbs-structural-equation-modeling/blob/main/05-model-images/sem_training.png)

**Ethics:**

![SEM Ethics](https://github.com/Dandata0101/mbs-structural-equation-modeling/blob/main/05-model-images/sem_ethics.png)

**Direct Relationships with AI Usage:**

![SEM Usage](https://github.com/Dandata0101/mbs-structural-equation-modeling/blob/main/05-model-images/sem_usage.png)

**Relationships Among Latent Variables:**

![SEM Trust Relationships](https://github.com/Dandata0101/mbs-structural-equation-modeling/blob/main/05-model-images/sem_trust_relationships.png)

### 3. Hypothesis Testing

The hypothesis testing in the notebook is based on the results from the SEM and regression models. It tests specific hypotheses related to the influence of AI training, fairness, ethics, and personalization on AI adoption and user trust.

### Exploring the Models

To explore the models used in the analysis:

1. **Open the Notebook:**
   - Navigate to the `/03-notebooks/` directory and open `Models.ipynb` using Jupyter Lab or Jupyter Notebook.
   - Example:
     ```bash
     jupyter notebook Models.ipynb
     ```

2. **Run the Cells:**
   - Follow the cells in the notebook to execute the models and view the results.
   - Each section of the notebook corresponds to a specific model or hypothesis being tested.

### Custom Python Modules

The `/package_models/` directory contains additional modules for more specialized regression and SEM analysis:

1. **`custom_var_regression.py`**: 
   - Enables customized regression analysis with flexible filtering, segmentation, and independent variable selection.
   - Example function:
     ```python
     custx_regression_analysis(segment_results='Y', segmentation_column='Generation', filter_column=None, pvalue_threshold=0.1)
     ```

2. **`regression_by_segment.py`**: 
   - Focuses on segmented regression analysis, producing outputs filtered by generation or any other chosen segmentation column.
   - Example function:
     ```python
     perform_regression_analysis(segment_results='Y', segmentation_column='Generation', y_column='Yvar_USE_AI_Work', pvalue_threshold=0.05)
     ```

3. **`sem_fx.py`**: 
   - Executes SEM modeling, tailored to include custom hypotheses and data segmentation, and generates visual representations of SEM pathways.
   - Example function:
     ```python
     sem_analysis(model_desc, hypothesis_criteria, dependent_variable='Yvar_USE_AI_Work', segmentation_column='Generation', p_value_threshold=0.05)
     ```

## Setup Instructions

### Cloning the Repository

To replicate the analysis or explore the models, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Dandata0101/mbs-structural-equation-modeling
   cd mbs-structural-equation-modeling
   ```

### Environment Setup

1. **Install Dependencies**:
   - Ensure you have Python 3.x installed along with the required libraries listed in `requirements.txt`.
   - Install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```

### Setting Up `package_models`

If you need to use the custom Python modules located in the `package_models` directory, follow these steps to set it up:

1. **Navigate to the Project Directory**:
   - Make sure you're in the root directory of the project.
   
2. **Install the `package_models` Module**:
   - Run the following command to install the module in editable mode:
     ```bash
     pip install -e .
     ```
   - This will make the `package_models` directory available as a Python package, allowing you to import its modules from anywhere in the project.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or further information, please contact:

**Dan Ramirez**  
Email: [d.ramirez-jr@gmontpellier-bs.com](mailto:d.ramirez-jr@gmontpellier-bs.com)  
MSc Big Data Science & AI
