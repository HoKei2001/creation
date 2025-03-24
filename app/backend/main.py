from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import asyncio
from datetime import datetime

app = FastAPI()

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

class ExecutionStep(BaseModel):
    id: str
    title: str
    description: str
    status: str
    details: Optional[str] = None

class ChatResponse(BaseModel):
    message: str
    steps: List[ExecutionStep]

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # 模拟执行流程
        steps = [
            ExecutionStep(
                id="reasoning",
                title="推理阶段",
                description="分析用户输入，理解任务需求",
                status="running",
                details="正在分析用户输入..."
            ),
            ExecutionStep(
                id="decomposition",
                title="任务分解",
                description="将任务分解为可执行的子任务",
                status="pending"
            ),
            ExecutionStep(
                id="analysis",
                title="执行前分析",
                description="分析每个子任务的执行条件和资源需求",
                status="pending"
            ),
            ExecutionStep(
                id="execution",
                title="执行任务",
                description="按顺序执行分解后的子任务",
                status="pending"
            ),
            ExecutionStep(
                id="evaluation",
                title="任务评估",
                description="评估任务执行结果和效果",
                status="pending"
            ),
            ExecutionStep(
                id="summary",
                title="输出总结",
                description="生成任务执行总结和后续建议",
                status="pending"
            )
        ]

        # 模拟异步处理
        await asyncio.sleep(1)
        
        # 更新步骤状态
        for i, step in enumerate(steps):
            if i == 0:
                step.status = "completed"
                step.details = "已完成用户输入分析"
            elif i == 1:
                step.status = "running"
                step.details = "正在分解任务..."
            else:
                step.status = "pending"

        return ChatResponse(
            message="这是一个模拟的回复消息。在实际应用中，这里会显示AI助手的真实回复。",
            steps=steps
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 