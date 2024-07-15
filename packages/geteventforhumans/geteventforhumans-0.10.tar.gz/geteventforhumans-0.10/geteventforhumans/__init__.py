import ctypes
import time
import threading
import subprocess
import sys
import struct
from .parsekeyevents import key_labels
from collections import deque

import shutil
import os

modulecfg = sys.modules[__name__]
modulecfg.screen_size_dict = {}
subprocess._USE_VFORK = False
subprocess._USE_POSIX_SPAWN = False
FORMAT = "llHHI"
chunk_size = struct.calcsize(FORMAT)
unpack_fu = struct.Struct(FORMAT).unpack

ResetAll = "\033[0m"

Bold = "\033[1m"
Dim = "\033[2m"
Underlined = "\033[4m"
Blink = "\033[5m"
Reverse = "\033[7m"
Hidden = "\033[8m"

ResetBold = "\033[21m"
ResetDim = "\033[22m"
ResetUnderlined = "\033[24m"
ResetBlink = "\033[25m"
ResetReverse = "\033[27m"
ResetHidden = "\033[28m"

Default = "\033[39m"
Black = "\033[30m"
Red = "\033[31m"
Green = "\033[32m"
Yellow = "\033[33m"
Blue = "\033[34m"
Magenta = "\033[35m"
Cyan = "\033[36m"
LightGray = "\033[37m"
DarkGray = "\033[90m"
LightRed = "\033[91m"
LightGreen = "\033[92m"
LightYellow = "\033[93m"
LightBlue = "\033[94m"
LightMagenta = "\033[95m"
LightCyan = "\033[96m"
White = "\033[97m"

BackgroundDefault = "\033[49m"
BackgroundBlack = "\033[40m"
BackgroundRed = "\033[41m"
BackgroundGreen = "\033[42m"
BackgroundYellow = "\033[43m"
BackgroundBlue = "\033[44m"
BackgroundMagenta = "\033[45m"
BackgroundCyan = "\033[46m"
BackgroundLightGray = "\033[47m"
BackgroundDarkGray = "\033[100m"
BackgroundLightRed = "\033[101m"
BackgroundLightGreen = "\033[102m"
BackgroundLightYellow = "\033[103m"
BackgroundLightBlue = "\033[104m"
BackgroundLightMagenta = "\033[105m"
BackgroundLightCyan = "\033[106m"
BackgroundWhite = "\033[107m"

colors2rotate = [
    LightRed,
    LightGreen,
    LightYellow,
    LightBlue,
    LightMagenta,
    LightCyan,
    White,
]


