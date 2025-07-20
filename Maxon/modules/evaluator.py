from Maxon.init import VERSION, START_TIME
import io
import contextlib
from pathlib import Path

__name__ = "Evaluator"
__description__ = "Выполняет Python код, переданный в аргументы"
__version__ = "1.2"
__author__ = "@nerkux"

async def handle(packet, args, client):
    if isinstance(args, (list, tuple)):
        code = "\n".join(args).strip()
    else:
        code = str(args).strip()

    if code.startswith("```") and code.endswith("```"):
        parts = code.splitlines()
        parts = parts[1:-1]
        if parts and parts[0].startswith(("python", "py")):
            parts = parts[1:]
        code = "\n".join(parts).strip()

    if not code:
        return "❌ Ошибка: передайте код для выполнения."

    buf = io.StringIO()
    try:
        local_vars = {}
        with contextlib.redirect_stdout(buf):
            exec(compile(code, "<evaluator>", "exec"), {}, local_vars)
    except Exception as e:
        return f"❌ Ошибка выполнения:\n{e}"
    else:
        output = buf.getvalue().strip()
        return output or "✅ Код выполнен без вывода."

def register(handlers):
    handlers[".eval"] = handle
    handlers[".exec"] = handle
