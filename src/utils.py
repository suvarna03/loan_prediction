import yaml
import sys
from loan_prediction.exception import  CustomException
from loan_prediction.logger import logger

def read_yaml(path_to_yaml):
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info(f"YAML file{path_to_yaml} Loaded Successfully!")
        return config
    except Exception as e:
        raise CustomException(e, sys)
