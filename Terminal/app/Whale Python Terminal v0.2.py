import re
import os
import webbrowser

variables = {}
functions = {}
current_lang = "en"


def wprint(text=""):
    print(text)


def get_inside(text, start, end):
    s = text.find(start)
    e = text.rfind(end)

    if s == -1 or e == -1 or e <= s:
        return ""

    return text[s + 1:e].strip()


def get_indent(line):
    return len(line) - len(line.lstrip(" "))


def is_print(line):
    return (
        line.startswith("print[") and line.endswith("]")
    ) or (
        line.startswith("출력[") and line.endswith("]")
    )


def is_assignment(line):
    if line.startswith("whale lang="):
        return False

    if line.startswith("print[") or line.startswith("출력["):
        return False

    return "=" in line


def is_block_start(line, block_type):
    if block_type == "repeat":
        return (line.startswith("repeat(") or line.startswith("반복(")) and line.endswith(":")

    if block_type == "func":
        return (line.startswith("func(") or line.startswith("함수(")) and line.endswith(":")

    return False


def collect_block(lines, start_index):
    result = []
    end = start_index
    base_indent = get_indent(lines[start_index])

    for i in range(start_index + 1, len(lines)):
        line = lines[i]

        if not line.strip():
            continue

        indent = get_indent(line)

        if indent <= base_indent:
            break

        result.append(line[base_indent + 4:])
        end = i

    return result, end


def split_string_concat(expr):
    result = []
    current = ""
    quote = None

    for i, ch in enumerate(expr):
        if ch in ("'", '"') and (i == 0 or expr[i - 1] != "\\"):
            quote = None if quote == ch else ch

        if ch == "+" and quote is None:
            result.append(current.strip())
            current = ""
        else:
            current += ch

    if current.strip():
        result.append(current.strip())

    has_string = False

    for part in result:
        if (part.startswith("'") and part.endswith("'")) or (
            part.startswith('"') and part.endswith('"')
        ):
            has_string = True
        elif part in variables and isinstance(variables[part], str):
            has_string = True

    return result if has_string else [expr]


def find_operator(expr, op):
    quote = None
    i = 0

    while i < len(expr):
        ch = expr[i]

        if ch in ("'", '"') and (i == 0 or expr[i - 1] != "\\"):
            quote = None if quote == ch else ch

        if quote is None and expr[i:i + len(op)] == op:
            if op == "-" and i == 0:
                i += 1
                continue
            return i

        i += 1

    return -1


