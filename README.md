# Laboratorio 8 Django - Usando una plantilla para ver Destinos Turísticos - Desarrollo de Aplicaciones Web 


🌄 Proyecto Destinos Turísticos de Arequipa


## ▶️ Video de Funcionamiento : https://youtu.be/JXdXaolxr38

Curso: Desarrollo de Aplicaciones Web.
Profesor: Carlo Jose Luis Corrales Delgado
Aplicación web desarrollada con Django para la gestión de destinos turísticos de la región de Arequipa. El sistema permite visualizar información turística y realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre los destinos registrados.

📌 Descripción

Este proyecto fue desarrollado como práctica de desarrollo de aplicaciones web utilizando el framework Django. La aplicación muestra destinos turísticos de Arequipa de forma dinámica obteniendo la información desde una base de datos SQLite.

Cada destino incluye:

Nombre de la ciudad o atractivo turístico.
Descripción.
Imagen.
Precio del tour.
Estado de oferta.

Además, el sistema implementa funcionalidades CRUD para administrar los registros de destinos turísticos.

🚀 Funcionalidades
📖 Lectura de datos (READ)
Visualización dinámica de destinos turísticos.
Consulta de información almacenada en la base de datos.
Presentación de imágenes y precios de los tours.
➕ Creación de datos (CREATE)
Registro de nuevos destinos turísticos mediante formularios Django.
✏️ Actualización de datos (UPDATE)
Modificación de información existente de un destino turístico.
🗑️ Eliminación de datos (DELETE)
Eliminación de registros de destinos turísticos.
🛠️ Tecnologías Utilizadas
Python 3
Django 6
SQLite3
HTML5
CSS3
Bootstrap
JavaScript
Template Travello (Colorlib)


📂 Estructura General del Proyecto
proyecto_destinosaqp/
│
├── destinos_arequipa/
│   ├── migrations/
│   ├── templates/
│   │   ├── index.html
│   │   ├── form_destino.html
│   │   └── confirmar_eliminacion.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── media/
├── static/
├── proyecto_destinosaqp/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
└── manage.py
🗄️ Modelo de Datos

La entidad principal del sistema es:

DestinoTuristico
Campo	Tipo
nombreCiudad	CharField
descripcionCiudad	TextField
imagenCiudad	ImageField
precioTour	DecimalField
ofertaTour	BooleanField
⚙️ Instalación y Ejecución
1. Clonar el repositorio
git clone https://github.com/tu-usuario/tu-repositorio.git
2. Ingresar al proyecto
cd proyecto_destinosaqp
3. Crear entorno virtual
python -m venv venv
4. Activar entorno virtual

Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate
5. Instalar dependencias
pip install django pillow
6. Ejecutar migraciones
python manage.py migrate
7. Iniciar servidor
python manage.py runserver
8. Abrir en el navegador
http://127.0.0.1:8000/
📸 Evidencias

👨‍💻 Autor: Diego Cervantes

Proyecto desarrollado con Django como práctica académica de Desarrollo de Aplicaciones Web y Bases de Datos.
