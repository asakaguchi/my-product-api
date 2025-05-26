import pytest
from datetime import datetime
from product_api.storage import InMemoryStorage
from product_api.models import ProductCreate


@pytest.fixture
def storage():
    """テスト用のストレージインスタンスを提供"""
    return InMemoryStorage()


@pytest.fixture
def sample_product_data():
    """テスト用の商品データを提供"""
    return ProductCreate(name="テスト商品", price=1000.0)


def test_create_product_returns_product_with_id_and_timestamp(
    storage, sample_product_data
):
    """商品作成時にIDと作成日時が自動設定されることをテスト"""
    # Act
    created_product = storage.create_product(sample_product_data)
    
    # Assert
    assert created_product.id == 1
    assert created_product.name == "テスト商品"
    assert created_product.price == 1000.0
    assert isinstance(created_product.created_at, datetime)


def test_create_multiple_products_increments_id(storage):
    """複数商品作成時にIDが自動採番されることをテスト"""
    # Arrange
    product1_data = ProductCreate(name="商品1", price=100.0)
    product2_data = ProductCreate(name="商品2", price=200.0)
    
    # Act
    product1 = storage.create_product(product1_data)
    product2 = storage.create_product(product2_data)
    
    # Assert
    assert product1.id == 1
    assert product2.id == 2


def test_get_product_by_existing_id_returns_product(
    storage, sample_product_data
):
    """存在するIDで商品取得が成功することをテスト"""
    # Arrange
    created_product = storage.create_product(sample_product_data)
    
    # Act
    retrieved_product = storage.get_product(created_product.id)
    
    # Assert
    assert retrieved_product is not None
    assert retrieved_product.id == created_product.id
    assert retrieved_product.name == created_product.name
    assert retrieved_product.price == created_product.price


def test_get_product_by_nonexistent_id_returns_none(storage):
    """存在しないIDで商品取得時にNoneが返ることをテスト"""
    # Act
    retrieved_product = storage.get_product(999)
    
    # Assert
    assert retrieved_product is None


def test_storage_is_empty_initially(storage):
    """初期状態でストレージが空であることをテスト"""
    # Act
    product = storage.get_product(1)
    
    # Assert
    assert product is None 