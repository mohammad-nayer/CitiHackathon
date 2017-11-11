import json
import regression
import pandas as pd

# Train the model on the training data
model = regression.generateModel('training_data')

# Load the applicant's info
with open('test_data') as data_file:
    json_data = json.load(data_file)["applicants"]
original_data = pd.DataFrame(json_data)

# Format the data for the model
pd_data = original_data.drop('id', 1)
pd_data = pd.get_dummies(pd_data)
pd_data = pd_data.drop("degree_Literature", 1)
pd_data = pd_data.drop("university_University of Nowhere", 1)

# Calculate the scores
academic_scores = model.predict(pd_data)

# Place the scores in the original data
pd_scores = pd.Series(academic_scores)
original_data['academic_score'] = pd_scores.values

# Show
print(original_data)
