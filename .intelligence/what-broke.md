# What Broke — SWD-BLOK-2-Blokopdracht

## 2026-06-07 — Terminal venv activation persistence
**What broke:**
Terminal still references `odysseus\.venv\Scripts\python.exe` after odysseus folder was removed. Error: `CommandNotFoundException`

**Why it broke:**
PowerShell terminal session retains activated venv path. The `(.venv)` prompt prefix indicates the venv is active in that terminal session. Removing the folder does not deactivate the terminal session.

**How we fixed it:**
Created dedicated `.venv` in `SWD-BLOK-2-Blokopdracht` with Python 3.13. Installed pygame 2.6.1. Script runs successfully with: `& c:\Users\rids\Documents\GitHub\SWD-BLOK-2-Blokopdracht\.venv\Scripts\python.exe c:/Users/rids/Documents/GitHub/SWD-BLOK-2-Blokopdracht/main.py`

**How to avoid it:**
- Run `deactivate` in terminal before switching projects
- Open a new terminal session when switching projects
- Always use the project's own `.venv` path, not shared venvs
- Never share `.venv` across projects — each project needs its own venv with its own dependencies

---

## 2026-06-07 — pygame install failure with Python 3.14
**What broke:**
pygame 2.6.1 fails to build/install with Python 3.14.2. Error: `ModuleNotFoundError: No module named 'setuptools._distutils.msvccompiler'`

**Why it broke:**
Python 3.14 removed `distutils.msvccompiler` which pygame's build process requires. No pre-built pygame wheel exists for Python 3.14.

**How we fixed it:**
Created dedicated `.venv` with Python 3.13 (which has pygame-2.6.1-cp313-cp313-win_amd64.whl available). Installed pygame successfully.

**How to avoid it:**
- Check pygame wheel compatibility: pygame wheels use `cp313` (Python 3.13) tag
- Use Python 3.13 for pygame projects
- Verify `pip install pygame --only-binary=all` finds a wheel matching your Python version before installing
- Never use Python 3.14 with pygame until a cp314 wheel is released

---