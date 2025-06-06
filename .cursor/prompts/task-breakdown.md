# タスク分解プロンプト

要件を分析し、以下の形式でタスクに分解してください。

## 分解の原則

1. 各タスクは 15-30 分で完了可能な粒度（2 時間ハンズオン用）
2. 依存関係を明確化
3. テスト可能な完了条件を定義
4. 初心者でも理解できるタスク名

## 出力形式

### Task N: [タスク名]（推定: XX 分）

- [ ] 具体的な作業1
- [ ] 具体的な作業2
- [ ] テスト作成
- [ ] 動作確認

## タスク分解の例

### Task 1: プロジェクト基盤構築（推定: 20 分）

- [ ] FastAPI プロジェクトの初期化
- [ ] 依存関係の設定（requirements.txt）
- [ ] 基本的なディレクトリ構造の作成
- [ ] ヘルスチェックエンドポイントの実装
- [ ] 基本的な起動確認テスト

### Task 2: データモデル定義（推定: 15 分）

- [ ] 商品データモデル（Pydantic）の定義
- [ ] メモリストレージクラスの実装
- [ ] モデルのバリデーションテスト

### Task 3: 商品作成API実装（推定: 25 分）

- [ ] POST /items エンドポイントの実装
- [ ] エラーハンドリング
- [ ] 商品作成 API のテストコード
- [ ] curl での動作確認

### Task 4: 商品取得 API 実装（推定: 20 分）

- [ ] GET /items/{id} エンドポイントの実装
- [ ] 404 エラーハンドリング
- [ ] 商品取得 API のテストコード
- [ ] 統合テストの作成

## 注意事項

- 初心者向けなので、複雑すぎるタスクは避ける
- 各タスクが独立してテスト可能であること
- TDD のサイクルを体験できる構成にする
