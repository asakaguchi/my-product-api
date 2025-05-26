from fastapi import FastAPI

app = FastAPI(
    title="商品管理API",
    description="シンプルな商品管理システムのREST API",
    version="1.0.0"
)


@app.get("/")
async def root():
    """ルートエンドポイント"""
    return {"message": "商品管理APIへようこそ"}


@app.get("/health")
async def health_check():
    """ヘルスチェックエンドポイント"""
    return {"status": "healthy"} 