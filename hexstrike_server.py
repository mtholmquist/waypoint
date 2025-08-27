# Compatibility shim: keep old module name working for CLI and WSGI.
from waypoint_server import app          # WSGI entry (gunicorn hexstrike_server:app)
from waypoint_server import *            # optional: re-export symbols for imports

if __name__ == "__main__":
    import sys, runpy

    # Forward ALL args to the real module.
    # Cosmetic: show the new script name in help/tracebacks.
    old_argv0 = sys.argv[0]
    try:
        sys.argv[0] = "waypoint_server.py"   # <- change if your new file is named differently
        # Run the real module as __main__; SystemExit will propagate naturally.
        runpy.run_module("waypoint_server", run_name="__main__")
    finally:
        # Restore argv[0] just in case something inspects it after return.
        sys.argv[0] = old_argv0
