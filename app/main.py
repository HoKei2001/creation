from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import docker
import os
from openai import OpenAI
from app.models import AVAILABLE_MODELS, DEFAULT_MODEL

app = FastAPI(title="Code Generation Platform")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Docker client with error handling
try:
    docker_client = docker.from_env()
except docker.errors.DockerException as e:
    print(f"Warning: Could not connect to Docker daemon: {e}")
    print("Code execution in sandbox will be disabled")
    docker_client = None

class CodeRequest(BaseModel):
    prompt: str
    language: str = "python"
    timeout: Optional[int] = 30
    model: str = DEFAULT_MODEL

class CodeResponse(BaseModel):
    code: str
    output: str
    error: Optional[str] = None

class ModelInfo(BaseModel):
    id: str
    name: str
    description: str

@app.get("/")
async def root():
    return {"message": "Welcome to Code Generation Platform API"}

@app.get("/models", response_model=List[ModelInfo])
async def list_models():
    return [
        ModelInfo(
            id=model_id,
            name=config.model_name,
            description=f"Available at {config.base_url}"
        )
        for model_id, config in AVAILABLE_MODELS.items()
    ]

@app.post("/generate", response_model=CodeResponse)
async def generate_code(request: CodeRequest):
    try:
        if request.model not in AVAILABLE_MODELS:
            raise HTTPException(status_code=400, detail=f"Model {request.model} not found")
        
        model_config = AVAILABLE_MODELS[request.model]
        
        # Initialize OpenAI client with custom base URL
        client = OpenAI(
            base_url=model_config.base_url,
            api_key=model_config.api_key
        )
        
        # Create the prompt for code generation
        system_prompt = f"""You are an expert programmer. Generate code in {request.language} based on the user's request.
        The code should be complete, well-documented, and follow best practices.
        Only return the code, no explanations or markdown formatting."""
        
        user_prompt = f"Generate {request.language} code for: {request.prompt}"
        
        # Generate code using the selected model
        response = client.chat.completions.create(
            model=model_config.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        generated_code = response.choices[0].message.content.strip()
        
        return CodeResponse(
            code=generated_code,
            output="Code generated successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/execute", response_model=CodeResponse)
async def execute_code(request: CodeRequest):
    if docker_client is None:
        return CodeResponse(
            code=request.prompt,
            output="",
            error="Docker is not available. Code execution is disabled."
        )
    
    try:
        # Create a temporary container
        container = docker_client.containers.run(
            f"{request.language}:latest",
            command=f"python -c '{request.prompt}'",
            detach=True,
            mem_limit="100m",
            cpu_period=100000,
            cpu_quota=50000,
            network_disabled=True,
            remove=True
        )
        
        # Wait for the container to finish
        container.wait(timeout=request.timeout)
        
        # Get the output
        output = container.logs().decode()
        
        return CodeResponse(
            code=request.prompt,
            output=output
        )
    except Exception as e:
        return CodeResponse(
            code=request.prompt,
            output="",
            error=str(e)
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


