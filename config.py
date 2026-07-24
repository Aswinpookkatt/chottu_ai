from pydantic import BaseModel

class Settings(BaseModel):
    base_url : str = "http://localhost:11434/v1"
    api_key : str = "ollama"
    model : str = "qwen3:8b"


settings = Settings()