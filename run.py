from app import create_app
from app.services.auth_service import AuthService

app = create_app()

if __name__ == "__main__":
    # Creamos un contexto de aplicación para poder acceder a la Base de Datos
    with app.app_context():
        # Ejecutamos la lógica de creación del admin automáticamente
        created = AuthService.crear_admin_por_defecto()
        
        if created:
            print("✅ Usuario 'admin' creado correctamente con contraseña '1234'.")
        else:
            print("ℹ️ El usuario 'admin' ya existía.")

    # Arrancamos el servidor
    app.run(debug=True)