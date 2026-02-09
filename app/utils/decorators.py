from functools import wraps
from flask import flash, redirect, url_for, session
from app.models.libro import Libro  # <--- CAMBIO: Importamos Libro, no Prestamo

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Si NO hay usuario en la sesión, lo mandamos al login
        if 'user_id' not in session:
            flash('Acceso denegado. Debes iniciar sesión.', 'danger')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

def libro_disponible_required(f):
    @wraps(f)
    def decorated_function(id, *args, **kwargs):
        # Buscamos el libro
        libro = Libro.query.get(id)
        if not libro:
            flash('Libro no encontrado.', 'danger')
            return redirect(url_for('libros.index'))
            
        # CAMBIO: Si tiene socio_id, es que está prestado
        if libro.socio_id is not None:
            flash('Este libro ya está prestado.', 'warning')
            return redirect(url_for('libros.index'))
            
        return f(id, *args, **kwargs)
    return decorated_function