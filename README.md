# 📚 Sistema de Gestión de Biblioteca (Flask MVC)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Framework-Flask-green?style=for-the-badge&logo=flask&logoColor=white)
![Status](https://img.shields.io/badge/Estado-Terminado-success?style=for-the-badge)

Aplicación web para la gestión integral de préstamos de libros y socios. El proyecto implementa una **Arquitectura por Capas (MVC + Servicios)** para asegurar un código limpio, escalable y mantenible, cumpliendo estrictamente con los requisitos de la práctica.

---

## 🚀 Características Principales

### 📖 Gestión de Libros
- **CRUD Completo (R9, R8, R7):** Altas, bajas (solo si no está prestado) y modificaciones.
- **Estado (R1, R2):** Visualización clara de si un libro está `Disponible` o `Prestado`.
- **Buscador (R3, R4):** Búsqueda por título (ignora mayúsculas/minúsculas y busca por fragmentos).
- **Préstamos y Devoluciones (R5, R6, R11):** Gestión de flujo de préstamos con validaciones.

### 👥 Gestión de Socios
- **Integridad de Datos (R15):** Sistema de protección que **impide borrar un socio** si tiene préstamos pendientes.
- **Historial (R18):** Vista detallada de los libros en posesión de cada socio.
- **Búsqueda (R16):** Filtrado de socios por nombre y email.

### 🔧 Aspectos Técnicos
- **Patrón MVC:** Separación estricta entre Modelos, Vistas y Controladores.
- **Decoradores (R29):** Implementación de decoradores propios para control de acceso.
- **ORM SQLAlchemy (R30, R31):** Modelado de datos con relaciones explícitas `Libro` <-> `Socio`.
- **Validaciones (R36):** Uso de `WTForms` para asegurar la calidad de los datos de entrada.

---

## 🛠️ Instalación y Configuración (R26)

Sigue estos pasos para desplegar el proyecto en tu entorno local:

### 1. Crear el Entorno Virtual
Genera un entorno aislado para las dependencias del proyecto. Ejecuta en la terminal:

```bash
python -m venv venv
```

### 2. Activar el Entorno
* **En Windows:**
  ```bash
  .\venv\Scripts\activate
  ```
* **En macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar Dependencias
Instala las librerías necesarias (`Flask`, `SQLAlchemy`, `WTForms`, etc.):

```bash
pip install -r requirements.txt
```

> **💡 Nota:** Si se añaden nuevas librerías, actualizar con:
> ```bash
> pip freeze > requirements.txt
> ```

---

## ▶️ Ejecución de la Aplicación

Con el entorno activado, lanza el servidor de desarrollo:

```bash
flask run
```

Accede a la aplicación en tu navegador:
👉 **http://127.0.0.1:5000**

---

## 📂 Estructura del Código (R27)

El proyecto sigue una arquitectura modular para facilitar el mantenimiento:

```text
flask_mvcDev
 ┣ 📂 app
 ┃ ┣ 📂 controllers  # (Blueprints) Rutas y gestión de peticiones HTTP
 ┃ ┣ 📂 forms        # Clases de formularios (WTForms) y validaciones
 ┃ ┣ 📂 models       # Modelos de BBDD (SQLAlchemy) - Entidades Libro y Socio
 ┃ ┣ 📂 services     # Lógica de Negocio (separada de las vistas)
 ┃ ┣ 📂 static       # Archivos estáticos (CSS, JS, Imágenes)
 ┃ ┣ 📂 templates    # Vistas HTML (Motor Jinja2)
 ┃ ┣ 📂 utils        # Utilidades y herramientas auxiliares
 ┃ ┗ 📜 __init__.py  # Inicialización de la app y configuración
 ┣ 📂 instance       # Base de datos SQLite local
 ┣ 📂 venv           # Entorno virtual
 ┣ 📜 README.md      # Documentación del proyecto
 ┣ 📜 requirements.txt # Lista de dependencias
 ┗ 📜 run.py         # Punto de entrada de la aplicación
```

---

## 📡 Documentación de la API (R21-R24)

Endpoints JSON disponibles para integración externa:

| Método | Endpoint | Descripción | Acceso |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/libros` | Listado de todos los libros y su estado. | 🟢 Público |
| `GET` | `/api/librosdisponibles/` | Listado único de libros disponibles. | 🟢 Público |
| `GET` | `/api/libros/buscar/<titulo>` | Busca libros que coincidan con el título. | 🟢 Público |
| `GET` | `/api/libros/socios/prestamos` | Lista de socios que tienen libros sin devolver. | 🔴 Admin |

---

## 🔮 Posibles Mejoras Futuras (R28)

Aunque el sistema es funcional, se plantean las siguientes evoluciones:

1.  **Paginación:** Implementar paginación en los listados de libros y socios para manejar grandes volúmenes de datos.
2.  **Autenticación JWT:** Migrar la seguridad de la API a Tokens JWT para clientes externos.
3.  **Historial Completo:** Crear una tabla histórica para guardar registros de préstamos ya devueltos (auditoría).
4.  **Dockerización:** Crear un `Dockerfile` para facilitar el despliegue en cualquier servidor.

---

## 👤 Aritz Urtizberea

**Desarrollo Web en Entorno Servidor**
*Proyecto de Práctica - Curso 2025/2026*