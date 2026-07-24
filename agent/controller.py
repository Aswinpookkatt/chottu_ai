from llm.client import chat
from prompts.prompt import SYSTEM_PROMPT 
from models.schemas import AgentResponse
from tools.terminal import run_command

import json

class AgentController:

    def process(self, user_input: str):

        messages = [
         {
             "role": "system",
             "content": SYSTEM_PROMPT
         },
         {
             "role": "user",
             "content": user_input
         }
        ]

        response = chat(messages)

        data = AgentResponse.model_validate(
            json.loads(response)
        )

        return data