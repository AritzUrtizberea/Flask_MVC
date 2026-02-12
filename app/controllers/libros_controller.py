from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms.libro_form import LibroForm
from app.forms.prestamo_form import PrestamoForm
from app.services.libros_service import LibroService
from app.services.socio_service import SocioService
from app.forms.libro_form_buscar import LibroBuscarForm
from app.utils.decorators import login_required  # <--- IMPORTANTE

libros_bp = Blueprint('libros', __name__)

# --- R1: LISTAR (Público - Sin login_required) ---
@libros_bp.route('/libros')
def listar():
    # 1. Instanciamos el formulario pasándole los datos de la URL (request.args)
    # IMPORTANTE: meta={'csrf': False} es necesario porque es un formulario GET
    form_busqueda = LibroBuscarForm(request.args, meta={'csrf': False})
    
    # Recogemos el filtro de disponibles (ese lo mantenemos igual si no está en el form)
    solo_disponibles = request.args.get('disponibles')
    
    # Variable para el texto a buscar
    busqueda = None
    
    # 2. Si el formulario es válido y tiene datos, sacamos la búsqueda de ahí
    if form_busqueda.validate():
        busqueda = form_busqueda.busqueda.data
    
    # 3. Llamamos al servicio pasando los parámetros
    libros = LibroService.obtener_todos(solo_disponibles=solo_disponibles, busqueda=busqueda)
    
    # 4. Pasamos 'form_busqueda' a la plantilla para poder pintarlo
    return render_template('paginas/libros/libros.html', 
                           libros=libros, 
                           form_busqueda=form_busqueda)

# --- GRID (Público - Sin login_required) ---
@libros_bp.route('/libros/grid')
def grid():
    libros = LibroService.obtener_todos()
    return render_template('paginas/libros/librosGrid.html', libros=libros)

# --- R9: CREAR LIBRO (Protegido) ---
@libros_bp.route('/libros/crear', methods=['GET', 'POST'])
@login_required  # <--- CANDADO PUESTO
def crear():
    form = LibroForm()
    if form.validate_on_submit():
        LibroService.crear_libro(
            titulo=form.titulo.data,
            autor=form.autor.data,
            genero=form.genero.data,
            anio=form.anio_publicacion.data,
            resumen=form.resumen.data
        )
        flash('Libro creado correctamente', 'success')
        return redirect(url_for('libros.listar'))
    return render_template('paginas/libros/libro_crear.html', form=form)

# --- R8: EDITAR LIBRO (Protegido) ---
@libros_bp.route('/libros/editar/<int:id>', methods=['GET', 'POST'])
@login_required  # <--- CANDADO PUESTO
def editar(id):
    libro = LibroService.obtener_por_id(id)
    form = LibroForm(obj=libro)
    
    if form.validate_on_submit():
        LibroService.actualizar_libro(
            id,
            form.titulo.data,
            form.autor.data,
            form.genero.data,
            form.anio_publicacion.data
        )
        flash('Libro actualizado correctamente', 'success')
        return redirect(url_for('libros.listar'))
        
    return render_template('paginas/libros/libro_editar.html', form=form, libro=libro)

# --- BORRAR (Protegido) ---
@libros_bp.route('/libros/borrar/<int:id>')
@login_required  # <--- CANDADO PUESTO
def borrar(id):
    if LibroService.eliminar_libro(id):
        flash('Libro eliminado.', 'success')
    else:
        flash('Error: No se puede borrar un libro prestado.', 'danger')
    return redirect(url_for('libros.listar'))

# --- ELIMINAR (Duplicado de borrar, protegido también por si acaso) ---
@libros_bp.route('/libros/eliminar/<int:id>')
@login_required  # <--- CANDADO PUESTO
def eliminar(id):
    if LibroService.eliminar_libro(id):
        flash('Libro eliminado correctamente', 'success')
    else:
        flash('Error: No se puede eliminar un libro que está prestado.', 'danger')
    return redirect(url_for('libros.listar'))

# --- R11: DEVOLVER (Protegido) ---
@libros_bp.route('/libros/devolver/<int:id>')
@login_required  # <--- CANDADO PUESTO
def devolver(id):
    LibroService.devolver_libro(id)
    flash('Libro devuelto', 'success')
    return redirect(url_for('libros.listar'))

# --- R10: PRESTAR (Protegido) ---
@libros_bp.route('/libros/prestar/<int:id>', methods=['GET', 'POST'])
@login_required  # <--- CANDADO PUESTO
def prestar(id):
    libro = LibroService.obtener_por_id(id)
    
    if libro.socio_id:
        flash('Error: Este libro ya está prestado.', 'danger')
        return redirect(url_for('libros.listar'))

    form = PrestamoForm()
    # Rellena el select con los socios
    form.socio_id.choices = [(s.id, f"{s.nombre} {s.apellido}") for s in SocioService.obtener_todos()]

    if form.validate_on_submit():
        if LibroService.prestar_libro(id, form.socio_id.data):
            flash('Libro prestado correctamente', 'success')
        else:
            flash('Error: El libro ya estaba prestado.', 'danger')
        return redirect(url_for('libros.listar'))

    return render_template('paginas/libros/libro_prestar.html', form=form, libro=libro)