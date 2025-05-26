from datetime import datetime
from typing import Dict, Optional
from product_api.models import Product, ProductCreate


class InMemoryStorage:
    """メモリ上で商品データを管理するストレージクラス"""
    
    def __init__(self) -> None:
        """ストレージを初期化"""
        self._products: Dict[int, Product] = {}
        self._next_id: int = 1
    
    def create_product(self, product_data: ProductCreate) -> Product:
        """
        新しい商品を作成してストレージに保存
        
        Args:
            product_data: 商品作成用データ
            
        Returns:
            作成された商品（IDと作成日時が自動設定済み）
        """
        # IDと作成日時を自動設定
        product = Product(
            id=self._next_id,
            name=product_data.name,
            price=product_data.price,
            created_at=datetime.now()
        )
        
        # ストレージに保存
        self._products[product.id] = product
        
        # 次のIDを準備
        self._next_id += 1
        
        return product
    
    def get_product(self, product_id: int) -> Optional[Product]:
        """
        指定されたIDの商品を取得
        
        Args:
            product_id: 商品ID
            
        Returns:
            商品データ（存在しない場合はNone）
        """
        return self._products.get(product_id) 