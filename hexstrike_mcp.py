
# Compatibility shim for the old CLI entry.
if __name__ == "__main__":
    import sys, runpy
    old_argv0 = sys.argv[0]
    try:
        sys.argv[0] = "waypoint_mcp.py"   # <- new file name if different
        runpy.run_module("waypoint_mcp", run_name="__main__")
    finally:
        sys.argv[0] = old_argv0
