from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    dataingestion = DataIngestionTrainingPipeline()
    dataingestion.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"Failed to execute {STAGE_NAME} due to error {e}")
    raise e

STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"Failed to execute {STAGE_NAME} due to error {e}")
    raise e

STAGE_NAME = "Model Training Stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"Failed to execute {STAGE_NAME} due to error {e}")
    raise e