from app import db

class Socio(db.Model):
    __tablename__ = "socios"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    # ESTO FALTABA: Permite usar socio.libros para ver su lista
    libros = db.relationship('Libro', back_populates='socio', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email
        }