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

If you use retina or HiDPI screen, you can use this settings and your text will become crisp and readable!

```json
    "font_options": ["gray_antialias"]
```

## Font

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

### Other suggestions

[Monoid](http://larsenwork.com/monoid/)

[Source Code Pro](https://github.com/adobe-fonts/source-code-pro)


## Theme and Color Schema

If you don't like of the Monokai, the default theme of Sublime you can change it. By default Sublime there are some fews options.

`Menu Bar` > `Preferences` > `Color Schema` > `Color Schema Default` > `Default Themes`

You also download a theme by Package Control.

[colorsublime](http://colorsublime.com/)

This is a good plugin that help you to preview themes before install.

### Creating your own Sublime Text theme

On the other hand, may you want your own theme.

[tmtheme-editor](http://tmtheme-editor.herokuapp.com/)

This is a web editor that you can make your theme and donwload.

[ColorSchemeEditor](https://github.com/bobef/ColorSchemeEditor)

This package helps you edit a theme directly in the Sublime Text.