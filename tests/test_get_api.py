import pytest
from fastapi.testclient import TestClient
from product_api.main import app

client = TestClient(app)


def test_get_existing_product_returns_200():
    """存在する商品IDで200が返ることをテスト"""
    # Arrange: まず商品を作成
    product_data = {"name": "テスト商品", "price": 1000.0}
    create_response = client.post("/items", json=product_data)
    created_product = create_response.json()
    product_id = created_product["id"]
    
    # Act: 作成した商品を取得
    response = client.get(f"/items/{product_id}")
    
    # Assert
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == product_id
    assert response_data["name"] == "テスト商品"
    assert response_data["price"] == 1000.0
    assert "created_at" in response_data


def test_get_nonexistent_product_returns_404():
    """存在しない商品IDで404が返ることをテスト"""
    # Arrange
    nonexistent_id = 999
    
    # Act
    response = client.get(f"/items/{nonexistent_id}")
    
    # Assert
    assert response.status_code == 404
    assert "detail" in response.json()


def test_get_product_with_invalid_id_type_returns_422():
    """無効なID形式で422が返ることをテスト"""
    # Arrange
    invalid_id = "invalid"
    
    # Act
    response = client.get(f"/items/{invalid_id}")
    
    # Assert
    assert response.status_code == 422
    assert "detail" in response.json()


def test_integration_create_and_get_product():
    """統合テスト: 商品作成→取得の流れをテスト"""
    # Arrange
    product_data = {"name": "統合テスト商品", "price": 2000.0}
    
    # Act: 商品作成
    create_response = client.post("/items", json=product_data)
    created_product = create_response.json()
    
    # Act: 作成した商品を取得
    get_response = client.get(f"/items/{created_product['id']}")
    retrieved_product = get_response.json()
    
    # Assert: 作成と取得で同じデータが返ることを確認
    assert create_response.status_code == 201
    assert get_response.status_code == 200
    assert created_product["id"] == retrieved_product["id"]
    assert created_product["name"] == retrieved_product["name"]
    assert created_product["price"] == retrieved_product["price"]
    assert created_product["created_at"] == retrieved_product["created_at"]


def test_get_multiple_different_products():
    """複数の異なる商品を取得できることをテスト"""
    # Arrange: 複数の商品を作成
    product1_data = {"name": "商品A", "price": 100.0}
    product2_data = {"name": "商品B", "price": 200.0}
    
    create_response1 = client.post("/items", json=product1_data)
    create_response2 = client.post("/items", json=product2_data)
    
    product1_id = create_response1.json()["id"]
    product2_id = create_response2.json()["id"]
    
    # Act: それぞれの商品を取得
    get_response1 = client.get(f"/items/{product1_id}")
    get_response2 = client.get(f"/items/{product2_id}")
    
    # Assert: 正しい商品データが返ることを確認
    assert get_response1.status_code == 200
    assert get_response2.status_code == 200
    
    product1 = get_response1.json()
    product2 = get_response2.json()
    
    assert product1["name"] == "商品A"
    assert product1["price"] == 100.0
    assert product2["name"] == "商品B"
    assert product2["price"] == 200.0
    assert product1["id"] != product2["id"] 