fields = {
    "per":[
        {
            "name":"otros_identificadores",
            "t": "024",
            "description": "Identificadores de la persona en otros catálogos (viaf, lcnf, isni, etc.)",
            "t_description": "$2: $a"
        },
        {
            "name": "fecha_nacimiento",
            "t": "046",
            "description": "Fecha de nacimiento de la persona",
            "t_description": "$f"
        },
        {
            "name": "fecha_muerte",
            "t": "_2046",
            "description": "Fecha de muerte de la persona",
            "t_description": "$g"
        },
        {
            "name": "nombre_de_persona",
            "t": "100",
            "description": "Nombre de persona",
            "t_description": "$a,$b,$c($d)($q)"
        },
        {
            "name": "otros_atributos_persona",
            "t": "368",
            "description": "Título, cargo, etc. ",
            "t_description": "$c$d"
        },
        {
            "name": "lugar_nacimiento",
            "t": "370",
            "description": "País, región, provincia y localidad donde ha nacido la persona",
            "t_description": "$a"
        },
        {
            "name": "lugar_muerte",
            "t": "_2370",
            "description": "País, región, provincia y localidad donde ha fallecido la persona",
            "t_description": "$b"
        },
        {
            "name": "pais_relacionado",
            "t": "_3370",
            "description": "Otro país relacionado con la persona",
            "t_description": "$c"
        },
        {
            "name": "otros_lugares_relacionados",
            "t": "_4370",
            "description": "Otros lugares relacionados con la persona",
            "t_description": "$f"
        },
        {
            "name": "lugar_residencia",
            "t": "_5370",
            "description": "Lugar de residencia de la persona, si es especialmente significativo",
            "t_description": "$e"
        },
        {
            "name": "campo_actividad",
            "t": "372",
            "description": "Disciplina o actividad a la que se dedica la persona",
            "t_description": "$a"
        },
        {
            "name": "grupo_o_entidad relacionada",
            "t": "373, 510",
            "description": "Grupo, organismo, etc., a la que pertenece la persona",
            "t_description": "373, $a; 510, $a$b"
        },
        {
            "name": "ocupacion",
            "t": "374",
            "description": "Profesión desempeñada por la persona",
            "t_description": "$a"
        },
        {
            "name": "genero",
            "t": "375",
            "description": "Género de la persona (masculino, femenino u otros)",
            "t_description": "$a"
        },
        {
            "name": "lengua",
            "t": "377",
            "description": "Lengua en la que la persona escribe la mayor parte de su obra",
            "t_description": "$l"
        },
        {
            "name": "otros_nombres",
            "t": "400",
            "description": "Otros nombres por los que es conocida la persona",
            "t_description": "$a,$b,$c($d)($q)"
        },
        {
            "name": "persona_relacionada",
            "t": "500",
            "description": "Otras personas relacionadas con la persona",
            "t_description": "$a,$b,$c($d)($q)"
        },
        {
            "name": "nota_general",
            "t": "667",
            "description": "Más información sobre la persona",
            "t_description": "$a"
        },
        {
            "name": "fuentes_de_informacion",
            "t": "670",
            "description": "Fuentes de información de las que se han obtenido los datos de la persona",
            "t_description": "$a: $b ($u)"
        },
        {
            "name": "otros_datos_biográficos",
            "t": "678",
            "description": "Otra información biográfica de la persona",
            "t_description": "$a"
        },
    ],
    "mon":[
        {
            "name": "pais_de_publicacion",
            "t": "008",
            "description": "País donde se ha publicado la monografía",
            "t_description": "008:15-17"
        },
        {
            "name": "lengua_principal",
            "t": "_2008, 041",
            "description": "Lengua del contenido principal del documento",
            "t_description": "008:35-37, 041: $a"
        },
        {
            "name": "otras_lenguas",
            "t": "_1041",
            "description": "Lenguas de otros contenidos (resúmenes, tablas de contenidos, notas, etc.)",
            "t_description": "$b, $d, $f,$j,$k"
        },
        {
            "name": "lengua_original",
            "t": "_2041",
            "description": "Lengua original de la que se ha traducido",
            "t_description": "$h"
        },
        {
            "name": "fecha_de_publicacion",
            "t": "_3008",
            "description": "Fecha en que se publicó la monografía o su primera entrega en caso de una monografía en varias partes",
            "t_description": "008/7-10"
        },
        {
            "name": "decada",
            "t": "_4008",
            "description": "Década en la que se publicó la monografía o su primera entrega en caso de una monografía en varias partes",
            "t_description": "A partir de fecha_de_publicacion"
        },
        {
            "name": "siglo",
            "t": "_5008",
            "description": "Siglo en el  que se publicó la monografía o su primera entrega en caso de una monografía en varias partes",
            "t_description": "A partir de fecha_de_publicacion"
        },
        {
            "name": "deposito_legal",
            "t": "017",
            "description": "Número de Depósito Legal",
            "t_description": "$a"
        },
        {
            "name": "isbn",
            "t": "020",
            "description": "International Standard Book Number",
            "t_description": "$a ($q) "
        },
        {
            "name": "nipo",
            "t": "024",
            "description": "Número de Identificación de Publicaciones Oficiales",
            "t_description": "$a ($q) "
        },
        {
            "name": "cdu",
            "t": "080",
            "description": "Número de la Clasificación Decimal Universalque representa el tema tratado en la monografía",
            "t_description": "$a"
        },
        {
            "name": "autores",
            "t": "100, 110, 700, 710",
            "description": "Responsables del contenido intelectual de la monografía",
            "t_description": "$a,$b,$c($d)($q)($e)"
        },
        {
            "name": "titulo",
            "t": "245",
            "description": "Título de la obra tal y como aparece citado en la monografía",
            "t_description": "$a:$b.$n,$p"
        },
        {
            "name": "mencion_de_autores",
            "t": "_2245",
            "description": "Responsables del contenido intelectual tal y como aparecen citados en la monografía",
            "t_description": "$c"
        },
        {
            "name": "otros_titulos",
            "t": "246, 740",
            "description": "Otros títulos de la obra que aparecen citados en la monografía",
            "t_description": "246: [$i]:$a:$b.$n,$p 740: $a$n, $p"
        },
        {
            "name": "edicion",
            "t": "250",
            "description": "Información sobre la edición",
            "t_description": "$a,$b"
        },
        {
            "name": "lugar_de_publicacion",
            "t": "260, 264",
            "description": "Localidad específica en la que se ha publicado la monografía",
            "t_description": "$a"
        },
        {
            "name": "editorial",
            "t": "_2260, 264",
            "description": "Nombre del editor responsable de la publicación de la monografía",
            "t_description": "$b"
        },
        {
            "name": "extension",
            "t": "300",
            "description": "Número de volúmenes, páginas, hojas, columnas, etc.",
            "t_description": "$a"
        },
        {
            "name": "otras_caracteristicas_fisicas",
            "t": "_2300",
            "description": "Ilustraciones, color, etc.",
            "t_description": "$b"
        },
        {
            "name": "dimensiones",
            "t": "_3300",
            "description": "Medida del alto de la publicación (en cm)",
            "t_description": "$c"
        },
        {
            "name": "material_anejo",
            "t": "_4300",
            "description": "Material complementario que acompaña a la publicación principal",
            "t_description": "$e"
        },
        {
            "name": "serie",
            "t": "440, 490",
            "description": "Colección a la que pertenece la monografía",
            "t_description": "$a$v"
        },
        {
            "name": "nota_de_contenido",
            "t": "505",
            "description": "Más información sobre el contenido de la obra",
            "t_description": "$a"
        },
        {
            "name": "notas",
            "t": "500, 504, 546, 563, 594",
            "description": "Más información sobre la monografía",
            "t_description": "$a"
        },
        {
            "name": "procedencia",
            "t": "561",
            "description": "Nombre del último propietario del ejemplar antes de pasar a la BNE",
            "t_description": "$a"
        },
        {
            "name": "premios",
            "t": "586",
            "description": "Premios con los que ha sido galardonada la obra",
            "t_description": "$a"
        },
        {
            "name": "tema",
            "t": "600, 610, 611, 630, 650, 651, 653",
            "description": "Materia sobre la que trata la monografía",
            "t_description": "Todos los subcampos excepto $2"
        },
        {
            "name": "genero_forma",
            "t": "655",
            "description": "Género al que pertenece la obra y forma que toma",
            "t_description": "Todos los subcampos excepto $2"
        },
        {
            "name": "tipo_ de_documento",
            "t": "994",
            "description": "tipo de monografía (en papel o electrónica)",
            "t_description": '$a',
        }
    ],
    "ent":[
        {
            "name": "otros_identificadores",
            "t": "024",
            "description": "Identificadores de la entidad en otros catálogos (viaf, lcnf, isni, etc.)",
            "t_description": "$2: $a ",
        },
        {
            "name": "fecha_establecimiento",
            "t": "046",
            "description": "Fecha de creación o inicio de actividad de la entidad",
            "t_description": "$q (o $s)",
        },
        {
            "name": "fecha_finalizacion",
            "t": "_2046",
            "description": "Fecha de desapaprición o cese de actividad de la entidad",
            "t_description": "$r (o $t)",
        },
        {
            "name": "nombre_de_entidad",
            "t": "110",
            "description": "Nombre de la entidad corporativa",
            "t_description": "$a,$b, $b...",
        },
        {
            "name": "tipo_entidad",
            "t": "368",
            "description": "tipo de entidad corporativa",
            "t_description": "$a",
        },
        {
            "name": "pais",
            "t": "370",
            "description": "País relacionado con la entidad",
            "t_description": "$c",
        },
        {
            "name": "sede",
            "t": "_2370",
            "description": "Lugar donde se encuentra la sede de la entidad, si es especialmente significativo",
            "t_description": "$e",
        },
        {
            "name": "campo_actividad",
            "t": "372",
            "description": "Disciplina o actividad a la que se dedica la entidad",
            "t_description": "$a",
        },
        {
            "name": "lengua",
            "t": "377",
            "description": "Lengua en la que la entidad suele publicar",
            "t_description": "$l",
        },
        {
            "name": "otros_nombres",
            "t": "410",
            "description": "Otros nombres por los que es conocida la entidad",
            "t_description": "$a,$b, $b...",
        },
        {
            "name": "persona_relacionada",
            "t": "500",
            "description": "Personas relacionadas con la entidad",
            "t_description": "$a,$b,$c($d)($q)",
        },
        {
            "name": "grupo_o_entidad_relacionada",
            "t": "510",
            "description": "Grupo, organismo, etc., relacionado con la entidad",
            "t_description": "$a,$b, $b...",
        },
        {
            "name": "nota_de_relacion",
            "t": "663",
            "description": "Otras relaciones de la entidad con personas, otras entidades, etc.",
            "t_description": "$a,$b,$b...",
        },
        {
            "name": "otros_datos_historicos",
            "t": "665, 678",
            "description": "Otra información histórica de la entidad",
            "t_description": "$a",
        },
        {
            "name": "nota_general",
            "t": "667",
            "description": "Más información sobre la entidad",
            "t_description": "$a",
        },
        {
            "name": "fuentes_de_informacion",
            "t": "670",
            "description": "Fuentes de información de las que se han obtenido los datos de la entidad",
            "t_description": "$a: $b ($u)",
        }
    ],
	"moa":[
        {
            "name":"pais_de_publicacion",
            "t":"008",
            "description":"país donde se ha publicado la monografía",
            "t_description":"008/15-17"
        },
        {
            "name":"lengua_principal",
            "t":"_2008, 041",
            "description":"lengua del contenido principal del documento",
            "t_description":"008:35-37, 041: $a"
        },
        {
            "name":"otras_lenguas",
            "t":"_2041",
            "description":"lenguas de otros contenidos (resúmenes, tablas de contenidos, notas, etc.)",
            "t_description":"$b, $d, $f,$j,$k"
        },
        {
            "name":"lengua_original",
            "t":"_3041",
            "description":"lengua original de la que se ha traducido",
            "t_description":"$h"
        },
        {
            "name":"fecha_de_publicacion",
            "t":"_3008",
            "description":"Fecha en que se publicó la monografía o su primera entrega en caso de una monografía en varias partes",
            "t_description":"008/7-10"
        },
        {
            "name":"decada",
            "t":"_4008",
            "description":"Década en la que se publicó la monografía o su primera entrega en caso de una monografía en varias partes",
            "t_description":"a partir de fecha_de_publicacion"
        },
        {
            "name":"siglo",
            "t":"_5008",
            "description":"Siglo en el  que se publicó la monografía o su primera entrega en caso de una monografía en varias partes",
            "t_description":"a partir de fecha_de_publicacion"
        },
        {
            "name":"CDU",
            "t":"080",
            "description":"número de la Clasificación Decimal Universalque representa el tema tratado en la monografía",
            "t_description":"sólo contenido de $a"
        },
        {
            "name":"autores",
            "t":"100, 110, 700, 710",
            "description":"responsables del contenido intelectual de la monografía",
            "t_description":"$a{$b$c}($d)($q)($e)"
        },
        {
            "name":"titulo",
            "t":"245",
            "description":"titulo de la obra tal y como aparece citado en la monografía",
            "t_description":"$a:$b.$n,$p"
        },
        {
            "name":"mencion_de_autores",
            "t":"245",
            "description":"responsables del contenido intelectual tal y como aparecen citados en la monografía",
            "t_description":"$c"
        },
        {
            "name":"otros_titulos",
            "t":"246, 740",
            "description":"otros títulos de la obra que aparecen citados en la monografía",
            "t_description":"246: [$i]:$a:$b.$n,$p 740: $a$n, $p"
        },
        {
            "name":"edicion",
            "t":"250",
            "description":"información sobre la edición",
            "t_description":"$a,$b"
        },
        {
            "name":"lugar_de_publicacion",
            "t":"260, 264",
            "description":"localidad específica en la que se ha publicado y/o impreso la monografía",
            "t_description":"$a, $e"
        },
        {
            "name":"editor_impresor",
            "t":"_2260, 264",
            "description":"nombre del editor y/o impresor responsable de la publicación de la monografía",
            "t_description":"$b, $f"
        },
        {
            "name":"extension",
            "t":"300",
            "description":"número de volúmenes, páginas, hojas, columnas, etc.",
            "t_description":"$a"
        },
        {
            "name":"otras_caracteristicas_fisicas",
            "t":"_2300",
            "description":"ilustraciones, color, etc.",
            "t_description":"$b"
        },
        {
            "name":"dimensiones",
            "t":"_3300",
            "description":"medida del alto de la publicación (en cm)",
            "t_description":"$c"
        },
        {
            "name":"material_anejo",
            "t":"_4300",
            "description":"material complementario que acompaña a la publicación principal",
            "t_description":"$e"
        },
        {
            "name":"serie",
            "t":"440, 490",
            "description":"colección a la que pertenece la monografía",
            "t_description":"$a$v"
        },
        {
            "name":"nota_de_contenido",
            "t":"505",
            "description":"más información sobre el contenido de la obra",
            "t_description":"$a"
        },
        {
            "name":"notas",
            "t":"593,594,595,597,599,546",
            "description":"más información sobre la monografía",
            "t_description":"$a"
        },
        {
            "name":"transcripcion_incipit_explicit",
            "t":"529",
            "description":"transcripciones del principio y/o el final del texto de la monografía",
            "t_description":"$a"
        },
        {
            "name":"procedencia",
            "t":"561",
            "description":"nombre del último propietario del ejemplar antes de pasar a la BNE",
            "t_description":"$a"
        },
        {
            "name":"cita",
            "t":"510",
            "description":"citas o referencias de descripciones bibliográficas, reseñas, resúmenes o índices de la monografía en diferentes repertorios",
            "t_description":"$a,$c"
        },
        {
            "name":"tema",
            "t":"600, 610, 611, 630, 650, 651, 653",
            "description":"materia sobre la que trata la monografía",
            "t_description":"todos los subbcampos menos $2"
        },
        {
            "name":"genero_forma",
            "t":"655",
            "description":"género al que pertenece la obra y forma que toma",
            "t_description":"todos los subbcampos menos $2"
        },
        {
            "name":"lugar_relacionado",
            "t":"752",
            "description":"lugar relacionado con la monografía, en formato normalizado",
            "t_description":"$d, $a ($e)"
        },
        {
            "name":"url",
            "t":"856",
            "description":"url de la digitalización o de un recurso digital relacionado",
            "t_description":"$y, $3: $u"
        }
    ],
    "mss":[
        {
            "name": "pais_de_publicacion",
            "t": "008",
            "description": "país de producción",
            "t_description": "$a: 15-17",
        },
        {
            "name": "lengua_principal",
            "t": "_2008",
            "description": "lengua del contenido principal del documento",
            "t_description": "$a: 35-37",
        },
        {
            "name": "otras_lenguas",
            "t": "041",
            "description": "lenguas de otros contenidos (resúmenes, tablas de contenidos, notas, etc.)",
            "t_description": "$b, $d, $f, $j, $k",
        },
        {
            "name": "lengua_original",
            "t": "_2041",
            "description": "lengua original de la que se ha traducido",
            "t_description": "$h",
        },
        {
            "name": "fecha_de_publicacion",
            "t": "_3008",
            "description": "fecha de la producción de la obra",
            "t_description": "$a: 7-10",
        },
        {
            "name": "decada",
            "t": "_4008",
            "description": "década de la producción de la obra ",
            "t_description": "$a: 7-10",
        },
        {
            "name": "siglo",
            "t": "_5008",
            "description": "siglo de la producción de la obra ",
            "t_description": "$a: 7-10",
        },
        {
            "name": "deposito_legal",
            "t": "017",
            "description": "número de Depósito Legal",
            "t_description": "$a",
        },
        {
            "name": "CDU",
            "t": "080",
            "description": "número de la Clasificación Decimal Universal que representa el tema tratado en la publicación",
            "t_description": "$a",
        },
        {
            "name": "autores",
            "t": "100, 700",
            "description": "responsables del contenido intelectual de la obra",
            "t_description": "$a{$b$c}($d)($q)($e)",
        },
        {
            "name": "titulo",
            "t": "245",
            "description": "título de la obra tal y como aparece citado en la misma ",
            "t_description": "$a:$b.$n,$p",
        },
        {
            "name": "mencion_de_autores",
            "t": "_2245",
            "description": "responsables del contenido intelectual tal y como aparecen citados en la obra",
            "t_description": "$c",
        },
        {
            "name": "otros_titulos",
            "t": "246",
            "description": "otros títulos de la obra que aparecen citados en la obra",
            "t_description": "[$i]:$a:$b.$n,$p",
        },
        {
            "name": "lugar_de_produccion",
            "t": "260, 264",
            "description": "otros títulos de la obra que aparecen citados en la obra",
            "t_description": "[$i]:$a:$b.$n,$p",
        },
        {
            "name": "extension",
            "t": "300",
            "description": "número de volúmenes, páginas, hojas, columnas, etc.",
            "t_description": "$a",
        },
        {
            "name": "otras_caracteristicas_fisicas",
            "t": "_2300",
            "description": "ilustraciones, color, etc.",
            "t_description": "$b",
        },
        {
            "name": "dimensiones",
            "t": "_3300",
            "description": "medida del alto del documento (en cm)",
            "t_description": "$c",
        },
        {
            "name": "material_anejo",
            "t": "_4300",
            "description": "material complementario que acompaña a la obra principal",
            "t_description": "$e",
        },
        {
            "name": "serie",
            "t": "440, 490",
            "description": "colección a la que pertenece la obra",
            "t_description": "$a$v",
        },
        {
            "name": "nota_de_contenido",
            "t": "505",
            "description": "más información sobre el contenido de la obra",
            "t_description": "$a",
        },
        {
            "name": "notas",
            "t": "500, 520, 594...",
            "description": "más información sobre la obra",
            "t_description": "$a",
        },
        {
            "name": "procedencia",
            "t": "561",
            "description": "nombre del último propietario del ejemplar antes de pasar a la BNE",
            "t_description": "$a",
        },
        {
            "name": "premios",
            "t": "586",
            "description": "premios con los que ha sido galardonada la obra",
            "t_description": "$a",
        },
        {
            "name": "incipit_explicit",
            "t": "529",
            "description": "inicio/fin (íncipit/explicit y primeros versos)",
            "t_description": "$a",
        },
        {
            "name": "tema",
            "t": "600, 610, 611...",
            "description": "materia sobre la que trata la obra",
            "t_description": "todos los subcampos menos $2",
        },
        {
            "name": "genero_forma",
            "t": "655",
            "description": "género al que pertenece la obra y forma que toma",
            "t_description": "todos los subcampos menos $2",
        },
    ],
    "ser":[
        {
            "name": "pais_de_publicacion",
            "t": "008",
            "description": "país de producción",
            "t_description": "$a: 15-17",
        },
        {
            "name": "lengua_principal",
            "t": "_2008",
            "description": "lengua del contenido principal del documento",
            "t_description": "$a: 35-37",
        },
        {
            "name": "otras_lenguas",
            "t": "041",
            "description": "lenguas de otros contenidos (resúmenes, tablas de contenidos, notas, etc.)",
            "t_description": "$b, $d, $f, $j, $k",
        },
        {
            "name": "lengua_original",
            "t": "_2041",
            "description": "lengua original de la que se ha traducido",
            "t_description": "$h",
        },
        {
            "name": "fecha_de_publicacion",
            "t": "_3008",
            "description": "fecha de la producción de la obra",
            "t_description": "$a: 7-10",
        },
        {
            "name": "decada",
            "t": "_4008",
            "description": "década de la producción de la obra ",
            "t_description": "$a: 7-10",
        },
        {
            "name": "siglo",
            "t": "_5008",
            "description": "siglo de la producción de la obra ",
            "t_description": "$a: 7-10",
        },
        {
            "name": "deposito_legal",
            "t": "017",
            "description": "número de Depósito Legal",
            "t_description": "$a",
        },
        {
            "name": "ISSN",
            "t": "024",
            "description": "International Standard Serial Number",
            "t_description": "$a ($q)",
        },
        {
            "name": "CDU",
            "t": "080",
            "description": "número de la Clasificación Decimal Universal que representa el tema tratado en la publicación",
            "t_description": "$a",
        },
        {
            "name": "autores",
            "t": "100, 700",
            "description": "responsables del contenido intelectual de la obra",
            "t_description": "$a{$b$c}($d)($q)($e)",
        },
        {
            "name": "titulo",
            "t": "245",
            "description": "título de la obra tal y como aparece citado en la misma ",
            "t_description": "$a:$b.$n,$p",
        },
        {
            "name": "titulo_abreviado",
            "t": "210",
            "description": "título abreviado de la publicación",
            "t_description": "$a($b)",
        },
        {
            "name": "titulo_clave",
            "t": "222",
            "description": "título de la publicacion que se asigna junto con el ISSN",
            "t_description": "$a$b",
        },
        {
            "name": "titulo_normalizado",
            "t": "130",
            "description": "título de la publicación tal y como aparece citado en la misma",
            "t_description": "$a$b.$n,$p",
        },
        {
            "name": "mencion_de_autores",
            "t": "_2245",
            "description": "responsables del contenido intelectual tal y como aparecen citados en la obra",
            "t_description": "$c",
        },
        {
            "name": "otros_titulos",
            "t": "246",
            "description": "otros títulos de la obra que aparecen citados en la obra",
            "t_description": "[$i]:$a:$b.$n,$p",
        },
        {
            "name": "lugar_de_publicacion",
            "t": "260, 264",
            "description": "otros títulos de la obra que aparecen citados en la obra",
            "t_description": "[$i]:$a:$b.$n,$p",
        },
        {
            "name": "editorial",
            "t": "_2260, 264",
            "description": "nombre del editor responsable de la publicación",
            "t_description": "$b",
        },
        {
            "name": "extension",
            "t": "300",
            "description": "número de volúmenes, páginas, hojas, columnas, etc.",
            "t_description": "$a",
        },
        {
            "name": "otras_caracteristicas_fisicas",
            "t": "_2300",
            "description": "ilustraciones, color, etc.",
            "t_description": "$b",
        },
        {
            "name": "dimensiones",
            "t": "_3300",
            "description": "medida del alto del documento (en cm)",
            "t_description": "$c",
        },
        {
            "name": "material_anejo",
            "t": "_4300",
            "description": "material complementario que acompaña a la obra principal",
            "t_description": "$e",
        },
        {
            "name": "periodicidad",
            "t": "310",
            "description": "periodicidad actual de la publicación",
            "t_description": "$a",
        },
        {
            "name": "periodicidad_anterior",
            "t": "321",
            "description": "periocidad anterior de la publicación",
            "t_description": "$a",
        },
        {
            "name": "fechas_y_numeracion",
            "t": "362",
            "description": "fechas de publicación y secuencia de números o fascículo",
            "t_description": "$a",
        },
        {
            "name": "serie",
            "t": "440, 490",
            "description": "colección a la que pertenece la obra",
            "t_description": "$a$v",
        },
        {
            "name": "notas",
            "t": "500, 520, 594...",
            "description": "más información sobre la obra",
            "t_description": "$a",
        },
        {
            "name": "tema",
            "t": "600, 610, 611...",
            "description": "materia sobre la que trata la obra",
            "t_description": "todos los subcampos menos $2",
        },
        {
            "name": "genero_forma",
            "t": "655",
            "description": "género al que pertenece la obra y forma que toma",
            "t_description": "todos los subcampos menos $2",
        },
        {
            "name": "lugar_relacionado",
            "t": "752",
            "description": "lugar de edición o distribución de la publicació",
            "t_description": "$e:$a:b:c:d",
        },
        {
            "name": "otras_ediciones",
            "t": "775",
            "description": "Otras ediciones de la publicación",
            "t_description": "$t ($x)",
        },
        {
            "name": "titulo_anterior",
            "t": "780",
            "description": "publicación de la que es continuación",
            "t_description": "$t ($x)",
        },
        {
            "name": "titulo_posterior",
            "t": "785",
            "description": "publicación que la continúa",
            "t_description": "$t ($x)",
        }
        
    ], 
    "geo":[
        {
                "name": "otros_identificadores",
                "t": "024",
                "description": "identificadores del lugar en otros catálogos (viaf, lcnf, geonames, etc.)",
                "t_description": "$2: $a",
        },
        {
                "name": "coordenadas_lat_lng",
                "t": "034",
                "description": "coordenadas geográficas decimales (latitud, longitud)",
                "t_description": "$d $e",
        },
        {
                "name": "CDU",
                "t": "080",
                "description": "número de la Clasificación Decimal Universal (sistema de clasificación temática usado en bibliotecas) que representa el lugar",
                "t_description": "$a",
        },
        {
                "name": "nombre_de_lugar",
                "t": "151",
                "description": "nombre de lugrar",
                "t_description": "$a",
        },
        {
                "name": "otros_nombre_de_lugar",
                "t": "451",
                "description": "otros nombres por los que es conocido el lugar",
                "t_description": "$a",
        },
        {
                "name": "materia relacionada",
                "t": "550",
                "description": "término del catálogo de materias de la BNE relacionado con el lugar (p. ej., gentilicio del lugar)",
                "t_description": "$a",
        },
        {
                "name": "lugar_relacionado",
                "t": "551",
                "description": "otros lugares relacionados con el lugar",
                "t_description": "$a",
        },
        {
                "name": "nota_general",
                "t": "667",
                "description": "más nformación sobre el lugar",
                "t_description": "$a",
        },
        {
                "name": "fuentes_de_informacion",
                "t": "670",
                "description": "fuentes de información de las que se han obtenido los datos del lugar",
                "t_description": "$a: $b ($u)",
        },
        {
                "name": "lugar_jerarquico",
                "t": "781",
                "description": "nombre del lugar precedido de país, región y/o provincia a los que pertenece",
                "t_description": "$a",
        }
        ],
    "son":[
        {
                "name": "soporte",
                "t": "_1007",
                "description": "Soporte",
                "t_description": "[01]",
        },
        {
                "name": "velocidad",
                "t": "_2007",
                "description": "Velocidad de reproducción",
                "t_description": "[03]",
        },
        {
                "name": "canales",
                "t": "_3007",
                "description": "Configuración de los canales de reproducción",
                "t_description": "[04]",
        },
        {
                "name": "pais_de_publicacion",
                "t": "_1008",
                "description": "País de publicación",
                "t_description": "[15-17]",
        },
        {
                "name": "lengua_principal",
                "t": "_2008",
                "description": "Lengua del contenido principal del documento",
                "t_description": "[35-37]",
        },
        {
                "name": "lengua_libreto",
                "t": "_1041",
                "description": "Lengua del libreto",
                "t_description": "$e",
        },
        {
                "name": "otras_lenguas",
                "t": "_2041",
                "description": "Lenguas de otros contenidos (resúmenes, tablas de contenidos, notas, etc.)",
                "t_description": "$b, $d, $f, $j, $k",
        },
        {
                "name": "lengua_original",
                "t": "_3041",
                "description": "Lengua original de la que se ha traducido",
                "t_description": "$h",
        },
        {
                "name": "fecha_de_publicacion",
                "t": "_3008",
                "description": "Fecha de la publicación o de su primera entrega",
                "t_description": "[7-10]",
        },
        {
                "name": "decada_publicacion",
                "t": "_4008",
                "description": "Década de la publicación o de su primera entrega ",
                "t_description": "[7-10]",
        },
        {
                "name": "siglo_publicacion",
                "t": "_5008",
                "description": "Siglo de la publicación o de su primera entrega ",
                "t_description": "[7-10]",
        },
        {
                "name": "deposito_legal",
                "t": "_1017",
                "description": "Número de Depósito Legal",
                "t_description": "$a",
        },

        {
                "name": "cdu",
                "t": "_1080",
                "description": "Número de la Clasificación Decimal Universal que representa el tema tratado en la publicación",
                "t_description": "$a",
        },
        {
                "name": "responsables_e_interpretes",
                "t": "100, 110, 700, 710",
                "description": "Responsables del contenido e intérpretes",
                "t_description": "$a{$b$c}($d)($q)($e)",
        },
        {
                "name": "nombre_de_congreso",
                "t": "_1111",
                "description": "Nombre de congreso",
                "t_description": "$a, $n, $c, $d",
        },
        {
                "name": "titulo_normalizado",
                "t": "130, 240",
                "description": "Título de la publicación en forma normalizada",
                "t_description": "$a",
        },
        {
                "name": "titulo",
                "t": "_1245",
                "description": "Título de la publicación tal y como aparece citado en la misma ",
                "t_description": "$a:$b.$n,$p",
        },

        {
                "name": "otros_titulos",
                "t": "246, 740",
                "description": "Otros títulos de la obra que aparecen citados en la publicación",
                "t_description": "[$i]:$a:$b.$n,$p",
        },
        {
                "name": "edicion",
                "t": "_1250",
                "description": "Información sobre la edición",
                "t_description": "$a, $b",
        },
        {
                "name": "lugar_de_publicacion",
                "t": "260,264",
                "description": "Localidad específica en la que se ha publicado",
                "t_description": "$a",
        },
        
        {
                "name": "editorial",
                "t": "260, 264",
                "description": "Nombre del editor responsable de la publicación",
                "t_description": "[$i]:$a:$b.$n,$p",
        },
        {
                "name": "extension",
                "t": "_1300",
                "description": "Número de cintas, discos, etc., y duración",
                "t_description": "$a, $b",
        },
        {
                "name": "otras_caracteristicas_fisicas",
                "t": "_2300",
                "description": "sonido, color, etc.",
                "t_description": "$b",
        },
        {
                "name": "dimensiones",
                "t": "_3300",
                "description": "Medida del alto de la publicación (en cm)",
                "t_description": "$c",
        },
        {
                "name": "material_anejo",
                "t": "_4300",
                "description": "Material complementario que acompaña a la publicación principal",
                "t_description": "$e",
        },
        {
                "name": "caracteristicas_archivo_digital",
                "t": "_1347",
                "description": "Características del archivo digital",
                "t_description": "$a$b",
        },
        {
                "name": "sonido",
                "t": "_1344",
                "description": "Características del sonido",
                "t_description": "$a$b$c$d$g",
        },
        {
                "name": "medio_interpretaccion",
                "t": "_1382",
                "description": "Medio de interpretación",
                "t_description": "$a$b$p",
        },
        {
                "name": "equipo",
                "t": "_1508",
                "description": "Nombres y funciones del equipo de producción",
                "t_description": "$a",
        },
        {
                "name": "interpretes",
                "t": "_1511",
                "description": "Intérpretes y participantes",
                "t_description": "$a",
        },
        {
                "name": "fecha_lugar_grabacion",
                "t": "_1518",
                "description": "Información sobre la fecha y el lugar de la grabación",
                "t_description": "$a",
        },
        {
                "name": "contenido",
                "t": "_1505",
                "description": "Contenido de la publicación",
                "t_description": "$a",
        },
        {
                "name": "serie",
                "t": "440,490",
                "description": "Colección a la que pertenece la publicación",
                "t_description": "$a$v",
        },
        {
                "name": "tema",
                "t": "600,610,630,650,651,653",
                "description": "Materia sobre la que trata la publicación",
                "t_description": "Todos los subbcampos menos |2subcampos separados por guiones",
        },
        {
                "name": "genero_forma",
                "t": "_1655",
                "description": "Género al que pertenece la obra y forma que toma",
                "t_description": "Todos los subbcampos menos |2subcampos separados por guiones",
        }        
        ],
    "ele":[
        {
                "name": "pais_de_publicacion",
                "t": "_1008",
                "description": "País de publicación",
                "t_description": "[15-17]",
        },
        {
                "name": "lengua_principal",
                "t": "_2008",
                "description": "Lengua del contenido principal del documento",
                "t_description": "[35-37]",
        },
        {
                "name": "lengua_libreto",
                "t": "_1041",
                "description": "Lengua del libreto",
                "t_description": "$e",
        },
        {
                "name": "otras_lenguas",
                "t": "_2041",
                "description": "Lenguas de otros contenidos (resúmenes, tablas de contenidos, notas, etc.)",
                "t_description": "$b, $d, $f, $j, $k",
        },
        {
                "name": "lengua_original",
                "t": "_3041",
                "description": "Lengua original de la que se ha traducido",
                "t_description": "$h",
        },
        {
                "name": "fecha_de_publicacion",
                "t": "_3008",
                "description": "Fecha de la publicación o de su primera entrega",
                "t_description": "[7-10]",
        },
        {
                "name": "decada_publicacion",
                "t": "_4008",
                "description": "Década de la publicación o de su primera entrega ",
                "t_description": "[7-10]",
        },
        {
                "name": "siglo_publicacion",
                "t": "_5008",
                "description": "Siglo de la publicación o de su primera entrega ",
                "t_description": "[7-10]",
        },
        {
                "name": "deposito_legal",
                "t": "_1017",
                "description": "Número de Depósito Legal",
                "t_description": "$a",
        },

        {
                "name": "cdu",
                "t": "_1080",
                "description": "Número de la Clasificación Decimal Universal que representa el tema tratado en la publicación",
                "t_description": "$a",
        },
        {
                "name": "responsables_e_interpretes",
                "t": "100, 110, 700, 710",
                "description": "Responsables del contenido e intérpretes",
                "t_description": "$a{$b$c}($d)($q)($e)",
        },
        {
                "name": "nombre_de_congreso",
                "t": "_1111",
                "description": "Nombre de congreso",
                "t_description": "$a, $n, $c, $d",
        },
        {
                "name": "titulo_normalizado",
                "t": "130, 240",
                "description": "Título de la publicación en forma normalizada",
                "t_description": "$a",
        },
        {
                "name": "titulo",
                "t": "_1245",
                "description": "Título de la publicación tal y como aparece citado en la misma ",
                "t_description": "$a:$b.$n,$p",
        },

        {
                "name": "otros_titulos",
                "t": "246, 740",
                "description": "Otros títulos de la obra que aparecen citados en la publicación",
                "t_description": "[$i]:$a:$b.$n,$p",
        },
        {
                "name": "edicion",
                "t": "_1250",
                "description": "Información sobre la edición",
                "t_description": "$a, $b",
        },
        {
                "name": "lugar_de_publicacion",
                "t": "260,264",
                "description": "Localidad específica en la que se ha publicado",
                "t_description": "$a",
        },
        
        {
                "name": "editorial",
                "t": "260, 264",
                "description": "Nombre del editor responsable de la publicación",
                "t_description": "[$i]:$a:$b.$n,$p",
        },
        {
                "name": "extension",
                "t": "_1300",
                "description": "Número de cintas, discos, etc., y duración",
                "t_description": "$a, $b",
        },
        {
                "name": "otras_caracteristicas_fisicas",
                "t": "_2300",
                "description": "sonido, color, etc.",
                "t_description": "$b",
        },
        {
                "name": "dimensiones",
                "t": "_3300",
                "description": "Medida del alto de la publicación (en cm)",
                "t_description": "$c",
        },
        {
                "name": "material_anejo",
                "t": "_4300",
                "description": "Material complementario que acompaña a la publicación principal",
                "t_description": "$e",
        },
        {
                "name": "sonido",
                "t": "_1344",
                "description": "Características del sonido",
                "t_description": "$a$b$c$d$g",
        },
        {
                "name": "imagen_video",
                "t": "345,346",
                "description": "Características de imagen y vídeo",
                "t_description": "$a$b$c$d",
        },
        {
                "name": "equipo",
                "t": "_1508",
                "description": "Nombres y funciones del equipo de producción",
                "t_description": "$a",
        },
        {
                "name": "interpretes",
                "t": "_1511",
                "description": "Intérpretes y participantes",
                "t_description": "$a",
        },
        {
                "name": "fecha_lugar_grabacion",
                "t": "_1518",
                "description": "Información sobre la fecha y el lugar de la grabación",
                "t_description": "$a",
        },
        {
                "name": "resumen",
                "t": "_1520",
                "description": "Resumen del contenido",
                "t_description": "$a",
        },
        {
                "name": "publico",
                "t": "_1521",
                "description": "Público al que va destinada la publicación",
                "t_description": "$a",
        },
        {
                "name": "contenido",
                "t": "_1505",
                "description": "Contenido de la publicación",
                "t_description": "$a",
        },
        {
                "name": "serie",
                "t": "440,490",
                "description": "Colección a la que pertenece la publicación",
                "t_description": "$a$v",
        },
        {
                "name": "tema",
                "t": "600,610,630,650,651,653",
                "description": "Materia sobre la que trata la publicación",
                "t_description": "Todos los subbcampos menos |2subcampos separados por guiones",
        },
        {
                "name": "genero_forma",
                "t": "_1655",
                "description": "Género al que pertenece la obra y forma que toma",
                "t_description": "Todos los subbcampos menos |2subcampos separados por guiones",
        }        
        ],
    "gra":[
        {
                "name": "pais_de_publicacion",
                "t": "_1008",
                "description": "País de publicación",
                "t_description": "[15-17]",
        },
        {
                "name": "lengua_principal",
                "t": "_2008",
                "description": "Lengua del contenido principal del documento",
                "t_description": "[35-37]",
        },
        {
                "name": "lengua_libreto",
                "t": "_1041",
                "description": "Lengua del libreto",
                "t_description": "$e",
        },
        {
                "name": "otras_lenguas",
                "t": "_2041",
                "description": "Lenguas de otros contenidos (resúmenes, tablas de contenidos, notas, etc.)",
                "t_description": "$b, $d, $f, $j, $k",
        },
        {
                "name": "lengua_original",
                "t": "_3041",
                "description": "Lengua original de la que se ha traducido",
                "t_description": "$h",
        },
        {
                "name": "fecha_de_publicacion",
                "t": "_3008",
                "description": "Fecha de la publicación o de su primera entrega",
                "t_description": "[7-10]",
        },
        {
                "name": "decada_publicacion",
                "t": "_4008",
                "description": "Década de la publicación o de su primera entrega ",
                "t_description": "[7-10]",
        },
        {
                "name": "siglo_publicacion",
                "t": "_5008",
                "description": "Siglo de la publicación o de su primera entrega ",
                "t_description": "[7-10]",
        },
        {
                "name": "deposito_legal",
                "t": "_1017",
                "description": "Número de Depósito Legal",
                "t_description": "$a",
        },

        {
                "name": "cdu",
                "t": "_1080",
                "description": "Número de la Clasificación Decimal Universal que representa el tema tratado en la publicación",
                "t_description": "$a",
        },
        {
                "name": "responsables_e_interpretes",
                "t": "100, 110, 700, 710",
                "description": "Responsables del contenido e intérpretes",
                "t_description": "$a{$b$c}($d)($q)($e)",
        },
        {
                "name": "nombre_de_congreso",
                "t": "_1111",
                "description": "Nombre de congreso",
                "t_description": "$a, $n, $c, $d",
        },
        {
                "name": "titulo_normalizado",
                "t": "130, 240",
                "description": "Título de la publicación en forma normalizada",
                "t_description": "$a",
        },
        {
                "name": "titulo",
                "t": "_1245",
                "description": "Título de la publicación tal y como aparece citado en la misma ",
                "t_description": "$a:$b.$n,$p",
        },

        {
                "name": "otros_titulos",
                "t": "246, 740",
                "description": "Otros títulos de la obra que aparecen citados en la publicación",
                "t_description": "[$i]:$a:$b.$n,$p",
        },
        {
                "name": "edicion",
                "t": "_1250",
                "description": "Información sobre la edición",
                "t_description": "$a, $b",
        },
        {
                "name": "lugar_de_publicacion",
                "t": "260,264",
                "description": "Localidad específica en la que se ha publicado",
                "t_description": "$a",
        },
        
        {
                "name": "editorial",
                "t": "260, 264",
                "description": "Nombre del editor responsable de la publicación",
                "t_description": "[$i]:$a:$b.$n,$p",
        },
        {
                "name": "extension",
                "t": "_1300",
                "description": "Número de cintas, discos, etc., y duración",
                "t_description": "$a, $b",
        },
        {
                "name": "otras_caracteristicas_fisicas",
                "t": "_2300",
                "description": "sonido, color, etc.",
                "t_description": "$b",
        },
        {
                "name": "dimensiones",
                "t": "_3300",
                "description": "Medida del alto de la publicación (en cm)",
                "t_description": "$c",
        },
        {
                "name": "material_anejo",
                "t": "_4300",
                "description": "Material complementario que acompaña a la publicación principal",
                "t_description": "$e",
        },
        {
                "name": "sonido",
                "t": "_1344",
                "description": "Características del sonido",
                "t_description": "$a$b$c$d$g",
        },
        {
                "name": "imagen_video",
                "t": "345,346",
                "description": "Características de imagen y vídeo",
                "t_description": "$a$b$c$d",
        },
        {
                "name": "equipo",
                "t": "_1508",
                "description": "Nombres y funciones del equipo de producción",
                "t_description": "$a",
        },
        {
                "name": "interpretes",
                "t": "_1511",
                "description": "Intérpretes y participantes",
                "t_description": "$a",
        },
        {
                "name": "fecha_lugar_grabacion",
                "t": "_1518",
                "description": "Información sobre la fecha y el lugar de la grabación",
                "t_description": "$a",
        },
        {
                "name": "resumen",
                "t": "_1520",
                "description": "Resumen del contenido",
                "t_description": "$a",
        },
        {
                "name": "publico",
                "t": "_1521",
                "description": "Público al que va destinada la publicación",
                "t_description": "$a",
        },
        {
                "name": "contenido",
                "t": "_1505",
                "description": "Contenido de la publicación",
                "t_description": "$a",
        },
        {
                "name": "serie",
                "t": "440,490",
                "description": "Colección a la que pertenece la publicación",
                "t_description": "$a$v",
        },
        {
                "name": "tema",
                "t": "600,610,630,650,651,653",
                "description": "Materia sobre la que trata la publicación",
                "t_description": "Todos los subbcampos menos |2subcampos separados por guiones",
        },
        {
                "name": "genero_forma",
                "t": "_1655",
                "description": "Género al que pertenece la obra y forma que toma",
                "t_description": "Todos los subbcampos menos |2subcampos separados por guiones",
        }        
        ],
    "par": [
        {
                "name": "pais_de_publicacion",
                "t": "_1008",
                "description": "País de publicación",
                "t_description": "[15-17]",
        },
        {
                "name": "lengua_principal",
                "t": "_2008",
                "description": "Lengua del contenido principal del documento",
                "t_description": "[35-37]",
        },
        {
                "name": "lengua_libreto",
                "t": "_1041",
                "description": "Lengua del libreto",
                "t_description": "$e",
        },
        {
                "name": "otras_lenguas",
                "t": "_2041",
                "description": "Lenguas de otros contenidos (resúmenes, tablas de contenidos, notas, etc.)",
                "t_description": "$b, $d, $f, $j, $k",
        },
        {
                "name": "lengua_original",
                "t": "_3041",
                "description": "Lengua original de la que se ha traducido",
                "t_description": "$h",
        },
        {
                "name": "fecha_de_publicacion",
                "t": "_3008",
                "description": "Fecha de la publicación o de su primera entrega",
                "t_description": "[7-10]",
        },
        {
                "name": "decada_publicacion",
                "t": "_4008",
                "description": "Década de la publicación o de su primera entrega ",
                "t_description": "[7-10]",
        },
        {
                "name": "siglo_publicacion",
                "t": "_5008",
                "description": "Siglo de la publicación o de su primera entrega ",
                "t_description": "[7-10]",
        },
        {
                "name": "deposito_legal",
                "t": "_1017",
                "description": "Número de Depósito Legal",
                "t_description": "$a",
        },

        {
                "name": "cdu",
                "t": "_1080",
                "description": "Número de la Clasificación Decimal Universal que representa el tema tratado en la publicación",
                "t_description": "$a",
        },
        {
                "name": "responsables_e_interpretes",
                "t": "100, 110, 700, 710",
                "description": "Responsables del contenido e intérpretes",
                "t_description": "$a{$b$c}($d)($q)($e)",
        },
        {
                "name": "nombre_de_congreso",
                "t": "_1111",
                "description": "Nombre de congreso",
                "t_description": "$a, $n, $c, $d",
        },
        {
                "name": "titulo_normalizado",
                "t": "130, 240",
                "description": "Título de la publicación en forma normalizada",
                "t_description": "$a",
        },
        {
                "name": "titulo",
                "t": "_1245",
                "description": "Título de la publicación tal y como aparece citado en la misma ",
                "t_description": "$a:$b.$n,$p",
        },

        {
                "name": "otros_titulos",
                "t": "246, 740",
                "description": "Otros títulos de la obra que aparecen citados en la publicación",
                "t_description": "[$i]:$a:$b.$n,$p",
        },
        {
                "name": "edicion",
                "t": "_1250",
                "description": "Información sobre la edición",
                "t_description": "$a, $b",
        },
        {
                "name": "lugar_de_publicacion",
                "t": "260,264",
                "description": "Localidad específica en la que se ha publicado",
                "t_description": "$a",
        },
        
        {
                "name": "editorial",
                "t": "260, 264",
                "description": "Nombre del editor responsable de la publicación",
                "t_description": "[$i]:$a:$b.$n,$p",
        },
        {
                "name": "extension",
                "t": "_1300",
                "description": "Número de cintas, discos, etc., y duración",
                "t_description": "$a, $b",
        },
        {
                "name": "otras_caracteristicas_fisicas",
                "t": "_2300",
                "description": "sonido, color, etc.",
                "t_description": "$b",
        },
        {
                "name": "dimensiones",
                "t": "_3300",
                "description": "Medida del alto de la publicación (en cm)",
                "t_description": "$c",
        },
        {
                "name": "material_anejo",
                "t": "_4300",
                "description": "Material complementario que acompaña a la publicación principal",
                "t_description": "$e",
        },
        {
                "name": "sonido",
                "t": "_1344",
                "description": "Características del sonido",
                "t_description": "$a$b$c$d$g",
        },
        {
                "name": "equipo",
                "t": "_1508",
                "description": "Nombres y funciones del equipo de producción",
                "t_description": "$a",
        },
        {
                "name": "interpretes",
                "t": "_1511",
                "description": "Intérpretes y participantes",
                "t_description": "$a",
        },
        {
                "name": "fecha_lugar_grabacion",
                "t": "_1518",
                "description": "Información sobre la fecha y el lugar de la grabación",
                "t_description": "$a",
        },
        {
                "name": "resumen",
                "t": "_1520",
                "description": "Resumen del contenido",
                "t_description": "$a",
        },
        {
                "name": "publico",
                "t": "_1521",
                "description": "Público al que va destinada la publicación",
                "t_description": "$a",
        },
        {
                "name": "contenido",
                "t": "_1505",
                "description": "Contenido de la publicación",
                "t_description": "$a",
        },
        {
                "name": "serie",
                "t": "440,490",
                "description": "Colección a la que pertenece la publicación",
                "t_description": "$a$v",
        },
        {
                "name": "tema",
                "t": "600,610,630,650,651,653",
                "description": "Materia sobre la que trata la publicación",
                "t_description": "Todos los subbcampos menos |2subcampos separados por guiones",
        },
        {
                "name": "genero_forma",
                "t": "_1655",
                "description": "Género al que pertenece la obra y forma que toma",
                "t_description": "Todos los subbcampos menos |2subcampos separados por guiones",
        }        
        ],
    "vid":[
        {
                "name": "pais_de_publicacion",
                "t": "_1008",
                "description": "País de publicación",
                "t_description": "[15-17]",
        },
        {
                "name": "lengua_principal",
                "t": "_2008",
                "description": "Lengua del contenido principal del documento",
                "t_description": "[35-37]",
        },
        {
                "name": "lengua_subtitulos",
                "t": "_1041",
                "description": "Lenguaje de los subtítulos disponibles",
                "t_description": "$j",
        },
        {
                "name": "otras_lenguas",
                "t": "_2041",
                "description": "Lenguas de otros contenidos (resúmenes, tablas de contenidos, notas, etc.)",
                "t_description": "$b, $d, $f, $j, $k",
        },
        {
                "name": "lengua_original",
                "t": "_3041",
                "description": "Lengua original de la que se ha traducido",
                "t_description": "$h",
        },
        {
                "name": "soporte",
                "t": "_1007",
                "description": "Soporte de la videograbación",
                "t_description": "[01]",
        },
        {
                "name": "color",
                "t": "_2007",
                "description": "Tipo de color o ausencia de la videograbación",
                "t_description": "[03]",
        },
        {
                "name": "sonido",
                "t": "_3007",
                "description": "Sonido de la distribución",
                "t_description": "[05]",
        },
        {
                "name": "fecha_de_publicacion",
                "t": "_3008",
                "description": "Fecha de la publicación o de su primera entrega",
                "t_description": "[7-10]",
        },
        {
                "name": "decada_publicacion",
                "t": "_4008",
                "description": "Década de la publicación o de su primera entrega ",
                "t_description": "[7-10]",
        },
        {
                "name": "siglo_publicacion",
                "t": "_5008",
                "description": "Siglo de la publicación o de su primera entrega ",
                "t_description": "[7-10]",
        },
        {
                "name": "deposito_legal",
                "t": "_1017",
                "description": "Número de Depósito Legal",
                "t_description": "$a",
        },

        {
                "name": "cdu",
                "t": "_1080",
                "description": "Número de la Clasificación Decimal Universal que representa el tema tratado en la publicación",
                "t_description": "$a",
        },
        {
                "name": "responsables_e_interpretes",
                "t": "100, 110, 700, 710",
                "description": "Responsables del contenido e intérpretes",
                "t_description": "$a{$b$c}($d)($q)($e)",
        },
        {
                "name": "titulo_normalizado",
                "t": "130, 240",
                "description": "Título de la publicación en forma normalizada",
                "t_description": "$a",
        },
        {
                "name": "titulo",
                "t": "_1245",
                "description": "Título de la publicación tal y como aparece citado en la misma ",
                "t_description": "$a:$b.$n,$p",
        },

        {
                "name": "otros_titulos",
                "t": "246, 740",
                "description": "Otros títulos de la obra que aparecen citados en la publicación",
                "t_description": "[$i]:$a:$b.$n,$p",
        },
        {
                "name": "lugar_de_publicacion",
                "t": "260,264",
                "description": "Localidad específica en la que se ha publicado",
                "t_description": "$a",
        },
        
        {
                "name": "editorial",
                "t": "260, 264",
                "description": "Nombre del editor responsable de la publicación",
                "t_description": "[$i]:$a:$b.$n,$p",
        },
        {
                "name": "extension",
                "t": "_1300",
                "description": "Número de cintas, discos, etc., y duración",
                "t_description": "$a, $b",
        },
        {
                "name": "otras_caracteristicas_fisicas",
                "t": "_2300",
                "description": "sonido, color, etc.",
                "t_description": "$b",
        },
        {
                "name": "dimensiones",
                "t": "_3300",
                "description": "Medida del alto de la publicación (en cm)",
                "t_description": "$c",
        },
        {
                "name": "material_anejo",
                "t": "_4300",
                "description": "Material complementario que acompaña a la publicación principal",
                "t_description": "$e",
        },
        {
                "name": "sonido",
                "t": "_1344",
                "description": "Características del sonido",
                "t_description": "$a$b$c$d$g",
        },
        {
                "name": "imagen_video",
                "t": "345,346",
                "description": "Características de imagen y vídeo",
                "t_description": "$a$b$c$d",
        },
        {
                "name": "equipo",
                "t": "_1508",
                "description": "Nombres y funciones del equipo de producción",
                "t_description": "$a",
        },
        {
                "name": "interpretes",
                "t": "_1511",
                "description": "Intérpretes y participantes",
                "t_description": "$a",
        },
        {
                "name": "fecha_lugar_grabacion",
                "t": "_1518",
                "description": "Información sobre la fecha y el lugar de la grabación",
                "t_description": "$a",
        },
        {
                "name": "resumen",
                "t": "_1520",
                "description": "Resumen del contenido",
                "t_description": "$a",
        },
        {
                "name": "publico",
                "t": "_1521",
                "description": "Público al que va destinada la publicación",
                "t_description": "$a",
        },
        {
                "name": "contenido",
                "t": "_1505",
                "description": "Contenido de la publicación",
                "t_description": "$a",
        },
        {
                "name": "serie",
                "t": "440,490",
                "description": "Colección a la que pertenece la publicación",
                "t_description": "$a$v",
        },
        {
                "name": "tema",
                "t": "600,610,630,650,651,653",
                "description": "Materia sobre la que trata la publicación",
                "t_description": "Todos los subbcampos menos |2subcampos separados por guiones",
        },
        {
                "name": "genero_forma",
                "t": "_1655",
                "description": "Género al que pertenece la obra y forma que toma",
                "t_description": "Todos los subbcampos menos |2subcampos separados por guiones",
        }        
        ]

}

if __name__ == "__main__":
    geo = fields["moa"]
    a = dict(zip((d["name"] for d in geo), (d["description"] for d in geo)))
    print(a)