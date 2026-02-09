from app import db
from app.models.libro import Libro

class LibroService:
    
    @staticmethod
    def obtener_todos(solo_disponibles=False, busqueda=None):
        query = Libro.query
        
        # Filtro R2: Solo disponibles
        if solo_disponibles:
            query = query.filter(Libro.socio_id == None)
            
        # Filtro R3 y R4: Búsqueda (ilike hace magia: ignora mayúsculas y parciales)
        if busqueda:
            query = query.filter(Libro.titulo.ilike(f'%{busqueda}%'))
            
        return query.all()

    @staticmethod
    def obtener_por_id(id):
        return Libro.query.get_or_404(id)

    @staticmethod
    def crear_libro(titulo, autor, genero, anio, resumen):
        nuevo_libro = Libro(
            titulo=titulo,
            autor=autor,
            genero=genero,
            anio_publicacion=anio,
            resumen=resumen
        )
        db.session.add(nuevo_libro)
        db.session.commit()
        return nuevo_libro

    @staticmethod
    def actualizar_libro(id, titulo, autor, genero):
        libro = LibroService.obtener_por_id(id)
        if libro:
            libro.titulo = titulo
            libro.autor = autor
            libro.genero = genero
            db.session.commit()
            return True
        return False

    @staticmethod
    def prestar_libro(id, socio_id):
        libro = LibroService.obtener_por_id(id)
        
        # R6: Validación de seguridad en el backend
        if libro.socio_id is not None:
            return False  # El libro ya está prestado, no se puede prestar de nuevo
            
        libro.socio_id = socio_id
        db.session.commit()
        return True

    @staticmethod
    def eliminar_libro(id):
        libro = LibroService.obtener_por_id(id)
        
        # R7: No permitir borrar si está prestado
        if libro.socio_id is not None:
            return False  # Indicamos que falló porque está prestado
            
        db.session.delete(libro)
        db.session.commit()
        return True

    @staticmethod
    def devolver_libro(id):
        libro = LibroService.obtener_por_id(id)
        libro.socio_id = None  # Quitamos el socio (queda disponible)
        db.session.commit()
    