def start_getevent_for_humans(
    adb_path=None,
    logfolder=None,
    device_serial="127.0.0.1:5555",
    runasdaemon=True,
    bufsize=256000,
    shell=True,
    multiply=24,
    keepbuffer=4,
    ljust=12,
    devices_to_observe=(),
):
    r"""
The function start_getevent_for_humans in the module is designed to capture and log Android device input events in a human-readable format. Here's a breakdown of each argument that can be passed to this function, along with their options and descriptions:

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

bufsize (optional, default: 256000):

Type: int
Description: The buffer size for reading data from the input streams. This size can impact performance and responsiveness in capturing event data.
shell (optional, default: True):

Type: bool
Description: Specifies whether the subprocesses should be invoked within a shell environment. This can affect the behavior of command execution and is typically set to True to ensure compatibility with command line parsing.
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
Description: A tuple containing the identifiers of specific input devices to monitor, e.g., ("event3", "event4"). If empty, the script may default to monitoring all available devices, depending on the implementation.
Usage Example
To initiate the event monitoring for specific devices with custom settings, you might call the function like this:

python
Copiar código
start_getevent_for_humans(
    adb_path="/usr/bin/adb",
    logfolder="/path/to/logfolder",
    device_serial="example_device_serial",
    runasdaemon=False,
    bufsize=1024,
    shell=True,
    multiply=10,
    keepbuffer=5,
    ljust=15,
    devices_to_observe=("event1", "event2")
)
This setup specifies all the parameters with custom values, tailoring the function behavior to specific monitoring needs.







    """

    def get_screen_data_with_adb(
        device_serial,
        inputdev="/dev/input/event4",
        adb_path=None,
        bufsize=256000,
        shell=True,
    ):
        adbsh = UniversalADBExecutor(adb_path, device_serial)

        getmax = (
            f"""getevent -lp {inputdev}"""
            + """ | grep "ABS_MT_POSITION" | awk 'BEGIN{FS="max[[:space:]]+";}{print $2}' | awk 'BEGIN{FS=",";}{printf $1" "}' | xargs"""
        )
        stdout, stderr, returncode = (
            adbsh.shell_with_capturing_import_stdout_and_stderr(
                getmax,
                debug=True,
                ignore_exceptions=False,
            )
        )
        p = stdout.decode("utf-8")
        x_max, y_max = p.split()
        x_max = int(x_max.strip())
        y_max = int(y_max.strip())
        stdout, stderr, returncode = (
            adbsh.shell_with_capturing_import_stdout_and_stderr(
                """wm size | awk '{print $NF}'""".encode("utf-8"),
                debug=True,
                ignore_exceptions=False,
            )
        )
        screensize = stdout.decode("utf-8").strip().split("x")
        screen_width, screen_height = screensize
        screen_width = int(screen_width.strip())
        screen_height = int(screen_height.strip())
        return x_max, y_max, screen_width, screen_height

    def killthread(threadobject):
        # based on https://pypi.org/project/kthread/
        if not threadobject.is_alive():
            return True
        tid = -1
        for tid1, tobj in threading._active.items():
            if tobj is threadobject:
                tid = tid1
                break
        if tid == -1:
            sys.stderr.write(f"{threadobject} not found")
            return False
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            ctypes.c_long(tid), ctypes.py_object(SystemExit)
        )
        if res == 0:
            return False
        elif res != 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
            return False
        return True

    class Subprocesswrite(subprocess.Popen):
        def __init__(self, *args, **kwargs):
            self.nameofevent = ""

            super().__init__(
                *args,
                **{
                    "stdin": subprocess.PIPE,
                    "stdout": subprocess.PIPE,
                    "stderr": subprocess.DEVNULL,
                    **adbshellexecuter.invisibledict,
                    **kwargs,
                },
            )
            self.t1 = threading.Thread(
                target=self._readstdout, name="stdout", daemon=runasdaemon
            )
            self.stop_thread1 = False
            self.t1.start()
            self.flushdata = False
            self.logfileopened = False
            self.tupledeque = deque([], maxlen=6)
            self.endsymbols = [(0, 0, 0, 0), (0, 0, 2, 0)]
            self.mouseevents = (3, 54), (3, 53)
            self.keyevents = (4, 4)

        def stdinwrite(self, data):
            self.nameofevent = data.split(maxsplit=1)[-1].strip()
            if isinstance(data, str):
                data = data.encode()
            self.stdin.write(data + b"\n")
            self.stdin.flush()
            return data.decode("utf-8", "backslashreplace")

        def createiter(self, channel, chunksize):
            if adbshellexecuter.iswindows:

                def newlinessubstituted():
                    nonlocal datachunk
                    while b"\r\n" in datachunk:
                        datachunk = datachunk.replace(b"\n", b"")

                rest = b""
                while data := channel.read(chunk_size * multiply):
                    try:
                        datachunk = (
                            rest.to_bytes() if hasattr(rest, "to_bytes") else rest
                        ) + data
                        newlinessubstituted()
                        if b"\n" in datachunk:
                            continue
                        while len(datachunk) >= chunksize * keepbuffer:
                            try:
                                yield datachunk[:chunksize]
                                datachunk = datachunk[chunksize:]
                            except Exception:
                                break
                        rest = datachunk
                    except Exception:
                        pass
            else:
                while data := channel.read(chunk_size):
                    yield data

        def _readstdout(self):
            cachedict = {}
            unpackeddatatuple = ()
            mylogfile = None
            last_chunk_counter = 0
            tupledeque = deque([], maxlen=6)
            try:
                for l in self.createiter(self.stdout, chunksize=chunk_size):
                    last_chunk_counter += 1
                    if self.stop_thread1:
                        break
                    if not self.logfileopened:
                        if hasattr(self, "save_data"):
                            try:
                                if self.save_data:
                                    mylogfile = open(
                                        self.save_data, "a", encoding="utf-8"
                                    )
                                    self.logfileopened = True
                            except Exception:
                                pass
                    try:
                        keyparsed = " " * 16
                        unpackeddatatuple = cachedict.setdefault(l, unpack_fu(l))
                        unpackeddatatupleasstring = cachedict.setdefault(
                            unpackeddatatuple,
                            "|".join(str(q).ljust(ljust) for q in unpackeddatatuple),
                        )

                        xstring = ""
                        try:
                            if hasattr(self, "screen_width") and self.screen_width:
                                if unpackeddatatuple[2:4] in self.mouseevents:
                                    ycoord = int(
                                        unpackeddatatuple[4]
                                        * self.screen_height
                                        / self.y_max
                                    )
                                    try:
                                        xcoord = int(
                                            tupledeque[-1][1]
                                            * self.screen_width
                                            / self.x_max
                                        )
                                        xstring = f"x:{xcoord}, "
                                    except Exception:
                                        pass
                                    keyparsed = f"{xstring}y:{ycoord}".ljust(16)
                                elif unpackeddatatuple[1] > 0:
                                    try:
                                        xcoord = int(
                                            unpackeddatatuple[1]
                                            * self.screen_width
                                            / self.x_max
                                        )
                                        if xcoord < self.screen_width:
                                            keyparsed = f"x:{xcoord}".ljust(16)
                                    except Exception:
                                        pass
                        except Exception:
                            pass
                        tupledeque.append(unpackeddatatuple)
                        if unpackeddatatuple[2:4] == self.keyevents:
                            keyparsed = parsekeyevents.key_labels.get(
                                unpackeddatatuple[4], ""
                            ).ljust(16)

                        unpackeddata = (
                            "|" + unpackeddatatupleasstring + "|" + keyparsed + "|"
                        )
                        try:
                            if (
                                hasattr(self, "save_data")
                                and self.save_data
                                and mylogfile
                                and self.logfileopened
                            ):
                                mylogfile.write(unpackeddata)
                                mylogfile.write(ascii(l))
                                mylogfile.write("\n")
                                mylogfile.flush()
                        except Exception:
                            pass

                        string2printcolored = (
                            colors2rotate[
                                alldevsdict[self.nameofevent] % len(colors2rotate)
                            ]
                            + unpackeddata
                            + ResetAll
                        )

                    except Exception:
                        pass
                        unpackeddata = "000000000000000000000000000000000000000"
                    sys.stdout.write(
                        f"{self.nameofevent}{string2printcolored}{ascii(l)}\n"
                    )
                    sys.stdout.flush()
                    # alllasttuples.append(unpackeddatatuple)
                    try:
                        if (
                            unpackeddatatuple[1:] in self.endsymbols
                            or unpackeddatatuple[:4] in self.endsymbols
                        ):
                            print(
                                f"{BackgroundLightYellow}Size of last chunk: {last_chunk_counter} / {last_chunk_counter*chunk_size} bytes{ResetAll}"
                            )
                            # alllasttuples.clear()
                            unpackeddatatuple = ()
                            last_chunk_counter = 0
                    except Exception:
                        pass

            finally:
                if hasattr(self, "save_data") and self.save_data:
                    try:
                        mylogfile.close()
                    except Exception:
                        pass

        def kill(self, *args, **kwargs):
            self.stop_thread1 = True
            time.sleep(2)
            killthread(self.t1)
            super().kill(*args, **kwargs)

        def terminate(self, *args, **kwargs):
            self.stop_thread1 = True
            time.sleep(2)
            killthread(self.t1)
            super().terminate(*args, **kwargs)

    import adbshellexecuter

    adbshellexecuter.SubprocessWrite = Subprocesswrite
    UniversalADBExecutor = adbshellexecuter.UniversalADBExecutor

    def startobservingthread(event, save_file):
        try:
            x_max, y_max, screen_width, screen_height = get_screen_data_with_adb(
                device_serial=device_serial, inputdev=event, adb_path=adb_path
            )
        except Exception:
            pass
            x_max, y_max, screen_width, screen_height = None, None, None, None
        adbshnew = UniversalADBExecutor(adb_path, device_serial)
        # adbshnew.save_data = save_file

        adbshnew.create_non_blocking_proc(bufsize=256000, shell=True)
        adbshnew.proc.save_data = save_file
        adbshnew.proc.x_max = x_max
        adbshnew.proc.y_max = y_max
        adbshnew.proc.screen_width = screen_width
        adbshnew.proc.screen_height = screen_height
        adbshnew.x_max = x_max
        adbshnew.y_max = y_max
        adbshnew.screen_width = screen_width
        adbshnew.screen_height = screen_height
        adbshnew.save_data = save_file
        adbshnew.proc.stdinwrite(f"cat {event}\n")
        allrunningsubprocesses.append(adbshnew.proc)

    alldevsdict = {}
    adb_path = adb_path or shutil.which("adb")

    adbsh = UniversalADBExecutor(adb_path, device_serial)
    adbsh.non_shell_adb_commands_without_s_serial(f"connect {device_serial}")
    print("Getting valid devices...")
    stdout, stderr, returncode = adbsh.shell_with_capturing_import_stdout_and_stderr(
        r'find /dev/input | grep -Ev "^/dev/input$" | sort'
    )
    alldevs = [
        h for x in stdout.decode("utf-8").strip().splitlines() if (h := x.strip())
    ]
    for ini, dev in enumerate(alldevs):
        alldevsdict[dev] = ini
    if logfolder:
        os.makedirs(logfolder, exist_ok=True)
    allrunningsubprocesses = []
    tstamp = str(time.time()).split(".")[0]
    if devices_to_observe:
        devicestouse = [
            x.strip().lower().rsplit("/", 1)[-1].strip() for x in devices_to_observe
        ]
    else:
        devicestouse = []
    for dev in alldevs:
        if devicestouse:
            if not any(dev.endswith(device) for device in devicestouse):
                continue
        print(dev)
        save_file = None
        if logfolder:
            save_file = os.path.join(
                logfolder,
                dev.replace("/", "_").strip("_") + f"_{tstamp}" + ".txt",
            )

        threading.Thread(
            target=startobservingthread, args=(dev, save_file), daemon=runasdaemon
        ).start()
    print("Press Ctrl-C to quit...")
    try:
        while True:
            try:
                time.sleep(0.01)
            except KeyboardInterrupt:
                print("\n\nShutting down...")
                try:
                    time.sleep(1)
                except KeyboardInterrupt:
                    pass
                break
    except KeyboardInterrupt:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            pass
    try:
        for p in allrunningsubprocesses:
            print(f"Killing {p}")
            try:
                p.kill()
            except Exception as e:
                print(e)
            except KeyboardInterrupt:
                continue
    except KeyboardInterrupt:
        pass


