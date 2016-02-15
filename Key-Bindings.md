## Table of Contents

* [Useful Key Bindings](#useful-key-bindings)
    - [Workspace](#workspace)
    - [Selection](#selection)
    - [Utilities](#utilities)
* [Custom Key Bindings](#custom-key-bindings)
* [Packages](#packages)
    - [Keymaps](#keymaps)
    - [Find Key Conflicts](#find-key-conflicts)


## Useful Key Bindings

If you're like me and always confused with a lot of key bindings, it's for us. A list of useful shortcuts.

### Workspace

| Win & Linux | Mac OS | description |
| --- | --- | --- |
| `f11` | |  Full screen |
| `shift` `f11` | | Distract mode |
| `alt` `shift` `2` | | Layout in 2 columns |
| `alt` `shift` `8` | | Layout in 2 rows |

### Selection

| Win & Linux | Mac OS | description |
| --- | --- | --- |
| `Ctrl` `d` | `Command` `d` | Quick Add Next. |
| `Click the word` <br> `Alt` `F3` | `Click the word` <br> `Ctrl` `Command` `g` | Find All <br> <img src="https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Screenshots/quick-find-all.gif" width="450" > |
| `Ctrl` `Shift` `l` | `Command` `Shift` `l` | Splitting the Selection with a cursor at the end of each line |
| `Ctrl` `k`, <br> `Ctrl` `d` | `Command` `k`, <br> `Command` `d` | Quick Skip Next |
| `Ctrl` `u` | `Command` `u` | If you go too far, use Undo Selection to step backwards |
| `ctrl` `shift` `a` | `Ctrl` `Shift` `w` | Expand selection to tag |
| `Ctrl` `Shift` `↑` or `↓` | `⌘` `Ctrl` `↑`  or `↓` | <img src="https://github.com/wesbos/Sublime-Text-Power-User-Talk/raw/gh-pages/images/bubble.gif" width="450"> |
| `Ctrl` `shift` `w` | `Ctrl` `alt` `enter` | wrap selection with tag |



### Utilities

| Win & Linux | Mac OS | description |
| --- | --- | --- |
| `ctrl` `shift` `ç` | | Delete tag |
| `ctrl` `enter` | `command` `enter` | Insert a new line after the current paragraph and jump to it |
| `ctrl` `shift` `enter` | `command` `shift` `enter` | Insert a new line before the current paragraph and jump to it |
| `ctrl` `k`, `ctrl` `space` | | Set Mark |
| `ctrl` `k`, `ctrl` `x` | | Swap with Mark |
| `ctrl` `r` | | Jump to any heading in the document or the project and see the indentation level |
| `ctrl` `x` | | Cut the line |
| `ctrl` `k` `k` | | Delete from cursor to end of line |
| `ctrl` `k`, `ctrl` `v` | | Paste History |
| `ctrl` `shift` `t` | | Reopen Closed Tab |
| `ctrl` `shift` `alt` `p` | | Get the syntax scope, useful when creating snippets |


[Sublime Text Keyboard Shortcut Cheat Sheet](http://sweetme.at/2013/08/08/sublime-text-keyboard-shortcuts/)

[Sublime Text 2 – Useful Shortcuts (PC)](https://gist.github.com/eteanga/1736542)


## Custom key bindings

All key bindings are configurable, you can change default key bindings or create new.

I have customized the following key bindings.

| Win & Linux | Mac OS | description |
| --- | --- | --- |
| `Ctrl` `b` | `⌘` `b` | `<strong>selection</strong>` |
| `Ctrl` `i` | `⌘` `i` | `<em>selection</em>` |
| `Ctrl` `u` | `⌘` `u` | `<u>selection</u>` |

### How to use

Download the file and save on the right folder

* [Default (Windows).sublime-keymap](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Sublime%20Settings/Default%20(Windows).sublime-keymap) in the folder `C:\Users\{username}\AppData\Roaming\Sublime Text 3\Packages\User` on Windows.

* [Default (OSX).sublime-keymap](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Sublime%20Settings/Default%20(OSX).sublime-keymap) in the folder `~/Library/Application Support/Sublime Text 3/Packages/User` in OS X.

## Packages

### [Keymaps](https://github.com/MiroHibler/sublime-keymaps)

Enables searching for keymaps and show all enabled keymaps in a searchable  Cheat Sheet.

### [Find Key Conflicts](https://github.com/skuroda/FindKeyConflicts)

Help identify conflicting key mappings.