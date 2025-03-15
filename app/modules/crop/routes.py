from flask import render_template, request, jsonify
from app.modules.crop import crop_bp
from app.modules.crop.forms import CropForm  # Si tienes algún formulario
from app.modules.crop.services import CropService


@crop_bp.route('/crops', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        query = request.args.get('query', '')
        form = CropForm()  # Formulario de búsqueda (si lo necesitas)
        return render_template('crop/index.html', form=form, query=query)

    if request.method == 'POST':
        # Recibir los criterios de filtrado en formato JSON
        criteria = request.get_json()
        datasets = CropService().filter(**criteria)
        return jsonify([dataset.to_dict() for dataset in datasets])
