import json
import pandas as pd
import requests
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression


def fetchData():
    print("fetching data..")
    r = requests.get('http://10.29.10.31:3997/uni/all')
    print("success!")
    for thisUni in r.json():
        print(thisUni["id"])
        print(thisUni["degree"])
        print(thisUni["grade"])
        print(thisUni["university"])


def generateModel(data_path):

    features = ['academic score','degree', 'grade', 'university']
    # Import the data
    with open(data_path) as data_file:
        json_data = json.load(data_file)["applicants"]
    original_data = pd.DataFrame(json_data)
    original_data = original_data[features]

    # Format the data (dummy the categorical variables - avoiding the dummy trap)
    pd_data = pd.get_dummies(original_data)
    pd_data = pd_data.drop("degree_Literature", 1)
    pd_data = pd_data.drop("university_University of Nowhere", 1)

    # Split the data into independent and dependent variables
    x = pd_data.iloc[:, 1:].values
    y = pd_data.iloc[:, 0].values

    # Train/test split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0)

    # Fitting Multiple Linear Regression to the Training set
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    # Predicting the Test set results
    #y_pred = regressor.predict(x_test)

    #print(y_test)
    #print(y_pred)

    return regressor


if __name__ == "__main__":

    #generateModel('training_data')
    fetchData()