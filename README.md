# 헥소 블랙홀 (HEX BLACKHOLE)

## 프로젝트 개요


## 주요 기능

[게임 규칙](./game/Rulebook(KR).md)

## 팀 소개

<table>
  <tr>
    <td align="center"><a href="https://github.com/zooniezi"><img src="https://avatars.githubusercontent.com/u/75923015?v=4" width="100px;" alt=""/><br /><sub><b>
 김재준</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/hyvnsevng"><img src="https://avatars.githubusercontent.com/u/175284278?v=4" width="100px;" alt=""/><br /><sub><b>
 여현승</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/ebeleey"><img src="https://avatars.githubusercontent.com/u/175283788?v=4" width="100px;" alt=""/><br /><sub><b>
이다이</b></sub></a><br /></td>
</table>

## 깃허브 협업

### 브랜치 전략- Github Flow
- **메인 브랜치**: `main`
  - 항상 배포 가능한 상태를 유지
  - 모든 Pull Request는 이 브랜치로 머지
- **기능 브랜치**: `feature/기능명`
  - 새로운 기능 추가 시 생성
  - 예: `feature/login`, `feature/signup`, `feature/product-comparison`

### 커밋 규칙
- **커밋 메시지 형식**
  - **타입**: `feat`(새로운 기능), `fix`(버그 수정), `docs`(문서 수정), `chore`(기타 변경)
  - **커밋 메시지 본문**: 작업 후 명확한 메시지로 커밋하기
    ```bash
    git commit -m "feat: 로그인 페이지 UI 구현 (FE)"
    git commit -m "feat: 로그인 API 추가 및 검증 로직 구현 (BE)"
    ```
- **커밋 빈도**
  - 작은 단위로 자주 커밋

### 작업 규칙
1. `main` 브랜치는 직접 수정하지 않습니다.
2. 새로운 작업은 항상 `feature/기능명` 브랜치에서 시작합니다.
    ```bash
    git checkout -b feature/{기능명}
    ```
3. 프론트엔드(FE)와 백엔드(BE)는 같은 기능 브랜치에서 작업합니다.
4. 작업 완료 후 `main`으로 Pull Request 작성 및 리뷰 진행
5. Pull Request 작성 시, 변경 사항과 테스트 내용을 상세히 기재합니다.
6. 모든 머지는 코드 리뷰를 통해 진행합니다.
5. 머지가 완료되면 해당 기능 브랜치를 삭제하여 저장소를 정리합니다.
    ```bash
    git branch -d feature/{기능명}
    ```