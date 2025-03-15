from flask_wtf import FlaskForm
from wtforms import SubmitField


class CropForm(FlaskForm):
    submit = SubmitField('Save crop')