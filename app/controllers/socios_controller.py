from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.socio_service import SocioService
from app.forms.socio_form import SocioForm
from app.utils.decorators import login_required # <--- 1. IMPORTAMOS EL DECORADOR

socios_bp = Blueprint('socios', __name__, url_prefix='/socios')

# --- LISTAR (Público) ---
@socios_bp.route('/') 
def listar():
    busqueda = request.args.get('busqueda')
    solo_con_prestamos = request.args.get('prestamos')
    
    socios = SocioService.obtener_todos(busqueda=busqueda, solo_con_prestamos=solo_con_prestamos)
    
    return render_template('paginas/socios/socios.html', socios=socios)

# --- CREAR (Protegido) ---
@socios_bp.route('/crear', methods=['GET', 'POST'])
@login_required # <--- 2. CANDADO PUESTO
def crear():
    form = SocioForm()
    
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        email = form.email.data
        
        if SocioService.crear_socio(nombre, apellido, email):
            flash('Socio creado exitosamente.', 'success')
            return redirect(url_for('socios.listar'))
        else:
            flash('Error: El email ya está registrado.', 'danger')
            
    return render_template('paginas/socios/socio_crear.html', form=form)

# --- BORRAR (Protegido) ---
@socios_bp.route('/borrar/<int:id>')
@login_required # <--- 3. CANDADO PUESTO
def borrar(id):
    if SocioService.borrar_socio(id):
        flash('Socio eliminado.', 'success')
    else:
        flash('No se puede borrar: El socio tiene libros prestados.', 'danger')
    return redirect(url_for('socios.listar'))

# --- EDITAR (Protegido) ---
@socios_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required # <--- 4. CANDADO PUESTO
def editar(id):
    socio = SocioService.obtener_por_id(id)
    form = SocioForm(obj=socio)
    
    if form.validate_on_submit():
        SocioService.actualizar_socio(
            id,
            form.nombre.data,
            form.apellido.data,
            form.email.data
        )
        flash('Socio actualizado correctamente.', 'success')
        return redirect(url_for('socios.listar'))
        
    return render_template('paginas/socios/socio_editar.html', form=form, socio=socio)