from wtforms import Form, StringField, validators, SubmitField


class CreatePostForm(Form):
    title = StringField("Title", validators=[
        validators.Length(min=10, message="Title must have at least 10 chars"),
        validators.DataRequired()], render_kw={"placeholder": "Enter a post title"})
    description = StringField("descrition",validators=[validators.Length(min="10",max="200",
                                message="Your post description must be between 10 and 250 characters")],
                              render_kw={"placeholder":"Enter a post description"})

    description = StringField("description", validators=[validators.Length(min=10,max=200,
                              message="Your post description must be between 10 and 250 characters"),
                              validators.DataRequired()], render_kw={"placeholder":"Enter a post description"})

    content = StringField("content", validators=[
        validators.Length(min=10, max=100000, message="Your post must contain between 10 and 100000 characters"),
        validators.DataRequired()], render_kw={"placeholder": "Enter a post"})

    submit = SubmitField("Create Post")
