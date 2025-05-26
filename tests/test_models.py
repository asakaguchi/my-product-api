import pytest
from datetime import datetime
from pydantic import ValidationError
from product_api.models import Product, ProductCreate


def test_product_create_with_valid_data():
    """正常な商品作成データのテスト"""
    # Arrange
    product_data = {"name": "テスト商品", "price": 1000.0}
    
    # Act
    product = ProductCreate(**product_data)
    
    # Assert
    assert product.name == "テスト商品"
    assert product.price == 1000.0


def test_product_create_with_empty_name_raises_error():
    """商品名が空の場合のバリデーションエラーテスト"""
    # Arrange
    product_data = {"name": "", "price": 1000.0}
    
    # Act & Assert
    with pytest.raises(ValidationError) as exc_info:
        ProductCreate(**product_data)
    
    assert "String should have at least 1 character" in str(exc_info.value)


def test_product_create_with_zero_price_raises_error():
    """価格が0の場合のバリデーションエラーテスト"""
    # Arrange
    product_data = {"name": "テスト商品", "price": 0.0}
    
    # Act & Assert
    with pytest.raises(ValidationError) as exc_info:
        ProductCreate(**product_data)
    
    assert "Input should be greater than 0" in str(exc_info.value)


def test_product_create_with_negative_price_raises_error():
    """価格が負の場合のバリデーションエラーテスト"""
    # Arrange
    product_data = {"name": "テスト商品", "price": -100.0}
    
    # Act & Assert
    with pytest.raises(ValidationError) as exc_info:
        ProductCreate(**product_data)
    
    assert "Input should be greater than 0" in str(exc_info.value)


def test_product_with_auto_generated_fields():
    """ID と作成日時が自動生成される商品モデルのテスト"""
    # Arrange
    product_data = {
        "id": 1,
        "name": "テスト商品",
        "price": 1000.0,
        "created_at": datetime.now()
    }
    
    # Act
    product = Product(**product_data)
    
    # Assert
    assert product.id == 1
    assert product.name == "テスト商品"
    assert product.price == 1000.0
    assert isinstance(product.created_at, datetime) 