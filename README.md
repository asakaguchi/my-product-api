# 商品管理API

シンプルな商品管理システムのREST APIです。FastAPIを使用して構築されており、商品の作成と取得機能を提供します。

## 機能

- ✅ 商品の作成（POST /items）
- ✅ 商品の取得（GET /items/{id}）
- ✅ ヘルスチェック（GET /health）
- ✅ 自動APIドキュメント生成（Swagger UI）

## 技術スタック

- **言語**: Python 3.12+
- **フレームワーク**: FastAPI
- **パッケージ管理**: uv
- **テスト**: pytest
- **データ保存**: メモリ（インメモリストレージ）

## セットアップ

### 前提条件

- Python 3.12以上
- uv（Python パッケージマネージャー）

### インストール

```bash
# リポジトリをクローン
git clone <repository-url>
cd my-product-api

# 依存関係をインストール
uv sync
```

## 使用方法

### アプリケーションの起動

```bash
uv run uvicorn product_api.main:app --reload
```

アプリケーションは `http://localhost:8000` で起動します。

### API ドキュメント

起動後、以下のURLでSwagger UIによる対話的なAPIドキュメントを確認できます：

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API 仕様

### エンドポイント一覧

| メソッド | パス | 説明 |
|---------|------|------|
| GET | `/` | ルートエンドポイント |
| GET | `/health` | ヘルスチェック |
| POST | `/items` | 商品作成 |
| GET | `/items/{id}` | 商品取得 |

### 商品作成 (POST /items)

**リクエスト:**
```json
{
  "name": "商品名",
  "price": 1000.0
}
```

**レスポンス (201 Created):**
```json
{
  "id": 1,
  "name": "商品名",
  "price": 1000.0,
  "created_at": "2025-05-26T10:58:50.524914"
}
```

**バリデーション:**
- `name`: 必須、1文字以上
- `price`: 必須、0より大きい値

### 商品取得 (GET /items/{id})

**レスポンス (200 OK):**
```json
{
  "id": 1,
  "name": "商品名",
  "price": 1000.0,
  "created_at": "2025-05-26T10:58:50.524914"
}
```

**エラーレスポンス (404 Not Found):**
```json
{
  "detail": "商品ID 999 が見つかりません"
}
```

## 使用例

### curlを使用した例

```bash
# ヘルスチェック
curl "http://localhost:8000/health"

# 商品作成
curl -X POST "http://localhost:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"name": "ノートPC", "price": 80000}'

# 商品取得
curl "http://localhost:8000/items/1"

# 存在しない商品の取得（404エラー）
curl "http://localhost:8000/items/999"
```

## テスト

### テストの実行

```bash
# 全テストを実行
uv run pytest tests/ -v

# 特定のテストファイルを実行
uv run pytest tests/test_create_api.py -v

# カバレッジ付きで実行
uv run pytest tests/ --cov=product_api --cov-report=html
```

### テスト構成

- `tests/test_main.py`: メインアプリケーションのテスト
- `tests/test_models.py`: データモデルのテスト
- `tests/test_storage.py`: ストレージクラスのテスト
- `tests/test_create_api.py`: 商品作成APIのテスト
- `tests/test_get_api.py`: 商品取得APIのテスト

## プロジェクト構造

```
my-product-api/
├── product_api/           # アプリケーションコード
│   ├── __init__.py
│   ├── main.py           # FastAPIアプリケーション
│   ├── models.py         # Pydanticモデル
│   └── storage.py        # インメモリストレージ
├── tests/                # テストコード
│   ├── __init__.py
│   ├── context.py
│   ├── test_main.py
│   ├── test_models.py
│   ├── test_storage.py
│   ├── test_create_api.py
│   └── test_get_api.py
├── docs/                 # ドキュメント
├── pyproject.toml        # プロジェクト設定
├── uv.lock              # 依存関係ロックファイル
└── README.md            # このファイル
```

## 開発

### 開発環境のセットアップ

```bash
# 開発用依存関係も含めてインストール
uv sync --dev

# 新しい依存関係を追加
uv add package-name

# 開発用依存関係を追加
uv add --dev package-name
```

### コーディング規約

- PEP 8に準拠
- 型ヒントを使用
- docstringで関数・クラスを説明
- TDD（テスト駆動開発）を採用

## 制約事項

- データはメモリ上に保存されるため、アプリケーション再起動時にデータは消失します
- 認証機能は実装されていません
- 商品の更新・削除機能は実装されていません

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。
