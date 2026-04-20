import os
from src.datascience import logger
import pandas as pd
from src.datascience.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config
    
    def validate_all_columns(self) ->bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status=False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status=True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_status}")
        except Exception as e:
            raise e
    
    def validate_datatypes(self) ->bool:
        try:
            validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir)
            schema= self.config.all_schema

            for col,expected_dtype in schema.items():
                if col in data.columns:
                    actual_dtype= str(data[col].dtype)

                    if actual_dtype != expected_dtype:
                        print(f"Data Type mismatch in {col}: expected {expected_dtype}")
                        validation_status = False
                        with open(self.config.STATUS_FILE,'w') as f:
                            f.write(f"Validation status for datatypes: {validation_status}")
                            break
                else:
                    validation_status=False 
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status for datatypes: {validation_status}")
                    break
        except Exception as e:
            raise e
