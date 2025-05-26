import pytest
from fastapi.testclient import TestClient
from product_api.main import app

client = TestClient(app)


def test_create_product_with_valid_data_returns_201():
    """正常な商品作成リクエストで201が返ることをテスト"""
    # Arrange
    product_data = {"name": "テスト商品", "price": 1000.0}
    
    # Act
    response = client.post("/items", json=product_data)
    
    # Assert
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["id"] == 1
    assert response_data["name"] == "テスト商品"
    assert response_data["price"] == 1000.0
    assert "created_at" in response_data


def test_create_product_with_empty_name_returns_422():
    """商品名が空の場合に422エラーが返ることをテスト"""
    # Arrange
    product_data = {"name": "", "price": 1000.0}
    
    # Act
    response = client.post("/items", json=product_data)
    
    # Assert
    assert response.status_code == 422
    assert "detail" in response.json()


def test_create_product_with_zero_price_returns_422():
    """価格が0の場合に422エラーが返ることをテスト"""
    # Arrange
    product_data = {"name": "テスト商品", "price": 0.0}
    
    # Act
    response = client.post("/items", json=product_data)
    
    # Assert
    assert response.status_code == 422
    assert "detail" in response.json()


def test_create_product_with_negative_price_returns_422():
    """価格が負の場合に422エラーが返ることをテスト"""
    # Arrange
    product_data = {"name": "テスト商品", "price": -100.0}
    
    # Act
    response = client.post("/items", json=product_data)
    
    # Assert
    assert response.status_code == 422
    assert "detail" in response.json()


def test_create_product_with_missing_name_returns_422():
    """商品名が欠けている場合に422エラーが返ることをテスト"""
    # Arrange
    product_data = {"price": 1000.0}
    
    # Act
    response = client.post("/items", json=product_data)
    
    # Assert
    assert response.status_code == 422
    assert "detail" in response.json()


def test_create_product_with_missing_price_returns_422():
    """価格が欠けている場合に422エラーが返ることをテスト"""
    # Arrange
    product_data = {"name": "テスト商品"}
    
    # Act
    response = client.post("/items", json=product_data)
    
    # Assert
    assert response.status_code == 422
    assert "detail" in response.json()


def test_create_multiple_products_increments_id():
    """複数商品作成時にIDが自動採番されることをテスト"""
    # Arrange
    product1_data = {"name": "商品1", "price": 100.0}
    product2_data = {"name": "商品2", "price": 200.0}
    
    # Act
    response1 = client.post("/items", json=product1_data)
    response2 = client.post("/items", json=product2_data)
    
    # Assert
    assert response1.status_code == 201
    assert response2.status_code == 201
    
    # IDが連続して採番されることを確認
    # 注意: 他のテストの影響でIDが1から始まらない可能性があるため、
    # 相対的な関係のみをテスト
    id1 = response1.json()["id"]
    id2 = response2.json()["id"]
    assert id2 == id1 + 1 