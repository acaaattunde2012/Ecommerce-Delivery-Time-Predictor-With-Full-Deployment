import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            preprocessor_path = 'artifacts/proprocessor.pkl'
            model_path = 'artifacts/model.pkl'
            preprocessor = load_object(file_path=preprocessor_path)
            model = load_object(file_path=model_path)
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e:
            logging.info('Exception occured in prediction pipeline')
            raise CustomException(e,sys)
        

class CustomData:
    def __init__(self,
                 Delivery_person_Age:float,
                 Delivery_person_Ratings:float,
                 Restaurant_latitude:float,
                 Restaurant_longitude:float,
                 Delivery_location_latitude:float,
                 Delivery_location_longitude:float,
                 Weather_conditions:str,
                 Road_traffic_density:str,
                 Vehicle_condition:int,
                 Type_of_order:str,
                 Type_of_vehicle:str,
                 multiple_deliveries:int,
                 Festival:str,
                 City:str,
                 Order_day:int,
                 Order_month:int,
                 Order_hour:float,
                 Order_min:float,
                 Hour_order_pk:float,
                 Min_order_pk:float
                 ):
                 self.Delivery_person_Age=Delivery_person_Age
                 self.Delivery_person_Ratings=Delivery_person_Ratings
                 self.Restaurant_latitude=Restaurant_latitude
                 self.Restaurant_longitude=Restaurant_longitude
                 self.Delivery_location_latitude=Delivery_location_latitude
                 self.Delivery_location_longitude=Delivery_location_longitude
                 self.Weather_conditions=Weather_conditions
                 self.Road_traffic_density=Road_traffic_density
                 self.Vehicle_condition=Vehicle_condition
                 self.Type_of_order=Type_of_order
                 self.Type_of_vehicle=Type_of_vehicle
                 self.multiple_deliveries=multiple_deliveries
                 self.Festival=Festival
                 self.City=City
                 self.Order_day=Order_day
                 self.Order_month=Order_month
                 self.Order_hour=Order_hour
                 self.Order_min=Order_min
                 self.Hour_order_pk=Hour_order_pk
                 self.Min_order_pk=Min_order_pk
       
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "Delivery_person_Age":[self.Delivery_person_Age],
                "Delivery_person_Ratings":[self.Delivery_person_Ratings],
                "Restaurant_latitude":[self.Restaurant_latitude],
                "Restaurant_longitude":[self.Restaurant_longitude],
                "Delivery_location_latitude":[self.Delivery_location_latitude],
                "Delivery_location_longitude":[self.Delivery_location_longitude],
                "Weather_conditions":[self.Weather_conditions],
                "Road_traffic_density":[self.Road_traffic_density],
                "Vehicle_condition":[self.Vehicle_condition],
                "Type_of_order":[self.Type_of_order],
                "Type_of_vehicle":[self.Type_of_vehicle],
                "multiple_deliveries":[self.multiple_deliveries],
                "Festival":[self.Festival],
                "City":[self.City],
                "Order_day":[self.Order_day],
                "Order_month":[self.Order_month],
                "Order_hour":[self.Order_hour],
                "Order_min":[self.Order_min],
                "Hour_order_pk":[self.Hour_order_pk],
                "Min_order_pk":[self.Min_order_pk]
                }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)
            
