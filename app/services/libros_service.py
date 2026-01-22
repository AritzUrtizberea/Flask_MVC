from sqlalchemy import func
from app import db
from app.models.libro import Libro



def listar_libros():
    return Libro.query.all()
    #return Libro.query.order_by(func.lower(Libro.titulo)).all()

def obtener_libro(id):
    return Libro.query.get(id)


def crear_libro(titulo, autor, resumen=None ):
    libro = Libro(titulo=titulo, autor=autor, resumen=resumen)
    db.session.add(libro)
    db.session.commit()
    return libro

def editar_libro(libro_id, titulo=None, autor=None, resumen=None):
    libro = Libro.query.get(libro_id)
    if not libro:
        return None

    if titulo is not None:
        libro.titulo = titulo
    if autor is not None:
        libro.autor = autor
    if resumen is not None:
        libro.resumen = resumen
    db.session.commit()
    return libro





