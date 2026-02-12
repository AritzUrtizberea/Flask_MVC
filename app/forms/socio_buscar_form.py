from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SocioBuscarForm(FlaskForm):
    busqueda = StringField('Búsqueda', render_kw={"placeholder": "Nombre o Email..."})
    submit = SubmitField('Buscar')