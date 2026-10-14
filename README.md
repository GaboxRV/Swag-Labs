# Automatización de inicio de sesión - Swag Labs

Prueba tecnica de inicio de sesión en [SauceDemo](https://www.saucedemo.com/), desarrollado con Python, Selenium y pytest.

## Matriz de casos de prueba

La matriz se encuentra en el siguiente enlace: [Matriz Saucedemo](https://docs.google.com/spreadsheets/d/1FrbaMl5kK6Ckmze5bXnt9OwcN_dQFuuIBFxuDzpanoI/edit?usp=sharing)


## Herramientas necesarias

- **Python 3.12 o superior**.
- **Poetry**, para instalar las dependencias y ejecutar el proyecto en un entorno virtual.
- **Google Chrome**, instalado en el equipo.

Selenium Manager, incluido en Selenium, administra el controlador de Chrome. La primera ejecución puede necesitar conexión a Internet para descargarlo.

### Instalar Poetry en Windows

Si Poetry aún no está instalado, abre PowerShell y ejecuta:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

> Para más información puede revisar el portal: https://python-poetry.org/docs/#installing-with-the-official-installer

Reinicia la terminal y verifica que el comando esté disponible:

```powershell
poetry --version
```

> Si no esta disponible hay que validar que exista la ruta en el PATH

## Instalación

Abre PowerShell en la carpeta del repositorio:

```powershell
cd C:\dev\Swag-Labs
```

Instala las dependencias declaradas en `pyproject.toml` y fijadas en `poetry.lock`:

```powershell
poetry install
```

Poetry administra el entorno virtual del proyecto; no es necesario instalar pytest ni Selenium globalmente ni activar el entorno manualmente.

## Ejecución de las pruebas

Para ejecutar la suite con la salida habitual de pytest:

```powershell
poetry run pytest
```

Para una salida más compacta que resuma los casos y muestre trazas breves cuando algo falla:

```powershell
poetry run pytest -q --tb=short
```

