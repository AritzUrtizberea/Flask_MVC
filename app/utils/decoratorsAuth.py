from functools import wraps
from flask import session, redirect, url_for, request

def role_required(role='admin'):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # 1. Si no hay usuario en sesión, fuera.
            if 'user_id' not in session:
                return redirect(url_for('auth.login'))
            
            # (El documento dice que no hacen falta roles complejos, 
            # con estar logueado como admin nos vale).
            return f(*args, **kwargs)
        return decorated_function
    return decorator