# Setting Up Sublime Text 3

<!-- https://github.com/orizens/html-extended
https://github.com/pafnuty/imgHolder -->

<p align="center"><img src="http://upload.wikimedia.org/wikipedia/en/4/4c/Sublime_Text_Logo.png" alt="Sublime Text Logo" width="120" ></p>

This is not a step by step guide for anyone who starts with [Sublime Text](http://www.sublimetext.com/). These are the settings and reminders that fit in my workflow. You can choose what is the best for you.

> If they are useful to me, may also be useful for you.

## Sublime Text

Download and install [Sublime Text 3](http://www.sublimetext.com/3).

## Table of Contents
* [Preferences](#preferences)
    * [Theme and Color Schema](#theme-and-color-schema)
    * [Font](#font)
* [Key Bindings](#key-bindings)
    * [Reminders](#reminders)
* [Snippets](#snippets)
* [Packages](#packages)
* [Additional Languages Support](#additional-languages-support)
* [Working With Markdown](#working-with-markdown-)
* [Backing Up Sublime Text](#backing-up-sublime-text)
* [Creating Project](creating-project)

## Preferences

> Sublime Text has many different settings to customize its behavior. Settings are changed by editing text files.

You can set your preferences like, font size, margin, theme and more in `Preferences.sublime-settings`. I like to use this options.

```json
{
    // Spacing between the gutter and the text
    "margin": 0,

    // Set to false to disable detection of tabs vs. spaces on load
    "detect_indentation": false,

    // Disables horizontal scrolling if enabled.
    // May be set to true, false, or 'auto', where it will be disabled for
    // source code, and otherwise enabled.
    "word_wrap": true,

    // Controls how the indent guides are drawn, valid options are
    // 'draw_normal' and 'draw_active'. draw_active will draw the indent
    // guides containing the caret in a different color.
    "indent_guide_options":
        [
            "draw_normal",
            "draw_active"
        ],

    // Set to true to removing trailing white space on save
    "trim_trailing_white_space_on_save": true,

    // The delay, in ms, before the auto complete window is shown after typing
    "auto_complete_delay": 5,

    // Makes tabs with modified files more visible
    "highlight_modified_tabs": true,

    // These files will still show up in the side bar, but won't be included in
    // Goto Anything or Find in Files
    "binary_file_patterns": [".DS_Store", ".gitignore", "node_modules/", "vendor/", "tmp/"]
}
```


### Font

You can change the default font used in sublime.

Personally I like to use the [Monaco](http://www.gringod.com/2006/11/01/new-version-of-monaco-font/) font.

```json
{
    // Set the family Font
    "font_face": "Monaco",

    // Set the font size
    "font_size": 8
}
```


If you like more control over typography, the [Input Font](http://input.fontbureau.com/) is a big family of Font Bureau and can be a good option, it has customs options, you can choose the line-heigth and differents glyphs or use the preset of other fonts.

[Input Family with Monaco Preset](http://input.fontbureau.com/download/index.html?family=InputMono&width=300&weight=400&line-height=1.3&a=ss&g=ss&i=serifs_round&l=serifs_round&zero=slash&asterisk=0&braces=straight&preset=monaco)


### Theme and Color Schema

If you don't like of the Monokai, the default theme of Sublime you can change it. By default Sublime there are some fews options.

`Menu Bar` > `Preferences` > `Color Schema` > `Color Schema Default` > `Default Themes`

You also download a theme by Package Control.

#### [colorsublime](http://colorsublime.com/)
This is a good plugin that help you to preview themes before install.

#### Creating your own Sublime Text theme

On the other hand, may you want your own theme.

##### [tmtheme-editor](http://tmtheme-editor.herokuapp.com/)

This is a web editor that you can make your theme and donwload.

##### [ColorSchemeEditor](https://github.com/bobef/ColorSchemeEditor)

This package helps you edit a theme directly in the Sublime Text.

## Key Bindings

All key bindings are configurable, you can change default key bindings or create new.

I have customized the following key bindings.

`Ctrl` `b` on Windows/Linux and `Super` `b` on OS X  = `<strong>selection</strong>`

`Ctrl` `i` on Windows/Linux and `Super` `i` on OS X = `<em>selection</em>`

`Ctrl` `u` on Windows/Linux and `Super` `u` on OS X = `<u>selection</u>`

### How to use

Download the file and save on the right folder

* [Default (Windows).sublime-keymap](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Sublime%20Settings/Default%20(Windows).sublime-keymap) in the folder `C:\Users\{username}\AppData\Roaming\Sublime Text 3\Packages\User` on Windows.

* [Default (OSX).sublime-keymap](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Sublime%20Settings/Default%20(OSX).sublime-keymap) in the folder `~/Library/Application Support/Sublime Text 3/Packages/User` in OS X.

* [Default (Linux).sublime-keymap](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Sublime%20Settings/Default%20(Linux).sublime-keymap) in the folder `~/.config/sublime-text-3/Packages/User` in Linux.

### Reminders

If you're like me and always confused with a lot of key bindings, it's for us. A list of useful shortcuts.

#### Workspace

* `f11` = full screen
* `shift` `f11` = distract mode
* `alt` `shift` `2` = Layout in 2 columns
* `alt` `shift` `8` = Layout in 2 rows

#### Selection

* `Ctrl` `d` on Windows/Linux, or `Command` `d` on OS X = Quick Add Next.
* `Alt` `F3` on Windows/Linux, or `Ctrl` `Command` `g` on OS X = Find All
* `Ctrl` `Shift` `l` or `Command` `Shift` `l` on OS X = Splitting the Selection into Lines
* `Ctrl` `k`, `Ctrl` `d` on Windows/Linux, or `Command` `k` `Command` `d` on OS X = Quick Skip Next
    * if you go too far, use Undo Selection (`Ctrl` `u`, or `Command` `u` on OS X) to step backwards
* `ctrl` `shift` `a` = Expand selection to tag
* `ctrl` `k` `ctrl` `space` = Set Mark
* `ctrl` `k` `ctrl` `x` = Swap with Mark
* `ctrl` `r` = Jump to any heading in the document or the project and see the indentation level

#### Utilities

* `ctrl` `k`, `ctrl` `v` = Paste History
* `ctrl` `shift` `t` = Reopen Closed Tab

## Snippets

> Snippets are smart templates that will insert text for you and adapt it to their context.

The snippets are triggered with the `tab` key after the snippet access string.

#### Example

When you write `jquery` and press `tab`, the Sublime Text identifies you need snippet `jQuery Fallback` and replaces the entire access sequence throughout the template. You can still edit some parts of the template by pressing `tab` to pass between the editable parts.

![Snippets Usage Example](Screenshots/snippet.gif)

### [Comment Snippets](https://github.com/hachesilva/Comment-Snippets)

> Several snippets to create fancy PHP, CSS and HTML comments.

![Comment Snippets Example](https://raw.githubusercontent.com/hachesilva/Comment-Snippets/master/CommentSnippets.gif)

### How it works

[See the documentation](https://github.com/hachesilva/Comment-Snippets)

### My Snippets

If you want use some of this snippets, download the file and copy in your local folder:

* `C:\Users\{username}\AppData\Roaming\Sublime Text 3\Packages\User` in windows

* ` ~/Library/Application Support/Sublime Text 3/Packages/User` in OS X

* `~/.config/sublime-text-3/Packages/User` in Linux


#### [Form Template](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Snippets/Form%20Template.sublime-snippet)

* [Example of Form Template Snippet](https://github.com/tiagoporto/setting-up-sublime-text/blob/master/form-template-snippet-example.md)

* To use write `form-template` and press `tab`.

#### [Placehold.it](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Snippets/Placehold%20it.sublime-snippet)

* To use write `phit` and press `tab`.

* Example

    ```html
    <!-- placehold.it package default image -->
    <img alt="Alternate Text" src="http://placehold.it/600x400/0eafff/ffffff.png" />
    ```

#### [Project Header](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Snippets/Project%20Header.sublime-snippet)

* Example

    ```css
    /*!
    *   My Project v1.0.0
    *   http://myproject.com
    *   Copyright (c) 2010-2015 Author Name (http://authorsite.com)
    *   Released under the MIT license
    */
    ```

* To use write `project-header` and press `tab`.


#### [Readme](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Snippets/Readme%20File.sublime-snippet)

* [Example of readme Snippet](https://github.com/tiagoporto/setting-up-sublime-text/blob/master/readme-snippet-example.md)

* To use write `readme` and press `tab`.

<!--
### Creating your own snippets

http://web-design-weekly.com/2012/07/03/snippets-in-sublime-text-2/
`ctrl` `shift` `alt` `p`
-->

## Packages

Packages in Sublime Text are a collection of resource files used to extend functionalities, they can be: plugins, syntax highlighting, menus, snippets...

There are a lot of custom packages to install, you can install packages to your necessity or you can create your own package.

### [Package Control](https://sublime.wbond.net/)

Package Control manage all packages, makes it simple to find, install, remove and keep packages up-to-date.

Go to [installation page](https://packagecontrol.io/installation)


#### How to use

##### Installing packages

* `ctrl` `shift` `p`
* Type `install`
* Select `Package Control: Install Package`
* Search the package you want to install

##### Removing packages

* `ctrl` `shift` `p`
* Type `remove`
* Select `Package Control: Remove Package`
* Find the package you want to remove

### [SideBarEnhancements](https://github.com/titoBouzout/SideBarEnhancements)

Provides enhancements to the operations on Sidebar of Files and Folders, like: new file/folder, edit, open/run, reveal, find in selected/parent/project, cut, copy, paste, paste in parent, rename, move, delete, refresh...

![screenshot sidebarEnhancements](http://dl.dropbox.com/u/43596449/tito/sublime/SideBar/screenshot.png)

### [AutoFileName](https://github.com/BoundInCode/AutoFileName)

Autocomplete filenames and paths in HTML and CSS.

#### How to use

* In the file press `ctrl` `space`

![Screenshot AutoFileName screenshots](Screenshots/AutoFileName.png)

#### Inserting markdown and stylus in the scope

* Copy the file [autofilename.sublime-settings](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Packages%20Settings/autofilename.sublime-settings) in the folder `C:\Users\{username}\AppData\Roaming\Sublime Text 3\Packages\User` in windows, ` ~/Library/Application Support/Sublime Text 3/Packages/User` in OS X or `~/.config/sublime-text-3/Packages/User` in Linux.

### [Tag](https://github.com/SublimeText/Tag)

Provides utilities to work with tags in HTML/XML: "Close tag on slash", "Tag indent or AutoFormat Tags", "Tag Remove", "Insert as Tag", "Tag Remove Attributes", "Tag Close", "Tag Lint"

#### How to use

* See the documentation: [https://github.com/SublimeText/Tag](https://github.com/SublimeText/Tag)

### [Bracket Highlighter](https://github.com/facelessuser/BracketHighlighter)

Finds and highlights matching brackets such as: [], (), {}, "", '', <tag></tag>, and even custom brackets.

![Screenshot](http://dl.dropbox.com/u/342698/BracketHighlighter/Example1.png )

### [Trailing Spaces](https://github.com/SublimeText/TrailingSpaces)

Highlight trailing spaces and delete them in a flash!

![Screenshot TrailingSpaces](Screenshots/TrailingSpaces.png "")

#### Setting Trim On Save

* Copy the file [trailing_spaces.sublime-settings](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Packages%20Settings/trailing_spaces.sublime-settings) in the folder
    * `C:\Users\{username}\AppData\Roaming\Sublime Text 3\Packages\User` in windows
    * ` ~/Library/Application Support/Sublime Text 3` in OS X.


### ![Emmet Logo](http://emmet.io/i/logo.svg) [Emmet](http://emmet.io/)

Emmet is the most essential plugin for web-developers, it helps you write HTML and CSS code easily, expanding simple abbreviations into complex code snippets.

![Emmet Screenshot](http://media.mediatemple.netdna-cdn.com/wp-content/uploads/2013/03/initializers.gif)

![Emmet Screnshot](http://media.mediatemple.netdna-cdn.com/wp-content/uploads/2013/03/multiplication.gif)

* Watch the demo in [http://emmet.io/](http://emmet.io/)
* Read this great tutorial: [Goodbye, Zen Coding. Hello, Emmet!](http://www.smashingmagazine.com/2013/03/26/goodbye-zen-coding-hello-emmet/)
* Learn the syntax in [Cheat Sheet](http://docs.emmet.io/cheat-sheet/)

### [Emmet LiveStyle](http://livestyle.emmet.io/install/)


### [Color Picker](http://weslly.github.io/ColorPicker/)

Open a Color Picker in Sublime Text.

![Windows screenshot](http://i.minus.com/iY1DDCRG5TsyR.png)

#### How to use

* `ctrl` `shift` `c` on Windows or `command` `shift` `c` on OS X

### [ColorHighlighter](https://github.com/Monnoroch/ColorHighlighter)

Live Preview of color values in Stylesheets.

![ColorHighlighter](http://i.imgur.com/UPmEk09.png)

#### Tip

The key bindings that plugin, use some of the same useful standards key bindins of the Sublime Text , I usually disable them

* Menu Option `tools -> color highlighter -> Disable default keybindings`

### [DocBlockr](https://github.com/spadgos/sublime-jsdocs)

Good plugin to help write documentation in __JavaScript__, __PHP__, __CofeeScript__, ...

![Screenshot DocBlockr](https://camo.githubusercontent.com/415148aecc6dac2e5ebb12b7f7584f4a8744eca4/687474703a2f2f73706164676f732e6769746875622e696f2f7375626c696d652d6a73646f63732f696d616765732f66756e6374696f6e2d74656d706c6174652e676966)

### How to use

* Press enter or tab after `/**` (or `###*` for Coffee-Script).

### ![EditorConfig Logo](http://editorconfig.org/logo.png) [EditorConfig](http://editorconfig.org/)

> EditorConfig helps developers define and maintain consistent coding styles between different editors and IDEs. The EditorConfig project consists of __a file format__ for defining coding styles and a collection of __text editor plugins__ that enable editors to read the file format and adhere to defined styles.

### How to use

* See the documentation: [EditorConfig Page](http://editorconfig.org/)

### [SFTP](http://wbond.net/sublime_packages/sftp)

FTP, FTPS and SFTP support for Sublime Text.

![Screenshots SFTP](http://wbond.net/sublime_packages/img/sftp/sidebar_menu_configured.png)

#### How to use

* Read the [instructions](http://wbond.net/sublime_packages/sftp/usage).

### [Can I Use](https://github.com/Azd325/sublime-text-caniuse)

Useful for quick check CSS property support on the [Can I Use site](http://caniuse.com/).

#### How to use

* Mark or place your cursor over a CSS property and press `ctrl` `alt` `f`.

### <img src="https://raw.githubusercontent.com/gulpjs/artwork/master/gulp.png" alt="gulpjs Logo" width="50"> [gulp](https://github.com/NicoSantangelo/sublime-gulp)

> A Gulp task runner with snippets.

#### How to use

> It's necessary a `gulpfile.js` in the open folder to run tasks.

* `ctrl` `shift` `p`
* Type `gulp`
* Select the task to run

![gulp screenshot](Screenshots/gulp.png)

See the documentation on [sublime-gulp](https://github.com/NicoSantangelo/sublime-gulp) to snippets.

### [Alignment](https://github.com/wbond/sublime_alignment)

> A simple key-binding for aligning multi-line and multiple selections.

![Alignment Screenshot](Screenshots/Alignment.gif)

#### How to use

* `ctrl` `alt` `a`

### [![CSS Comb Logo](https://raw.githubusercontent.com/csscomb/csscomb.js/master/logo.png) CSS Comb](http://csscomb.com/)

Coding style formatter for CSS.

#### How to use

* `ctrl` `shift` `c`

### [SublimeLinter](http://www.sublimelinter.com/)

### [Terminal](https://github.com/wbond/sublime_terminal)

> Launch terminals from the current file or the root project folder.

#### How to use

* `ctrl` `alt` `shift` `t` - Open Terminal at Project Folder

* `ctrl` `shift` `t` - Open Terminal at File -
    
    This key binding is the same of the default sublime reopen closed tab, I prefer to switch to `alt` `shift` `t`.

### [Icon-Fonts-Sublime-Text](https://github.com/idleberg/Icon-Fonts-Sublime-Text)

### [![GhostText for Sublime Text](https://raw.githubusercontent.com/Cacodaimon/GhostText-for-Chrome/master/promo/gt_banner-for-sublimetext.png)](https://github.com/Cacodaimon/GhostText-for-SublimeText)

> Allows live editing of Chrome text area or JS Code editor content with Sublime Text.

![Screenshot GhostText](http://img.youtube.com/vi/e0aLFPtYPZI/maxresdefault.jpg)

#### Addition Installation

- [Chrome Extension](https://chrome.google.com/webstore/detail/ghosttext-for-chrome/godiecgffnchndlihlpaajjcplehddca?utm_source=chrome-ntp-icon)

#### How to use

* In Chrome, click the GhostText button in the upper-right corner to open up Sublime Text.

## Additional Languages Support

Sublime Text has support for multiple languages, that aren't supported by default it's possible to be added with packages.

### [<img src="https://angularjs.org/img/AngularJS-large.png" alt="Angular JS Logo" width="170">](https://github.com/angular-ui/AngularJS-sublime-package)

Code completion, snippets, syntax file `HTML (Angular.js)` and more.

[JavaScript Completions](https://github.com/pichillilorenzo/JavaScript-Completions)

This package adds autocompletion for JavaScript codes.

![JavaScript Completions Example](https://camo.githubusercontent.com/f5fd60fb5e665a60891f04415afa3197965850c9/687474703a2f2f6935372e74696e797069632e636f6d2f3576363569612e676966)

[PHP Completions Kit](https://github.com/gerardroche/sublime-phpck)

Adds autocompletion for PHP codes.

### [<img src="http://lesscss.org/public/img/logo.png" alt="less logo" width="140">](https://github.com/danro/LESS-sublime)

Provides syntax highlighting for less.

### [<img src="http://sass-lang.com/assets/img/logos/logo-b6e1ef6e.svg" alt="Sass Logo" width="100">](https://sublime.wbond.net/packages/Sass)

Provides syntax highlighting and tab/code completion for Sass and SCSS files.

### [<img src="http://learnboost.github.io/stylus/docs/graphics/Logos/stylus.png" alt="Stylus Logo" width="120">](https://github.com/billymoon/Stylus)

> Includes build system and syntax highlighting for stylus CSS preprocessor.

#### Addition package

* [Stylus-Snippets](https://github.com/billymoon/Stylus-Snippets)

    This package complements [Stylus Package](https://github.com/billymoon/Stylus) includes Stylus Snippets, and allow dynamic expansion of CSS properties (use with Stylus plugin instead of emmet).

### [![Jquery](http://upload.wikimedia.org/wikipedia/en/thumb/9/9e/JQuery_logo.svg/200px-JQuery_logo.svg.png)](https://github.com/SublimeText/jQuery)

Provides syntax highlighting for jquery and snippets with methods.

### <img src="http://upload.wikimedia.org/wikipedia/commons/c/cd/ASF-logo.svg" alt="Apache Logo" width="90"> [Apache Conf](https://github.com/colinta/ApacheConf.tmLanguage)

Syntax Highlighting for .conf, .htaccess, .htgroups and .htpasswd

### [![Laravel Logo](http://laravel.com/assets/img/laravel-logo.png) Laravel Blade](https://github.com/Medalink/laravel-blade)

Syntax definitions for the Laravel Blade engine.

### [Robots](https://github.com/andriyko/sublime-robot-framework-assistant)

Provides some features for working with Robot Framework (.txt and .robot), like: Syntax highlighting, autocomplete and more.

## Working with Markdown ![Markdown Logo](https://raw.githubusercontent.com/dcurtis/markdown-mark/master/png/48x30.png)

There are softwares ([Mou](http://25.io/mou/), [Atom](https://atom.io/) and [Brackets](http://blog.brackets.io/2013/04/23/markdown-extension-for-brackets/)) that have a live preview when editing markdown. The Sublime Text doesn't have this feature, even with plugins, the closest to this was using these plugins.

### [MarkdownEditing](https://github.com/SublimeText-Markdown/MarkdownEditing)

Powerful Markdown package with syntax highlighter, snippets and themes.

![MarkdownEditing](https://raw.github.com/SublimeText-Markdown/MarkdownEditing/master/screenshots/light.png)

#### How to use

* See the documentation: [MarkdownEditing Page](https://github.com/SublimeText-Markdown/MarkdownEditing/blob/master/README.md)

### [OmniMarkupPreviewer](https://github.com/timonwong/OmniMarkupPreviewer)

Plugin to live preview markup files.

![OmniMarkupPreviewer Screenshots](Screenshots/OmniMarkupPreviewer.png)

#### How to use

* Open the markdown file
* `ctrl` `shift` `p`
* Select `OmniMarkupPreviewer: Preview Current Markup in Browser`


## Backing Up Sublime text

If you need reinstall Sublime Text, the best way to install all you packages fast is backing up the file `Package Control.sublime-settings`. This file store all installed packages.

To get the file, press `Ctrl` `Shift` `p` e type `Package Control Settings - User`.

Before reinstall Sublime Text, you need install the [package control](#package-control) and do the same step before and past the old file and save, just restart the Sublime Text and they will install all the packages.

## Creating Project

### Remove folders and files from project

Open the `.sublime-project` file

Insert `folder_exclude_patterns` to ignore folders and `file_exclude_patterns` to ignore files.

```
{
   "folders":
   [
      {
         "path": "/home/jack/workspace/myproject",
         "folder_exclude_patterns": ["*", "*"],
         "file_exclude_patterns": ["*", "*"]
      }
   ]
}
```





<!--
http://code.tutsplus.com/courses/perfect-workflow-in-sublime-text-2/lessons/your-first-snippet
https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/
http://tableless.com.br/dicas-truques-sublime-text/?utm_content=buffer5dd8f&utm_medium=social&utm_source=facebook.com&utm_campaign=buffer
 -->
