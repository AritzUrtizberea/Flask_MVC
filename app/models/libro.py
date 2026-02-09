from app import db

class Libro(db.Model):
    __tablename__ = "libros"
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)  
    autor = db.Column(db.String(100), nullable=False)
    resumen = db.Column(db.Text, nullable=True)
    genero = db.Column(db.String(50))
    anio_publicacion = db.Column(db.Integer)

    # CAMBIO CLAVE: Ponemos el socio aquí directamente (Relación 1:N)
    # Si socio_id es None, el libro está libre. Si tiene un número, está prestado.
    socio_id = db.Column(db.Integer, db.ForeignKey('socios.id'), nullable=True)
    socio = db.relationship('Socio', back_populates='libros')
    
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "genero": self.genero,
            "anio_publicacion": self.anio_publicacion,
            # Simple: ¿Tiene socio? Entonces NO está disponible.
            "disponible": self.socio_id is None
        }