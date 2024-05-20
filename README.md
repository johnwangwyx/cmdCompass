# CmdCompass: Your Command-Line Compass
<img src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/2c58004e-4d2f-4982-bda3-ed53ad6d7c79" height="150">

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

### Feature: Command templating for variables replacement
![image](https://github.com/johnwangwyx/cmdCompass/assets/78456315/e6010159-84a5-4fbf-a9c8-d614be41ce43)
### Feature: Automatic Man Page Option Hightling

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
* Download the zip or the 7z archive from [release](https://github.com/johnwangwyx/cmdCompass/releases/tag/v0.9.0) and decompress them. You are now ready to use the App (cmdCompass.exe)!
  
Note: When you open the app for the first time, the Windows Smart Screen will open, Windows will block the app because it is an "unreconized app". You have to click on `More Info` and then a button will show up for you to open the app. (The App remain unreconized unless I pay $$$ to get a [certificate](https://www.reddit.com/r/electronjs/comments/17sizjf/a_guide_to_code_signing_certificates_for_the/) to sign my app)

<img src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/db4f526c-3008-4c9f-b020-d98c715b964c" width="400">
<img src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/020caeda-0dce-4975-b986-5d04c7eab8d8" width="400">

In case you are wondering, for Windows, you don't need to install groff like Mac users. Groff is not available natively on Windows anyway but thanks to the project [EZWinPorts](https://www.gnu.org/software/emacs/manual/html_node/efaq-w32/EZWinPorts.html), I have added the groff binary built for Windows to the Windows build.


## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests. The tool is still in early stage so please bear with me. :)
A detailed breakdown of the components and dev instruction will be shortly uploaded to the readme.
