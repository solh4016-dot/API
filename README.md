# API propia: FastAPI + MySQL (reemplazo de fakestoreapi.com)

Replica los endpoints de fakestoreapi que usa tu app de Flutter, con las
mismas historias de usuario (US01 a US08), pero con **tu propia base de
datos MySQL**. A diferencia de fakestoreapi, aquí crear, editar y
eliminar **sí se guardan de verdad**.

## Endpoints

| Historia | Método y ruta | Qué hace | Respuestas |
|---|---|---|---|
| US01 | `GET /users` | Lista de usuarios (forma JSON idéntica a fakestoreapi) | 200 |
| US01 | `POST /auth/login` | Valida usuario y contraseña, devuelve un JWT con el id en `sub` | 200 / 401 |
| US03 | `GET /products` | Catálogo completo | 200 |
| US04 | `GET /products/categories` | Categorías disponibles | 200 |
| US04 | `GET /products/category/{categoria}` | Productos de una categoría | 200 |
| US05 | `GET /products/{id}` | Detalle de un producto | 200 / 404 |
| US06 | `POST /products` | Crea un producto (valida precio > 0 y URL de imagen) | 201 / 422 |
| US07 | `PUT /products/{id}` | Edita un producto | 200 / 404 / 422 |
| US08 | `DELETE /products/{id}` | Elimina un producto (devuelve el objeto borrado) | 200 / 404 |

Los permisos por rol (solo Administrador puede crear/editar/eliminar) los
controla la app de Flutter leyendo la sesión local, tal como piden US05 a
US08. La API no maneja roles.

---

## PASO 1. Instalar lo necesario (una sola vez)

1. **Python 3.10 o superior**: https://www.python.org/downloads/
   (en el instalador marca la casilla **"Add Python to PATH"**).
   Comprueba en una terminal: `python --version`

2. **MySQL** (elige UNA opción):
   - **XAMPP** (la más fácil): https://www.apachefriends.org → instala,
     abre el panel y dale **Start** a **MySQL**. Usuario `root`, contraseña
     vacía.
   - **MySQL Community Server + Workbench**: https://dev.mysql.com/downloads/
     (anota la contraseña de `root` que elijas al instalar).

## PASO 2. Crear la base de datos

**Opción A (recomendada): con el script SQL**

