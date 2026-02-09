from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SocioForm(FlaskForm):
    nombre = StringField("Nombre", validators=[
        DataRequired(message="El nombre es obligatorio"), 
        Length(max=100)
    ])
    
    # --- AÑADIMOS ESTO ---
    apellido = StringField("Apellido", validators=[
        DataRequired(message="El apellido es obligatorio"), 
        Length(max=100)
    ])
    # ---------------------

    email = StringField("Email", validators=[
        DataRequired(),
        Email(message="El email no es válido"), 
        Length(max=100)
    ])
    
    submit = SubmitField("Guardar Socio")