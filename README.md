# setup-python-env
set up Python + VScode + Devcontainer

## Usage
Linux環境で動作する。
Ubuntu22.04で動作確認済み

Macでは、UID/GID関係でエラーが出て動作しない


## ディレクトリ構成

```
project/
├── .devcontainer/     # devcontainerの設定ファイル
├── .vscode/           # 分析ファイル
├── data/              # データ
│   ├── raw/           # 生データ(変更しない)
│   ├── interim/       # 中間データ(前処理済み)
│   └── processed/     # 最終データ(分析・モデル用)
├── docs/              # ドキュメントファイル
│   ├── analysis/      # 分析に関するドキュメント
│   └── manual/        # 開発環境に関するドキュメント
├── images/            # 分析結果の図表
├── models/            # 保存されたモデルやチェックポイント
├── notebooks/         # データ分析ファイル
├── scripts/           # Pythonスクリプト(データ処理、分析、モデルなど)
├── tests/             # テストコード
├── pyproject.toml     # プロジェクト設定ファイル
├── pyrightconfig.json # プロジェクト設定ファイル
├── uv.lock            # プロジェクト設定ファイル
└── README.md          # プロジェクトの概要説明
```
