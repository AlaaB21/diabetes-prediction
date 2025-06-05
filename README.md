# diabetes-prediction
**1.0 | Introduction**
Diabetes is one of the most widespread chronic diseases in the United States, with profound health and economic impacts. The condition arises when the body cannot properly produce or use insulin, leading to elevated blood sugar levels. Early diagnosis is critical to managing diabetes effectively and preventing complications such as heart disease, kidney failure, and vision loss.

This project explores the development of a machine learning model that predicts the presence of diabetes using survey data from the CDC’s 2015 Behavioral Risk Factor Surveillance System (BRFSS). The model’s goal is to assist in early screening efforts, especially in populations at high risk.
**
1.1 | Problem Statement**
The objective of this project is to develop a predictive model that determines whether an individual has diabetes (binary outcome: 0 = no, 1 = yes) using survey responses collected in BRFSS 2015. The original dataset contains 330 features and 441,455 samples. Due to the dataset’s size and complexity, we focus on a curated subset of 21 relevant features strongly associated with diabetes, based on public health literature.

**The final model aims to:**

Predict diabetes risk from survey responses.

Identify key predictors among lifestyle and health indicators.

Support efficient screening and public health decision-making.

**1.2 | Dataset Description**
Dataset Origin:
Source: CDC BRFSS 2015 Dataset

Original size: ~330 features and over 400,000 samples.

Format: Structured CSV, with variables coded from raw survey questions.

Selected Version:
The dataset used for this analysis includes 21 variables most relevant to diabetes risk.

It is derived from the uncleaned full BRFSS data, filtered and cleaned using medical research and domain expertise.

Target Variable:
Diabetes_binary: 0 = no diabetes, 1 = prediabetes or diabetes.

Key Features:
HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income.

**2.0 | Data Cleaning**
Challenges Addressed:
Many features in the original BRFSS data required decoding and transformation.

We selected only the most relevant 21 features from the larger dataset.

Missing values were handled by:

Checking distributions.

Imputing medians or mode depending on variable type.

Encoded categorical variables where needed (e.g., age categories, education levels).

Verified and balanced class labels for binary classification.

**3.0 | Exploratory Data Analysis (EDA)**
**3.1 | Univariate Analysis:**
Histogram and boxplot of features like BMI, Age, MentHlth.

Categorical variable distributions via countplots (e.g., HighBP, Smoker, Sex).

**3.2 | Bivariate Analysis:**
Cross-tabulations and visual comparisons (e.g., diabetes by BMI level).

Correlation heatmap between all numerical predictors and target.

**3.3 | Key Observations:**
Higher BMI and high blood pressure are strongly associated with diabetes.

Age and education showed trends where older and less-educated individuals had higher diabetes rates.

Lifestyle features (smoking, physical activity, diet) showed expected directional relationships.
**
4.0 | Feature Engineering & Selection**
Feature Engineering:
Created a combined "Risk Score" by aggregating binary lifestyle risk indicators.

Encoded multi-class features (Age, Income, Education) using ordinal mapping.

Feature Selection Techniques:
Filter Method: Used Pearson correlation and chi-square tests.

Wrapper Method: Applied Recursive Feature Elimination (RFE).

Embedded Method: Feature importance from tree-based models.

Final Selected Features:
HighBP, HighChol, BMI, PhysActivity, Age, GenHlth, MentHlth, DiffWalk.

**5.0 | Modeling & Tuning**
Algorithms Used:
Logistic Regression – Baseline interpretable model.

Random Forest Classifier – Tree ensemble model.

XGBoost – Advanced boosting method for structured data.

**Tuning:**
GridSearchCV for hyperparameter optimization.

**Parameters tuned:**

Random Forest: n_estimators, max_depth, min_samples_split

XGBoost: learning_rate, max_depth, gamma, subsample

**6.0 | Evaluation & Validation**
Metrics:
Accuracy

Precision

Recall

F1-score

ROC-AUC Curve

Best Model:
XGBoost

Accuracy: 0.86

Precision: 0.78

Recall: 0.76

AUC: 0.89

Validation:
Stratified train-test split and cross-validation used to avoid data leakage and overfitting.
