from app import db
from app.models.user import User

class AuthService:
    @staticmethod
    def register_user(username, password):
        # Validar si ya existe
        if User.query.filter_by(username=username).first():
            return None # El usuario ya existe
        
        new_user = User(username=username)
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def login_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return user
        return None
    
    @staticmethod
    def crear_admin_por_defecto():
        if not User.query.filter_by(username='admin').first():
            # Reutilizamos tu método register_user
            AuthService.register_user('admin', '1234')
            return True
        return False