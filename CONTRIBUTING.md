## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests. The tool is still in early stage so please bear with me. :)

### Project Structure & file description
The project is structured as follows:
```
cmdCompass/
├── cmdcompass/
│   ├── __init__.py
│   ├── main.py              # The entry point for the application. It creates and runs the MainWindow instance.
│   ├── data/
│   │   ├── __init__.py
│   │   ├── datamanager.py   # Handles data persistence for collections, commands, and tags.
│   │   └── man_pages/
│   │       ├── __init__.py
│   │       ├── tmp/         # Temporary directory used for extracting man pages.
│   │       └── html_core/   # Directory to store downloaded man pages in HTML format.
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── main_window.py            # Defines the main application window and its UI elements.
│   │   ├── command_tag_operation.py  # Defines the TagOperation class for managing tags associated with commands.
│   │   ├── collection_operations.py  # Defines UI elements for managing collections.
│   │   ├── commandbox.py             # Defines the CommandBox class to display a single command and its associated tags.
│   │   ├── utilitybox.py             # Defines the UtilityBox class for displaying template variables and the "Generate" button.
│   │   ├── commandbodybox.py         # Defines the CommandBodyBox class to display and allow editing of the command string.
│   │   ├── commentbox.py             # Defines the CommentBox class to display and allow editing of the comment for the command.
│   │   ├── global_tag.py             # Defines the GlobalTagWindow class for creating and managing global tags. 
│   │   ├── set_man_page_window.py    # Defines the SetManPageWindow class to allow the user to specify a specific man page for a command.
│   │   ├── manpagebox.py             # Defines the ManPageBox class to display the man page associated with a command.
│   │   └── progresswindow.py         # Defines the ProgressWindow class, a simple window with a textbox to display progress messages.
│   ├── man_parser/
│   │   ├── __init__.py
│   │   ├── html_coverter.py          # Contains the logic to convert man pages to HTML using groff.
│   │   └── loader.py                 # Handles the process of downloading man pages and extracting the relevant man page.
│   └── models/
│       ├── __init__.py
│       ├── collection.py             # Defines the data structure for a collection of commands.
│       ├── command.py                # Defines the data structure for a single command. 
│       └── tag.py                    # Defines the data structure for a single tag.
├── static/       # Contain static images and vectors used by the buttons and icon of the app.
├── utils/
    ├── __init__.py
    └── utils.py  # Contains utility functions for various tasks.
```
### Customtkinter
The application utilizes the [customtkinter](https://github.com/TomSchimansky/CustomTkinter) library, a modern and visually appealing toolkit for creating graphical user interfaces (GUIs) with Python. 
CustomTkinter provides a set of themed widgets that are designed to look modern and consistent across different operating systems.

### Main Application Entry Point (main.py)
The main entry point for the application is the `cmdcompass/main.py` file. This file initializes the MainWindow class, which is responsible for setting up the entire user interface (UI) of the application. 

### Man Page Loading Process
Below are the steps that cmdCompass retrieves the package containing the man page, downloads the package, extract it, and convert the man page to HTML.

1. The application retrieves a list of Debian packages that contain man pages. This information is stored in a local database called `man_pages_kv.db`, which is a key-value store using the `sqlitedict` library. The keys in the database are command names (e.g., "cat"), and the values are tuples containing the download link and the number of man pages in the package, ordered by the number of man pages. (e.g command `cat` as a key will map to the value `[('pool/main/9/9base/9base_6-13_amd64.deb', 46), ('pool/main/c/coreutils/coreutils_9.1-1_amd64.deb', 106)]`. So there will be two packages containing the man page for `cat`. As of now, the app will just use the first one as there are only 46 man pages(commands) in this package, thus reducing our time of downloading and extraction)
2. The application downloads the Debian package (.deb file) using the provided link from the database and extracts it.
3. The extracted man pages are moved to the `/data/man_pages/man` directory. After the man pages are moved, the extraction directory is cleaned up. Then, the application will convert the man pages into HTML format using the `groff` command and put the converted HTML file into `/data/man_pages/html_download`.
