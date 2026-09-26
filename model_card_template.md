# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Brigina Coleman created this model. September 2026. Model Version 1.0.0. It is a RandomForest Classified model developed using the Scikit-learn library, implemented as part of the Udacity Machine Learning DevOps course that references tthe UCI Cencus Income Dataset.
## Intended Use
This model was designed for educational purposes and should be used to predict whether an individual's salary is above $50,000 per year based on demographic and employment attributes. The intended users are Machine learning engineers, business analytics teams or data science evaluators.
## Training Data
UCI Census Income Dataset. 80% of the data was used to train the model. For reproducible train-test splits, random_state=42 was used. OneHotEncoder used for categorical variables and LabelBinarizer used for the target variable.
## Evaluation Data
The remaining 20% test set withheld during model training was used to evaluate the data. Slice-level evaluation was conducted on categorical features to access model fairness across subgroups.
## Metrics
The below metrics were obtained from the evaluation data:

- Precision: 0.74
- Recall: 0.64
- F1 Score: 0.69
## Ethical Considerations
The dataset reflects socioeconomic disparities across gender, race, and native country. Slice evaluations were performed to inspect model performance across demographics to ensure the model does not exhibit disproportionate error rates for specific groups.
## Caveats and Recommendations
The census data was collected in 1994, so income thresholds and socioeconomic features may not accurately reflect modern income distributions. I recommend that the model be recalibrated or retrained with updated census data prior to deploying to any real world application.