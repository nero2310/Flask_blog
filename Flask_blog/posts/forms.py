from wtforms import Form, StringField, validators, SubmitField


class CreatePostForm(Form):
    title = StringField("Title", validators=[
        validators.Length(min=10, message="Title must have at least 10 chars"),
        validators.DataRequired()], render_kw={"placeholder": "Enter a post title"})

    content = StringField("content", validators=[
        validators.Length(min=10, max=100000, message="Your post must contain between 10 and 100000 characters"),
        validators.DataRequired()], render_kw={"placeholder": "Enter a post content"})

    submit = SubmitField("Create Post")
