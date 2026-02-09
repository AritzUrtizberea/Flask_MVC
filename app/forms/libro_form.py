from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
# IMPORTANTE: Asegúrate de tener DataRequired aquí
from wtforms.validators import DataRequired, Length 

class LibroForm(FlaskForm):
    # Añade validators=[DataRequired()] a los campos obligatorios
    titulo = StringField('Título', validators=[DataRequired(), Length(max=100)])
    autor = StringField('Autor', validators=[DataRequired(), Length(max=100)])
    genero = StringField('Género', validators=[DataRequired()])
    anio_publicacion = IntegerField('Año', validators=[DataRequired()])
    resumen = TextAreaField('Resumen') # Este puede ser opcional
    submit = SubmitField('Guardar')