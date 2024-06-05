import os
import sys

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if path_to_add not in sys.path:
    sys.path.insert(0, path_to_add)

import platform
from cmdcompass.gui.main_window import MainWindow
from cmdcompass.utils.utils import get_data_and_static_parent_dir, copy_data_and_static_to_app_support_dir


if __name__ == "__main__":
    if getattr(sys, 'frozen', False) and platform.system() == "Darwin":
        copy_data_and_static_to_app_support_dir()

    app = MainWindow()
    app.lift()
    app.attributes('-topmost', True)
    app.after_idle(app.attributes, '-topmost', False)

    if platform.system() == "Windows":
        icon_path = os.path.join(".", "static", "icon.ico")
    elif platform.system() == "Darwin":  # Darwin is the system name for macOS
        icon_path = os.path.join(get_data_and_static_parent_dir(), "static", "icon.icns")
    else:
        icon_path = None

    if icon_path:
        app.iconbitmap(icon_path)

    app.mainloop()