from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class BaseService(ABC):
    """基础服务类，定义所有服务的基本接口"""
    
    def __init__(self):
        self.status: str = "pending"
        self.details: Optional[str] = None
        self.result: Optional[Dict[str, Any]] = None
        self.error: Optional[str] = None

    @abstractmethod
    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """执行服务的主要逻辑"""
        pass

    def set_status(self, status: str, details: Optional[str] = None):
        """设置服务状态和详细信息"""
        self.status = status
        self.details = details

    def set_result(self, result: Dict[str, Any]):
        """设置服务执行结果"""
        self.result = result

    def set_error(self, error: str):
        """设置错误信息"""
        self.error = error
        self.status = "error"

    def get_status(self) -> Dict[str, Any]:
        """获取服务当前状态"""
        return {
            "status": self.status,
            "details": self.details,
            "result": self.result,
            "error": self.error
        } 