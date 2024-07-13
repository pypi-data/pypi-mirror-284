# Siura

**Siura** es una biblioteca de Python diseñada para facilitar la interacción con servicios y APIs de forma eficiente y estructurada. Su enfoque se centra en proporcionar una interfaz intuitiva y fácil de usar, permitiendo a los desarrolladores integrar funcionalidades complejas sin complicaciones.

## Características Principales

- **Interfaz Simple**: Ofrece una API clara y accesible, lo que facilita su uso incluso para aquellos que están comenzando con Python.
- **Manejo de Errores**: Incluye mecanismos para el manejo de errores y excepciones, garantizando que los desarrolladores puedan manejar situaciones inesperadas de manera eficaz.
- **Documentación Completa**: Cuenta con documentación detallada que incluye ejemplos prácticos, permitiendo a los usuarios comprender rápidamente cómo utilizar sus funcionalidades.
- **Modularidad**: Su estructura modular permite a los desarrolladores usar solo las partes que necesitan, manteniendo el código limpio y eficiente.
- **Compatibilidad**: Compatible con las versiones más recientes de Python, asegurando un funcionamiento óptimo en diversos entornos.

## Casos de Uso

- Integración con APIs RESTful.
- Automatización de tareas relacionadas con servicios web.
- Desarrollo de aplicaciones que requieren interacción con múltiples fuentes de datos.

## Instalación

Para instalar Siura, puedes usar `pip`:

```bash
pip install siura
```

```python

from dotenv import load_dotenv
import siura

load_dotenv()

# Ejemplo de uso de Siura
print("Siura importado correctamente.")

```


# Problemas en instalar

## Linux
Crea un archivo llamado setup_project.sh

```bash

#!/bin/bash

# Nombre del entorno virtual
ENV_NAME="venv"

# Directorio del proyecto
PROJECT_DIR=$(pwd)

# Verificar si el entorno virtual ya existe
if [ -d "$ENV_NAME" ]; then
    echo "El entorno virtual '$ENV_NAME' ya existe. Activándolo..."
else
    # Crear entorno virtual
    echo "Creando el entorno virtual..."
    python3 -m virtualenv $ENV_NAME
fi

# Activar entorno virtual
echo "Activando el entorno virtual..."
source $ENV_NAME/bin/activate

# Asegurarse de que setuptools, pip y wheel estén instalados y actualizados
echo "Actualizando setuptools, pip y wheel..."
pip install --upgrade setuptools pip wheel

# Instalar paquetes necesarios
echo "Instalando paquetes..."
pip install twine siura python-dotenv

# Crear estructura de directorios
echo "Creando estructura de directorios..."
mkdir -p src

# Crear archivo main.py en src si no existe
if [ ! -f src/main.py ]; then
    echo "Creando archivo main.py..."
    cat <<EOL > src/main.py
from dotenv import load_dotenv
import siura

load_dotenv()

print("Siura importado correctamente.")
EOL
else
    echo "El archivo src/main.py ya existe."
fi

# Crear archivo .env en la raíz del proyecto si no existe
if [ ! -f .env ]; then
    echo "Creando archivo .env..."
    cat <<EOL > .env
PYTHONPATH=./src
EOL
else
    echo "El archivo .env ya existe."
fi

# Crear archivo .vscode/settings.json
echo "Configurando VSCode..."
mkdir -p .vscode
cat <<EOL > .vscode/settings.json
{
    "python.envFile": "\${workspaceFolder}/.env",
    "python.defaultInterpreterPath": "\${workspaceFolder}/$ENV_NAME/bin/python"
}
EOL

# Desactivar entorno virtual
echo "Desactivando el entorno virtual..."
deactivate

echo "Configuración completa. Abre VSCode y selecciona el intérprete de Python."

```


## Windows

Crea un archivo setup_project.bat

```bat
@echo off
SET ENV_NAME=venv

REM Verificar si el entorno virtual ya existe
IF EXIST %ENV_NAME% (
    echo El entorno virtual "%ENV_NAME%" ya existe. Activándolo...
) ELSE (
    REM Crear entorno virtual
    echo Creando el entorno virtual...
    python -m virtualenv %ENV_NAME%
)

REM Activar entorno virtual
echo Activando el entorno virtual...
call %ENV_NAME%\Scripts\activate.bat

REM Asegurarse de que setuptools, pip y wheel estén instalados y actualizados
echo Actualizando setuptools, pip y wheel...
pip install --upgrade setuptools pip wheel

REM Instalar paquetes necesarios
echo Instalando paquetes...
pip install twine siura python-dotenv

REM Crear estructura de directorios
echo Creando estructura de directorios...
mkdir src

REM Crear archivo main.py en src si no existe
IF NOT EXIST src\main.py (
    echo Creando archivo main.py...
    echo from dotenv import load_dotenv > src\main.py
    echo import siura >> src\main.py
    echo. >> src\main.py
    echo load_dotenv() >> src\main.py
    echo. >> src\main.py
    echo print("Siura importado correctamente.") >> src\main.py
) ELSE (
    echo El archivo src\main.py ya existe.
)

REM Crear archivo .env en la raíz del proyecto si no existe
IF NOT EXIST .env (
    echo Creando archivo .env...
    echo PYTHONPATH=./src > .env
) ELSE (
    echo El archivo .env ya existe.
)

REM Crear archivo .vscode/settings.json
echo Configurando VSCode...
mkdir .vscode
(
    echo {
    echo     "python.envFile": "%workspaceFolder%\\.env",
    echo     "python.defaultInterpreterPath": "%workspaceFolder%\\%ENV_NAME%\\Scripts\\python.exe"
    echo }
) > .vscode\settings.json

REM Desactivar entorno virtual
echo Desactivando el entorno virtual...
deactivate

echo Configuración completa. Abre VSCode y selecciona el intérprete de Python.
```