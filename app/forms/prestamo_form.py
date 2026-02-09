from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class PrestamoForm(FlaskForm):
    # 'coerce=int' es importante porque los IDs de la base de datos son números,
    # pero HTML suele enviar textos. Esto lo convierte automáticamente.
    socio_id = SelectField('Seleccionar Socio', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Confirmar Préstamo')