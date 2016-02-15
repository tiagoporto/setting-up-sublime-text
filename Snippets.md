## Table of Contents

* [What's snippets?](#Whats-snippets)
    - [Example](#example)
* [Creating your own snippets](#creating-your-own-snippets)
    - [My Snippets](#my-snippets)
        + [Form template](#form-template)
        + [Project Header](#project-header)
        + [Readme](#readme)
* [Packages](#packages)
    - [Comment Snippets](#comment-snippets)
    - [Front-end Project Snippets](#front-end-project-snippets)
    - [Ionic Framework](#ionic-framework)
    - [Svg Icon](#svg-icon)
    - [Icon-Fonts-Sublime-Text](#icon-fonts-sublime-text)

## What's snippets?

> Snippets are smart templates that will insert text for you and adapt it to their context.

The snippets are triggered with the `tab` key after the snippet access string.

### Example

When you write `jquery` and press `tab`, the Sublime Text identifies you need snippet `jQuery Fallback` and replaces the entire access sequence throughout the template. You can still edit some parts of the template by pressing `tab` to pass between the editable parts.

![Snippets Usage Example](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Screenshots/snippet.gif)

## Creating your own snippets

[Snippets in Sublime Text 2](http://web-design-weekly.com/2012/07/03/snippets-in-sublime-text-2/)


### My Snippets

If you want use some of this snippets, download the files and copy in your local folder:

* `C:\Users\{username}\AppData\Roaming\Sublime Text 3\Packages\User` in windows

* ` ~/Library/Application Support/Sublime Text 3/Packages/User` in OS X

* `~/.config/sublime-text-3/Packages/User` in Linux


#### [Form Template](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Snippets/Form%20Template.sublime-snippet)

To use write `form-template` and press `tab`.

```html
<form action="#" method="POST">
    <fieldset>
        <legend>My Semantic Form</legend>

        <p>
            <label for="username">Username*</label>
            <input id="username" type="text" name="username" maxlength="10" aria-required="true" required>
        </p>

        <p>
            <label for="email">Email*</label>
            <input id="email" type="email" name="email" required>
        </p>

        <p>
            <label for="disabled">Disabled</label>
            <input id="disabled" type="text" name="disabled" disabled>
        </p>

        <p>
            <label for="number">Number</label>
            <input id="number" type="number" name="number" min="1" max="5">
        </p>

        <p>
            <label for="birthday">Birthday</label>
            <input id="birthday" type="text" maxlength="10" name="birthday" pattern="[0-9]{2}\/[0-9]{2}\/[0-9]{4}$">
        </p>

        <p>
            <label for="hour">Hour</label>
            <input id="hour" type="text" maxlength="8" name="hour" pattern="[0-9]{2}:[0-9]{2} [0-9]{2}$">
        </p>

        <p>
            <input type="range" name="points" min="0" max="10">
        </p>

        <p>
            <label for="phone">Phone</label>
            <input id="phone" type="text" name="phone" maxlength="15" pattern="\([0-9]{2}\) [0-9]{4,6}-[0-9]{3,4}$">
        </p>

        <p>
            <label>Sex</label>

            <label><input type="radio" name="sex" value="male" checked>Male</label>

            <label><input type="radio" name="sex" value="female">Female</label>
        <p>

        <p>
            <label>Checkbox</label>

            <label><input type="checkbox" name="vehicle" value="Bike"> I have a bike</label>

            <label><input type="checkbox" name="vehicle" value="Car"> I have a car</label>
        </p>

        <p>
            <label id="choose2">Drop</label>

            <select name="choose">
                <optgroup label="Swedish Cars">
                    <option value="volvo">Volvo</option>
                    <option value="saab">Saab</option>
                </optgroup>
                <optgroup label="German Cars">
                    <option value="mercedes">Mercedes</option>
                    <option value="audi">Audi</option>
                </optgroup>
            </select>
        </p>

        <p>
            <label for="comment">Comment</label>

            <textarea id="comment" name="comment" rows="3" cols="50"></textarea>
        </p>


        Send a file <input type="file" name="file">


        <input type="hidden" name="userID" value="1">
    </fieldset>

    <fieldset>
        <p>
            <label for="password">Password</label>
            <input id="password" type="password" name="password">
        </p>
    </fieldset>

    <p><em>* Required Fields</em></p>

    <button type="submit">Send</button>
</form>
```



#### [Project Header](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Snippets/Project%20Header.sublime-snippet)

To use write `project-header` and press `tab`.

```css
/*!
+   My Project v1.0.0
+   http://myproject.com
+   Copyright (c) 2010-2015 Author Name (http://authorsite.com)
+   Released under the MIT license
*/
```


#### [Readme](https://raw.githubusercontent.com/tiagoporto/setting-up-sublime-text/master/Snippets/Readme%20File.sublime-snippet)

To use write `readme` and press `tab`.

* [Example of readme Snippet](https://github.com/tiagoporto/setting-up-sublime-text/blob/master/readme-snippet-example.md)


## Packages

### [Comment Snippets](https://github.com/hachesilva/Comment-Snippets)

> Several snippets to create fancy PHP, CSS and HTML comments.

![Comment Snippets Example](https://raw.githubusercontent.com/hachesilva/Comment-Snippets/master/CommentSnippets.gif)

### How it works

[See the documentation](https://github.com/hachesilva/Comment-Snippets)

### [Front-end Project Snippets](https://github.com/brazilian-dev/sublime-front-end-snippets)

A lot of useful front-end snippets

![Front-end Project Snippets examples](https://cloud.githubusercontent.com/assets/1963897/12625364/a94decc8-c51a-11e5-8546-ca331af65982.gif)

### [Ionic Framework](https://github.com/imsingh/ionic-sublime-plugin)

Snippets for Ionic Framework



### [SVG Icon](https://github.com/s10wen/Sublime-Text-SVG-Icon-Snippets)

> A collection of SVG icon snippets

![Svg printscreen](https://camo.githubusercontent.com/ec5b66022217a1041f472bafe7bd752d4d4df5b7/687474703a2f2f672e7265636f726469742e636f2f4a62797374385953736a2e676966)
![Svg printscreen](https://raw.githubusercontent.com/s10wen/Sublime-Text-SVG-Icon-Snippets/master/images/icons-preview.png)




## [Icon Fonts Sublime Text](https://github.com/idleberg/Icon-Fonts-Sublime-Text)

> Completions for popular icon fonts such as Font Awesome, Glyphicons and many more!

![Icon fonts print](https://raw.github.com/idleberg/Icon-Fonts-Sublime-Text/master/screenshot.gif)