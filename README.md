# setup-python-env
Python + VScode + Devcontainerを用いてデータ分析環境を構築する．

## 特長
* Pythonでよく用いられるデータ分析環境をdevcontainer上ですぐに使える
* ruffによるリント・フォーマット
  * 保存時にフォーマットがかかるように設定
  * 注意点: 未使用パッケージは消去されるため，`import numpy as np # noqa: F401`のように，コメントで`# noqa: F401` と記載する
* Jupyter拡張機能によるPythonスクリプトファイル上でのセル実行

## 使い方
### 前提
* Dockerをインストールしている．
* VSCodeをインストールしている．
* VSCodeの拡張機能で Dev Containers をインストールしている．

### 初期設定
1. このリポジトリを作業PC内にクローンする．
2. クローンしたディレクトリをVisual Studio Codeで開く．
3. コマンドパレエットを開き(`Ctrl + Shift + P`)， `dev containers: Rebuild and Reopen Container` を選択する．これにより，VSCode内でコンテナに入って作業ができる．
4. `uv init`で仮想環境を作成する．
5. `uv sync`でデフォルトでインストールされているパッケージをインストールする．

### Pythonの実行方法
* Jupyterの拡張機能により，Pythonスクリプト内でマジックコマンド(`# %%`)を用いることができる．
  * 詳細は[こちら](https://code.visualstudio.com/docs/python/jupyter-support-py)．
* スクリプトを実行する場合，`uv run <file>.py`を実行する．
  * 詳細は[こちら](https://docs.astral.sh/uv/guides/scripts/)

## 動作環境
以下のホストOSで検証済
* Ubuntu22.04で動作確認
* MacOSでは、UID/GID関係でエラーが出て動作しない(将来的にはMac版も作成予定)
* Windowsは未検証


## ディレクトリ構成

```
project/
├── .devcontainer/     # devcontainerの設定ファイル
├── .vscode/           # VScodeの設定ファイル(拡張機能やスニペットの設定を記載)
├── data/              # データ(gitによるバージョン管理はしない)
│   ├── raw/           # 生データ(変更しない)
│   ├── interim/       # 中間データ(前処理済み)
│   └── processed/     # 最終データ(分析・モデル用)
├── docs/              # ドキュメントファイル
│   ├── analysis/      # 分析に関するドキュメント
│   └── manual/        # 開発環境に関するドキュメント
├── images/            # 分析結果の図表
├── models/            # 保存されたモデルやチェックポイント
├── notebooks/         # データ分析ファイル
├── scripts/           # Pythonスクリプト(データ処理、モデルなど)
├── tests/             # テストコード
├── pyproject.toml     # プロジェクト設定ファイル
├── pyrightconfig.json # pyrightの設定ファイル
├── uv.lock            # パッケージの依存関係を示したファイル
└── README.md          # プロジェクトの概要説明
```

`data`ディレクトリに関して，フォルダは作成しておくが，gitでのバージョン管理は行わない．
もしデータのバージョン管理が必要な場合，別のソフトウェア(dvcなど)の導入を検討する．
別のディレクトリをバインドマウントしたい場合は，`data/raw`ディレクトリ以下にバインドマウントするのが良い．


## ツールの紹介
各ツールの使い方は， `docs/manuals` ディレクトリ以下に格納している．

* [VScode](./docs/manual/vscode.md)
* [Python](./docs/manual/python.md)
* [MLflow](./docs/manual/mlflow.md)