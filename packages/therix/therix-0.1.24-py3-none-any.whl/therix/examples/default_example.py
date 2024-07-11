from therix.core.agent import Agent
from therix.core.inference_models import (
    GroqLlama370b
)
import sys
from therix.core.trace import Trace
from therix.core.system_prompt_config import SystemPromptConfig
from pydantic import BaseModel, Field
from typing import List
from therix.core.output_parser import OutputParserWrapper



GROQ_API_KEY=''

variables = {
    "name": "Abhishek Dubey",
}

agent = Agent(name="New bot")
(
        agent.add(GroqLlama370b(config={"groq_api_key": GROQ_API_KEY}))
        .add(SystemPromptConfig(config={"system_prompt" : "ragprompt","variables" : variables}))
       .save()
    )


print(agent.id)

ans = agent.invoke(question="What is the difference between eating an apple and eating a cake?")
print(ans)