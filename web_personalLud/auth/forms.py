from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, 
                    SubmitField, EmailField, 
                    IntegerField, RadioField, 
                    SelectField, TextAreaField)
from wtforms.validators import DataRequired, Email

################### Formularios de WTForms ##############
class LoginForm(FlaskForm):
    email = EmailField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

class RegisterForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Email()])
    last_name =StringField('Apellidos', validators=[DataRequired(), Email()])
    email = EmailField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Email()])
    phone = IntegerField('Telefono')
    is_married = RadioField('Estado Civil', choices=[{'True', 'Casado'}, {'False', 'Soltero'}])
    gender = SelectField('Genero', choices=[{'male', 'Masculino'}, {'female', 'Femenino'}, {'other', 'Otro'}])
    submit = SubmitField('Registrar')  
