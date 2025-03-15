from flask_wtf import FlaskForm
from wtforms import SubmitField


class PlantingCalendarForm(FlaskForm):
    submit = SubmitField('Save planting_calendar')