@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

:: === CONFIGURACIÓN GENERAL ===
SET PROJECT_PATH=D:\T\Proyectos\ProyectoPGH
SET PROJECT_NAME=ProyectoPGH
SET APP_NAME=Mprincipal
SET VENV_NAME=PGH
SET PYTHON_PATH=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python312\python.exe

echo ================================================
echo =     SCRIPT DE CREACION DE PROYECTO DJANGO     =
echo ================================================
echo.
echo Proyecto Django:      %PROJECT_NAME%
echo Ruta del proyecto:    %PROJECT_PATH%
echo Nombre del entorno:   %VENV_NAME%
echo App Django inicial:   %APP_NAME%
echo Ruta de Python:       %PYTHON_PATH%
echo.

:: === CONFIRMAR CON EL USUARIO ===
CHOICE /M "¿Deseas continuar con la creación del proyecto?"
IF ERRORLEVEL 2 (
    echo Operación cancelada por el usuario.
    pause
    exit /b
)

:: === VERIFICAR EXISTENCIA DE PYTHON ===
IF NOT EXIST "%PYTHON_PATH%" (
    echo [ERROR] No se encontró Python 3.12.3 en: %PYTHON_PATH%
    echo Por favor instálalo desde: https://www.python.org/downloads/release/python-3123/
    pause
    exit /b
) ELSE (
    echo [OK] Python 3.12.3 está instalado.
)

:: === VERIFICAR EXISTENCIA DE DISCO Y CARPETA ===
IF NOT EXIST "D:\Proyectos" (
    echo [INFO] La carpeta D:\Proyectos no existe. Se creará.
    mkdir D:\Proyectos
)

IF EXIST "%PROJECT_PATH%" (
    echo [ADVERTENCIA] Ya existe la carpeta del proyecto: %PROJECT_PATH%
    CHOICE /M "¿Deseas continuar (esto puede sobrescribir archivos existentes)?"
    IF ERRORLEVEL 2 (
        echo Operación cancelada.
        pause
        exit /b
    )
) ELSE (
    echo [OK] Se creará la carpeta del proyecto en: %PROJECT_PATH%
)

:: === CREAR CARPETA DEL PROYECTO ===
mkdir "%PROJECT_PATH%" >nul 2>&1
cd "%PROJECT_PATH%"

:: === CREAR ENTORNO VIRTUAL ===
echo Creando entorno virtual: %VENV_NAME%...
"%PYTHON_PATH%" -m venv %VENV_NAME%

:: === ACTIVAR ENTORNO VIRTUAL ===
CALL %VENV_NAME%\Scripts\activate.bat

:: === ACTUALIZAR pip y setuptools ===
echo Actualizando pip...
python -m pip install --upgrade pip

:: === INSTALAR DEPENDENCIAS BASE ===
echo Instalando dependencias requeridas...
pip install ^
    asgiref==3.8.1 ^
    Django==5.0.4 ^
    djangorestframework==3.15.1 ^
    setuptools==80.4.0 ^
    sqlparse==0.5.3 ^
    tzdata==2025.2 ^
    pillow==11.2.1

:: === CREAR PROYECTO DJANGO ===
IF NOT EXIST "manage.py" (
    echo Creando proyecto Django: %PROJECT_NAME%...
    django-admin startproject %PROJECT_NAME% .
) ELSE (
    echo Ya existe un archivo manage.py, se omite la creación del proyecto Django.
)

:: === CREAR APP PRINCIPAL ===
IF NOT EXIST "%APP_NAME%\apps.py" (
    echo Creando app Django llamada %APP_NAME%...
    python manage.py startapp %APP_NAME%
) ELSE (
    echo Ya existe la app %APP_NAME%, se omite la creación.
)

:: === GUARDAR DEPENDENCIAS ===
echo Generando archivo requirements.txt...
pip freeze > requirements.txt

:: === MIGRACIONES Y SERVIDOR ===
echo Ejecutando migraciones iniciales...
python manage.py migrate

echo Proyecto Django listo. Ejecutando servidor...
python manage.py runserver

ENDLOCAL
pause