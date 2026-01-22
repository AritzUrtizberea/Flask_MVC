from app import db
class Libro(db.Model):
    __tablename__ = "libros"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)  
    autor = db.Column(db.String(100), nullable=False)
    resumen = db.Column(db.Text, nullable=True)



    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
             "autor": self.autor,
            "resumen": self.resumen
        }
