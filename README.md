# Buscador de Productos en MercadoLibre con Playwright

Este proyecto automatiza la búsqueda de productos en MercadoLibre utilizando Playwright en Python. El objetivo principal del script es realizar la búsqueda de "PlayStation 5", aplicar filtros de "Nuevo" y "Distrito Federal", ordenar los resultados por "Mayor precio", y extraer información sobre los primeros 5 productos, incluyendo su nombre y precio. Además, el script toma capturas de pantalla en cada paso clave del proceso para documentar visualmente las acciones realizadas.

## Requisitos

Antes de ejecutar el script, asegúrese de contar con Python instalado y con las dependencias necesarias para ejecutar el proyecto.

### 1. Crear un entorno virtual

Es recomendable crear un entorno virtual para gestionar las dependencias del proyecto de manera aislada. Para ello, ejecute los siguientes comandos:

- Para crear un entorno virtual:  
  `python -m venv venv`

### 2. Activar el entorno virtual

Para activar el entorno virtual, utilice el siguiente comando según su sistema operativo:

- En **Windows**:  
  `venv\Scripts\activate`

- En **macOS/Linux**:  
  `source venv/bin/activate`

### 3. Instalación de dependencias

Una vez activado el entorno virtual, instale Playwright ejecutando el siguiente comando:

`pip install playwright`

### 4. Instalación de los navegadores

Después de instalar Playwright, será necesario instalar los navegadores que se utilizarán para la automatización (Chromium en este caso). Ejecute el siguiente comando para completar la instalación de los navegadores:

`python -m playwright install`

### 5. Ejecución del script

Una vez que haya instalado todas las dependencias necesarias, puede proceder a ejecutar el script con el siguiente comando:

`py .\scraper.py`

Este comando abrirá un navegador, realizará la búsqueda en MercadoLibre, aplicará los filtros establecidos y tomará capturas de pantalla en cada etapa del proceso.
