import inspect
import os


# TODO: Test if it works for more just functions!
def open(func):
    "Open the source code of given function in your editor"

    code = inspect.getsourcefile(func)
    line_no = inspect.getsourcelines(func)[1]

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
