from pydantic import BaseModel
from enum import Enum

# Architecture. input, output, cache_read, cache_write / M

class LLM(Enum):
    sonnett_46 = {"input": 3.0, "output": 15.0, "cache_read": 0.3, "cache_write": 3.75}
    haiku_45 = {"input": 1.0, "output": 5.0, "cache_read": 0.10, "cache_write": 1.25}

class TokenModel(BaseModel):
    t_in: int
    t_out: int
    t_c_read: int
    t_c_write: int

def calculate_cost(t_models: list[TokenModel], ai_model: LLM) -> float:
    res = 0.0
    for m in t_models:
        res += (m.t_in/1000000) * ai_model.value["input"]
        res += (m.t_out/1000000) * ai_model.value["output"]
        res += (m.t_c_read/1000000) * ai_model.value["cache_read"]
        res += (m.t_c_write/1000000) * ai_model.value["cache_write"]
    return res