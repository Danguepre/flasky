from flask import render_template, request, jsonify
from app.modules.favourite_crop import favourite_crop_bp
from app.modules.favourite_crop.forms import FavouriteCropForm  # Si tienes algún formulario
from app.modules.favourite_crop.services import FavouriteCropService


@favourite_crop_bp.route('/favouriteCrops', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        query = request.args.get('query', '')
        form = FavouriteCropForm()  # Formulario de búsqueda (si lo necesitas)
        return render_template('crop/index.html', form=form, query=query)

    if request.method == 'POST':
        # Recibir los criterios de filtrado en formato JSON
        criteria = request.get_json()
        datasets = FavouriteCropService().filter(**criteria)
        return jsonify([dataset.to_dict() for dataset in datasets])
