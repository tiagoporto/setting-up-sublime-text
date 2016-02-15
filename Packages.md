Packages in Sublime Text are a collection of resource files used to extend functionalities, they can be: plugins, syntax highlighting, menus, snippets...

There are a lot of custom packages to install, you can install packages to your necessity or you can create your own package.

## Packages
* [Package Control](#package-control)
* [SideBarEnhancements](#sidebarenhancements)
* [AutoFileName](#autofilename)
* [Tag](#tag)
* [Bracket Highlighter](#bracket-highlighter)
* [Trailing Spaces](#trailing-spaces)
* [Emmet](#emmet)
* [Emmet LiveStyle](#emmet-liveStyle)
* [Color Picker](#color-picker)
* [ColorHighlighter](#colorhighlighter)
* [Move Tab](#movetab)
* [DocBlockr](#docblockr)
* [EditorConfig](#editorconfig)
* [SFTP](#sftp)
* [SublimeServer](#sublimeserver)
* [Gulp](#gulp)
* [Alignment](#alignment)
* [Can I Use](#caniuse)
* [CSS Comb](#csscomb)
* [Cheat Sheets](#cheat-sheets)
* [Terminal](#terminal)
* [GhostText for Sublime Text](#ghostText-for-sublime-text)

## [Package Control](https://sublime.wbond.net/)

Package Control manage all packages, makes it simple to find, install, remove and keep packages up-to-date.

Go to [installation page](https://packagecontrol.io/installation)


### How to use

#### Installing packages

* `ctrl` `shift` `p`
* Type `install`
* Select `Package Control: Install Package`
* Search the package you want to install

#### Removing packages

* `ctrl` `shift` `p`
* Type `remove`
* Select `Package Control: Remove Package`
* Find the package you want to remove

## [SideBarEnhancements](https://github.com/titoBouzout/SideBarEnhancements)

Provides enhancements to the operations on Sidebar of Files and Folders, like: new file/folder, edit, open/run, reveal, find in selected/parent/project, cut, copy, paste, paste in parent, rename, move, delete, refresh...

![screenshot sidebarEnhancements](http://dl.dropbox.com/u/43596449/tito/sublime/SideBar/screenshot.png)

## [AutoFileName](https://github.com/BoundInCode/AutoFileName)

Autocomplete filenames and paths in HTML and CSS.

### How to use

* In the file press `ctrl` `space`

![Screenshot AutoFileName screenshots](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Screenshots/AutoFileName.png)

### Inserting markdown and stylus in the scope

Copy the file [autofilename.sublime-settings](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Packages%20Settings/autofilename.sublime-settings) in the folder `C:\Users\{username}\AppData\Roaming\Sublime Text 3\Packages\User` in windows, ` ~/Library/Application Support/Sublime Text 3/Packages/User` in OS X or `~/.config/sublime-text-3/Packages/User` in Linux.



## [Tag](https://github.com/SublimeText/Tag)

Provides utilities to work with tags in HTML/XML: "Close tag on slash", "Tag indent or AutoFormat Tags", "Tag Remove", "Insert as Tag", "Tag Remove Attributes", "Tag Close", "Tag Lint"

### How to use

* See the documentation: [https://github.com/SublimeText/Tag](https://github.com/SublimeText/Tag)



## [Bracket Highlighter](https://github.com/facelessuser/BracketHighlighter)

Finds and highlights matching brackets such as: [], (), {}, "", '', <tag></tag>, and even custom brackets.

![Screenshot](http://dl.dropbox.com/u/342698/BracketHighlighter/Example1.png )

## [Trailing Spaces](https://github.com/SublimeText/TrailingSpaces)

Highlight trailing spaces and delete them in a flash!

![Screenshot TrailingSpaces](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Screenshots/TrailingSpaces.png "")

### Setting Trim On Save

* Copy the file [trailing_spaces.sublime-settings](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Packages%20Settings/trailing_spaces.sublime-settings) in the folder
    * `C:\Users\{username}\AppData\Roaming\Sublime Text 3\Packages\User` in windows
    * ` ~/Library/Application Support/Sublime Text 3` in OS X.


## ![Emmet Logo](http://emmet.io/i/logo.svg) [Emmet](http://emmet.io/)

Emmet is the most essential plugin for web-developers, it helps you write HTML and CSS code easily, expanding simple abbreviations into complex code snippets.

![Emmet Screenshot](http://media.mediatemple.netdna-cdn.com/wp-content/uploads/2013/03/initializers.gif)

![Emmet Screnshot](http://media.mediatemple.netdna-cdn.com/wp-content/uploads/2013/03/multiplication.gif)

* Watch the demo in [http://emmet.io/](http://emmet.io/)
* Read this great tutorial: [Goodbye, Zen Coding. Hello, Emmet!](http://www.smashingmagazine.com/2013/03/26/goodbye-zen-coding-hello-emmet/)
* Learn the syntax in [Cheat Sheet](http://docs.emmet.io/cheat-sheet/)



## [Emmet LiveStyle](http://livestyle.emmet.io/install/)

>Changes are transmitted from the editor to the browser and the browser into the editor.

## [Color Picker](http://weslly.github.io/ColorPicker/)

Open a Color Picker in Sublime Text.

<img src="https://developers.google.com/web/shows/ttt/series-1/images/color-picker-screenshot.png" alt="" width="200">

### How to use

* `ctrl` `shift` `c` on Windows or `command` `shift` `c` on OS X




## [ColorHighlighter](https://github.com/Monnoroch/ColorHighlighter)

Live Preview of color values in Stylesheets.

![ColorHighlighter](http://i.imgur.com/UPmEk09.png)

### Tip

The key bindings that plugin, use some of the same useful standards key bindins of the Sublime Text , I usually disable them

* Menu Option `tools -> color highlighter -> Disable default keybindings`


* Menu Preferences -> Package Settings -> Color Highlighter -> Settings – User
```
{
    "ha_style": "filled"
}
```

## [Move Tab](https://github.com/SublimeText/MoveTab)

Plugin for Sublime Text to move tabs around with keyboard shortcut

![Move tab](https://s3.amazonaws.com/f.cl.ly/items/3G193M3e3h2f141H3O1U/Screen%20Recording%202016-01-14%20at%2009.43%20AM.gif)


## [DocBlockr](https://github.com/spadgos/sublime-jsdocs)

Good plugin to help write documentation in __JavaScript__, __PHP__, __CofeeScript__, ...

![Screenshot DocBlockr](https://camo.githubusercontent.com/415148aecc6dac2e5ebb12b7f7584f4a8744eca4/687474703a2f2f73706164676f732e6769746875622e696f2f7375626c696d652d6a73646f63732f696d616765732f66756e6374696f6e2d74656d706c6174652e676966)

## How to use

* Press enter or tab after `/**` (or `###*` for Coffee-Script).



## ![EditorConfig Logo](http://editorconfig.org/logo.png) [EditorConfig](http://editorconfig.org/)

> EditorConfig helps developers define and maintain consistent coding styles between different editors and IDEs. The EditorConfig project consists of __a file format__ for defining coding styles and a collection of __text editor plugins__ that enable editors to read the file format and adhere to defined styles.

## How to use

* See the documentation: [EditorConfig Page](http://editorconfig.org/)



## [SFTP](http://wbond.net/sublime_packages/sftp)

FTP, FTPS and SFTP support for Sublime Text.

![Screenshots SFTP](http://wbond.net/sublime_packages/img/sftp/sidebar_menu_configured.png)

### How to use

* Read the [instructions](http://wbond.net/sublime_packages/sftp/usage).


## [SublimeServer](https://github.com/learning/SublimeServer)

> Turn you Sublime Text editor into a HTTP server


## <img src="https://raw.githubusercontent.com/gulpjs/artwork/master/gulp.png" alt="gulpjs Logo" width="50"> [gulp](https://github.com/NicoSantangelo/sublime-gulp)

> A Gulp task runner with snippets.

### How to use

> It's necessary a `gulpfile.js` in the open folder to run tasks.

* `ctrl` `shift` `p`
* Type `gulp`
* Select the task to run

![gulp screenshot](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Screenshots/gulp.png)

See the documentation on [sublime-gulp](https://github.com/NicoSantangelo/sublime-gulp) to snippets.

## [Alignment](https://github.com/wbond/sublime_alignment)

> A simple key-binding for aligning multi-line and multiple selections.

![Alignment Screenshot](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Screenshots/Alignment.gif)

### How to use

* `ctrl` `alt` `a`



## [Can I Use](https://github.com/Azd325/sublime-text-caniuse)

Useful for quick check CSS property support on the [Can I Use site](http://caniuse.com/).

### How to use

* Mark or place your cursor over a CSS property and press `ctrl` `alt` `f`.



## [![CSS Comb Logo](https://raw.githubusercontent.com/csscomb/csscomb.js/master/logo.png) CSS Comb](http://csscomb.com/)

Coding style formatter for CSS.

### How to use

* `ctrl` `shift` `c`

## [Cheat Sheets](https://github.com/dmikalova/sublime-cheat-sheets)

> Quickly accessing cheat sheets

![Cheat sheets print](https://raw.github.com/dmikalova/sublime-cheat-sheets/master/example.png)

## [Terminal](https://github.com/wbond/sublime_terminal)

> Launch terminals from the current file or the root project folder.

### How to use

* `ctrl` `alt` `shift` `t` - Open Terminal at Project Folder

* `ctrl` `shift` `t` - Open Terminal at File -

    This key binding is the same of the default sublime reopen closed tab, I prefer to switch to `alt` `shift` `t`.



## [![GhostText for Sublime Text](https://raw.githubusercontent.com/Cacodaimon/GhostText-for-Chrome/master/promo/gt_banner-for-sublimetext.png)](https://github.com/Cacodaimon/GhostText-for-SublimeText)

> Allows live editing of Chrome text area or JS Code editor content with Sublime Text.

![Screenshot GhostText](http://img.youtube.com/vi/e0aLFPtYPZI/maxresdefault.jpg)

### Addition Installation

- [Chrome Extension](https://chrome.google.com/webstore/detail/ghosttext-for-chrome/godiecgffnchndlihlpaajjcplehddca?utm_source=chrome-ntp-icon)

### How to use

* In Chrome, click the GhostText button in the upper-right corner to open up Sublime Text.