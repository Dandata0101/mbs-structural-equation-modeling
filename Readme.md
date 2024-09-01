
# AI Ethics & Innovation: Data Analysis, Models, and Datasets

## Overview

This repository contains all the scripts, models, and datasets used in the research project titled **"The Balance Between AI Ethics & Innovation"**. The primary objective of this project is to explore the relationship between AI ethics and innovation within the public sector, providing a framework to understand and address the concerns of employees and consumers while fostering ethical AI adoption.

## Repository Structure

The repository is organized into the following directories:

- **`/01-data/`**: Contains the datasets used for analysis. The data has been preprocessed and segmented to align with the research objectives.
- **`/02-Charts/`**: Contains visual representations of the data analysis, including charts and graphs that illustrate key findings and trends.
- **`/03-notebooks/`**: Jupyter notebooks that provide a step-by-step walkthrough of the analyses conducted.
- **`/04-summary/`**: Output files such as regression analysis results, figures, and tables used in the final report.

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

## Usage

To replicate the analysis or explore the models, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Dandata0101/mbs-structural-equation-modeling
   cd mbs-structural-equation-modeling
   ```

2. **Environment Setup**:
   - Ensure you have Python 3.x installed along with the required libraries listed in `requirements.txt`.
   - Install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```

3. **Exploring the Notebooks**:
   - Open any notebook in the `/03-notebook/` directory using Jupyter Lab or Jupyter Notebook to see the detailed analysis.
   - Example:
     ```bash
     jupyter notebook model.ipynb
     ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or further information, please contact:

**Dan Ramirez**  
Email: [d.ramirez-jr@gmontpellier-bs.com](mailto:d.ramirez-jr@gmontpellier-bs.com)  
MSc Big Data Science & AI
