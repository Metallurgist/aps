import os,sys
import pandas as pandas
from sklearn import train_test_split
from sensor import utils
from sensor.entity import config_entity
from sensor.entity import artifact_entity
from sensor.exception import SensorException
from sensor.logger import logging


class DataIngestion:
    def __init__(self,data_ingestion_config:config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise SensorException(e,sys)
    
    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            df:pd.DataFrame=utils.get_collection_as_dataframe(database_name, collection_name)
        except Exception as e:
            raise SensorException(error_message=e, error_detail=sys)