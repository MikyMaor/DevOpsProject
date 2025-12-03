import logging
from pydantic import BaseModel, field_validator

# Configure logging
logging.basicConfig(
    filename="logs/machine.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# log creation event to provisioning log.
def log_creation(self):
    logging.info(f"Machine created: {self.name} | OS={self.os}, CPU={self.cpu}, RAM={self.ram}")


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
            raise ValueError(f"OS must be one of: {valid_os}")
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
        logging.info(f"Machine created: {self.name} ({self.os}, {self.cpu}, {self.ram})")
        
    # log creation event to provisioning log.
    def log_creation(self):
        logging.info(f"Machine created: {self.name} | OS={self.os}, CPU={self.cpu}, RAM={self.ram}")
