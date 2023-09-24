import sys
import markdown

if len(sys.argv) != 4:
    print("Usage: python3 markdown-to-HTML-converter.py input.md output.html")
    sys.exit(1)

markdown_file = sys.argv[1]
html_file = sys.argv[2]

try:
    with open(markdown_file, 'r') as file:
        markdown_text = file.read()

    html_text = markdown.markdown(markdown_text)

    with open(html_file, 'w') as file:
        file.write(html_text)

    print("変換が完了しました。")
except FileNotFoundError:
    print(f"エラー: ファイル '{markdown_file}' が見つかりません。")
except Exception as e:
    print(f"エラー: {e}")
