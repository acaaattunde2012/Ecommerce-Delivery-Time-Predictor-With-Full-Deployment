from flask import Flask, request, render_template,jsonify
from flask_cors import CORS,cross_origin
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import pandas as pd

application = Flask(__name__)

app = application

@app.route('/')
@cross_origin()
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        Order_date = request.form['Order_date']
        Order_time= request.form['Order_time']
        Time_order_picked = request.form['Time_order_picked']

        data = CustomData(
            Delivery_person_Age = float(request.form.get('Delivery_person_Age')),
            Delivery_person_Ratings = float(request.form.get('Delivery_person_Ratings')),
            Restaurant_latitude = float(request.form.get('Restaurant_latitude')),
            Restaurant_longitude = float(request.form.get('Restaurant_longitude')),
            Delivery_location_latitude = float(request.form.get('Delivery_location_latitude')),
            Delivery_location_longitude = float(request.form.get('Delivery_location_longitude')),
            Weather_conditions = request.form.get('Weather_conditions'),
            Road_traffic_density= request.form.get('Road_traffic_density'),
            Vehicle_condition = request.form.get('Vehicle_condition'),
            Type_of_order = request.form.get('Type_of_order'),
            Type_of_vehicle = request.form.get('Type_of_vehicle'),
            multiple_deliveries = request.form.get('multiple_deliveries'),
            Festival= request.form.get('Festival'),
            City = request.form.get('City'),
            Order_month = int(pd.to_datetime(Order_date,format="%Y-%m-%dT%H:%M").month),
            Order_day = int(pd.to_datetime(Order_date,format="%Y-%m-%dT%H:%M").day),
            Order_hour= int(pd.to_datetime(Order_time,format="%Y-%m-%dT%H:%M").hour),
            Order_min = int(pd.to_datetime(Order_time,format="%Y-%m-%dT%H:%M").minute),
            Hour_order_pk = int(pd.to_datetime(Time_order_picked,format="%Y-%m-%dT%H:%M").hour),
            Min_order_pk = int(pd.to_datetime(Time_order_picked,format="%Y-%m-%dT%H:%M").minute)
        )

        pred_df = data.get_data_as_dataframe()
        
        print(pred_df)

        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(pred_df)
        results = round(pred[0],2)
        return render_template('result.html',results=results,pred_df = pred_df)
    


if __name__ == '__main__':
    app.run(debug=True)