from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class LibroBuscarForm(FlaskForm):
    busqueda = StringField('Búsqueda', render_kw={"placeholder": "Buscar título..."})
    submit = SubmitField('Buscar')