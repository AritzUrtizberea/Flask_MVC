from sqlalchemy import or_
from app import db
from app.models.socio import Socio


class SocioService:
    @staticmethod
    def obtener_todos(busqueda=None, solo_con_prestamos=False):
        query = Socio.query

        # R18: Filtro para ver solo los que tienen libros
        if solo_con_prestamos:
            query = query.join(Socio.libros)

        # R16: Buscador (Nombre O Apellido O Email)
        if busqueda:
            filtro = f'%{busqueda}%'
            # ⚠️ OJO: Asegúrate de que en tu modelo Socio existe el campo 'apellido'.
            # Si solo tienes 'nombre', borra la línea de Socio.apellido.
            query = query.filter(or_(
                Socio.nombre.ilike(filtro),
                Socio.apellido.ilike(filtro), 
                Socio.email.ilike(filtro)
            ))
        
        # Añadimos distinct() por si acaso el join duplica filas
        return query.distinct().all()
    @staticmethod
    def obtener_por_id(id):
        return Socio.query.get(id)

    @staticmethod
    def crear_socio(nombre, apellido, email):
        # Primero verificamos si ya existe el email (Validación de negocio)
        existente = Socio.query.filter_by(email=email).first()
        if existente:
            return None # O lanzar error
            
        nuevo_socio = Socio(nombre=nombre, apellido=apellido, email=email)
        db.session.add(nuevo_socio)
        db.session.commit()
        return nuevo_socio
        
    @staticmethod
    def actualizar_socio(id, nombre, apellido, email):
        socio = SocioService.obtener_por_id(id)
        if socio:
            socio.nombre = nombre
            socio.apellido = apellido
            socio.email = email
            db.session.commit()
            return True
        return False

    @staticmethod
    def borrar_socio(id):
        socio = SocioService.obtener_por_id(id)
        
        if not socio:
            return False

        # R15: NO borrar si tiene libros prestados.
        # Al acceder a 'socio.libros', SQLAlchemy hace la consulta por ti.
        # No necesitas importar la clase Libro para esto.
        if socio.libros: 
            return False # Tiene libros, cancelamos borrado
            
        db.session.delete(socio)
        db.session.commit()
        return True