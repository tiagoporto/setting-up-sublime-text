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
            <label for="birthday">Birthday</label>
            <input id="birthday" type="text" maxlength="10" name="birthday" pattern="[0-9]{2}\/[0-9]{2}\/[0-9]{4}\$">
        </p>

        <p>
            <label for="hour">Hour</label>
            <input id="hour" type="text" maxlength="8" name="hour" pattern="[0-9]{2}:[0-9]{2} [0-9]{2}\$">
        </p>

        <p>
            <input type="range" name="points" min="0" max="10">
        </p>

        <p>
            <label for="phone">Phone</label>
            <input id="phone" type="text" name="phone" maxlength="15" pattern="\([0-9]{2}\) [0-9]{4,6}-[0-9]{3,4}\$">
        </p>

        <p>
            <label>Sex</label>

            <input type="radio" name="sex" value="male" checked>Male
            <input type="radio" name="sex" value="female">Female
        <p>

        <p>
            <label>Checkbox</label>

            <input type="checkbox" name="vehicle" value="Bike"> I have a bike
            <input type="checkbox" name="vehicle" value="Car"> I have a car
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
        <label for="password">Password</label>
        <input id="password" type="password" name="password">
    </fieldset>

    <p><em>* Required Fields</em></p>

    <button type="submit">Send</button>
</form>
``