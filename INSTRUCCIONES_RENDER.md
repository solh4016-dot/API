# Instrucciones: API MVC en Render (sin Railway)

## Estructura de tu proyecto
- `app/models/models.py`: **Modelo**, tablas SQLAlchemy.
- `app/views/schemas.py`: **Vista**, validación de entrada y formato de salida JSON mediante Pydantic.
- `app/controllers/products.py`, `users.py`, `carts.py`: **Controladores**, lógica y rutas.
- `app/main.py`: entrada FastAPI y registro de controladores.
- `app/database.py`: conexión a MySQL a través de variables de entorno.

## Local (Visual Studio Code)
1. Abre esta carpeta; crea entorno virtual `python -m venv .venv` y actívalo.
2. `pip install -r requirements.txt`
3. Copia `.env.example` a `.env`; escribe tus credenciales locales, nunca subas `.env`.
4. `uvicorn app.main:app --reload --port 8000`
5. Revisa `http://localhost:8000/health`, `http://localhost:8000/health/db` y `/docs`.
6. Si MySQL todavía no tiene las tablas/datos, importa `database/schema.sql` en MySQL Workbench (inspecciona primero los datos de ejemplo y haz copia de cualquier base existente). El SQL crea/selecciona `fakestore_clone` e incluye tablas de carritos. Ejecutarlo dos veces sobre tablas existentes dará error: es una instalación inicial, NO una migración.

## Render + MySQL
1. Sube el contenido de esta carpeta a tu repo de GitHub, SIN `.env` ni credenciales.
2. Render > New > Web Service > conecta el repositorio; selecciona Python 3.
3. Root Directory: vacío si la raíz del repo contiene `requirements.txt` y `app/`.
4. Build: `pip install -r requirements.txt`
5. Start: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. En Environment agrega `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `JWT_SECRET`. `DB_HOST` debe resolver desde Render y aceptar conexiones desde el servicio web. **Render aloja la API, pero no sustituye automáticamente tu servidor MySQL**. Puedes usar MySQL en un servidor accesible desde Render; si eliges hospedar MySQL dentro de Render, requiere configurar otro servicio y almacenamiento persistente. No uses `localhost` salvo si MySQL se ejecuta verdaderamente en el mismo contenedor (no es el caso típico).
7. Prueba primero `https://TU-SERVICIO.onrender.com/health` (solo aplicación web), luego `/health/db` (conexión MySQL), luego `/products` y `/docs`.
8. La API NO crea ni llena tablas al arrancar. Si no hay tablas, importa el esquema de forma controlada en el servidor MySQL al que Render se conecta.
9. Cuando todo responda, actualiza la URL base en Flutter a `https://TU-SERVICIO.onrender.com` y prueba el CRUD.

## Diagnóstico rápido
- Build falla: revisa Requirements / versión de Python y Logs.
- No open ports: verifica `--host 0.0.0.0 --port $PORT`.
- `/health` 200, `/health/db` 503: la API está iniciada; falla host, usuario, contraseña, red, firewall o permisos de MySQL.
- `/health/db` 200, `/products` 500: posible falta de tabla `products` o discrepancia con el esquema.
- MySQL no está en Render de forma automática. La conexión requiere una instancia real y accesible.

## Seguridad
- Si publicaste un archivo `.env` o claves en GitHub, cambia las claves expuestas y elimínalas del historial del repositorio (borrarlo del último commit NO basta para limpiar el historial).
- El código de autenticación heredado compara contraseñas en texto plano y deduce privilegios por ID. Es solo apto como práctica académica con datos ficticios; **no es seguro para producción real**.
- El endpoint de salud de base de datos no revela credenciales ni mensajes SQL internos.
