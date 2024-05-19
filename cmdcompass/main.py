from cmdcompass.gui.main_window import MainWindow
from cmdcompass.utils.utils import get_current_working_dir
import os
import platform

if __name__ == "__main__":
    app = MainWindow()
    app.lift()
    app.attributes('-topmost', True)
    app.after_idle(app.attributes, '-topmost', False)
    if platform.system() == "Windows":
        icon_path = os.path.join(".", "static", "icon.ico")
    elif platform.system() == "Darwin":  # Darwin is the system name for macOS
        icon_path = os.path.join(get_current_working_dir(), "static", "icon.icns")
    else:
        icon_path = None

    if icon_path:
        app.iconbitmap(icon_path)
    app.mainloop()