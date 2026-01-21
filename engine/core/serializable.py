# engine/core/serializable.py
import json
from typing import Any, Dict
from abc import ABC, abstractmethod
import uuid

class Serializable(ABC):
    """所有游戏对象的基类，支持序列化和唯一标识"""
    
    def __init__(self):
        self.id = str(uuid.uuid4())[:8]  # 短ID
        self.created_at = None
        self.updated_at = None
    
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典（用于序列化）"""
        pass
    
    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Serializable':
        """从字典还原对象"""
        pass
    
    def to_json(self) -> str:
        """转换为JSON字符串"""
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'Serializable':
        """从JSON字符串还原"""
        return cls.from_dict(json.loads(json_str))