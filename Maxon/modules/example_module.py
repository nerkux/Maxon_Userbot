from Maxon.init import VERSION, START_TIME

__name__ = "module_name"
__description__ = "module_description"
__version__ = "1.0"
__author__ = "@username"

async def handle(packet, args):
    return "example answer"

def register(handlers):
    handlers[".example"] = handle
