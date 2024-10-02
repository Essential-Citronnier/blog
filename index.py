import os

def generate_index_html(src_base_folder, output_file):
    # HTML 시작 부분
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Index of Files</title>
        <link rel="stylesheet" href="./styles.css">
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
                line-height: 1.5;
                color: #24292f;
            }
            header, footer {
                text-align: center;
                padding: 1em;
                background-color: #f6f8fa;
            }
            main {
                padding: 1em;
            }
            h1, h2 {
                font-size: 1.5em;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            ul li {
                margin: 0.5em 0;
            }
            ul li a {
                text-decoration: none;
                color: #0366d6;
            }
            ul li a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>File Index</h1>
        </header>
        <main>
    """

    # data_html 하위 폴더를 순회하며 HTML 컨텐츠 생성
    for sub_folder in os.listdir(src_base_folder):
        folder_path = os.path.join(src_base_folder, sub_folder)
        if os.path.isdir(folder_path):
            # 섹션 헤더 추가
            html_content += f"<section>\n<h2>{sub_folder}</h2>\n<ul>\n"

            # 폴더 내의 HTML 파일을 리스트로 추가
            for filename in os.listdir(folder_path):
                if filename.endswith('.html'):
                    file_path = os.path.join(folder_path, filename).replace('\\', '/')
                    display_name = filename[:-5]  # .html 확장자 제거
                    html_content += f'<li><a href="{file_path}">{display_name}</a></li>\n'

            # 섹션 마무리
            html_content += "</ul>\n</section>\n<hr>\n"

    # HTML 끝 부분
    html_content += """
        </main>
        <footer>
            <p>© 2024 File Index</p>
        </footer>
    </body>
    </html>
    """

    # index.html 파일로 저장
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"{output_file} 생성 완료.")

# 사용 예시
src_base = 'data_html'  # HTML 파일들이 위치한 기본 경로
output_html = 'index.html'  # 생성할 HTML 파일 경로

generate_index_html(src_base, output_html)
