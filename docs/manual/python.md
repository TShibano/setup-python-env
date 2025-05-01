# python開発環境の概要

Python開発環境の概要を説明し、使用する主要なパッケージやツール（Ruff、Pyrightなど）について記載している．

## uv
### Python
* uv version: 0.7.0
* Python version: 3.13


## pythonパッケージ
* `uv add <package>` でパッケージをインストールできる
  * 開発用のパッケージは， `uv add --dev <package>` でインストールする
* 下記のライブラリはデフォルト設定としている

#### パッケージ
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
* boto3: MLflowで，MinIOにアーティファクトを格納するために必要


#### 開発用パッケージ
* ruff: リンター・フォーマッター
* pyright: 型チェック
* pytest: テストを行う
* ipykernel: Jupyterを扱う
* typing-extensions: 型ヒントを拡張する

## Ruff

RuffはPythonコードの静的解析ツールで，コードの品質向上やバグの早期発見を目的としている．
Ruffを使用することで，Pythonプロジェクトのコード品質を効率的に管理できる．
以下の特徴を持つ．

- 高速: Rustで実装されており，大規模なコードベースでも高速に動作する
- 多機能: コードスタイルのチェック，未使用のインポートの検出，型ヒントの検証など，多くの機能を持つ．
- 柔軟な設定: pyproject.tomlやruff.tomlを使用して，プロジェクトに応じたカスタマイズが可能．
- 統合性: Flake8やPylintなどの他のツールのルールセットをサポートし，既存のワークフローに簡単に統合できる．

### Ruffの使い方
VScodeの拡張機能である，[charliermarsh.ruff](https://github.com/astral-sh/ruff-vscode)を用いており，
設定によりファイル保存時に自動でフォーマットされる．

### Ruffの設定
* Ruffのルールコードの一覧は[こちら](https://docs.astral.sh/ruff/rules/)
* https://zenn.dev/egg_glass/books/flet-development-practical/viewer/ruff-setup

## Pyright

Pyrightは、Microsoftが開発したPython用の静的型チェックツールである. 以下の特徴を持つ.

- 高速: 大規模なコードベースでも高速に動作する.
- 型チェック: Pythonコードの型ヒントを検証し、型の不整合を検出する.
- 柔軟な設定: `pyproject.toml`や`pyrightconfig.json`を使用して、プロジェクトに応じた設定が可能.
- VSCodeとの統合: VSCodeの拡張機能として利用でき、リアルタイムで型チェックを実行する.

Pyrightを使用することで、型安全性を向上させ、バグの早期発見が可能となる.