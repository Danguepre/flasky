from flask_wtf import FlaskForm
from wtforms import SubmitField


class FavouriteCropForm(FlaskForm):
    submit = SubmitField('Save favourite crop')