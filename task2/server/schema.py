from pydantic import (
    BaseModel,
    ConfigDict,
)

class RequestSchema(BaseModel):
    session_id: int
    message:str
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "session_id": 1,
                "message": "hi. how can you help me? ",
            }
        },
    )