from loan_prediction.constants import(
    CONFIG_FILE_PATH,
    PARAMS_FILE_PATH,
    SCHEMA_FILE_PATH
)
from loan_prediction.utils import read_yaml
from loan_prediction.entity import DataIngestionConfig
def __init__(self):
    self.config = read_yaml(CONFIG_FILE_PATH)
    self.params = read_yaml(PARAMS_FILE_PATH)
    self.schema = read_yaml(SCHEMA_FILE_PATH)

def get_data_ingestion_config(self):

    config = self.config.data_ingestion

    data_ingestion_config = DataIngestionConfig(
        root_dir=Path(config.root_dir),
        source_URL=config.source_URL,
        local_data_file=Path(config.local_data_file),
        unzip_dir=Path(config.unzip_dir)
    )

    return data_ingestion_config