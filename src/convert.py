# data 하위 폴더 내의 md 파일을 html로 변환하여 data_html 폴더에 저장
# 지속적으로 업데이트 진행해야 html 파일이 최신 상태로 유지됨
# 파일 덮어쓰기 주의
import os
import markdown

# 하위 폴더 내의 Markdown 파일을 HTML로 변환하여 저장하는 함수
def convert_markdown_to_html(src_base_folder, dest_base_folder):
    # 저장할 경로의 폴더가 없으면 생성
    if not os.path.exists(dest_base_folder):
        os.makedirs(dest_base_folder)
    
    # src_base_folder의 모든 하위 폴더를 찾음
    sub_folders = [f.name for f in os.scandir(src_base_folder) if f.is_dir()]
    
    # 각 sub_folder에 대해 변환 작업 수행
    for sub_folder in sub_folders:
        # 소스 폴더와 목적지 폴더 경로 설정
        src_folder = os.path.join(src_base_folder, sub_folder)
        dest_folder = os.path.join(dest_base_folder, sub_folder)
        
        # 목적지 폴더가 존재하지 않으면 생성
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        
        # 소스 폴더 내의 모든 파일을 순회
        for filename in os.listdir(src_folder):
            file_path = os.path.join(src_folder, filename)
            
            # 파일이 .md 파일일 때만 변환
            if os.path.isfile(file_path) and filename.endswith('.md'):
                name, ext = os.path.splitext(filename)
                
                # 입력 파일과 출력 파일 경로 설정
                input_file = file_path
                output_file = os.path.join(dest_folder, f"{name}.html")
                
                # Markdown 파일을 읽어서 HTML로 변환
                with open(input_file, 'r', encoding='utf-8') as f:
                    text = f.read()
                
                html = markdown.markdown(text)
                
                # 변환된 HTML을 파일로 저장
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(html)
                
                print(f"변환 완료: {input_file} -> {output_file}")

# 사용 예시
src_base = 'data'  # Markdown 파일이 들어 있는 기본 경로
dest_base = 'data_html'  # 변환된 HTML 파일을 저장할 기본 경로

convert_markdown_to_html(src_base, dest_base)
