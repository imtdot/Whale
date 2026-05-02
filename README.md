# 🐋 Whale Programming Language

[![Download](https://img.shields.io/badge/Download-Whale-blue?style=for-the-badge&logo=github)](https://github.com/imtdot/Whale/releases)

[![Download](https://img.shields.io/badge/Go-Website-green?style=for-the-badge&logo=website)](https://whale.imtdot.kr)

**Whale** is a beginner-friendly programming language designed to be **easy to read, easy to write, and easy to learn**.

It supports both **English and Korean syntax**, making coding more accessible to everyone.

---

## ✨ Features

* 🌐 Dual language support (English / Korean)
* 🧠 Simple and intuitive syntax
* 🔤 Supports English, numbers, and Korean in identifiers
* 🚀 Beginner-friendly design
* 📦 Minimal and clean structure

---

## 📁 File Extension

```
.whl
```

---

## 🌐 Language Mode

Whale supports two modes:

```whl
whale lang='en'   # English (default)
whale lang='kr'   # Korean
```

---

## 🖨 Output

### English

```whl
print['hello whale']
```

### Korean

```whl
출력['안녕 웨일']
```

---

## ⌨ Input

### English

```whl
name = input('Enter your name >>> ')
```

### Korean

```whl
이름 = 입력('이름을 입력하세요 >>> ')
```

---

## 📦 Variables

```whl
name = 'whale'
age = int(14)
```

---

## ➕ Operators

| Operation | Symbol |
| --------- | ------ |
| Add       | +      |
| Subtract  | -      |
| Multiply  | *      |
| Divide    | /      |
| Quotient  | //     |
| Remainder | ///    |
| Power     | **     |

---

## 🔁 Loop

### English

```whl
repeat(3):
    print['hi']
```

### Korean

```whl
반복(3):
    출력['안녕']
```

### Infinite Loop

```whl
repeat(r)
```

---

## 🧠 Functions

### Define

```whl
func(sayhi):
    print['hi whale']
```

### Call

```whl
sayhi
```

---

## 🔤 Identifier Rules

Allowed:

* English letters (a-z, A-Z)
* Numbers (0-9)
* Korean characters (가-힣)

Not allowed:

* Spaces ❌
* Special characters ❌

---

## 🧱 Syntax Rules

* Indentation-based (like Python)
* No semicolons
* Use `#` for comments

```whl
# This is a comment
```

---

## 🧪 Example

```whl
whale lang='kr'

이름 = 입력('이름을 입력하세요 >>> ')
출력['안녕하세요 ' + 이름]

반복(3):
    출력['Whale is easy!']

함수(인사):
    출력['반가워요!']

인사
```

---

## 🚀 Goal

> Make programming accessible to **everyone**, not just developers.

---

## 📌 Roadmap

* [ ] Condition statements (if / 만약)
* [ ] Lists / Arrays
* [ ] File I/O
* [ ] Package system
* [ ] Official Interpreter

---

## 🤝 Contributing

This project is in early development.
Feel free to open issues or suggest improvements!

---

## 📄 License

MIT License

---

## 💡 Author

Created by **iM티닷 | Big Industry** 🚀
