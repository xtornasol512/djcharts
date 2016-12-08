##Creando nuevos modelos

### Pasos a seguir
1. creas en model en graficas.models
graficas/models.py

2. lo registras en la BD
python manage.py makemigrations
python manage.py migrate


3. Creas el view en 
graficas/views.py

4. Lo registras en las urls 
chartsdj/urls.py

5. creas su template, 
templates/graficas/grafica_NOMBRE.html
6. corres el servidor
python manage.py runserver 8080


##agregandolos al admin

###Pasos a seguir

1. editar admin.py
graficas/admin.py


2. agregar modelo y reegistrarlo
