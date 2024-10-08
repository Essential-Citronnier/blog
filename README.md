# ECR 블로그

ECR blog는 의학 지식과 알고리즘에 대한 글을 작성하고 공유하는 플랫폼입니다. 의학 교육 플랫포인 ECR 서비스와 유기적인 연계를 추구합니다.
현재 개발 단계이며, 2025년 1월 1일까지 version 1 release를 목표로 개발 및 데이터 제작 중입니다.

## Quickstart

```macos
git clone https://github.com/Essential-Citronnier/blog.git
python main.py 8000
```


## 개요
이 플랫폼은 다양한 사용자가 의학 지식과 알고리즘에 대한 글을 작성하고 게시할 수 있도록 하는 오픈 플랫폼입니다. 각 사용자는 자신의 블로그 글에 대한 저작권을 보유하며, 플랫폼 코드에 대한 저작권은 ECR에 속합니다.

## 라이선스

### 1. 블로그 글 작성자 저작권
모든 블로그 글의 저작권은 해당 글을 작성한 저자에게 있습니다. 저자는 자신의 글을 플랫폼에 게시함으로써, 해당 글을 게시 및 표시할 수 있는 비독점적 라이선스를 ECR에 부여합니다. 저작자는 언제든지 자신의 글을 삭제할 수 있으며, 삭제된 글은 플랫폼에서 더 이상 사용되지 않습니다.

### 2. 플랫폼 코드 라이선스
이 플랫폼의 소스 코드는 MIT 라이선스에 따라 자유롭게 사용할 수 있습니다. 다만, 해당 소스 코드를 사용하는 모든 배포본에는 원 저작권자인 ECR의 저작권 표시를 포함해야 합니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## How-to-use

### 기여 방법
1. 블로그 글을 작성하고 싶다면 [블로그 작성 가이드](CONTRIBUTING.md)를 참고하세요.
2. 플랫폼 코드에 기여하고 싶은 경우, [기여 가이드](CONTRIBUTING.md)를 참고하세요.

### 문의
더 궁금한 사항이 있으면 ECR의 지원팀에 문의해주세요: [essentialcitronnier@gmail.com]



### 업데이트 알림
- fastapi 서버를 통해 마크다운 파일을 blog 형태로 확인할 수 있고
- 현재 아래 전환 기능 오류(수정 중)
  - 마크다운 형식으로 입력된 유튜브 링크는 자동으로 유튜브 임베딩으로 전환된다.
  - e.g. (반드시 YouTube 링크 라고 써야 embedding 이 된다.)
  [YouTube 링크](https://www.youtube.com/watch?v=sZwgpz4s8Jw&t=97s)


## For developers

### fastapi 서버 or 정적 사이트 (github pages)
fastapi - main.py & data
[main.py](main.py) 는 fastapi 실행 함수로서, data 디렉터리 하위의 md 파일을 보여준다.


static - index.html & data_html
[index.html](index.html) 은 github pages 기본 페이지로, data_html 디렉터리의 파일을 보여주는 메인 페이지이다.

md -> html 동기화
항상 md 파일을 기준으로 생성하고 html 파일을 md 파일에 동기화하는 방식으로 진행한다.

[index.py](index.py)는 data_html 디렉터리 안 정적 파일의 리스트를 담고 있는 index.html 파일을 업데이트하는 함수로, 주기적으로 실행하는 것을 추천한다.

[convert.py](convert.py)는 data 디렉터리에 md 파일을 생성하면 자동을로 html 파일을 생성해주는 함수로, 이또한 주기적으로 실행하는 것을 추천한다.
