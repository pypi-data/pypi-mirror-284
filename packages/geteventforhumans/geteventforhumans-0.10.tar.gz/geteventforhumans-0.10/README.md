# Android's getevent for Humans!

### Tested against Windows 10/ Python 3.11 / Anaconda

### pip install geteventforhumans


[![YT](https://i.ytimg.com/vi/np2KZXZHzsY/maxresdefault.jpg)](https://www.youtube.com/watch?v=np2KZXZHzsY)
[https://www.youtube.com/watch?v=np2KZXZHzsY]()


```PY

The function start_getevent_for_humans in the module is designed to capture and log Android device input events in a human-readable format. 

adb_path (optional, default: None):
Type: str
Description: The file path to the Android Debug Bridge (ADB) executable. If not specified, the function attempts to locate ADB using the system's environment variables.

logfolder (optional, default: None):
Type: str
Description: The directory path where event logs should be saved. If not specified, the logs will not be saved

device_serial (optional, default: '127.0.0.1:5555'):
Type: str
Description: The serial number of the Android device to be monitored. This is crucial when multiple devices are connected to the ADB host.

runasdaemon (optional, default: True):
Type: bool
Description: If set to True, the threads started by this function will run as daemons, allowing the main program to exit without having to manually terminate these threads.

bufsize (optional, default: 0):
Type: int
Description: The buffer size for reading data from the input streams. This size can impact performance and responsiveness in capturing event data.

shell (optional, default: True):
Type: bool
Description: Specifies whether the subprocesses should be invoked within a shell environment. 

multiply (optional, default: 24):
Type: int
Description: Used as a multiplier in calculating the chunk size for data processing in some contexts. The exact usage should be confirmed within specific subprocess or threading implementations.


keepbuffer (optional, default: 4):
Type: int
Description: Determines the number of chunks to keep in memory buffer for processing, affecting how much past event data is accessible at any time.


ljust (optional, default: 12):
Type: int
Description: Specifies the padding length for string formatting within the logging output, ensuring alignment in log visualizations.


devices_to_observe (optional, default: empty tuple ()):
Type: tuple of str
Description: A tuple containing the identifiers of specific input devices to monitor, e.g., ("event3", "event4"). If empty, the script may default to monitoring all available devices.

Usage Example
To initiate the event monitoring for specific devices with custom settings, you might call the function like this:

from geteventforhumans import start_getevent_for_humans
import shutil

start_getevent_for_humans(
    adb_path=shutil.which("adb"),
    device_serial="127.0.0.1:5645",
    logfolder="c:\\neuelogsadb",
    runasdaemon=True,
    bufsize=0,
    shell=False,
    multiply=24,
    keepbuffer=1,
    ljust=12,
    devices_to_observe=("event3", "event4"),
)

```