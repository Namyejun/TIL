# Day_5

## Branch Merge
>지금까지는 브랜치를 통해서 독립된 작업 공간을 만드는 것 까지 진행했습니다.
이제 각 브랜치에서의 작업이 끝나면 어떻게 할까요? 
그 작업 내용을 master에 반영해야 하지 않을까요?
지금부터는 Merge라고 하는 병합을 학습하면서 브랜치를 합치는 것을 살펴보겠습니다.

### git merge
- 분기된 브랜치들을 하나로 합치는 명령어
- `git merge <합칠 브랜치 이름>`의 형태로 사용합니다.
- **Merge하기 전에 일단 다른 브랜치를 합치려고 하는, 즉 메인 브랜치로 switch 해야합니다.**

```bash
# 1. 현재 branch1과 branch2가 있고, HEAD가 가리키는 곳은 branch1 입니다.
$ git branch
* branch1
  branch2

# 2. branch2를 branch1에 합치려면?
$ git merge branch2

# 3. branch1을 branch2에 합치려면?
$ git switch branch2
$ git merge branch1
```

### Merge의 세 종류

1. **Fast-Forward**
    - 브랜치를 병합할 때 마치 `빨리감기`처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 것
    따로 merge 과정 없이 브랜치의 포인터가 이동하는 것을 **Fast-Forward**라고 합니다.

2. **3-Way Merge**
    - 브랜치를 병합할 때 `각 브랜치의 커밋 두개와 공통 조상 하나`를 사용하여 병합하는 것
    - 두 브랜치에서 `다른 파일` 혹은 `같은 파일의 다른 부분`을 수정했을 때 가능합니다.

3. **Merge Conflict**
    - 병합하는 두 브랜치에서 `같은 파일의 같은 부분`을 수정한 경우, Git이 어느 브랜치의 내용으로 작성해야 하는지 판단하지 못해서 발생하는 충돌(Conflict) 현상
    - 결국은 사용자가 **직접 내용을 선택해서 Conflict를 해결**해야 합니다.