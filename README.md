# 🐋 Whale Language

> Make programming readable like a sentence.

Whale은 초보자도 쉽게 읽고 쓸 수 있도록 만든 프로그래밍 언어입니다.  
Python처럼 배우기 쉽지만, 영어와 한국어 문법을 함께 지원하고, 입력하기 편한 `[]` 기반 호출 문법을 사용합니다.

[![Download](https://img.shields.io/badge/Download-Whale-blue?style=for-the-badge&logo=github)](https://github.com/imtdot/Whale/releases)
[![Download](https://img.shields.io/badge/Go-Website-green?style=for-the-badge&)](https://whale.imtdot.kr/)

---

## 🌐 Links

| Name | URL |
|---|---|
| Home | https://whale.imtdot.kr |
| Terminal | https://whale.imtdot.kr/terminal |
| Editor | https://whale.imtdot.kr/editor |
| Releases | https://github.com/imtdot/Whale/releases |

---

## ✨ Features

- English/Korean syntax
- Easy `[]` function call style
- HTML Terminal
- Python Terminal
- Whale-only `.whl` files
- URL-based import
- Terminal-based input, no browser popup input

---

## 🧠 Language Mode

```whale
whale lang='en'
whale lang='kr'
```

---

## 🖨 Output

```whale
print['Hello Whale']
출력['안녕 웨일']
```

---

## ⌨ Input

```whale
name = input['Name >>> ']
이름 = 입력['이름 >>> ']
```

---

## 📦 Variables

```whale
x = 10
name = 'whale'
이름 = '웨일'
```

---

## ➕ Operators

```whale
+   -   *   /   //   ///   **
```

Examples:

```whale
x = 10 + 3
y = 10 /// 3
z = 2 ** 3
```

---

## 🔍 Conditions

```whale
if x > 10:
    print['big']
else:
    print['small']
```

```whale
만약 x > 10:
    출력['크다']
아니면:
    출력['작다']
```

---

## 🔁 Loops

```whale
repeat[3]:
    print['hi']
```

```whale
반복[3]:
    출력['안녕']
```

---

## 🧩 Functions

```whale
func add[a, b]:
    return a + b

result = add[3, 5]
print[result]
```

```whale
함수 더하기[a, b]:
    돌려줘 a + b

결과 = 더하기[3, 5]
출력[결과]
```

---

## 📚 Lists

```whale
nums = [1, 2, 3]
print[nums[0]]
```

`[]` 충돌 방지 규칙:

```whale
print['hello']   # 이름 바로 뒤 [] → 함수 호출
nums = [1,2,3]   # 값으로 쓰이는 [] → 리스트
nums[0]          # 변수 뒤 숫자 [] → 리스트 접근
```

---

## 🌍 URL Import

Whale은 HTML 터미널과 Python 터미널 모두에서 URL 기반 import를 사용합니다.

```whale
import 'https://example.com/helper.whl'
가져와 'https://example.com/helper.whl'
```

예시:

```whale
whale lang='kr'

가져와 'https://whale.imtdot.kr/lib/helper.whl'

출력[인사['승우']]
```

### Import Rules

- `.whl` 파일만 허용
- URL로만 가져오기
- 같은 URL은 한 번만 가져오기
- HTML 터미널은 `fetch()` 사용
- Python 터미널은 HTTP 요청 사용
- 가져온 파일은 현재 실행 환경에 함수/변수를 등록

### CORS Notice for HTML Terminal

HTML 터미널에서 다른 도메인의 `.whl` 파일을 가져올 때 브라우저 CORS 정책 때문에 차단될 수 있습니다.

이 경우 Whale HTML 터미널은 다음처럼 표시합니다.

```text
ImportError: CORS 오류가 발생했습니다.
```

해결 방법:

- `.whl` 파일을 CORS가 허용된 서버에 올리기
- 공식 Whale 라이브러리 경로 사용
- 같은 도메인에서 모듈 제공

추천 공식 경로:

```whale
가져와 'https://whale.imtdot.kr/lib/helper.whl'
```

---

## 🖥 Terminal Commands

```text
open
editor
help
clear
whale shutdown
```

> `whale shutdown`은 Python 터미널에서 종료 명령으로 사용됩니다.

---

## 💡 Philosophy

> Make programming readable like a sentence.

---

## 🧑‍💻 Author

Project by iM티닷 | Big Industry


---

## 🌐 Links

| Name | URL |
|---|---|
| Home | https://whale.imtdot.kr |
| Terminal | https://whale.imtdot.kr/terminal |
| Editor | https://whale.imtdot.kr/editor |
| Releases | https://github.com/imtdot/Whale/releases |

---

## ✨ Features

- English/Korean syntax
- Easy `[]` function call style
- HTML Terminal
- Python Terminal
- Whale-only `.whl` files
- URL-based import
- Terminal-based input, no browser popup input

---

## 🧠 Language Mode

```whale
whale lang='en'
whale lang='kr'
```

---

## 🖨 Output

```whale
print['Hello Whale']
출력['안녕 웨일']
```

---

## ⌨ Input

```whale
name = input['Name >>> ']
이름 = 입력['이름 >>> ']
```

---

## 📦 Variables

```whale
x = 10
name = 'whale'
이름 = '웨일'
```

---

## ➕ Operators

```whale
+   -   *   /   //   ///   **
```

Examples:

```whale
x = 10 + 3
y = 10 /// 3
z = 2 ** 3
```

---

## 🔍 Conditions

```whale
if x > 10:
    print['big']
else:
    print['small']
```

```whale
만약 x > 10:
    출력['크다']
아니면:
    출력['작다']
```

---

## 🔁 Loops

```whale
repeat[3]:
    print['hi']
```

```whale
반복[3]:
    출력['안녕']
```

---

## 🧩 Functions

```whale
func add[a, b]:
    return a + b

result = add[3, 5]
print[result]
```

```whale
함수 더하기[a, b]:
    돌려줘 a + b

결과 = 더하기[3, 5]
출력[결과]
```

---

## 📚 Lists

```whale
nums = [1, 2, 3]
print[nums[0]]
```

`[]` 충돌 방지 규칙:

```whale
print['hello']   # 이름 바로 뒤 [] → 함수 호출
nums = [1,2,3]   # 값으로 쓰이는 [] → 리스트
nums[0]          # 변수 뒤 숫자 [] → 리스트 접근
```

---

## 🌍 URL Import

Whale은 HTML 터미널과 Python 터미널 모두에서 URL 기반 import를 사용합니다.

```whale
import 'https://example.com/helper.whl'
가져와 'https://example.com/helper.whl'
```

예시:

```whale
whale lang='kr'

가져와 'https://whale.imtdot.kr/lib/helper.whl'

출력[인사['승우']]
```

### Import Rules

- `.whl` 파일만 허용
- URL로만 가져오기
- 같은 URL은 한 번만 가져오기
- HTML 터미널은 `fetch()` 사용
- Python 터미널은 HTTP 요청 사용
- 가져온 파일은 현재 실행 환경에 함수/변수를 등록

### CORS Notice for HTML Terminal

HTML 터미널에서 다른 도메인의 `.whl` 파일을 가져올 때 브라우저 CORS 정책 때문에 차단될 수 있습니다.

이 경우 Whale HTML 터미널은 다음처럼 표시합니다.

```text
ImportError: CORS 오류가 발생했습니다.
```

해결 방법:

- `.whl` 파일을 CORS가 허용된 서버에 올리기
- 공식 Whale 라이브러리 경로 사용
- 같은 도메인에서 모듈 제공

추천 공식 경로:

```whale
가져와 'https://whale.imtdot.kr/lib/helper.whl'
```

---

## 🖥 Terminal Commands

```text
open
editor
help
clear
whale shutdown
```

> `whale shutdown`은 Python 터미널에서 종료 명령으로 사용됩니다.

---

## 💡 Philosophy

> Make programming readable like a sentence.

---

## 🧑‍💻 Author

Project by iM티닷 | Big Industry
