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
g_out: Path

def configure(settings: dict) -> bool:
  global g_exe
  if "exe" in settings:
    g_exe = settings["exe"]

  global g_src
  if "src" not in settings:
    bip.error("Source directory not specified.")
    return False

  g_src = Path(settings["src"])

  global g_out
  if "out" not in settings:
    bip.error("Destination bundle file not specified.")
    return False

  g_out = Path(settings["out"])

  g_src = g_src.resolve()
  g_out = g_out.resolve()
  if not g_out.parent.exists():
    g_out.parent.mkdir(parents=True)

  return True

def clean() -> bool:
  if g_out.exists():
    g_out.unlink()
  return True

def want_run() -> bool:
  if not g_out.exists():
    return True

  bndl_mod_time = g_out.stat().st_mtime

  # only iterate top level since bundles don't include subdirectories
  for file in g_src.iterdir():
    if file.stat().st_mtime > bndl_mod_time:
      return True

  return False

def run() -> bool:
  if not g_src.exists():
    bip.error(f"Source directory '{g_src}' does not exist.")
    return False

  return bip.cmd(g_exe, ["create", str(g_src), str(g_out)])
