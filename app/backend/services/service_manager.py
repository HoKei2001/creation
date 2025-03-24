from typing import Any, Dict, List
from .base_service import BaseService
from .reasoning_service import ReasoningService
from .decomposition_service import DecompositionService
from .analysis_service import AnalysisService
from .execution_service import ExecutionService
from .evaluation_service import EvaluationService
from .summary_service import SummaryService

class ServiceManager:
    """服务管理器，负责协调各个服务的执行"""
    
    def __init__(self):
        self.services: Dict[str, BaseService] = {
            "reasoning": ReasoningService(),
            "decomposition": DecompositionService(),
            "analysis": AnalysisService(),
            "execution": ExecutionService(),
            "evaluation": EvaluationService(),
            "summary": SummaryService()
        }
        self.context: Dict[str, Any] = {}
    
    async def execute_all(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """按顺序执行所有服务"""
        try:
            self.context = initial_context.copy()
            results = {}
            
            # 按顺序执行各个服务
            for service_name, service in self.services.items():
                # 执行服务
                result = await service.execute(self.context)
                
                # 更新上下文
                self.context[f"{service_name}_result"] = result
                results[service_name] = {
                    "status": service.get_status(),
                    "result": result
                }
                
                # 如果服务执行失败，停止后续服务
                if service.status == "error":
                    break
            
            return results
            
        except Exception as e:
            # 发生错误时，返回所有已执行服务的结果
            return {
                "error": str(e),
                "results": results
            }
    
    def get_service_status(self, service_name: str) -> Dict[str, Any]:
        """获取指定服务的状态"""
        service = self.services.get(service_name)
        if not service:
            raise ValueError(f"服务 {service_name} 不存在")
        return service.get_status()
    
    def get_all_status(self) -> Dict[str, Dict[str, Any]]:
        """获取所有服务的状态"""
        return {
            name: service.get_status()
            for name, service in self.services.items()
        } 