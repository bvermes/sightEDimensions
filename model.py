import numpy as np
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

dtc_model = DecisionTreeClassifier(random_state=0)

def create_model(dimensions_db):
    if(len(dimensions_db) != 0):
        df = pd.DataFrame(dimensions_db, columns = ['index','x','y','z','t','value'] )
        df.drop('index', axis = 'columns', inplace=True)
        X = df.loc[:,[
                  'x','y','z','t',
                  ]]
        y = df.loc[:,['value']]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        dtc_model.fit(X_train.values,y_train)
        print(f"Model is loaded. Accuracy: {dtc_model.score(X_test, y_test)*100}%")
    else:
        print("Model coudn't be trained. No data in database")


def make_prediction():
    x = int(input("What column do you want x axis to be?"))
    y = int(input("What column do you want y axis to be?"))
    z = int(input("What column do you want z axis to be?"))
    t = int(input("What column do you want t axis to be?"))
    data = np.array([x,y,z,t]).reshape(1, -1)
    print(f"The Models prediction for the value is {dtc_model.predict(data)[0]}")
