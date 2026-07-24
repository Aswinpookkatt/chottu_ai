from llm.client import chat
from prompts.prompt import SYSTEM_PROMPT 
from models.schemas import AgentResponse
from tools.terminal import run_command
from logger_util import get_logger

import json

logger = get_logger(__name__)

class AgentController:

    def __init__(self):

        self.messages = [
         {
             "role": "system",
             "content": SYSTEM_PROMPT
         }
        ]

    def add_message(self, role: str, content: str):
        self.messages.append(
         {
             "role": role,
             "content": content
         }
        )

    def process(self, user_input: str):

        self.add_message("user", user_input)
        

        response = chat(self.messages)
        logger.info(f"User Input: {self.messages}")
        data = AgentResponse.model_validate(
            json.loads(response)
        )

        return data