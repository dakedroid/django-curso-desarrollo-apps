# Instalar el cliente de MySQL
pip uninstall mysqlclient -y; pip install --only-binary :all: mysqlclient


# Realizar migraciones
python manage.py migrate

# Crear Super usuario y establecer una contraseña
python manage.py createsuperuser


# Habilitar Hosts
ALLOWED_HOSTS = ['*']


#Agregar Middleware whitenose  
'whitenoise.middleware.WhiteNoiseMiddleware',  # Add Whitenoise for static files


# Configurar rutas estaticas 
'DIRS': [BASE_DIR / 'templates'],

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Recopilar estaticos
python manage.py collectstatic --noinput


# Ejecutar servidor web
cd mi_proyecto
waitress-serve --port=8000 mi_proyecto.wsgi:application


# Comando para verificar direccion ip local
ipconfig