def eval_expression(expr, lang):
    expr = expr.strip()

    string_parts = split_string_concat(expr)

    if len(string_parts) > 1:
        return "".join(str(eval_value(part, lang)) for part in string_parts)

    math_ops = ["///", "//", "**", "*", "/", "-", "+"]

    for op in math_ops:
        idx = find_operator(expr, op)

        if idx > -1:
            left = eval_value(expr[:idx], lang)
            right = eval_value(expr[idx + len(op):], lang)

            if op == "+":
                return float(left) + float(right)
            if op == "-":
                return float(left) - float(right)
            if op == "*":
                return float(left) * float(right)
            if op == "/":
                return float(left) / float(right)
            if op == "//":
                return int(float(left) // float(right))
            if op == "///":
                return int(float(left) % float(right))
            if op == "**":
                return float(left) ** float(right)

    return expr


def eval_value(expr, lang):
    expr = expr.strip()

    if (expr.startswith("'") and expr.endswith("'")) or (
        expr.startswith('"') and expr.endswith('"')
    ):
        return expr[1:-1]

    if expr.startswith("int(") and expr.endswith(")"):
        return int(eval_value(get_inside(expr, "(", ")"), lang))

    if expr.startswith("정수(") and expr.endswith(")"):
        return int(eval_value(get_inside(expr, "(", ")"), lang))

    if expr.startswith("input(") and expr.endswith(")"):
        msg = eval_value(get_inside(expr, "(", ")"), lang)
        return input(str(msg))

    if expr.startswith("입력(") and expr.endswith(")"):
        msg = eval_value(get_inside(expr, "(", ")"), lang)
        return input(str(msg))

    if expr in variables:
        return variables[expr]

    if re.fullmatch(r"-?\d+(\.\d+)?", expr):
        if "." in expr:
            return float(expr)
        return int(expr)

    return eval_expression(expr, lang)


def execute_line(line, lang):
    line = line.strip()

    if not line or line.startswith("#"):
        return

    if line.startswith("whale lang="):
        set_language(line)
        return

    if is_print(line):
        value = get_inside(line, "[", "]")
        wprint(eval_value(value, lang))
        return

    if is_assignment(line):
        eq_index = line.find("=")
        key = line[:eq_index].strip()
        value = line[eq_index + 1:].strip()
        variables[key] = eval_value(value, lang)
        return

    if line in functions:
        execute_lines(functions[line], lang)
        return

    wprint(f"Error: Cannot execute code: {line}")


def execute_lines(lines, lang):
    i = 0

    while i < len(lines):
        line = lines[i]
        trimmed = line.strip()

        if not trimmed or trimmed.startswith("#"):
            i += 1
            continue

        if is_block_start(trimmed, "repeat"):
            count_raw = get_inside(trimmed, "(", ")")
            block, end = collect_block(lines, i)

            count = eval_value(count_raw, lang)

            if count_raw == "r":
                wprint("Infinite repeat is limited to 20 times.")
                count = 20

            for _ in range(int(count)):
                execute_lines(block, lang)

            i = end + 1
            continue

        if is_block_start(trimmed, "func"):
            name = get_inside(trimmed, "(", ")")
            block, end = collect_block(lines, i)
            functions[name] = block

            i = end + 1
            continue

        execute_line(trimmed, lang)
        i += 1


def set_language(line):
    global current_lang

    if "'kr'" in line or '"kr"' in line:
        current_lang = "kr"
    else:
        current_lang = "en"

    wprint(f"Language mode: {current_lang}")


def run_whale(code):
    global current_lang

    variables.clear()
    functions.clear()

    raw_lines = code.replace("\r", "").split("\n")
    lines = [
        line for line in raw_lines
        if line.strip() and not line.strip().startswith("#")
    ]

    lang = "en"

    if lines and lines[0].strip().startswith("whale lang="):
        first = lines.pop(0).strip()

        if "'kr'" in first or '"kr"' in first:
            lang = "kr"
        elif "'en'" in first or '"en"' in first:
            lang = "en"

    current_lang = lang
    execute_lines(lines, lang)


def open_whl_file():
    path = ""

    try:
        import tkinter as tk
        from tkinter import filedialog

        root = tk.Tk()
        root.withdraw()

        path = filedialog.askopenfilename(
            title="Open Whale File",
            filetypes=[("Whale files", "*.whl"), ("All files", "*.*")]
        )

        root.destroy()

    except Exception:
        wprint("Tkinter not available. Switching to manual path input.")
        path = input("Enter .whl file path >>> ").strip().strip('"').strip("'")

    if not path:
        return

    if not path.endswith(".whl"):
        wprint("Error: Only .whl files can be executed.")
        return

    try:
        with open(path, "r", encoding="utf-8") as f:
            code = f.read()

        wprint("")
        wprint(f"Running: {path}")
        wprint("--------------------------------")
        run_whale(code)
        wprint("--------------------------------")
        wprint("Finished.")
        wprint("")

    except Exception as e:
        wprint(f"Error: {e}")


def show_help():
    wprint("Whale Help")
    wprint("")
    wprint("Terminal commands")
    wprint("  open    : Open and run a .whl file")
    wprint("  editor  : Open https://whale.imtdot.kr/editor")
    wprint("  help    : Show this help")
    wprint("  clear   : Clear the screen")
    wprint("  exit    : Exit Whale Terminal")
    wprint("")
    wprint("Direct execution examples")
    wprint("  print['hello whale']")
    wprint("  whale lang='kr'")
    wprint("  출력['안녕 웨일']")
    wprint("  name = input('Name >>> ')")
    wprint("  print['Hello ' + name]")
    wprint("  print[1 + 1]")
    wprint("")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def handle_command(value):
    global current_lang

    if value == "open":
        open_whl_file()
        return

    if value == "editor":
        webbrowser.open("https://whale.imtdot.kr/editor")
        wprint("Opening Whale Editor...")
        return

    if value == "help":
        show_help()
        return

    if value == "clear":
        clear_screen()
        boot()
        return

    if value == "exit":
        raise SystemExit

    execute_line(value, current_lang)


def boot():
    wprint("[ Whale Terminal ]")
    wprint("Whale Python Terminal v0.2")
    wprint("Commands: open, editor, help, clear, exit")
    wprint("You can also type Whale code directly.")
    wprint("")


def main():
    boot()

    while True:
        try:
            value = input("whale> ").strip()

            if not value:
                continue

            handle_command(value)

        except KeyboardInterrupt:
            wprint("\nUse exit to close Whale Terminal.")

        except SystemExit:
            wprint("Bye.")
            break

        except Exception as e:
            wprint(f"Error: {e}")


if __name__ == "__main__":
    main()
