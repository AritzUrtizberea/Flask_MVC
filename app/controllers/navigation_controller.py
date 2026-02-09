from flask import Blueprint, render_template
from app.utils.decoratorsAuth import role_required # Importamos el decorador

navigation_bp = Blueprint('navigation', __name__)

@navigation_bp.route('/')
@role_required('admin') # REQUISITO CUMPLIDO
def home():
    return render_template('paginas/inicio.html')