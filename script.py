import subprocess

def restart_or_open(program_name, program_path):
    try:
        subprocess.run(["taskkill", "/f", "/im", program_name], shell=True)
        subprocess.Popen(program_path, shell=True)
        print(f"Restarted or started: {program_name}")
    except Exception as e:
        print(f"Error restarting or starting: {program_name} - {e}")

def main():
    apps = [
        {"name": "HWiNFO64.exe", "path": "C:\\Program Files\\HWiNFO64\\HWiNFO64.EXE"},
        {"name": "MSIAfterburner.exe", "path": "C:\\Program Files (x86)\\MSI Afterburner\\MSIAfterburner.exe"},
        {"name": "RTSS.exe", "path": "C:\\Program Files (x86)\\RivaTuner Statistics Server\\RTSS.exe"}
    ]

    for app in apps:
        restart_or_open(app["name"], app["path"])

if __name__ == "__main__":
    main()
