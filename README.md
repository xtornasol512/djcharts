Proyecto Django con Higcharts
==================================

Requerimientos

python 2.7.6+
virtualenv
pip



###Pasos

1. Crear virtualenv
virtualenv venv/djcharts

2. Encender entorno
C:\proyectos\djcharts\venv\djcharts\Scripts\activate.bat
o 
source djcharts/venv/djcharts/bin/activate


3. Instalar requerimientos
pip install -r requirements.txt

4. entrar  directorio donde esta manage.py
cd /chartsdj

5. correr migraciones
python manage.py migrate

6. Opcional cargar fixtures
python mnage.py loaddata fixtures/initil_data.json

7. Encender el sistema
python manage.py runserver


Extras
=============
1. Desctivar entorno
deactivate

2. Para correr el servidor 
cd chartsdj/
python manage.py runserver 8080


3.



