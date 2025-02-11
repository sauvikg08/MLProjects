# End to End Machine Learning Project
This project aims to predict students' math exam scores based on various features such as gender, race/ethnicity, parental level of education, lunch type, test preparation course and their performance in other subjects. Using machine learning algorithms, the goal is to build a predictive model that can estimate math scores from the scores of other subjects, such as reading and writing.

## Introduction
The objective of this project is to explore the relationship between student characteristics and their academic performance. By applying machine learning techniques, this project predicts student scores based on their demographic information and test preparation habits.

## Dataset
The dataset used in this project is from Kaggle's Students Performance in Exams dataset. The dataset consists of the following columns:

gender: Gender of the student.
race/ethnicity: A categorical variable representing the student's race or ethnicity.
parental level of education: The highest level of education attained by the student's parents.
lunch: The type of lunch the student receives (standard or free/reduced).
test preparation course: Whether or not the student completed a test preparation course.

## Project Workflow

### Exploratory Data Analysis (EDA)
* Inspect the dataset for missing values and outliers.
* Analyze the distribution of each feature and target variable.
* Visualize correlations between different variables.

### Data Preprocessing
* Handle missing data (if any).
* Encode categorical variables (e.g., one-hot encoding).
* Split the dataset into training and testing sets.

### Model Training
* Apply multiple machine learning models such as Linear Regression, Decision Trees, and Random Forest to predict student scores.
* Evaluate model performance using R² score.
* Apply hyperparameter tuning to find the best model based on R² score

### Model Evaluation
* Compare the performance of different models.
* Choose the best model based on accuracy and other metrics.