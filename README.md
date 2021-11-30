# Herramienta de descarga de los diarios oficiales

El proyecto fue creado con la librería de Python [Scrapy](https://scrapy.org/).

## ¿Cómo usar las arañas?


En el directorio del proyecto, crea la carpeta 'descargas' y luego ejecuta los siguientes comandos:

### scrapy crawl diarios

Con este comando, scrapy descargará todos los diarios oficiales.\
Es importante que tengas al menos 300 Gb disponibles, así como una conexión estable a internet.

### scrapy crawl yearspider

Con esta araña puedes descargar todos los diarios oficiales de un año específico.\
Para los diarios cuyo año sea igual o superior a 1954, debes ingresar do-YYYY\
mientras que para años inferiores, el año directamente.

## Notas importantes

Es necesario que tengas instalado Python y scrapy. Busca tutoriales en internet de cómo hacerlo.\
