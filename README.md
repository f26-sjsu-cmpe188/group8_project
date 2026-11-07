# Obesity Risk Level Prediction

## Project Overview

This project uses machine-learning methods to predict obesity risk levels based on a person's health, eating habits, physical activity, and lifestyle information.

The project includes:

- Data exploration
- Data cleaning and preprocessing
- Feature encoding and scaling
- Training multiple machine-learning models
- Model comparison
- Model evaluation
- Final written report
- Final presentation

## Dataset

The dataset used in this project is:

```text
11_obesity_risk_levels_train.csv
```

The dataset contains 1,794 rows and 17 columns. The target column is:

```text
NObeyesdad
```

The target contains seven obesity-risk categories:

- `Insufficient_Weight`
- `Normal_Weight`
- `Overweight_Level_I`
- `Overweight_Level_II`
- `Obesity_Type_I`
- `Obesity_Type_II`
- `Obesity_Type_III`

The dataset includes information about:

- Gender
- Age
- Height
- Weight
- Family history of overweight
- Food consumption habits
- Water consumption
- Physical activity
- Technology use
- Transportation habits

## Team Members

| Team Member | Responsibility |
|---|---|
| Thien Doan | Machine Learning |
| Jonathan Estudillo | Data Processing |
| Isa Pudiyapura | Project Management |

## Project Responsibilities

### Data Processing

The data-processing portion of the project includes:

- Loading and inspecting the dataset
- Checking the data types
- Checking for missing values
- Checking for duplicate rows
- Separating features and target labels
- Splitting the data into training and testing sets
- Using stratified splitting to preserve class proportions
- Encoding categorical features
- Scaling numerical features when appropriate
- Preventing data leakage by fitting preprocessing only on training data

### Machine Learning

Multiple machine-learning models will be trained and compared. Possible models include:

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors
- Support Vector Machine

The best model will be selected based on its performance and suitability for the project.

### Model Evaluation

The models may be evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Cross-validation

The final evaluation methods will be updated according to the professor's project requirements.

## Repository Structure

```text
group8_project/
│
├── data/
│   └── 11_obesity_risk_levels_train.csv
│
├── notebooks/
│   ├── 01_data_exploration_preprocessing.ipynb
│   ├── 02_model_training_comparison.ipynb
│   └── 03_model_evaluation_tuning.ipynb
│
├── report/
│   └── final_report.pdf
│
├── presentation/
│   └── final_presentation.pptx
│
├── README.md
└── .gitignore
```

## Installation

Install the required Python libraries:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/f26-sjsu-cmpe188/group8_project.git
```

2. Open the project directory:

```bash
cd group8_project
```

3. Start Jupyter Notebook:

```bash
jupyter notebook
```

4. Open the notebooks in the `notebooks` folder.

5. Run the notebooks in the following order:

```text
01_data_exploration_preprocessing.ipynb
02_model_training_comparison.ipynb
03_model_evaluation_tuning.ipynb
```

## Data-Processing Principles

To prevent data leakage:

- The dataset will be split before fitting preprocessing steps.
- Imputers, scalers, and encoders will be fitted using training data only.
- The same fitted preprocessing steps will be applied to the test data.
- The test set will be used only for final evaluation.
- Categorical features will be encoded consistently across training and testing data.

## Project Deliverables

The final submission will include:

- Data-processing notebook
- Machine-learning notebook
- Model comparison and evaluation
- Final written report
- Final presentation

## Project Requirements

The official project requirements and grading rubric have not been provided yet. This section will be updated when the professor releases the final instructions.

## Project Status

The project is currently in the initial setup and data-processing stage.

Future milestones include:

1. Complete data exploration and preprocessing
2. Train multiple machine-learning models
3. Compare model performance
4. Tune the best-performing model
5. Complete the final report
6. Prepare the presentation
7. Review and submit the final project
