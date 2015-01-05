# Setting Up Sublime Text 3

<p align="center"><img src="http://upload.wikimedia.org/wikipedia/en/4/4c/Sublime_Text_Logo.png" alt="Sublime Text Logo" width="120" ></p>

This is not a step by step guide for anyone who starts with [Sublime Text](http://www.sublimetext.com/). These are the settings and reminders that fit in my workflow. You can choose what to install.

> If they are useful to me, may also be useful for you.

## Sublime Text

Download and install [Sublime Text](http://www.sublimetext.com/).

[http://www.sublimetext.com/3](http://www.sublimetext.com/3)

## Summary
* [Key Bindings](#key-bindings)
* [Snippets](#snippets)
* [Packages](#packages)
* [Additional Syntax Support](#additional-syntax-support)
* [Working With Markdown](#working-with-markdown-)
* [Reminders](#reminders)


## Key Bindings

All key bindings are configurable, you can change default key bindings or create new.

<!--
### Mac OS

`Super` `b` = `<strong>selection</strong>`

`Super` `i` = `<em>selection</em>`

`Super` `u` = `<u>selection</u>`

`Super` `alt` `7` = `encode_html_entities`

### Windows

`Ctrl` `b` = `<strong>selection</strong>`

`Ctrl` `i` = `<em>selection</em>`

`Ctrl` `u` = `<u>selection</u>`

`Ctrl` `alt` `7` = `encode_html_entities`
-->


## Snippets

> Snippets are smart templates that will insert text for you and adapt it to their context.

### How it works

The snippets are triggered with the `tab` key after the snippet access string.

#### Example

When you write `jquery` and press `tab`, the Sublime Text identifies you need snippet `jQuery Fallback` and replaces the entire access sequence throughout the template. You can still edit some parts of the template by pressing `tab` to pass between the editable parts.

![Snippets Usage Example](Screenshots/snippet.gif)

<!--
Local Folder

* Windows

`C:\Users\{username}\AppData\Roaming\Sublime Text 3\Packages\User`

[Readme](https://gist.github.com/zenorocha/4526327) - Snippet from Zeno Rocha

-->

### Creating your own snippets

<!--
`ctrl` `shift` `alt` `p`
-->

## Packages

Packages in Sublime Text are a collection of resource files used to extend functionalities, they can be: plugins, syntax highlighting, menus, snippets...

There are a lot of custom packages to install, you can install packages to your necessity or you can create your own package.

### [Package Control](https://sublime.wbond.net/)

Package Control manage all packages, makes it simple to find, install, remove and keep packages up-to-date.

#### Installation

* Open Console in the menu options `View > Show Console`

* Paste the following code and execute

<code>import urllib.request,os,hashlib; h = '2deb499853c4371624f5a07e27c334aa' + 'bf8c4e67d14fb0525ba4f89698a6d7e1'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)</code>

#### How to use

Installing packages

* `ctrl` `shift` `p`
* Type `install`
* Select `Package Control: Install Package`
* Search the package you want to install

Removing packages

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

* Copy the file [trailing_spaces.sublime-settings](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Packages%20Settings/trailing_spaces.sublime-settings) in the folder `C:\Users\{username}\AppData\Roaming\Sublime Text 3\Packages\User` in windows or ` ~/Library/Application Support/Sublime Text 3` in OS X.


### ![Emmet Logo](http://emmet.io/i/logo.svg) [Emmet](http://emmet.io/)

Emmet is the most essential plugin for web-developers, it helps you write HTML and CSS code easily, expanding simple abbreviations into complex code snippets.

![Emmet Screenshot](http://media.mediatemple.netdna-cdn.com/wp-content/uploads/2013/03/initializers.gif)

![Emmet Screnshot](http://media.mediatemple.netdna-cdn.com/wp-content/uploads/2013/03/multiplication.gif)

* Watch the demo in [http://emmet.io/](http://emmet.io/)
* Read this great tutorial: [Goodbye, Zen Coding. Hello, Emmet!](http://www.smashingmagazine.com/2013/03/26/goodbye-zen-coding-hello-emmet/)
* Learn the syntax in [Cheat Sheet](http://docs.emmet.io/cheat-sheet/)

### [Color Picker](http://weslly.github.io/ColorPicker/)

Open a Color Picker in Sublime Text.

![Mac OSX](http://i.minus.com/i5KI6SBAfs7Qk.png)

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

![Screenshot SFTP](http://wbond.net/sublime_packages/img/sftp/sidebar_menu_unconfigured.png)

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

##### Run Tasks

> It's necessary a `gulpfile.js` in an open folder.

* `ctrl` `shift` `p`
* Type `gulp`
* Select the task to run

![gulp screenshot](Screenshots/gulp.png)

##### Snippets

* See the documentation on [sublime-gulp](https://github.com/NicoSantangelo/sublime-gulp)

### [Terminal](https://github.com/wbond/sublime_terminal)

> Launch terminals from the current file or the root project folder.

#### How to use

##### Open Terminal at Project Folder
* `ctrl` `alt` `shift` `t`

##### Open Terminal at File

* `alt` `shift` `t`

The default key binding is `ctrl` `shift` `t`, the same of the default sublime reopen closed tab, I changed.

* Copy the file
    * [Default (Windows).sublime-keymap](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Packages%20Settings/Terminal/Default%20(Windows).sublime-keymap) in the folder `C:\Users\{username}\AppData\Roaming\Sublime Text 3\Packages\Terminal` in windows
    * [Default (OSX).sublime-keymap](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Packages%20Settings/Terminal/Default%20(OSX).sublime-keymap) in the folder `~/Library/Application Support/Sublime Text 3/Packages/Terminal` in OS X
    * [Default (Linux).sublime-keymap](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Packages%20Settings/Terminal/Default%20(Linux).sublime-keymap) in the folder `~/.config/sublime-text-3/Packages/Terminal` in OS X

### [![GhostText for Sublime Text](https://raw.githubusercontent.com/Cacodaimon/GhostText-for-Chrome/master/promo/gt_banner-for-sublimetext.png)](https://github.com/Cacodaimon/GhostText-for-SublimeText)

> Allows live editing of Chrome text area or JS Code editor content with Sublime Text.

![Screenshot GhostText](http://img.youtube.com/vi/e0aLFPtYPZI/maxresdefault.jpg)

#### Addition Installation

- [Chrome Extension](https://chrome.google.com/webstore/detail/ghosttext-for-chrome/godiecgffnchndlihlpaajjcplehddca?utm_source=chrome-ntp-icon)

#### How to use

* In Chrome, click the GhostText button in the upper-right corner to open up Sublime Text.

## Additional Syntax Support

Sublime Text has support for multiple languages, that aren't supported by default it's possible to be added with packages.

### [<img src="http://lesscss.org/public/img/logo.png" alt="less logo" width="140">](https://github.com/danro/LESS-sublime)

Provides syntax highlighting for less.

### [<img src="http://sass-lang.com/assets/img/logos/logo-235e394c.png" alt="Sass Logo" width="100">](https://sublime.wbond.net/packages/Sass)

Provides syntax highlighting and tab/code completion for Sass and SCSS files.

### [<img src="http://learnboost.github.io/stylus/docs/graphics/Logos/stylus.png" alt="Stylus Logo" width="120">](https://github.com/billymoon/Stylus)

> Includes build system and syntax highlighting for stylus CSS preprocessor.

#### Addition package

* [Stylus-Snippets](https://github.com/billymoon/Stylus-Snippets)

    This package complements [Stylus Package](https://github.com/billymoon/Stylus) includes Stylus Snippets, and allow dynamic expansion of CSS properties (use with Stylus plugin instead of emmet).

### [![Jquery](http://upload.wikimedia.org/wikipedia/en/thumb/9/9e/JQuery_logo.svg/200px-JQuery_logo.svg.png)](https://github.com/SublimeText/jQuery)

Provides syntax highlighting for jquery and snippets with methods.

### [<img src="https://angularjs.org/img/AngularJS-large.png" alt="Angular JS Logo" width="170">](https://github.com/angular-ui/AngularJS-sublime-package)

Code completion, snippets, syntax file `HTML (Angular.js)` and more.

### <img src="http://upload.wikimedia.org/wikipedia/commons/c/cd/ASF-logo.svg" alt="Apache Logo" width="90"> [Apache Conf](https://github.com/colinta/ApacheConf.tmLanguage)

Syntax Highlighting for .conf, .htaccess, .htgroups and .htpasswd

### [![Laravel Logo](http://laravel.com/assets/img/logo-head.png) Blade](https://github.com/Medalink/laravel-blade)

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

## Reminders

If you're like me and always confused with a lot of shortcuts, it's for us. A list of useful shortcuts.

<!--
### Multiple Selection

`Ctrl+D` on Windows and Linux, or `Command+D` on OS X Quick Add Next

* `Alt+F3` on Windows and Linux, or `Ctrl+Command+G` on OS X. Find All

`Ctrl+Shift+L` or `Command+Shift+L` on OS X. Splitting the Selection into Lines

`Ctrl+K,Ctrl+D` on Windows and Linux, or `Command+K,Command+D` on OS X. Quick Skip Next

 if you go too far, use Undo Selection (Ctrl+U, or Command+U on OS X) to step backwards

* `ctrl` `k` `ctrl` `v` = Paste History
* `f11` = full screen
* `shift` `f11` = distract mode
* `ctrl` `shift` `t` = Reopen Closed Tab
* `ctrl` `shift` `a` = expand selection to tag

### Workspace

* Layout in 2 columns `view/layout/Columns:2` or `alt+shift+2`
* -->


<!--
http://code.tutsplus.com/courses/perfect-workflow-in-sublime-text-2/lessons/your-first-snippet

[Comment Snippets](https://github.com/hachesilva/Comment-Snippets)
[JavaScript Console snippets](https://github.com/caiogondim/js-console-sublime-snippets)
https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/
https://github.com/mrmartineau/Placeholders
https://github.com/wbond/sublime_alignment
http://csscomb.com/
https://github.com/sobstel/SyncedSideBar
https://github.com/purplefish32/sublime-text-2-wordpress
https://github.com/SublimeLinter/SublimeLinter-for-ST2
http://www.sublimelinter.com/en/latest/
 -->