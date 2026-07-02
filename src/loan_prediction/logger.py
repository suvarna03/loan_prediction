import logging
from datetime import datetime
from loan_prediction.constants import ROOT_PATH

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y')}.log"
logs_path = ROOT_PATH/ "logs"
logs_path.mkdir(parents=True, exist_ok=True)

LOG_FILE_PATH = logs_path / LOG_FILE

logging.basicConfig(filename= LOG_FILE_PATH,
                    format= "%(asctime)s | %(levelname)s | %(filename)s | %(message)s",
                    filemode= "a",
                    level=logging.INFO)

logger = logging.getLogger(__name__)