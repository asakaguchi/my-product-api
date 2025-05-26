from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class ProductCreate(BaseModel):
    """商品作成用のデータモデル"""
    name: str = Field(..., min_length=1, description="商品名（必須、1文字以上）")
    price: float = Field(..., gt=0, description="価格（必須、0より大きい）")


class Product(BaseModel):
    """商品データモデル"""
    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.isoformat()
        }
    )
    
    id: int = Field(..., description="商品ID（自動採番）")
    name: str = Field(..., min_length=1, description="商品名（必須、1文字以上）")
    price: float = Field(..., gt=0, description="価格（必須、0より大きい）")
    created_at: datetime = Field(..., description="作成日時（自動設定）") 