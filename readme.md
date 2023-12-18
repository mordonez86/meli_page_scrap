# MELI SEARCH SCRAP

## Descripción
Este repositorio contiene un script para realizar scraping en MercadoLibre. El script realiza las siguientes funciones:

- **Scrapeo de Búsquedas**: Permite realizar búsquedas específicas en MercadoLibre.
  - Ejemplo de uso: `https://mercadolibre.com.ar?search=iphone`

- **Almacenamiento de Datos**: Guarda la página completa en formato HTML. Además, registra el número de página, la fecha de la descarga y el término de búsqueda utilizado.

- **Búsqueda Eficiente**: Se enfoca en dos botones específicos (botón de cookies y botón de página siguiente), lo que reduce la posibilidad de errores.

- **Entorno de Ejecución**: Funciona dentro de un contenedor llamado `browserless`, que opera un navegador Chrome en modo headless.

## Pendiente
- Mejorar la lógica del `user_agent` para descargarlo de manera aleatoria de internet.

## Funcionamiento
- Buildear el contenedor y ejecutar desde airflow usando el operador `DockerOperator`.
- Va a generar en el host en la ruta /data una carpeta donde guardara con el nombre de la busqueda y el dia de bajada las primeras 40 paginas de determinada busqueda
