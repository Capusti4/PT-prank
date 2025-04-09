import subprocess



pc = input("Номер пк: ")

mount_disk = f"""
    mount Z 'FileSystem' \\\\{pc}\\d
"""

go_to_disk = """
    pushd Z
"""

subprocess.run(
    [
        'powershell',
        '-Command',
        mount_disk,
        go_to_disk
    ], check=True
)
