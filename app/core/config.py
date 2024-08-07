from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "CashCam"
    PROJECT_VERSION: str = "1.0.0"
    OBJECT_DETECTION_MODEL: str = "models/bill_coin_yolo_best.pt"
    CLASSIFICATION_MODEL: str = "models/class_YOLO_model_best.pt"
    API_PREFIX: str = "/api"
    TEST_OUTPUT_PATH: str = "tests/test_output.txt"
    PORT: int = 8000
    LOCAL_IP: str = "0.0.0.0"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()