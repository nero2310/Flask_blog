from wtforms import Form, PasswordField, StringField, validators, SubmitField


class UserRegisterForm(Form):
    username = StringField("Username", validators=[
        validators.Length(min=4, max=20, message="Your user name must contain bettwen 4 and 20 characters"),
        validators.DataRequired()], render_kw={"placeholder": "Enter a user name"})

    password = PasswordField("password", validators=[
        validators.Length(min=8, max=64, message="Your password must contain between 8 and 64 characters"),
        validators.DataRequired(), validators.EqualTo("confirm_password", message="Password must match")],
        render_kw={"placeholder": "Enter a password"})

    email = StringField("Email", validators=[validators.email(message="This is not a valid email adress"),
                                             validators.DataRequired()], render_kw={"placeholder": "Enter a email"})

    confirm_password = PasswordField("Repeat password", validators=[validators.DataRequired()],
                                     render_kw={"placeholder": "Repeat password"})

    submit = SubmitField("Sign Up")
