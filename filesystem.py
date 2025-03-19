import os
import os.path

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

def total_size(root="."):
    ttl_size = 0
    for path, _, files in os.walk(root):
        for name in files:
            ttl_size += os.path.getsize(os.path.join(path, name))
    return ttl_size

def filesize(filename):
    from os import stat
    size = stat(filename).st_size
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
