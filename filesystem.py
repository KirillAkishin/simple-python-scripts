import os
import os.path
import sys
from pathlib import Path

def rel_walk(root=".", start=None):
    for path, _, files in os.walk(root):
        for name in files:
            filename = os.path.join(path, name)
            relative_filename = os.path.relpath(filename, start=start)
            yield relative_filename

def walk(root="."):
    for path, _, files in os.walk(root):
        for name in files:
            filename = os.path.join(path, name)
            yield filename

def count(root="."):
    cnt = 0
    for _, _, files in os.walk(root):
        for _ in files:
            cnt += 1
    return cnt

# todo: du-command
def total_size(root="."):
    """
    du [ROOT] # Directories only
    """

    ttl_size = 0
    for path, _, files in os.walk(root):
        for name in files:
            ttl_size += os.path.getsize(os.path.join(path, name))
    return ttl_size

def filesize(filename):
    """
    du -h [FILENAME] # Files only
    """

    size = os.stat(filename).st_size
    if size == 0:
        return False
    if (size // 1024) == 0:
        return f"{size} B"
    size /= 1024
    if (size // 1024) == 0:
        return f"{size:.1f} KiB"
    size /= 1024
    if (size // 1024) == 0:
        return f"{size:.1f} MiB"
    size /= 1024
    return f"{size:.1f} GiB"


def resolve_path(path_str: str) -> Path:
    expanded_vars = os.path.expandvars(path_str)
    expanded_user = Path(expanded_vars).expanduser()
    absolute_path = expanded_user.resolve()
    return absolute_path

def smart_resolve(path_str: str, *, strict: bool = True) -> Path:
    def check_invalid_chars(p: str) -> None:
        if sys.platform.startswith('win'):
            forbidden = '<>:"/\\|?*'
            if any(ch in forbidden for ch in p):
                raise ValueError(f"Path contains invalid characters: {forbidden}")
            if any(ord(ch) < 32 for ch in p):
                raise ValueError("Path contains control characters (ASCII < 32)")
        else:
            if '\x00' in p:
                raise ValueError("Path contains invalid NULL character: '\\x00'")

    expanded_vars = os.path.expandvars(path_str)
    expanded_user = Path(expanded_vars).expanduser()
    check_invalid_chars(str(expanded_user))
    abs_path = expanded_user.resolve()
    if abs_path.exists():
        if not os.access(abs_path, os.R_OK):
            msg = f"No permission to read file: `{abs_path}`"
            if strict:
                raise PermissionError(msg)
            else:
                print(f"Warning! {msg}", file=sys.stderr)
    else:
        msg = f"Path does not exist: '{abs_path}'"
        if strict:
            raise FileNotFoundError(msg)
        else:
            print(f"Warning! '{msg}'", file=sys.stderr)
    return abs_path

def touch_file(filename: str, atime_only:bool=False):
    """
    touch [-a] [FILENAME]
    """

    if not os.path.exists(filename):
        with open(filename, 'a'):
            pass
    current_time = time.time()
    if atime_only:
        mtime = os.path.getmtime(filename)
        atime = current_time
    else:
        atime = mtime = current_time
    os.utime(filename, (atime, mtime))

