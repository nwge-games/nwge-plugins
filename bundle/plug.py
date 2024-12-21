"""
Nwge Bundle Plugin
------------------
Automatically create a bundle from a directory on every build. This will check
if any file present in the directory has been modified and if so, it will
create a bundle from the directory.
"""

import bip
from pathlib import Path

# Executable used to create the bundle. You can use a different tool if you
# want. Default is the official nwgebndl tool.
g_exe: str = "nwgebndl"

# Source directory from which the bundle will be created.
g_src: Path

# Destination bundle file.
g_dst: Path

def configure(settings: dict) -> bool:
  global g_exe
  if "exe" in settings:
    g_exe = settings["exe"]

  global g_src
  if "src" not in settings:
    bip.error("Source directory not specified.")
    return False

  g_src = Path(settings["src"])
  if not g_src.exists():
    bip.error("Source directory does not exist.")
    return False

  global g_dst
  if "dst" not in settings:
    bip.error("Destination bundle file not specified.")
    return False

  g_dst = Path(settings["dst"])

  return True

def clean() -> bool:
  if g_out.exists():
    g_out.unlink()
  return True

def want_run() -> bool:
  if not g_dst.exists():
    return True

  bndl_mod_time = g_dst.stat().st_mtime

  # only iterate top level since bundles don't include subdirectories
  for file in g_src.iterdir():
    if file.stat().st_mtime > bndl_mod_time:
      return True

  return False

def run() -> bool:
  return bip.cmd(g_exe, ["create", str(g_src), str(g_dst)])