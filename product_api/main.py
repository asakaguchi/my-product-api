from fastapi import FastAPI, HTTPException, status
from product_api.models import Product, ProductCreate
from product_api.storage import InMemoryStorage

app = FastAPI(
    title="商品管理API",
    description="シンプルな商品管理システムのREST API",
    version="1.0.0"
)

# グローバルストレージインスタンス
storage = InMemoryStorage()


@app.get("/")
async def root():
    """ルートエンドポイント"""
    return {"message": "商品管理APIへようこそ"}


@app.get("/health")
async def health_check():
    """ヘルスチェックエンドポイント"""
    return {"status": "healthy"}


@app.post("/items", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product_data: ProductCreate) -> Product:
    """
    新しい商品を作成
    
    Args:
        product_data: 商品作成用データ
        
    Returns:
        作成された商品データ（IDと作成日時が自動設定済み）
    """
    created_product = storage.create_product(product_data)
    return created_product 