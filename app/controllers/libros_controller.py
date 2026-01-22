from flask import Blueprint,  request, render_template, redirect, url_for
from app.forms.libro_form import LibroForm
from app.models.libro import Libro
from app.services.libros_service import *

libros_bp = Blueprint(
    "libros",
    __name__,
    url_prefix="/libros"
)

@libros_bp.route("/")
def listar():
    libros = listar_libros()
    return render_template("paginas/libros/libros.html", libros=libros)

@libros_bp.route("/grid")
def grid():
    libros = listar_libros()
    return render_template("paginas/libros/librosGrid.html", libros=libros)

@libros_bp.route("/<int:id>", methods=["GET","POST"])
def detalle(id):
    libro = Libro.query.get_or_404(id)
    form = LibroForm(obj=libro)  # ← precarga datos
    if request.method == "POST":
        if form.validate_on_submit():
            libro.titulo = form.titulo.data
            libro.autor = form.autor.data
            libro.resumen = form.resumen.data

            editar_libro(
                libro_id=id,
                titulo=libro.titulo,
                autor=libro.autor,
                resumen=libro.resumen
            )

          
   #return render_template("libro.html", form=form, libro=libro)
    return render_template("paginas/libros/libro_editar.html", form=form, libro=libro)


@libros_bp.route("/crear", methods=["GET", "POST"])
def crear():
    form = LibroForm()
    if request.method == "POST":
        if form.validate_on_submit():
            titulo = form.titulo.data
            autor = form.autor.data
            resumen = form.resumen.data

            crear_libro(titulo, autor, resumen)

            return redirect(url_for("libros.listar"))

    return render_template("paginas/libros/libro_crear.html", form=form)


