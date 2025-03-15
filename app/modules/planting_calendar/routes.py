from flask import render_template, request, jsonify
from app.modules.planting_calendar import planting_calendar_bp
from app.modules.planting_calendar.forms import PlantingCalendarForm  # Si tienes algún formulario
from app.modules.planting_calendar.services import PlantingCalendarService


@planting_calendar_bp.route('/planting_calendar', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        query = request.args.get('query', '')
        form = PlantingCalendarForm()  # Formulario de búsqueda (si lo necesitas)
        return render_template('planting_calendar/index.html', form=form, query=query)

    if request.method == 'POST':
        # Recibir los criterios de filtrado en formato JSON
        criteria = request.get_json()
        datasets = PlantingCalendarService().filter(**criteria)
        return jsonify([dataset.to_dict() for dataset in datasets])
