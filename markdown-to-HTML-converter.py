import sys
import markdown

markdown_file = sys.argv[2]
html_file = sys.argv[3]

with open(markdown_file, 'r') as file:
    markdown_text = file.read()

html_text = markdown.markdown(markdown_text)

with open(html_file, 'w') as file:
    file.write(html_text)

print("変換が完了しました。")