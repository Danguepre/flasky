from flask import render_template, request, jsonify
from app.modules.env_requirement import env_requirement_bp
from app.modules.env_requirement.forms import EnvRequirementForm
from app.modules.env_requirement.services import EnvRequirementService


@env_requirement_bp.route('/env_requirement', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        query = request.args.get('query', '')
        form = EnvRequirementForm()  # Formulario de búsqueda (si lo necesitas)
        return render_template('env_requirement/index.html', form=form, query=query)

    if request.method == 'POST':
        # Recibir los criterios de filtrado en formato JSON
        criteria = request.get_json()
        datasets = EnvRequirementService().filter(**criteria)
        return jsonify([dataset.to_dict() for dataset in datasets])
