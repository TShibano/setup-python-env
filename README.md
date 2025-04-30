# setup-python-env
Python + VScode + Devcontainerを用いてデータ分析環境を構築する．

## 使い方
### 前提
* Dockerをインストールしている．
* VSCodeをインストールしている．
* VSCodeの拡張機能で Dev Containers をインストールしている．

### 使い方
1. このリポジトリを作業PC内にクローンする．
2. クローンしたディレクトリをVisual Studio Codeで開く．
3. コマンドパレエットを開き(`Ctrl + Shift + P`)， `dev containers: Rebuild and Reopen Container` を選択する．これにより，VSCode内でコンテナに入って作業ができる．
4. `uv init`で仮想環境を作成する
5. `uv sync`でデフォルトでインストールされているパッケージをインストールする


## 動作環境
Ubuntu22.04で動作確認済み
Macでは、UID/GID関係でエラーが出て動作しない(将来的にはMac版も作成予定)


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

## ツールの紹介
### Python
* ver: 3.13
* `uv add <package>` でパッケージをインストールできる
  * 開発用のパッケージは， `uv add --dev <package>` でインストールする
* 下記のライブラリはデフォルト設定としている

#### Python packages
* numpy: 配列用
* polars: データフレームライブラリ
* openpyxl: エクセルデータを扱う
* pandera: データフレームのデータ検証を行う
* matplitlib: グラフ描画
* matpliblib-fontja: グラフで日本語を扱う
* seaborn: グラフ描画
* scipy: 科学技術計算
* statsmodels: 統計解析
* scikit-learn: 機械学習
* xgboost: XGBoost
* mlflow: 実験結果の管理


#### Python develop packages
* ruff: リンター・フォーマッター
* pyright: 型チェック
* pytest: テストを行う
* ipykernel: Jupyterを扱う
* typing-extensions: 型ヒントを拡張する

### VScode extensions
* ms-python.python: Python用
* ms-toolsai.jupyter: Jupyter用
* kevinrose.vsc-python-indent: Pythonのインデント
* charliermarsh.ruff: ruff(ruffの設定は`pyproject.toml`を参照)
* njpwerner.autodocstring: docstringを自動で設定(google styleを採用)
* yzhang.markdown-all-in-on: markdown用