import subprocess

pc = input("Номер пк: ")

rdp = f"""
cmdkey /generic:{pc} /user:student /pass:edu-759
mstsc /v:{pc}
"""

subprocess.run([
    "powershell",
    "-Command",
    rdp
], check=True)
