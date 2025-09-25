Veterinaria

Aplicación web sencilla construida con Django para administrar categorías de veterinarios (creadas desde el administrador) y gestionar los veterinarios asociados mediante formularios CRUD.

## Requisitos previos

- Python 3.11+
- Entorno virtual recomendado (`python -m venv .venv`)
- Paquetes: `Django>=5.2`, `mysqlclient`, `Pillow`
- Servidor MySQL en ejecución

## Configuración

1. Instala las dependencias:

```powershell
pip install -r requirements.txt
```

2. Actualiza los datos de conexión MySQL en `veterinaria/settings.py` (`NAME`, `USER`, `PASSWORD`, `HOST`, `PORT`).

3. Ejecuta migraciones:

```powershell
python manage.py makemigrations
python manage.py migrate
```

4. Crea un usuario administrador para gestionar las categorías:

```powershell
python manage.py createsuperuser
```

5. Ejecuta el servidor de desarrollo:

```powershell
python manage.py runserver
```

Visita `http://127.0.0.1:8000/` para usar la aplicación y `http://127.0.0.1:8000/admin/` para gestionar las categorías.

## Estructura principal

- `home_veterinarios/models.py`: modelos `Categoria` y `Veterinario`.
- `home_veterinarios/forms.py`: formulario reutilizable `VeterinarioForm`.
- `home_veterinarios/services.py`: funciones auxiliares para obtener datos desde las vistas.
- `home_veterinarios/views.py`: vistas con operaciones CRUD para veterinarios.
- `templates/`: `base.html` y páginas específicas para home, listado, detalle y formularios.
- `static/home_veterinarios/styles.css`: estilos base con la paleta solicitada.

## Notas

- Las categorías solo se administran vía Django Admin.
- Las fotos y las imágenes se suben desde tu computador y se guardan en la carpeta `media/`.
- El archivo `services.py` centraliza consultas simples para reutilizar código entre vistas.
