import inspect
import os


def open(obj):
    "Open the source code of given object in your editor"

    if inspect.isbuiltin(obj):
        print(f"{obj} is builtin, cannot open its source!")
        return

    # Get original function before decorators
    obj = inspect.unwrap(obj)

    try:
        code = inspect.getsourcefile(obj)
        line_no = inspect.getsourcelines(obj)[1]
    except TypeError:
        t = type(obj)
        print(t)
        if t is obj:
            raise
        open(t)
        return

    editor = os.environ.get("EDITOR", "code")

    if editor == "code":
        arg = f"--goto {code}:{line_no}"
    elif editor == "subl":
        arg = f"{code}:{line_no}"
    elif editor.endswith("vim"):
        # Open in remote editor to avoid making notebooks stuck!
        arg = f"--remote +{line_no} {code}"
    else:
        arg = f"+{line_no} {code}"

    os.system(f"{editor} {arg}")
