# VSCodeの概要

## 拡張機能
### インストール済の拡張機能
* ms-python.python: Python用
* ms-toolsai.jupyter: Jupyter用
* kevinrose.vsc-python-indent: Pythonのインデント
* charliermarsh.ruff: ruff(ruffの設定は`pyproject.toml`を参照)
* njpwerner.autodocstring: docstringを自動で設定(google styleを採用)
* yzhang.markdown-all-in-on: markdown用

### 拡張機能の設定
- settings.json: VSCodeの設定ファイル.
  - 主な設定:
    - Python仮想環境のインタプリタパスを指定 (`./.venv/bin/python`).
    - Ruffをデフォルトフォーマッタに設定.
    - 保存時にコードフォーマットやインポート整理を実行.
    - Jupyter Notebookの保存時フォーマットを有効化.
    - DocstringフォーマットをGoogleスタイルに設定.

## ユーザスニペット
python.code-snippetsに，よく使うスニペットを最低限登録している．

* `template`: ファイルを最初に作成するときに記入するテンプレート
* `section`: ファイルである程度の区分で分割したいときに作成するブロック
* `cell`: セル実行する時のブロック
* `ifmain`: Pythonでスクリプトファイルを実行するときに書くコードブロック


## git
ここでは，gitの基本機能の紹介は行わず，VScode上で操作できる便利なツールを紹介する．
* 分割addの設定
  * 分割addとは，1ファイル内で複数箇所の変更がある時，変更箇所を指定してステージングエリアに追加すること．
  * https://zenn.dev/appgrape/scraps/073cdea2f66665
* コミットを分割する
* コミットを圧縮する