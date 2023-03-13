# Day_3

## .gitignore
> 특정 파일 혹은 폴더에 대해 Git이 버전 관리를 하지 못하도록 지정하는 것

### .gitignore에 작성하는 목록
- 민감한 개인 정보가 담긴 파일 (전화번호, 계좌번호, 각종 비밀번호, API KEY 등)
- OS(운영체제)에서 활용되는 파일
- IDE(통합 개발 환경 - pycharm) 혹은 Text editor(vscode) 등에서 활용되는 파일
    - 예) pycharm -> .idea/
- 개발 언어(python) 혹은 프레임워크(django)에서 사용되는 파일
    - 가상 환경 : `venv/`
    - `__pycache__/`

### .gitignore 작성 시 주의 사항- 반드시 이름을 `.gitignore`로 작성합니다. 앞의 점(.)은 숨김 파일이라는 뜻입니다.
- `.gitignore` 파일은 `.git` 폴더와 동일한 위치에 생성합니다.
- **제외 하고 싶은 파일은 반드시 `git add` 전에 `.gitignore`에 작성합니다.**
    
    <aside>
    ❗ **왜 git add 전에 .gitignore에 작성해야 할까요?**
    
    `git add a.txt` 라고 작성하면, 이제 Git은 `a.txt`를 버전 관리의 대상으로 여깁니다.
    한 번 버전 관리의 대상이 된 `a.txt`는 이후에 .gitignore에 작성하더라도
    무시되지 않고 계속 버전 관리의 대상으로 인식됩니다.
    
    따라서 제외 하고 싶은 파일은 반드시 git add 전에 .gitignore에 작성해야 합니다!
    
    </aside>

### .gitignore 쉽게 작성하기

> .gitignore의 내용을 쉽게 작성할 수 있도록 도와주는 두 개의 사이트를 소개합니다.
자신의 개발 환경에 맞는 것을 찾아서 `전체 복사, 붙여넣기`를 하면 됩니다.

1. **웹사이트**

[gitignore.io](https://gitignore.io/)

1. **gitignore 저장소**

[https://github.com/github/gitignore](https://github.com/github/gitignore)

1. **Python에 대한 .gitignore 예시**
    
    ![[https://gitignore.io/](https://gitignore.io/) 에서 가져옴](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fd7bd601-9433-418a-b08e-7b027db9a301/Untitled.png)
    
    [https://gitignore.io/](https://gitignore.io/) 에서 가져옴

### .gitignore 패턴 규칙
1. 아무것도 없는 라인이나, `#`로 시작하는 라인은 무시합니다.
2. `슬래시(/)`로 시작하면 하위 디렉터리에 재귀적으로 적용되지 않습니다.
3. 디렉터리는 `슬래시(/)`를 끝에 사용하는 것으로 표현합니다.
4. `느낌표(!)`로 시작하는 패턴의 파일은 ignore(무시)하지 않습니다.
5. **표준 Glob 패턴을 사용합니다.**
    - `*(asterisk)`는 문자가 하나도 없거나 하나 이상을 의미합니다.
    - `[abc]`는 중괄호 안에 있는 문자 중 하나를 의미합니다.
    - `물음표(?)`는 문자 하나를 의미합니다.
    - `[0-9]`처럼 중괄호 안에 하이픈(-)이 있는 경우 0에서 9사이의 문자 중 하나를 의미합니다.
    - `**(2개의 asterisk)`는 디렉터리 내부의 디렉터리까지 지정할 수 있습니다.
    (`a/**/z`라고 작성하면 `a/z`, `a/b/z`, `a/b/c/z` 까지 모두 영향을 끼칩니다.)