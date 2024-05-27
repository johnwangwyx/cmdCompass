# CmdCompass: Your Command-Line Compass
<img src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/2c58004e-4d2f-4982-bda3-ed53ad6d7c79" height="150">

https://github.com/johnwangwyx/cmdCompass/assets/78456315/a0074ff6-7416-4127-87e7-0b8958e72c99



# Table of Contents
1. [Features](#features)
2. [Screenshots](#screenshots)
3. [User Installation-Mac](#user-installation---mac)
4. [User Installation-Windows](#user-installation---windows)
5. [User Guide](#user-guide)
6. [Contributing](#contributing)

## Features

* **Collections, Tags, Comments:** Group related commands into collections for easy access, categorize commands using tags with customizable colors, and add notes and descriptions to commands for better understanding.
* **Command Templates:** Define commands with {{variables}} for dynamic replacement.
* **Man (Manual) Page Integration:** View man pages directly within the app. Support automatic Highlighting for your command options.
* **Dark/Light Mode:** Choose your preferred theme.
* **Cross-Platform:** Works on Windows, and macOS. (Linux support will be added by May 26th)

## Screenshots
![image](https://github.com/johnwangwyx/cmdCompass/assets/78456315/e6010159-84a5-4fbf-a9c8-d614be41ce43)
![image](https://github.com/johnwangwyx/cmdCompass/assets/78456315/c179fb52-c970-483a-88c0-944cba6ccff8)

### Support 1000+ Cached Core Utility Man pages for instant Lookup. (With the ability to get ~90000 Man pages from ~60000 packages from download and converted to HTML)

<img src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/7f1c15be-61a0-4d0c-98ea-3d450357916d" width="600">

## User Installation - Mac

### Step 1:
The tool uses groff ([GNU Roff](https://www.gnu.org/software/groff/)) to convert downloaded man pages to HTML. 

Please install groff by:

`brew install groff`

### Step 2: 
* Download the dmg app installer from [release](https://github.com/johnwangwyx/cmdCompass/releases/tag/v0.9.0). Open the installer and drag the CmdCompass app to your Application folder.
  
  <img width="300" alt="Screenshot 2024-05-23 at 4 38 37 PM" src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/b709618a-2c40-4c48-887b-b628f3eb4dff">


* **For the first time only, open the Application folder on Finder, right-click the app and choose `open`.** (This is to trust app because I am an "unreconized developer" and don't have 99 USD to pay for the [Apple Developer Program](https://developer.apple.com/support/enrollment/#:~:text=Completing%20your%20enrollment&text=The%20Apple%20Developer%20Program%20annual,currency%20during%20the%20enrollment%20process.) to be able to sign a certificate to my app)
  
  <img width="280" alt="Screenshot 2024-05-23 at 4 40 15 PM" src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/5f043910-c01b-4e3f-832a-2377255c2fb7">


## User Installation - Windows
* Download the zip or the 7z archive from [release](https://github.com/johnwangwyx/cmdCompass/releases/tag/v0.9.0) and decompress it. You are now ready to use the App (cmdCompass.exe)!
  
Note: When you open the app for the first time, the Windows Smart Screen will open, Windows will block the app because it is an "unreconized app". You have to click on `More Info` and then a button will show up for you to open the app. (The App remain unreconized unless I pay $$$ to get a [certificate](https://www.reddit.com/r/electronjs/comments/17sizjf/a_guide_to_code_signing_certificates_for_the/) to sign my app)

<img src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/db4f526c-3008-4c9f-b020-d98c715b964c" width="400">
<img src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/020caeda-0dce-4975-b986-5d04c7eab8d8" width="400">

In case you are wondering, for Windows, you don't need to install groff like Mac users. Groff is not available natively on Windows anyway but thanks to the project [EZWinPorts](https://www.gnu.org/software/emacs/manual/html_node/efaq-w32/EZWinPorts.html), I have added the groff binary built for Windows to the Windows build.

## User Guide
### GUI breakdown
Below is a breakdown of the different components and their use cases:
<img width="782" alt="Screenshot 2024-05-23 at 4 30 33 PM" src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/53c73dfc-71ea-4d15-84b5-cce480fc7e8c">


1. **[Tag Definations]** You can define your tags here with custom colors, and remove existing tags.
2. **[Collection Management]** You can choose an existing collection to view your command in this collection. Additionally, you can use the add (<img width="25" alt="Screenshot 2024-05-23 at 4 26 27 PM" src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/d68956d7-5a65-4760-8075-0a672e17be4a">
) and remove (<img width="25" alt="Screenshot 2024-05-23 at 4 26 53 PM" src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/aafcf589-f098-46f0-b84c-c05b2dbf8bff">) buttons to add a new collection or remove the current selected collection.

3. **[Command List]** This List contains all your commands within the currently selected collection. You can use the select (<img width="20" alt="Screenshot 2024-05-23 at 4 27 27 PM" src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/54acbc4c-a4aa-4112-9716-2c2ec6f22b7c">) button to view the command in detail in the right penale. Or you can click on the <img width="24" alt="Screenshot 2024-05-23 at 4 28 24 PM" src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/dd5a2376-aba9-47f5-aa94-525cb5f47a9f"> button to add/remove your existing tags to this command.

4. **[Command Body]** The full body of your command will be displayed here. You can use the copy (<img width="32" alt="Screenshot 2024-05-23 at 4 31 26 PM" src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/327e3b46-a085-4805-b63c-247acdc9fa9e">) button on the right to copy this command to your clipboard. Note: the save (<img width="31" alt="Screenshot 2024-05-23 at 4 32 14 PM" src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/10513e3f-61e3-482b-90c9-118eadb1d977">)
button will be enabled once you made changes to your command body.

5. **[Comment Tab]** You can add your comment for the selected command here.
6. **[Man Page Tab]** The man page of your current command will be displayed here. You can also choose to highlight your command options (<img width="177" alt="Screenshot 2024-05-23 at 4 32 42 PM" src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/13c77780-254d-4f23-bfed-f1539ef1785f">) to view the man pages with your options highlighted. 

7. **[Theme Switch]** Toggle your theme between day and dark mode.

### Enabling variable replacement
If you define your command with `{{variable}}`, an input box will be automatically created after the command body window. You can specify as many as you want as long as your variables are enclosed in `{{}}`.


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
