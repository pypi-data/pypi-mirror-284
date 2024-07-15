# Checks what os is running

### Tested against Windows 10/Android/Linux / Python 3.11 / Anaconda

### pip install osversionchecker

### The main focus is differentiating classic Linux / Android


``` py
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

from osversionchecker import check_os

os_system_points, active_os_system = check_os()
print(active_os_system)
print(os_system_points)


windows
{'windows': 5, 'linux': 0, 'darwin': 0, 'android': 0}


```