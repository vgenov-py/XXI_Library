<h1 id="version">
BNE API - Versión: 1.2.1
</h1>

### Para hacer uso del API deberá indicar el conjunto de datos a consultar

URL BASE: [https://apidatosabiertos.bne.es](https://apidatosabiertos.bne.es)

    Geográfico: geo,
    Persona: per,
    Monografías modernas: mon
    Monografías antiguas: moa
    Entidades: ent
    Manuscritos: mss
    Prensa y Revista: ser

dataset
-------

    GET /geo

*   Las respuestas serán emitidas en formato JSON y contarán con las siguientes claves en el caso exitoso:
    
        success: boolean
        time: float
        data: array
    
*   Caso fallido:
    
        success: boolean
        message: str
    
<h3 id="responses">
Ejemplo de respuesta:
</h3>
```
{
    "success": true,
    "time": 0.01,
    "data": [
        {
        "id":"XX450536",
        "lugar_jerarquico": "España, Cataluña"
        }
    ]
}
```

### Parámetros opcionales:

<h3 id="order" class="mt-4">
order by
</h3>
--------

    GET /geo?order_by=t_781

*   El parámetro **order\_by** permite ordenar los resultados a en base a un determinado campo existente en el modelo.
    
        GET /geo?order_by=t_781
    
*   Es posible ordenar de manera ascendente y de manera descendente agregando una coma seguido por **asc** o **desc**.
    
        GET /geo?order_by=t_781,desc
    
<h3 id="fields">
fields
</h3>
    GET /geo?limit=10&fields=id,t_024

*   El parámetro **fields** permite seleccionar los campos a mostrar por cada registro.
*   Cada campo adicional deberá ser separado por comas.

Ejemplo de respuesta:

    GET /geo?t_024=viaf&fields=id,t_024
```
{
    "success": true,
    "time": 0.01,
    "data": [
        {
            "id":"XX450536",
            "t_024": "|ahttp://id.loc.gov/authorities/names/n79089624|2lcnaf /**/ |ahttp://viaf.org/viaf/316429160|2viaf"
        }
    ]
}
```

Si indicamos un campo inexistente en el conjunto se mostrará el siguiente error:
```
{
    "success": false,
    "message": "This field doesn't exist in the db: 1 - available fields: ('id', 't_001', 't_024'..."
}
```
<h3 id="filters">
Campos filtro
</h3>

Para filtrar una búsqueda por un determinado valor deberemos indicar como parámetro la columna a buscar y el valor por el cual queramos filtrar.

    GET /geo?t_024=Andalucía

*   Las etiquetas MARC deben ser indicadas con el prefijo **t\_**
*   Cada filtro adicional debe ser agregado como un nuevo parámetro utilizando el caracter **&**

    GET /geo?t_024=Andalucía&lugar_jerarquico=España

*   La búsqueda será **insensible** a las mayúsculas.
*   El valor introducido será buscado dentro del campo diana/objetivo. Si indicamos **esp** en el campo **lugar\_jerarquico** entregará todos los registros que contengan las letras **esp**

Ejemplo de respuesta:

    GET /geo?lugar_jerarquico=esp
```
{
    "success": true,
    "time": 0.0123,
    "data": [
        {
            "id":"XX450537",
            "lugar_jerarquico": "España, Andalucía"
        }
    ]
}
```

Es posible utilizar operadores lógicos, para éste cometido agregar entre valor y valor algunos de los siguientes operadores lógicos:

* AND
* OR
* NOT

Ejemplo de respuesta:

    GET /geo?lugar_jerarquico=españa NOT andorra
```
{
    "success": true,
    "time": 0.0123,
    "data": [
        {
        "id":"XX450557",
        "lugar_jerarquico": "Gran Bretaña, Escocia"
        }
    ]
}
```

Es posible buscar campos sin valor, utilizar **null** o **!null** para buscar campos con valor

Ejemplo de respuesta:

    GET /geo?lugar_jerarquico=null
```
{
    "success": true,
    "time": 0.0123,
    "data": [
        {
        "id":"XX450557",
        "lugar_jerarquico": null
        }
    ]
}
```

Desde la versión 1.1.0 es posible hacer consultas cruzadas, consultar el conjunto de datos **A** con filtros del conjunto de datos **B** La sintaxis es la siguiente: /api/{conjunto\_1}?{conjunto\_2}={filtro\_1}:{valor},{filtro\_2}:valor
<h3 id="csv">
Descargar
</h3>

Para descargar el conjunto en formato CSV o JSON, agregar al final de la url **.csv** o **.json** respectivamente

    GET /geo?t_781=Andalucía.csv
<h3 id="joining-queries">
Consultas cruzadas
</h3>

Las consultas cruzadas, están disponibles sobre los conjuntos Monografías Modernas y Persona

    GET /mon?per=t_100:vito dumas,genero:masculino
```
{
    "success": true,
    "time": 20.33,
    "data": [
        {"id": "bimo0000120763",
        "siglo": "XX"
        }
    ]
}
```

### Diagramas

Los diagramas de los distintos conjuntos de datos pueden ser consultados [aquí](https://bneapi.infofortis.com/api/schema)

<h3 id="tutorial">
Tutorial
</h3>

Con ánimo de facilitar el uso de ésta aplicación, ofrecememos el siguiente ejemplo consultado el conjunto de datos **Persona**, recomendamos utilizar Firefox o Microsoft Edge, ya que ambos muestran la respuesta en JSON en un formato legible. 

Si queremos utilizar Google Chrome os recomendamos agregar la extensión <a href="https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh" target="_blank">json viewer</a> , aunque bajo ningún punto es necesario.

1. Acceder a **https://bneapi.infofortis.com/api/per**

    * Ésta petición nos devolvera los primeros 1000 resultados encontrados en formato JSON:
    * Respuesta:
    <img src="/static/tuto_json.png"
        alt="JSON_1"
        />
    
2. Para filtrar los datos encontrados en el paso anterior, debemos agregar los filtros y su valor, separados por **=**

    * Filtrar por **nombre de persona**, nombre_de_persona=**Fernández**
    * https://bneapi.infofortis.com/api/per?**nombre_de_persona=Fernández**
    * Respuesta:
    <img src="/static/tuto_json2.png"
        alt="JSON_2"
        />

3. Para agregar más filtros debemos separar las parejas **filtro=valor** con el caracter **&**

    * https://bneapi.infofortis.com/api/per?nombre_de_persona=Fernández**&genero=masculino**
    * Respuesta:
    <img src="/static/tuto_json3.png"
        alt="JSON_2"
        />

4. Si queremos mostrar solo algunos campos como por ejemplo el **id**, **nombre_de_persona** y **género**, podemos agregar la clave **fields** separados por comsas y sin espacios entre ellos:
    
    * https://bneapi.infofortis.com/api/per?nombre_de_persona=Fernández&genero=masculino**&fields=id,nombre_de_persona,genero**
    * Respuesta: 
    <img src="/static/tuto_json4.png"
        alt="JSON_2"
        />

5. Una vez tengamos el conjunto filtrado con los campos que deseamos ver, agregaremos **.json** o **.csv** al final, para descargar los resultados.
    * https://bneapi.infofortis.com/api/per?nombre_de_persona=Fernández&genero=masculino&fields=id,nombre_de_persona,genero**.csv**
    * Respuesta: 
    <img src="/static/tuto_csv.png" class="my-4"
        alt="JSON_2"
        />
    * CSV:
    <img src="/static/tuto_csv2.png"
        alt="JSON_2"
        />

<h3 id="examples">
Ejemplos de consulta
</h3>

Algunos ejemplos de consulta 

1. Guitarristas nacidos en **Andalucía**

```
/api/per?lugar_nacimiento=andalucía&ocupacion=guitarrista
```

2. Libros escritos en inglés durante la Guerra Civil (1936-1939) sobre la temática

```
/api/mon?fecha_de_publicacion=1936-1939&lengua_principal=inglés&tema=guerra civil
```

3. Todos los registros geográficos de País Vasco

```
api/geo?t_781=país vasco
```

4. Archivos sonoros en soporte **discos**

```
api/son?soporte=disco
```

5. Revistas en formatos digital

```
/api/ser?t_655=páginas web
```