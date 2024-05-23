# CmdCompass: Your Command-Line Compass
<img src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/2c58004e-4d2f-4982-bda3-ed53ad6d7c79" height="150">

https://github.com/johnwangwyx/cmdCompass/assets/78456315/a0074ff6-7416-4127-87e7-0b8958e72c99



# Table of Contents
1. [Features](#features)
2. [Screenshots](#screenshots)
3. [User Installation-Mac](#user-installation---mac)
4. [User Installation-Windows](#user-installation---windows)
5. [Contributing](#contributing)

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
* Download the dmg app installer from [release](https://github.com/johnwangwyx/cmdCompass/releases/tag/v0.9.0). Open the installer and drag the CmdCompass app to your Application folder as usuall.

* **For the first time only, open Application folder on Finder, right click the app and chooss `open`.** (This is to trust app because I am an "unreconized developer" and don't have 99 USD to pay for the [Apple Developer Program](https://developer.apple.com/support/enrollment/#:~:text=Completing%20your%20enrollment&text=The%20Apple%20Developer%20Program%20annual,currency%20during%20the%20enrollment%20process.) to be able to sign a certificate to my app)

## User Installation - Windows
* Download the zip or the 7z archive from [release](https://github.com/johnwangwyx/cmdCompass/releases/tag/v0.9.0) and decompress it. You are now ready to use the App (cmdCompass.exe)!
  
Note: When you open the app for the first time, the Windows Smart Screen will open, Windows will block the app because it is an "unreconized app". You have to click on `More Info` and then a button will show up for you to open the app. (The App remain unreconized unless I pay $$$ to get a [certificate](https://www.reddit.com/r/electronjs/comments/17sizjf/a_guide_to_code_signing_certificates_for_the/) to sign my app)

<img src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/db4f526c-3008-4c9f-b020-d98c715b964c" width="400">
<img src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/020caeda-0dce-4975-b986-5d04c7eab8d8" width="400">

In case you are wondering, for Windows, you don't need to install groff like Mac users. Groff is not available natively on Windows anyway but thanks to the project [EZWinPorts](https://www.gnu.org/software/emacs/manual/html_node/efaq-w32/EZWinPorts.html), I have added the groff binary built for Windows to the Windows build.

## User Guide
### GUI breakdown
Below is a breakdown of the different components and their use cases:
<img width="787" alt="Screenshot 2024-05-23 at 4 09 58 PM" src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/8f1fcb1d-157e-4578-a58a-eee471a9ffd0">

1. **[Tag Definations]** You can define your tags here with custom colors, and remove existing tags.
2. **[Collection Management]** You can choose an existing collection to view your command in this collection. Additionally, you can use the add and remove buttons to add a new collection or remove the current selected collection.
3. **[Command List]** This List contains all your commands within the currently selected collection. You can use the select (`>`) button to view the command in detail in the right penale. Or you can click on the `tag` button to add/remove your existing tags to this command.
4. **[Command Body]** The full body of your command will be displayed here. You can use the copy button on the right to quickly copy this command to your clipboard. Note the save button will be enabled once you made changes to your command body.
5. **[Comment Tab]** You can add your comment for the selected command here.
6. **[Man Page Tab]** The man page of your current command will be displayed here. You can also choose to highlight your command options to view the man pages with your options highlighted.
7. **[Theme Switch]** Toggle your theme between day and dark mode.

### Enabling variable replacement
If you define your command with `{{variable}}`, an input box will be automatically created after the command body window. You can specify as many as you want as long as your variables are enclosed in `{{}}`.


## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests. The tool is still in early stage so please bear with me. :)
A detailed breakdown of the components and dev instruction will be shortly uploaded to the readme.
