import logging
import os
from pydantic import BaseModel, field_validator

# define log directory and file path.
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)
MACHINE_LOG_PATH = os.path.join(LOG_DIR, "machine.log")

# Create a dedicated logger for machine events
machine_logger = logging.getLogger("machine_logger")
machine_logger.setLevel(logging.INFO)

# Ensure no duplicate handlers are added
if not machine_logger.handlers:
    file_handler = logging.FileHandler(MACHINE_LOG_PATH)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    machine_logger.addHandler(file_handler)


# Machine class with validation and logging
class Machine(BaseModel):
    name: str
    os: str
    cpu: str
    ram: str

    # Validate OS (only Ubuntu or OS)
    @field_validator("os")
    def validate_os(cls, v):
        valid_os = ["Windows", "windows", "linux", "Linux"]
        if v not in valid_os:
            raise ValueError(f"OS must be one of: Windows/Linux")
        return v

    # RAM must end with "GB"
    @field_validator("ram")
    def validate_ram(cls, v):
        v = v.upper()
        if not v.endswith("GB"):
            raise ValueError("RAM must be in format like: 4GB / 8GB / 16GB")
        return v

    # CPU must be at least 3 chars
    @field_validator("cpu")
    def validate_cpu(cls, v):
        if len(v.strip()) < 3:
            raise ValueError("CPU model is too short.")
        return v

    # Convert machine to dictionary
    def to_dict(self):
        return self.model_dump()
    
        
    # Log creation event to machine log.
    def log_creation(self):
        machine_logger.info(f"Machine created: {self.name} | OS={self.os}, CPU={self.cpu}, RAM={self.ram}")
