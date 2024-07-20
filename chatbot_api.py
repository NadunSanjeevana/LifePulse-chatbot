from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ollama

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str

# Define the RAG chain function


def get_response_from_model(question):
    response = ollama.chat(model='qwen', messages=[
                           {'role': 'user', 'content': question}])
    return response['message']['content']


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        model_response = get_response_from_model(request.message)
        return ChatResponse(response=model_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
