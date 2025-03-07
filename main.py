import subprocess

input()

rdp = f"""
cmdkey /generic:{} /user:ВашЛогин /pass:ВашПароль
mstsc /v:192.168.1.100
"""

subprocess.run([
    "powershell"
    "-ExecutionPolicy", "Bypass",
    "-Command", rdp
], check=True)
