from mcp.server.fastmcp import FastMCP
import subprocess
import re

mcp = FastMCP("terminal")

BLOCKED_KEYWORDS = [
    "del", "erase", "format", "shutdown", "taskkill", "net user",
    "rd", "reg delete", "bootcfg", "bcdedit", "cipher /w",
    "vssadmin delete", "diskpart", "attrib -h -r -s", 
    "powershell remove-item", "powershell start-process", 
    "powershell stop-computer", "rmdir /s", "sethc", "copy con"
]

def is_unsafe(cmd: str) -> bool:
    lowered = re.sub(r'\s+', ' ', cmd.lower())
    for keyword in BLOCKED_KEYWORDS:
        if re.search(rf"\b{re.escape(keyword)}\b", lowered):
            return True
    return False

@mcp.tool()
def cmdRun(what: str) -> str:
    if is_unsafe(what):
        return f"❌ Command blocked for safety: contains a restricted operation"

    try:
        result = subprocess.run(what, shell=True, text=True, capture_output=True)
        return result.stdout.strip() if result.stdout else result.stderr.strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
