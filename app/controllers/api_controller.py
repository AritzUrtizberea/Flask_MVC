from flask import Blueprint, jsonify
from app.services.libros_service import LibroService
from app.services.socio_service import SocioService
from app.utils.decorators import login_required 

api_bp = Blueprint('api', __name__, url_prefix='/api')

# --- R21: api/libros (Cualquiera) ---
@api_bp.route('/libros', methods=['GET'])
def api_listar_libros():
    libros = LibroService.obtener_todos()
    # CAMBIO: Usamos to_dict() en lugar de crear el diccionario aquí
    return jsonify([libro.to_dict() for libro in libros])

# --- R22: api/libros/disponibles (Cualquiera) ---
@api_bp.route('/libros/disponibles', methods=['GET'])
def api_libros_disponibles():
    libros = LibroService.obtener_todos(solo_disponibles=True)
    # CAMBIO: Delegamos la estructura al Modelo
    return jsonify([libro.to_dict() for libro in libros])

# --- R23: api/libros/buscar/<titulo> (Cualquiera) ---
@api_bp.route('/libros/buscar/<string:titulo>', methods=['GET'])
def api_buscar_libro(titulo):
    libros = LibroService.obtener_todos(busqueda=titulo)
    # CAMBIO: Código mucho más limpio
    return jsonify([libro.to_dict() for libro in libros])

# --- R24: api/libros/socios/prestamos (Admin) ---
@api_bp.route('/libros/socios/prestamos', methods=['GET'])
@login_required 
def api_socios_con_prestamos():
    socios = SocioService.obtener_todos(solo_con_prestamos=True)
    # CAMBIO: El modelo Socio ya sabe cómo listar sus libros en su to_dict()
    return jsonify([socio.to_dict() for socio in socios])