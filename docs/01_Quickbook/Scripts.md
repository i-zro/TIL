01. 현재 로컬 브랜치 모두 삭제 후 원격에서 브랜치 받아오기
```
# 현재 브랜치를 제외하고 모든 로컬 브랜치 삭제
git branch | grep -v "\*" | xargs git branch -D

# 원격의 브랜치를 로컬에 체크아웃
git fetch --all
git branch -r | grep -v '\->' | while read remote; do git branch --track "${remote#origin/}" "$remote"; done
git pull --all
```