from Maxon.init import VERSION, START_TIME
from pathlib import Path
import importlib

__name__ = "List"
__description__ = "Lists all loaded modules"
__version__ = "1.0"
__author__ = "@nerkux"

MODULES_DIR = Path(__file__).parent / "modules"

async def handle(packet, args, client):
    modules_path = Path(__file__).parent
    lines = []
    for py_file in modules_path.glob("*.py"):
        if py_file.name == "__init__.py":
            continue
        mod_name = py_file.stem
        full_module_path = f"Maxon.modules.{mod_name}"
        try:
            module = importlib.reload(importlib.import_module(full_module_path))
            display_name = getattr(module, "__name__", mod_name)
            desc = getattr(module, "__description__", "—")
            ver = getattr(module, "__version__", "—")
            lines.append(f"▪️ {display_name} — {desc} (v{ver})")
        except Exception as e:
            lines.append(f"v `{mod_name}` — ошибка при загрузке: {e}")
    if not lines:
        return "Модули не найдены 😳"
    header = f"🧩 Список доступных модулей:\n"
    return "\n".join([header, *lines])

def register(handlers):
    handlers[".list"] = handle
