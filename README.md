# 🐋 Whale Programming Language

[![Download](https://img.shields.io/badge/Download-Whale-blue?style=for-the-badge&logo=github)](https://github.com/imtdot/Whale/releases)
[![Download](https://img.shields.io/badge/Go-Website-green?style=for-the-badge&)](https://whale.imtdot.kr)

**Whale** is a beginner-friendly programming language designed to be easy to read, easy to write, and easy to learn.

Whale supports both **English and Korean syntax**.

---

## ✨ Whale 0.2 Features

- 🌐 English / Korean syntax
- 🖨 Output: `print[]`, `출력[]`
- ⌨ Input: `input()`, `입력()`
- 📦 Variables
- 🔢 Integer conversion: `int()`, `정수()`
- ➕ Operators: `+`, `-`, `*`, `/`, `//`, `///`, `**`
- 🔁 Loops: `repeat()`, `반복()`
- 🧠 Functions: `func()`, `함수()`
- ✅ Conditions: `if`, `else`, `만약`, `아니면`
- 🔍 Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`

---

## 📁 File Extension

```txt
.whl
```

---

## 🌐 Language Mode

```whl
whale lang='en'   # English mode, default
whale lang='kr'   # Korean mode
```

---

## 🖨 Output

```whl
print['hello whale']
```

```whl
출력['안녕 웨일']
```

---

## ⌨ Input

```whl
name = input('Name >>> ')
print['Hello ' + name]
```

```whl
이름 = 입력('이름 >>> ')
출력['안녕 ' + 이름]
```

---

## 📦 Variables

```whl
name = 'whale'
age = int(14)
```

```whl
이름 = '웨일'
나이 = 정수(14)
```

---

## ➕ Operators

| Operation | Symbol |
|---|---|
| Add | `+` |
| Subtract | `-` |
| Multiply | `*` |
| Divide | `/` |
| Quotient | `//` |
| Remainder | `///` |
| Power | `**` |

---

## ✅ Conditions

### English

```whl
age = int(input('Age >>> '))

if(age >= 14):
    print['Middle school or older']
else:
    print['Still young']
```

### Korean

```whl
whale lang='kr'

나이 = 정수(입력('나이 >>> '))

만약(나이 >= 14):
    출력['중학생 이상입니다']
아니면:
    출력['아직 어려요']
```

---

## 🔁 Loop

```whl
repeat(3):
    print['hi']
```

```whl
반복(3):
    출력['안녕']
```

Infinite loop is limited in browser-based terminals for safety.

```whl
repeat(r):
    print['loop']
```

---

## 🧠 Functions

```whl
func(sayhi):
    print['hi whale']

sayhi
```

```whl
함수(인사):
    출력['안녕 웨일']

인사
```

---

## 🖥 Whale Terminal

Whale can run on two platforms:

- `Whale Terminal.html`
- `Whale Terminal.py`

### Terminal Commands

```txt
open
editor
help
clear
whale shutdown
```

`whale shutdown` exits the Python Terminal.

---

## 🌍 Website

- Homepage: https://whale.imtdot.kr
- Terminal: https://whale.imtdot.kr/terminal
- Editor: https://whale.imtdot.kr/editor
- Download: https://github.com/imtdot/Whale/releases

---

## 📦 Download

Download Whale from the official releases page:

https://github.com/imtdot/Whale/releases

---

## 📄 License

MIT License

---

## 🧑‍💻 Author

Copyright 2026 iM티닷 | Big Industry
