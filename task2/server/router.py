import json

from fastapi import APIRouter
from fastapi import status
from starlette.responses import StreamingResponse
from .controller import Controller
from .schema import RequestSchema
router = APIRouter()

@router.post(
    "/invoke",
    status_code=status.HTTP_200_OK,
    summary="response chat completely",

)
def invoke(
        form_data: RequestSchema):
    """
    ## API Endpoint

     **Params:**

    **Response:**
    """
    return Controller.invoke(session_id=form_data.session_id,message=form_data.message)


@router.post(
    "/stream",
    status_code=status.HTTP_200_OK,
    summary="response chat live",

)
def stream(
        form_data: RequestSchema):
    """
    ## API Endpoint

     **Params:**

    **Response:**
    """

    session_id = form_data.knowledge  # Generate unique session ID

    async def stream_data():
        yield f"event: status\ndata: [Start]\n\n"
        content =''
        async for chunk, full_message in Controller.stream(knowledge=form_data.knowledge,query=form_data.query):

            if isinstance(chunk, dict):
                chunk = json.dumps(chunk)  # Serialize the chunk to JSON
            yield f"event: delta\ndata: {chunk}\n\n"

        yield f"event: status\ndata: [Done]\n\n"

    response = StreamingResponse(stream_data(), media_type="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["Connection"] = "keep-alive"
    return response