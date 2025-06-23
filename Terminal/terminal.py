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
        raise RuntimeError(f"❌ Command blocked for safety: contains a restricted operation")

    try:
        result = subprocess.run(what, shell=True, text=True, capture_output=True)
        if len(result.stderr) != 0:
            raise RuntimeError()
        return result.stdout.strip() if result.stdout else result.stderr.strip()
    except Exception as e:
        raise RuntimeError(f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    mcp.run(transport="stdio")
