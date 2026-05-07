# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

TDD 연습용 Bowling Kata. 미국식 텐핀 볼링 한 게임의 최종 총점을 계산한다. 전체 스펙은 `docs/SPEC.md` 참조.

**구현 범위에서 명시적으로 제외:**
- 투구 유효성 검사
- 투구 횟수 / 프레임 수 정합성 확인
- 중간 프레임 점수 제공

## TDD 필수 적용

**모든 기능 구현 및 버그 수정 전에 `/test-driven-development` 스킬을 호출할 것.**

스킬 위치: `.claude/skills/tdd-skill/SKILL.md`

핵심 원칙: 실패하는 테스트가 먼저 존재하지 않는 한 프로덕션 코드를 작성하지 않는다.

## 요구 인터페이스

`Game` 클래스에 두 메서드를 구현한다.

```python
class Game:
    def roll(self, pins: int) -> None: ...  # 투구마다 호출, pins = 쓰러뜨린 핀 수
    def score(self) -> int: ...             # 게임 최종 총점 반환
```

## 볼링 점수 규칙

- **스페어**: 두 번 투구로 핀 10개 전부 → 해당 프레임 보너스 = 다음 투구 1회 핀 수
- **스트라이크**: 첫 투구로 핀 10개 전부 → 프레임은 1회 투구로 종료, 보너스 = 이후 2회 투구 핀 수 합계
- **10번 프레임**: 스페어/스트라이크 시 최대 3회까지 추가 투구 가능

## 구현 현황

### 파일 구조

| 파일 | 역할 |
|------|------|
| `game.py` | `Game` 클래스 구현 (프로덕션 코드) |
| `test_game.py` | pytest 테스트 스위트 |

### 핵심 설계

`score()`는 투구 리스트를 10프레임 단위로 순회한다. 스트라이크면 인덱스를 1 전진, 그 외엔 2 전진. 10번 프레임 추가 투구는 별도 처리 없이 인덱스 범위로 자연스럽게 처리된다.

### 테스트 목록

| 테스트 | 시나리오 | 기대값 |
|--------|----------|--------|
| `test_gutter_game` | 20구 모두 0 | 0 |
| `test_all_ones` | 20구 모두 1 | 20 |
| `test_one_spare` | 1프레임 5+5 스페어, 이후 3 → 나머지 0 | 16 |
| `test_one_strike` | 1프레임 스트라이크, 이후 3+4 → 나머지 0 | 24 |
| `test_perfect_game` | 12구 연속 스트라이크 | 300 |

## Environment

Python 3.14 (CPython), virtualenv at `.venv`.

```bash
# pytest 설치 (최초 1회)
.venv\Scripts\pip install pytest

# 테스트 전체 실행
.venv\Scripts\pytest

# 단일 파일 실행
.venv\Scripts\pytest test_game.py

# 단일 테스트 실행
.venv\Scripts\pytest test_game.py::test_name

# 첫 실패에서 멈춤 (RED 확인용)
.venv\Scripts\pytest -x

# 자세한 출력
.venv\Scripts\pytest -v
```
