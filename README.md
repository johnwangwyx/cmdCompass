# CmdCompass: Collect, Learn, and Recall All Your Terminal Commands
<img src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/2c58004e-4d2f-4982-bda3-ed53ad6d7c79" height="150">

https://github.com/johnwangwyx/cmdCompass/assets/78456315/8e5a3321-6680-4857-a782-5e337547bacf


# Table of Contents
1. [Screenshots](#screenshots)
2. [User Installation-Mac](#user-installation---mac)
3. [User Installation-Windows](#user-installation---windows)
4. [User Installation-Linux & Distro Compatibility](#user-installation---linux)
5. [User Guide](#user-guide)
6. [Contributing](#contributing)

## Screenshots
<img src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/5b8d24b2-8627-47ca-ba05-c3919830226b" width="700">

#### View Manual Page with Option Highlighting
<img src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/ed3f7706-a1a0-4430-85d4-521fe2dfd7b1" width="700">



### Support 1000+ Cached Core Utility Man pages for instant Lookup. (With the ability to get ~90000 Man pages from ~60000 packages from download and converted to HTML)

<img src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/7f1c15be-61a0-4d0c-98ea-3d450357916d" width="600">

## User Installation - Mac

### Step 1:
The tool uses groff ([GNU Roff](https://www.gnu.org/software/groff/)) to convert downloaded man pages to HTML. 

Please install groff by:

`brew install groff`

### Step 2: 
* Download the dmg app installer from [release](https://github.com/johnwangwyx/cmdCompass/releases/tag/v1.0.0). Open the installer and drag the CmdCompass app to your Application folder.
  
  <img width="300" alt="Screenshot 2024-05-23 at 4 38 37 PM" src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/b709618a-2c40-4c48-887b-b628f3eb4dff">


* **For the first time only, open the Application folder on Finder, right-click the app and choose `open`.** (This is to trust app because I am an "unreconized developer" and don't have 99 USD to pay for the [Apple Developer Program](https://developer.apple.com/support/enrollment/#:~:text=Completing%20your%20enrollment&text=The%20Apple%20Developer%20Program%20annual,currency%20during%20the%20enrollment%20process.) to be able to sign a certificate to my app)
  
  <img width="280" alt="Screenshot 2024-05-23 at 4 40 15 PM" src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/5f043910-c01b-4e3f-832a-2377255c2fb7">


## User Installation - Windows
* Download the zip or the 7z archive from [release](https://github.com/johnwangwyx/cmdCompass/releases/tag/v1.0.0) and decompress it. You are now ready to use the App (cmdCompass.exe)!
  
Note: When you open the app for the first time, the Windows Smart Screen will open, Windows will block the app because it is an "unreconized app". You have to click on `More Info` and then a button will show up for you to open the app. (The App remain unreconized unless I pay $$$ to get a [certificate](https://www.reddit.com/r/electronjs/comments/17sizjf/a_guide_to_code_signing_certificates_for_the/) to sign my app)

<img src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/db4f526c-3008-4c9f-b020-d98c715b964c" width="400">
<img src="https://github.com/johnwangwyx/cmdCompass/assets/78456315/020caeda-0dce-4975-b986-5d04c7eab8d8" width="400">

In case you are wondering, for Windows, you don't need to install `groff` like Mac users. Groff is not available natively on Windows anyway but thanks to the project [EZWinPorts](https://www.gnu.org/software/emacs/manual/html_node/efaq-w32/EZWinPorts.html), I have added the groff binary built for Windows to the Windows build.

## User Installation - Linux
* Install `groff` with your package manager.
**Note on Debian or Ubuntu, even with `groff` already installed, you may likely need to run `sudo apt install groff` again as the pre-installed version is unable to convert to HTML documents, resulting in empty man HTML pages being displayed**
* Download and decompress the app from [release](https://github.com/johnwangwyx/cmdCompass/releases/tag/v1.0.0). You can just right-click and run the `cmdCompass` executable with `GNOME` or run with `./cmdCompass` in terminal.

Below distros are tested:
- [x] Ubuntu 24.04 with GNOME
- [x] Debian 12.5.0 with GNOME
- [x] CentOS-Stream-9 with GNOME
- [x] Arch 2024.5.01 with GNOME

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

Please read [CONTRIBUTING.md](/CONTRIBUTING.md) for the project structure and workflows.
