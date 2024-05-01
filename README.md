# Markdown to HTML Converter

## 概要
このプログラムは、Markdownファイル（.md）をHTMLファイルに変換するコマンドラインツールです。マークダウン形式の文書をHTML形式に変換することで、Webサイトなどで表示や共有が容易になります。

## 使用方法
1. Python 3がインストールされていることを確認します。
2. プログラムをダウンロードまたはクローンします。
3. ターミナルまたはコマンドプロンプトを開き、プログラムが保存されているディレクトリに移動します。
4. コマンドラインで以下のように実行します。

python3 file-converter.py markdown inputfile outputfile

- `markdown`: 実行するコマンドです。
- `inputfile`: .mdファイルのパスです。
- `outputfile`: 生成されるHTMLファイルのパスです。

## 依存関係
このプログラムは、Pythonの標準ライブラリおよび `python-markdown` ライブラリに依存しています。`python-markdown` ライブラリは、Markdown形式のテキストをHTMLに変換するためのパッケージです。

## インストール
1. Pythonのパッケージマネージャであるpipを使用して、 `python-markdown` ライブラリをインストールします。

pip install markdown

2. インストールが完了したら、プログラムを実行できます。

## 注意事項
- 入力ファイルはMarkdown形式である必要があります。
- 出力ファイルはHTML形式で保存されます。
- コマンドの引数は正確に指定する必要があります。
