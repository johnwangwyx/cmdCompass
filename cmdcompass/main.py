from cmdcompass.gui.main_window import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.lift()
    app.attributes('-topmost', True)
    app.after_idle(app.attributes, '-topmost', False)
    app.mainloop()