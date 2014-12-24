# Setting Up Sublime Text 3

<p align="center"><img src="http://upload.wikimedia.org/wikipedia/en/4/4c/Sublime_Text_Logo.png" alt="Sublime Text Logo" width="120" ></p>

> This is not a step by step guide for anyone who starts with [Sublime Text](http://www.sublimetext.com/), these are the settings and reminders that fit in my workflow. You can choose what to install.

> If they works for me, may also be useful for you.

## Sublime Text

Download and install [Sublime Text](http://www.sublimetext.com/)

[http://www.sublimetext.com/3](http://www.sublimetext.com/3)

## Packages (Plugins)

[Package Control](https://sublime.wbond.net/)

1. Open Console in the menu options `View > Show Console`

1. Paste and execute

<code>import urllib.request,os,hashlib; h = '2deb499853c4371624f5a07e27c334aa' + 'bf8c4e67d14fb0525ba4f89698a6d7e1'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)</code>

[SideBarEnhancements](https://github.com/titoBouzout/SideBarEnhancements)



[AngularJS](https://github.com/angular-ui/AngularJS-sublime-package)

[AutoFileName](https://github.com/BoundInCode/AutoFileName)

[Bracket Highlighter](https://github.com/facelessuser/BracketHighlighter)

[Can I Use](https://github.com/Azd325/sublime-text-caniuse)

Keyboard shortcut `ctrl+alt+f`

[Color Picker](http://weslly.github.io/ColorPicker/)

Keyboard shortcut `ctrl+shift+c`

[ColorHighlighter](https://github.com/Monnoroch/ColorHighlighter)

Disable keybindings

`tools -> color highlighter -> Disable default keybindings`

[EditorConfig](http://editorconfig.org/)

[Emmet](http://docs.emmet.io/)

[GhostText](https://github.com/Cacodaimon/GhostText-for-SublimeText)

- [Extension for Chrome](https://chrome.google.com/webstore/detail/ghosttext-for-chrome/godiecgffnchndlihlpaajjcplehddca?utm_source=chrome-ntp-icon)

[Gist](https://github.com/condemil/Gist)

[Gulp](https://github.com/NicoSantangelo/sublime-gulp)

[Markdown Preview](https://github.com/revolunet/sublimetext-markdown-preview)

[SFTP](http://wbond.net/sublime_packages/sftp)

[Tag](https://github.com/SublimeText/Tag)

[Terminal](https://github.com/wbond/sublime_terminal)

Keyboard shortcut `ctrl+alt+shift+t` to project folder

Keyboard shortcut `ctrl+shift+t` to file

[Trailing Spaces](https://github.com/SublimeText/TrailingSpaces)

[Jquery](https://github.com/SublimeText/jQuery)


## Additional Syntax Support

[Apache Conf](https://github.com/colinta/ApacheConf.tmLanguage)

[LESS](https://github.com/danro/LESS-sublime)

[Robots](https://github.com/andriyko/sublime-robot-framework-assistant)

[SASS](https://sublime.wbond.net/packages/Sass)

[Stylus](https://github.com/billymoon/Stylus)

[Stylus-Snippets](https://github.com/billymoon/Stylus-Snippets)


## Snippets

Local Folder

* Windows

`C:\Users\Name User\AppData\Roaming\Sublime Text 3\Packages\User`

[Comment Snippets](https://github.com/hachesilva/Comment-Snippets)

[JavaScript Console snippets](https://github.com/caiogondim/js-console-sublime-snippets)

[Jquery](https://sublime.wbond.net/packages/jQuery)

[Readme](https://gist.github.com/zenorocha/4526327) - Snippet from Zeno Rocha


## Key Bindings

### Mac OS

Super + b = `<strong>selection</strong>`

Super + i = `<em>selection</em>`

Super + u = `<u>selection</u>`

Super + alt + 7 = `encode_html_entities`

### Windows

 = `<strong>selection</strong>`

Ctrl + i = `<em>selection</em>`

Ctrl + u = `<u>selection</u>`

Ctrl + alt + 7 = `encode_html_entities`

## Tips

* `Ctrl + k + Ctrl + v` = Paste History

* `f11` = full screen

* `shift + f11` = distract mode

### Workspace

* Layout in 2 columns `view/layout/Columns:2` or `alt+shift+2`