1. Abre MySQL Workbench (o phpMyAdmin si usas XAMPP: http://localhost/phpmyadmin).
2. Abre el archivo `database/schema.sql` y ejecútalo completo.
   Crea la base `fakestore_clone`, las tablas, 10 usuarios y 17 productos.

**Opción B: con Python** (si prefieres no usar el script SQL)

1. Crea solo la base vacía: `CREATE DATABASE fakestore_clone CHARACTER SET utf8mb4;`
2. Más adelante, en el Paso 4, ejecutarás `python -m app.seed_data`.

## PASO 3. Configurar la conexión

1. En esta carpeta, copia `.env.example` y renombra la copia a **`.env`**
2. Ábrelo y pon tu contraseña de MySQL:

```
DB_USER=root
DB_PASSWORD=tu_password_de_mysql     <- vacío si usas XAMPP
DB_HOST=localhost
DB_PORT=3306
DB_NAME=fakestore_clone
JWT_SECRET=pon-aqui-cualquier-texto-largo
```

## PASO 4. Instalar dependencias y cargar datos

Abre una terminal **dentro de la carpeta `backend_api`** (en VS Code:
Archivo → Abrir carpeta → `backend_api`, luego `Ctrl+ñ`):

```
pip install -r requirements.txt
python -m app.seed_data
```

(El segundo comando solo hace falta si usaste la Opción B del Paso 2.
**Ojo:** borra y recrea las tablas, úsalo solo para "resetear" los datos.)

Verás: `✔ 10 usuarios y 17 productos cargados.`

## PASO 5. Encender la API

```
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Déjala corriendo (esa terminal queda ocupada). Para detenerla: `Ctrl+C`.

Pruébala en el navegador:
- http://localhost:8000/ → debe decir "API funcionando correctamente"
- http://localhost:8000/products → lista de productos en JSON
- http://localhost:8000/docs → **documentación interactiva**: desde ahí
  puedes probar todos los endpoints con un clic ("Try it out"). Útil para
  mostrarle a tu profesor que la API funciona.

---

## PASO 6. Conectar la app de Flutter

1. Copia al proyecto Flutter los archivos nuevos/modificados:
   - `lib/config/api_config.dart` (**nuevo**: crea la carpeta `config`)
   - `lib/services/auth_service.dart`
   - `lib/services/product_service.dart`
   - `lib/screens/catalog_screen.dart`
   - `lib/screens/add_product_screen.dart`
   - `lib/screens/login_screen.dart`

2. Abre `lib/config/api_config.dart` y pon la URL según dónde corras la app:

| Dónde corres la app | `apiBaseUrl` |
|---|---|
| Chrome (web) o Windows | `http://localhost:8000` |
| Emulador de Android | `http://10.0.2.2:8000` |
| Teléfono real (mismo WiFi que la PC) | `http://TU_IP:8000` (ej. `http://192.168.1.65:8000`) |

   Tu IP la ves ejecutando `ipconfig` en una terminal → "Dirección IPv4".

3. **Solo para Android (emulador o teléfono)**: Android bloquea por defecto
   las direcciones `http://` (sin https). Abre
   `android/app/src/main/AndroidManifest.xml` y agrega
   `android:usesCleartextTraffic="true"` dentro de `<application`:

```xml
<application
    android:label="mi_app"
    android:usesCleartextTraffic="true"
    android:name="${applicationName}"
    android:icon="@mipmap/ic_launcher">
```

   (el permiso de INTERNET que agregaste antes debe seguir ahí).

4. Ejecuta `flutter pub get` y corre la app. Para volver a fakestoreapi
   basta cambiar `apiBaseUrl` a `https://fakestoreapi.com`.

### Si usas el teléfono real
- La API debe estar encendida con `--host 0.0.0.0` (ya lo trae el comando).
- Prueba primero desde el navegador del teléfono: `http://TU_IP:8000/docs`.
  Si no abre, el firewall (Windows o **Avast**) está bloqueando el puerto
  8000: permite Python/uvicorn o crea una regla de entrada para el puerto 8000.

---

## Usuarios de prueba (mismos de siempre)

| Usuario | Contraseña | Rol (según el id que asigna la app) |
|---|---|---|
| johnd | m38rmF$ | Administrador |
| mor_2314 | 83r5^_ | Auditor |
| kevinryan | kev02937@ | Cliente |

## Problemas frecuentes

| Síntoma | Causa probable | Solución |
|---|---|---|
| `Can't connect to MySQL server` | MySQL apagado | Inicia MySQL (XAMPP → Start) |
| `Access denied for user 'root'` | Contraseña incorrecta en `.env` | Corrige `DB_PASSWORD` |
| `Unknown database 'fakestore_clone'` | No creaste la base | Haz el Paso 2 |
| `No module named 'app'` | Terminal en la carpeta equivocada | Entra a `backend_api` antes de ejecutar |
| La app dice "Sin conexión" | API apagada o URL incorrecta en `api_config.dart` | Verifica el Paso 5 y la tabla del Paso 6 |
| En el emulador no conecta | Falta `usesCleartextTraffic` o usaste `localhost` | Usa `10.0.2.2` y agrega el atributo |

## Estructura

```
backend_api/
  app/
    main.py         <- app FastAPI + CORS
    database.py     <- conexión a MySQL
    models.py       <- tablas (users, products)
    schemas.py      <- validaciones de entrada/salida
    security.py     <- generación y verificación del JWT
    seed_data.py    <- datos iniciales
    routers/
      users.py      <- /users y /auth/login
      products.py   <- /products (CRUD, categorías)
  database/
    schema.sql      <- script SQL equivalente al seed
  requirements.txt
  .env.example
```
# API git init git add . git commit -m first commit git branch -M main git remote add origin https://github.com/solh4016-dot/API.git git push -u origin main
