from pydantic import BaseModel

class AgentResponse(BaseModel):

    action : str
    command : str | None = None
    reason : str | None = None
    response : str | None = None