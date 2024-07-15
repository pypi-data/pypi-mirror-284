import subprocess
import sys
import platform
import os
subprocess._USE_VFORK = False
subprocess._USE_POSIX_SPAWN = False

def check_os():
    """
    Determines the operating system by analyzing various system characteristics
    and assigns points based on detected features. The OS with the highest points
    is considered the active operating system.

    Returns:
        tuple: A dictionary with the points for each operating system and the 
        name of the detected active operating system.

    The function checks the following:
    - If the sys.executable path indicates a Windows system.
    - If the sys.executable path starts with '/data/data/' indicating an Android system.
    - The count of backslashes and slashes in the environment variables string.
    - The presence of certain files or directories that are specific to Windows or Android.
    - The output of certain shell commands that indicate an Android system.
    - The content of the uname command output to check for Linux, Darwin (macOS), or Android.
    - The platform information from the platform module to check for Linux, Darwin (macOS), or Android.
    - The sys.platform value to check for Linux, Darwin (macOS), Windows, or Android.
    - The sys.version string to check for Linux, Darwin (macOS), or Windows.
    """
    points = {
        "windows": 0,
        "linux": 0,
        "darwin": 0,
        "android": 0,
    }
    sysexe = str(sys.executable)

    try:
        if (sysexe[1] == ":") and (sysexe[2][2:].startswith("\\")):
            points["windows"] += 1
    except Exception:
        pass
    try:
        if sysexe.startswith("/data/data/"):
            points["android"] += 2
    except Exception:
        pass
    try:
        osenvstr = str(os.environ.__dict__)
        backslahes = osenvstr.count("\\")
        slahes = osenvstr.count("/")
        if backslahes / 10 > slahes:
            points["windows"] += 1
    except Exception:
        pass
    try:
        os.stat("c:\\pagefile.sys")
        points["windows"] += 1
    except Exception:
        pass
    try:
        os.stat("c:\\Windows\\System32")
        points["windows"] += 1
    except Exception:
        pass
    try:
        os.stat("/sdcard/DCIM")
        points["android"] += 2
    except Exception:
        pass
    try:
        os.stat("/sdcard/Downloads")
        points["android"] += 2
    except Exception:
        pass
    try:
        if (
            b"XXXXXXXXXXXXXXXXX"
            in subprocess.run(
                "if [[ -e /data/adb ]]; then echo XXXXXXXXXXXXXXXXX; fi",
                capture_output=True,
                shell=True,
            ).stdout
        ):
            points["android"] += 2

    except Exception:
        pass
    try:
        if (
            len(
                subprocess.run(
                    "getprop | grep -i sdk", capture_output=True, shell=True
                ).stdout.splitylines()
            )
            > 3
        ):
            points["android"] += 2
    except Exception:
        pass
    try:
        if (
            len(
                subprocess.run(
                    'pm list packages -f | grep -i "apk"',
                    capture_output=True,
                    shell=True,
                ).stdout.splitylines()
            )
            > 5
        ):
            points["android"] += 2
    except Exception:
        pass
    try:
        vax = (
            subprocess.run("uname -a", capture_output=True, shell=True)
            .stdout.splitylines()
            .strip()
            .lower()
        )
        if "linux" in vax:
            points["linux"] += 1
        elif "darwin" in vax:
            points["darwin"] += 1
        if "android" in vax:
            points["android"] += 2
            points["linux"] -= 1

    except Exception:
        pass

    try:
        vax = str(platform.platform()).lower()
        if "linux" in vax:
            points["linux"] += 1
        elif "darwin" in vax:
            points["darwin"] += 1
        if "android" in vax:
            points["android"] += 2
            points["linux"] -= 1
    except Exception:
        pass
    try:
        platystem = str(platform.system()).lower()
        if "linux" in platystem:
            points["linux"] += 1
        elif "darwin" in platystem:
            points["darwin"] += 1
        if "android" in platystem:
            points["android"] += 2
            points["linux"] -= 1
        if "windows" in platystem:
            points["windows"] += 1
    except Exception:
        pass
    try:
        if sys.platform == "linux":
            points["linux"] += 1
        elif sys.platform == "darwin":
            points["darwin"] += 1
        elif sys.platform == "win32":
            points["windows"] += 1
        elif "android" in sys.platform:
            points["android"] += 2
    except Exception:
        pass
    try:
        platystem = str(sys.version).lower()
        if "linux" in platystem:
            points["linux"] += 1
        elif "darwin" in platystem:
            points["darwin"] += 1
        if "android" in platystem:
            points["android"] += 2
            points["linux"] -= 1
        if "windows" in platystem:
            points["windows"] += 1
    except Exception:
        pass
    os_system_points = {
        xk: vk for xk, vk in sorted(points.items(), key=lambda x: x[1], reverse=True)
    }

    active_os_system = max(os_system_points, key=os_system_points.get)
    return os_system_points, active_os_system
