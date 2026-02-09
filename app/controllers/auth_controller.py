from flask import Blueprint, render_template, redirect, url_for, flash, session
from app.services.auth_service import AuthService
from app.forms.auth_form import LoginForm # Importamos el form seguro

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm() # Usamos la clase form
    
    # Esto sustituye a 'if request.method == POST' y valida seguridad
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Usamos tu servicio
        user = AuthService.login_user(username, password)
        
        if user:
            session['user_id'] = user.id
            session['username'] = user.username
            # session['role'] = 'admin' # Descomenta si usas roles
            
            flash(f"Bienvenido, {user.username}", "success")
            return redirect(url_for('libros.listar'))
        else:
            flash("Usuario o contraseña incorrectos", "danger")

    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Has cerrado sesión correctamente.", "info")
    return redirect(url_for('auth.login'))

# --- RUTA TEMPORAL PARA CREAR ADMIN ---
# Entra aquí una vez: http://localhost:5000/crear-admin
@auth_bp.route('/crear-admin')
def crear_admin():
    if AuthService.crear_admin_por_defecto():
        return "Usuario 'admin' creado. Ve a /login"
    return "El usuario admin ya existe."