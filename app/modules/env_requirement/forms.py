from flask_wtf import FlaskForm
from wtforms import SubmitField


class EnvRequirementForm(FlaskForm):
    submit = SubmitField('Save env_requirement')
