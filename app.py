import os
from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
import datetime

application=Flask(__name__)

app=application

## Route for a home page


def update_csv(data_dict, file_path):
    # Convert the dictionary to a DataFrame
    df_new = pd.DataFrame(data_dict)

    # Read the existing CSV file
    df_old = pd.read_csv(file_path)

    # Append the new data to the old DataFrame
    df_updated = pd.concat([df_old, df_new], ignore_index=True)

    # Write the updated DataFrame back to the CSV file
    df_updated.to_csv(file_path, index=False)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            yom=request.form.get('yom'),
            milage=request.form.get('milage'),
            strock=request.form.get('strock'),
            light_type=request.form.get('light_type'),

        )

        # expected_value=request.form.get('expected')
    
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print(results)

        # net_facillity=float(expected_value)
        # charges=0
        # internal_valuation=float(results[0])

        # try:
        #     exposhor_value=((net_facillity+charges)/internal_valuation)*100
        # except Exception as e:
        #     print("error in calculating exposhor")

        # print(exposhor_value)
        print("after Prediction")

        # custom_data_input_dict = {
        #         "yom": [data.yom],
        #         "mileage": [data.mileage],
        #         "stroke_values": [data.strock],
        #         "Light_Type": [data.light_type] ,
        #         "Customer_Expectation": [net_facillity] ,
        #         "Charges": [charges] ,
        #         "AI_Calculated": [internal_valuation] ,
        #         "Exposhior": [exposhor_value]      
        #     }
        # print(custom_data_input_dict)

        # csv_path=os.path.join('artifacts',"ModelTesting.csv")

        # update_csv(custom_data_input_dict, csv_path)
        
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    # app.run(host="0.0.0.0",port=5000)  
    app.run(port=5000,debug=True)       

