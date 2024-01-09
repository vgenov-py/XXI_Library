const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
console.log("Código desarrollado por Vito Genovese para la BNE, visita https://infofortis.com")
const datasets = ["per", "mon", "moa", "ent", "ser", "mss", "geo"]
new bootstrap.Tooltip(document.body, {selector:".tooltip_bne"});
const tooltips = {
    per: {"id": "identificador de la persona en el catálogo de la BNE", "otros_identificadores": "identificadores de la persona en otros catálogos (viaf, lcnf, isni, etc.)", "fecha_nacimiento": "fecha de nacimiento de la persona", "fecha_muerte": "fecha de muerte de la persona", "nombre_de_persona": "", "otros_atributos_persona": "título, cargo, etc. ", "lugar_nacimiento": "país, región, provincia y localidad donde ha nacido la persona", "lugar_muerte": "país, región, provincia y localidad donde ha fallecido la persona", "pais_relacionado": "otro país relacionado con la persona", "otros_lugares_relacionados": "otros lugares relacionados con la persona", "lugar_residencia": "lugar de residencia de la persona, si es especialmente significativo", "campo_actividad": "disciplina o actividad a la que se dedica la persona", "grupo_o_entidad_relacionada": "grupo, organismo, etc., a la que pertenece la persona", "ocupacion": "profesión desempeñada por la persona", "genero": "género de la persona (masculino, femenino u otros)", "lengua": "lengua en la que la persona escribe la mayor parte de su obra", "otros_nombres": "otros nombres por los que es conocida la persona", "persona_relacionada": "otras personas relacionadas con la persona", "nota_general": "más información sobre la persona", "fuentes_de_informacion": "fuentes de información de las que se han obtenido los datos de la persona", "otros_datos_biograficos": "otra información biográfica de la persona", "obras_relacionadas_en_el_catalogo_BNE": "obras relacionadas con la persona que se pueden encontrar en el catálogo de la BNE", "nombre_de_persona": "nombre de persona"},
    geo: {"id": "identificador del geográfico en el catálogo de la BNE",'otros_identificadores': 'identificadores del lugar en otros catálogos (viaf, lcnf, geonames, etc.)', 'coordenadas_lat_lng': 'coordenadas geográficas decimales (latitud, longitud)', 'CDU': 'número de la Clasificación Decimal Universal (sistema de clasificación temática usado en bibliotecas) que representa el lugar', 'nombre_de_lugar': 'nombre de lugrar', 'otros_nombres_de_lugar': 'otros nombres por los que es conocido el lugar', 'materia relacionada': 'término del catálogo de materias de la BNE relacionado con el lugar (p. ej., gentilicio del lugar)', 'lugar_relacionado': 'otros lugares relacionados con el lugar', 'nota_general': 'más nformación sobre el lugar', 'fuentes_de_informacion': 'fuentes de información de las que se han obtenido los datos del lugar', 'lugar_jerarquico': 'nombre del lugar precedido de país, región y/o provincia a los que pertenece'},
    mon: {
        "id": "Identificador de la monografía en el catálogo de la BNE", "pais_de_publicacion":"País donde se ha publicado la monografía",
        "lengua_principal":"Lengua del contenido principal del documento","otras_lenguas":"Lenguas de otros contenidos (resúmenes, tablas de contenidos, notas, etc.)",
        "lengua_original":"Lengua original de la que se ha traducido","fecha_de_publicacion":"Fecha en que se publicó la monografía o su primera entrega en caso de una monografía en varias partes",
        "decada":"Década en la que se publicó la monografía o su primera entrega en caso de una monografía en varias partes","siglo":"Siglo en el  que se publicó la monografía o su primera entrega en caso de una monografía en varias partes",
        "deposito_legal":"Número de Depósito Legal","ISBN":"International Standard Book Number","NIPO":"Número de Identificación de Publicaciones Oficiales",
        "CDU":"Número de la Clasificación Decimal Universalque representa el tema tratado en la monografía", "autores":"responsables del contenido intelectual de la monografía",
        "titulo":"Título de la obra tal y como aparece citado en la monografía", "mencion_de_autores":"Responsables del contenido intelectual tal y como aparecen citados en la monografía",
        "otros_titulos":"Otros títulos de la obra que aparecen citados en la monografía","edicion":"Información sobre la edición",
        "lugar_de_publicacion":"Localidad específica en la que se ha publicado la monografía", "editorial":"Nombre del editor responsable de la publicación de la monografía",
        "extension":"Número de volúmenes, páginas, hojas, columnas, etc.", "otras_caracteristicas_fisicas":"ilustraciones, color, etc.","dimensiones":"Medida del alto de la publicación (en cm)",
        "material_anejo":"Material complementario que acompaña a la publicación principal","serie":"Colección a la que pertenece la monografía","nota_de_contenido":"Más información sobre el contenido de la obra",
        "notas":"Más información sobre la monografía","procedencia":"Nombre del último propietario del ejemplar antes de pasar a la BNE","premios":"Premios con los que ha sido galardonada la obra","tema":"Materia sobre la que trata la monografía",
        "genero_forma":"Género al que pertenece la obra y forma que toma"},
    ser: {'id': 'identificador de la publicación en el catálogo de la BNE', 'pais_de_publicacion': 'país de publicación ', 'lengua_principal': 'lengua del contenido principal del documento', 'otras_lenguas': 'lenguas de otros contenidos (resúmenes, tablas de contenidos, notas, etc.)', 'lengua_original': 'lengua original de la que se ha traducido', 'fecha_de_publicacion': 'Fecha de la publicación o de su primera entrega ', 'decada': 'Década de la publicación o de su primera entrega ', 'siglo': 'Siglo de la publicación o de su primera entrega ', 'deposito_legal': 'número de Depósito Legal', 'ISSN': 'International Standard Serial Number', 'NIPO': 'Número de Identificación de Publicaciones Oficiales', 'CDU': 'número de la Clasificación Decimal Universalque representa el tema tratado en la publicación', 'autores': 'responsables del contenido intelectual de la publicación', 'titulo_clave': 'título de la publicacion que se asigna junto con el ISSN ', 'titulo': 'título de la publicación tal y como aparece citado en la misma ', 'mencion_de_autores': 'responsables del contenido intelectual tal y como aparecen citados en la publicación', 'otros_titulos': 'otros títulos de la obra que aparecen citados en la publicación', 'lugar_de_publicacion': 'localidad específica en la que se ha publicado ', 'editorial': 'nombre del editor responsable de la publicación ', 'extension': 'número de volúmenes, páginas, hojas, columnas, etc.', 'otras_caracteristicas_fisicas': 'ilustraciones, color, etc.', 'dimensiones': 'medida del alto de la publicación (en cm)', 'material_anejo': 'material complementario que acompaña a la publicación principal', 'periodicidad': 'periodicidad (actual) de la publicación', 'fechas_y_numeracion': 'fechas de publicación y secuencia de números o fascículos', 'serie': 'colección a la que pertenece la publicación', 'nota_de_contenido': 'más información sobre el contenido de la obra', 'notas': 'más información sobre la publicación', 'procedencia': 'nombre del último propietario del ejemplar antes de pasar a la BNE', 'premios': 'premios con los que ha sido galardonada la publicación', 'tema': 'materia sobre la que trata la publicación', 'genero_forma': 'género al que pertenece la obra y forma que toma'},
    mss: {'id': 'identificador de la obra en el catálogo de la BNE', 'pais_de_publicacion': 'país de producción', 'lengua_principal': 'lengua del contenido principal del documento', 'otras_lenguas': 'lenguas de otros contenidos (resúmenes, tablas de contenidos, notas, etc.)', 'lengua_original': 'lengua original de la que se ha traducido', 'fecha_de_publicacion': 'Fecha de la producción de la obra ', 'decada': 'Década de la producción de la obra ', 'siglo': 'Siglo de la producción de la obra ', 'deposito_legal': 'número de Depósito Legal', 'CDU': 'número de la Clasificación Decimal Universal que representa el tema tratado en la publicación', 'autores': 'responsables del contenido intelectual de la obra', 'titulo': 'título de la obra tal y como aparece citado en la misma ', 'mencion_de_autores': 'responsables del contenido intelectual tal y como aparecen citados en la obra', 'otros_titulos': 'otros títulos de la obra que aparecen citados en la obra', 'lugar_de_producción': 'localidad específica en la que se ha producido la obra', 'extension': 'número de volúmenes, páginas, hojas, columnas, etc.', 'otras_caracteristicas_fisicas': 'ilustraciones, color, etc.', 'dimensiones': 'medida del alto del documento (en cm)', 'material_anejo': 'material complementario que acompaña a la obra principal', 'serie': 'colección a la que pertenece la obra', 'nota_de_contenido': 'más información sobre el contenido de la obra', 'notas': 'más información sobre la obra', 'procedencia': 'nombre del último propietario del ejemplar antes de pasar a la BNE', 'premios': 'premios con los que ha sido galardonada la obra', 'incipit/explicit': 'inicio/fin (íncipit/explicit y primeros versos)', 'tema': 'materia sobre la que trata la obra', 'genero_forma': 'género al que pertenece la obra y forma que toma'},
    ent: {'id': 'identificador de la obra en el catálogo de la BNE','otros_identificadores': 'Identificadores de la entidad en otros catálogos (viaf, lcnf, isni, etc.)', 'fecha_establecimiento': 'Fecha de creación o inicio de actividad de la entidad', 'fecha_finalizacion': 'Fecha de desapaprición o cese de actividad de la entidad', 'nombre_de_entidad': 'Nombre de la entidad corporativa', 'tipo_entidad': 'tipo de entidad corporativa', 'pais': 'País relacionado con la entidad', 'sede': 'Lugar donde se encuentra la sede de la entidad, si es especialmente significativo', 'campo_actividad': 'Disciplina o actividad a la que se dedica la entidad', 'lengua': 'Lengua en la que la entidad suele publicar', 'otros_nombres': 'Otros nombres por los que es conocida la entidad', 'persona_relacionada': 'Personas relacionadas con la entidad', 'grupo_o_entidad_relacionada': 'Grupo, organismo, etc., relacionado con la entidad', 'nota_de_relacion': 'Otras relaciones de la entidad con personas, otras entidades, etc.', 'otros_datos_historicos': 'Otra información histórica de la entidad', 'nota_general': 'Más información sobre la entidad', 'fuentes_de_informacion': 'Fuentes de información de las que se han obtenido los datos de la entidad'},
    moa: {'id': 'Identificador de la monografía en el catálogo de la BNE','pais_de_publicacion': 'país donde se ha publicado la monografía', 'lengua_principal': 'lengua del contenido principal del documento', 'otras_lenguas': 'lenguas de otros contenidos (resúmenes, tablas de contenidos, notas, etc.)', 'lengua_original': 'lengua original de la que se ha traducido', 'fecha_de_publicacion': 'Fecha en que se publicó la monografía o su primera entrega en caso de una monografía en varias partes', 'decada': 'Década en la que se publicó la monografía o su primera entrega en caso de una monografía en varias partes', 'siglo': 'Siglo en el  que se publicó la monografía o su primera entrega en caso de una monografía en varias partes', 'CDU': 'número de la Clasificación Decimal Universalque representa el tema tratado en la monografía', 'autores': 'responsables del contenido intelectual de la monografía', 'titulo': 'titulo de la obra tal y como aparece citado en la monografía', 'mencion_de_autores': 'responsables del contenido intelectual tal y como aparecen citados en la monografía', 'otros_titulos': 'otros títulos de la obra que aparecen citados en la monografía', 'edicion': 'información sobre la edición', 'lugar_de_publicacion': 'localidad específica en la que se ha publicado y/o impreso la monografía', 'editor_impresor': 'nombre del editor y/o impresor responsable de la publicación de la monografía', 'extension': 'número de volúmenes, páginas, hojas, columnas, etc.', 'otras_caracteristicas_fisicas': 'ilustraciones, color, etc.', 'dimensiones': 'medida del alto de la publicación (en cm)', 'material_anejo': 'material complementario que acompaña a la publicación principal', 'serie': 'colección a la que pertenece la monografía', 'nota_de_contenido': 'más información sobre el contenido de la obra', 'notas': 'más información sobre la monografía', 'transcripcion_incipit_explicit': 'transcripciones del principio y/o el final del texto de la monografía', 'procedencia': 'nombre del último propietario del ejemplar antes de pasar a la BNE', 'cita': 'citas o referencias de descripciones bibliográficas, reseñas, resúmenes o índices de la monografía en diferentes repertorios', 'tema': 'materia sobre la que trata la monografía', 'genero_forma': 'género al que pertenece la obra y forma que toma', 'lugar_relacionado': 'lugar relacionado con la monografía, en formato normalizado', 'url': 'url de la digitalización o de un recurso digital relacionado'},
    vid: {'id': 'Identificador de la publicación en el catálogo de la BNE', 'pais_de_publicacion': 'País de publicación ', 'lengua_principal': 'Lengua del contenido principal del documento', 'lengua_subtitulos': 'Subtítulos de la obra', 'otras_lenguas': 'Lenguas de otros contenidos (resúmenes, tablas de contenidos, notas, etc.)', 'lengua_original': 'Lengua original de la que se ha traducido', 'soporte': 'Formato de distribución', 'color': 'Color prevalente del recurso', 'sonido': 'Sonido', 'fecha_de_publicacion': 'Fecha de la publicación o de su primera entrega', 'decada_publicacion': 'Década de la publicación o de su primera entrega', 'siglo_publicacion': 'Siglo de la publicación o de su primera entrega', 'deposito_legal': 'número de Depósito Legal', 'isbn': 'ISBN', 'otros_identificadores': 'Otros identificadores de la publicación (EAN, ISAN, número de productor, etc.)', 'cdu': 'Número de la Clasificación Decimal Universalque representa el tema tratado en la publicación', 'responsables_e_interpretes': 'Responsables del contenido e intérpretes', 'titulo_normalizado': 'Título de la publicación en forma normalizada', 'titulo': 'Título de la publicación tal y como aparece citado en la misma ', 'otros_titulos': 'Otros títulos de la obra que aparecen citados en la publicación', 'edicion': 'Información sobre la edición', 'lugar_de_publicacion': 'Localidad específica en la que se ha publicado ', 'editorial': 'Nombre del editor responsable de la publicación ', 'extension': 'Número de cintas, discos, etc., y duración', 'otras_caracteristicas_fisicas': 'Sonido, color, etc.', 'dimensiones': 'Medida del alto de la publicación (en cm)', 'material_anejo': 'Material complementario que acompaña a la publicación principal', 'tipo_de_medio': 'Tipo de medio', 'tipo_de_soporte': 'Tipo de soporte', 'sonido_vid': 'Características de sonido', 'imagen_video': 'Características de imagen y vídeo', 'equipo': 'Nombres y funciones del equipo de producción', 'interpretes': 'Intérpretes y participantes', 'fecha_lugar_de_grabacion': 'Información sobre la fecha y el lugar de rodaje', 'resumen': 'Resumen del contenido', 'publico': 'Público al que va destinada la publicación', 'contenido': 'Contenido de la publicación', 'serie': 'colección a la que pertenece la publicación', 'notas': 'Más información sobre la publicación', 'tema': 'Materia sobre la que trata la publicación', 'genero_forma': 'Vito', 'url': 'url'}
};

const base_url = config.base_url;

let fields;

const get_fields = (view="") => {
    const dataset = document.querySelector("#dataset_value").value;
    const input_fields = JSON.parse(document.querySelector("#fields").value);
    fields = input_fields[dataset];
    document.querySelector("#dataset").value = dataset;
};
let view = document.querySelector("#view").value;
// get_fields(document.querySelector("#view").value);

const reset_and_ors = () => {
    [...document.querySelectorAll(".bne_and_or")].forEach((and_or) => {
        and_or.getElementsByTagName("input")[0].checked = false;
    });
};
const get_fields_2 = () => {
    view = document.querySelector("#view").value;
    const dataset = document.querySelector("#dataset").value;
    const input_fields = JSON.parse(document.querySelector("#fields").value)[dataset];
    let result = [];
    if (view == "human") {
        for (let field of input_fields) {
            if (!field.startsWith("t_")) {
                result.push(field);
            };
        };
    } else if (view == "marc") {
        for (let field of input_fields) {
            if (field.startsWith("t_")) {
                result.push(field);
            };
        };
    } else {
        result = input_fields;
    };
    return result;
};


reset_and_ors();

const add_filter = () => {
    const filter_html = `
    <div class="d-flex flex-row border-1 border mb-4 justify-content-center align-items-center bne_and_or" style="width: 120px;height: 30px;" id="bne_and_or_1">
        <span class="text-primary">Y&nbsp&nbsp</span>
            <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault" onclick="and_or_switch(this)">
            </div>
            <span class="">O</span>
    </div>
    <div class="container-sm border border-1 d-flex align-items-center my-4  position-relative" style="height:75px">
        <div class="input-group b_filter_group" style="height: 50px;">
            <input  type="text" class="form-control k" placeholder="Nombre, fecha de nacimiento..." onkeydown="show_ul(this)">
            <select class="form-select" aria-label="Default select example">
                <option selected onclick="set_value(this)">con valor</option>
                <option onclick="without_value(this)">sin valor</option>
                <option value="3" onclick="regardless_value(this)">sin importar valor</option>
              </select>
            <input  type="text" class="form-control v" placeholder="Valor">
            <div class="d-flex align-items-center">
            <button class="btn" onclick="trash_filter(this)">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                    <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                    <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                </svg>
            </button>
            </div>
        </div>
    </div>
`

    const container = document.querySelector("#filter_container");
    const filter_div = document.createElement("div");
    filter_div.innerHTML = filter_html;
    filter_div.className = "filter_div";
    container.appendChild(filter_div);
    return filter_div;
};


const populate_filters = () => {
    const get_args = _ =>
        [...new URLSearchParams(window.location.href.split('?')[1])].reduce(
            (a, [k, v]) => ((a[k] = v), a),
            {}
        );
    let args = get_args();
        const view_i = Object.keys(args).indexOf("view");
        console.log(Object.values(args).at(view_i))
        document.querySelector("#view").value =  ["marc", "human"].indexOf(Object.values(args).at(view_i))  >= 0? Object.values(args).at(view_i): "";
        
        delete args.view;
    if (!args) {
        return;
    };
    Object.entries(args).forEach((arg, i) => {
        [k,v] = arg;
        if (i > 1) add_filter();
    });
    Object.entries(args).forEach((arg, i) => {
        [k,v] = arg;
        if (k === "dataset") {
            document.querySelector("#dataset").value = v;
        } else {
            const filter = [...document.querySelectorAll(".filter_div")].at(i-1);
            const inputs = Array(...filter.getElementsByTagName("input"));
            inputs[1].value = k;
            inputs[2].value = v;    
        };
    });
};
// populate_filters();
const show_filters = () => {
    let result = "";
    const kvs = {};
    keys_or = [];
    const keys = Array(...document.getElementsByClassName("k"));
    const values = Array(...document.getElementsByClassName("v"));
    

    for (let i = 0; i < keys.length; i++) {
        let key = keys.at(i);
        let value = values.at(i).value;
        // let and_or_switch = key.parentElement.parentElement.parentElement.getElementsByClassName("bne_and_or")[0].getElementsByTagName("input")[0];
        key = key.value;
        

        if (kvs[key]) {
            kvs[key] += `||${value}`;
        } else {
            kvs[key] = value;
        };
    };
    for ([k,v] of Object.entries(kvs)) {
        if (v) {
            result += `${k}=${v}&`;
        };
    };
    return result.substring(0,result.length -1);
};
const trash_filter = (button) => {
    const div_filter = button.parentElement.parentElement.parentElement.parentElement;
    div_filter.remove();
};

let query;
let headers;
let url;
// const get_headers = async () => {
//     const dataset = document.querySelector("#dataset").value;
//     const view = document.querySelector("#view").value;
//     let url = `${base_url}/fields/${dataset}`;
//     if (view) {
//         url += `?view=${view}`;
//     };
//     const res = await fetch(url);
//     const data = await res.json();
//     if (data.fields) {
//         console.log(data.fields);
//         headers = data.fields;
//     };

// };


const get_headers = () => {
    view = document.querySelector("#view").value;
    const dataset = document.querySelector("#dataset").value;
    const input_fields = JSON.parse(document.querySelector("#fields").value)[dataset];
    if (view == "human") {
        fields = [];
        for (let field of input_fields) {
            if (!field.startsWith("t_")) {
                fields.push(field);
            };
        };
    } else if (view == "marc") {
        fields = [];
        for (let field of input_fields) {
            if (field.startsWith("t_")) {
                fields.push(field);
            };
        };
    } else {
        fields = input_fields;
    };
    headers = fields;
};

get_headers();
const get_data = (download=false, selected_fields=false) => {
    const dataset = document.querySelector("#dataset").value;
    const limit = document.querySelector("#limit").value;
    let view = document.querySelector("#view").value;
    let fields = selected_fields ? selected_fields: null;
    url = `${base_url}/${dataset}?limit=${limit}&is_from_web=true`;
    get_headers();
    const filters = show_filters();
    if (fields) {
        url += `&fields=${fields.join(",")}`;
    } else {
        url += `&view=${view}`;
    };
    if (filters) {
        url += filters === "="? "":`&${filters}`;
    };
    // window.history.replaceState("", "", `?dataset=${dataset}&${filters}`);
    // window.location.href = `?dataset=${dataset}&${filters}`;
    return url;

};

const remove_col = (button) => {
    cls_name = button.className.split(" ").at(-1);
    headers.splice(headers.indexOf(cls_name),1);
    button.parentElement.parentElement.remove()
    elements = Array(...document.getElementsByClassName(cls_name));
    elements.forEach((element) => {
        element.remove();
    });
    // console.log(headers);
};

const show_data = () => {
    const results_div = document.querySelector("#results_div");
    const spinner = document.querySelector("#results_spinner");
    const title = document.querySelector("#results_title");
    const download_button = document.querySelector("#download_button");
    const results_thead = document.querySelector("#results_thead");
    const results_tbody = document.querySelector("#results_tbody");
    results_thead.innerHTML = "";
    results_tbody.innerHTML = "";
    download_button.className = "btn btn-dark dropdown-toggle disabled";
    download_button.innerHTML = "Descargar";
    results_div.className = "container-sm d-flex flex-column justify-content-center mt-5";
    spinner.className = "text-center";
    title.innerHTML = "";
    try  {
        document.querySelector("#data").value;
    } catch {
        return;
    };
    const data = JSON.parse(document.querySelector("#data").value);
    if (!data.success) {
        if (data.message.startsWith("El filtro")) {
            title.innerHTML = data.message;
            spinner.className = "visually-hidden";
            return;
        } 
        else if (data.message == "SQLite3 Operational Error") {
            title.innerHTML = `Debe ser indicado un valor correcto`;
            spinner.className = "visually-hidden";
            return;
        };
        return;
    }
    else if (data.data.length == 0) {
        title.innerHTML = `No hay resultados que cumplan los criterios de búsqueda.`;
        spinner.className = "visually-hidden";
        return;
    };
    spinner.className = "visually-hidden";
    // title.innerHTML = `Tiempo de respuesta: ${parseFloat(data.time).toFixed(2)}s`
    title.innerHTML = "Resultados"
    download_button.className = "btn btn-dark dropdown-toggle";
    const records = data.data;
    const tr_k = document.createElement("tr");
    const new_fields = get_fields_2();
    for  (let k of new_fields) {
        const th = document.createElement("th");
        const btn_close = document.createElement("button");
        th.style.backgroundColor = "#39adcc"; //c8d8e4 078ca9
        btn_close.className = `d-inline btn-close text-white ${k}`;
        btn_close.setAttribute("onclick", "remove_col(this)");
        try {
            const tooltip_title = tooltips[dataset.value][k];
            th.innerHTML = `<div  class="d-flex justify-content-between text-white"><span class="tooltip_bne"data-bs-custom-class="tooltip_bne" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="${tooltip_title}">${k}</span></div>`; // data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Tooltip on top"
            th.firstChild.appendChild(btn_close);
            tr_k.appendChild(th)
        } catch {
            const tooltip_title = "Estamos trabajando en ello"
            th.innerHTML = `<div  class="d-flex justify-content-between text-white"><span class="tooltip_bne"data-bs-custom-class="tooltip_bne" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="${tooltip_title}">${k}</span></div>`; // data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Tooltip on top"
            th.firstChild.appendChild(btn_close);
            tr_k.appendChild(th)
        };
    };
    results_thead.appendChild(tr_k);
    records.forEach((record) => {
        const tr_v = document.createElement("tr");
        for (let k of new_fields) {
            const td = document.createElement("td");
            td.scope = "col";
            td.className = k;
            td.innerHTML = record[k]?record[k].trim():"";
            tr_v.appendChild(td);
        };
        results_tbody.appendChild(tr_v);
    })
};

if (document.querySelector("#data")) {
    populate_filters();
    show_data();
};

const set_download_link =  (button) => {
    const csv_a = document.querySelector("#d_csv");
    const json_a = document.querySelector("#d_json");
    const url = get_data(false, fields);
    csv_a.href = url + ".csv";
    json_a.href = url + ".json";

};

const create_form = () => {
    show_data();
    const keys = Array(...document.getElementsByClassName("k"));
    const values = Array(...document.getElementsByClassName("v"));
    const showing_form = document.querySelector("#showing_form");
    let view = document.querySelector("#view").value;
    
    console.log("view", document.querySelector("#view"), view)
    const view_input = document.createElement("input");
    view_input.setAttribute("name", "view");
    view_input.setAttribute("type", "hidden");
    view_input.value = view;
    showing_form.prepend(view_input);
    const dataset = document.querySelector("#dataset").value;
    const dataset_input = document.createElement("input");
    dataset_input.setAttribute("name", "dataset");
    dataset_input.setAttribute("type", "hidden");
    dataset_input.value = dataset;
    showing_form.prepend(dataset_input);

    for (let i = 0; i < keys.length; i++) {
        let key = keys.at(i);
        let value = values.at(i).value;
        key = key.value;
        
        const new_input = document.createElement("input");
        new_input.setAttribute("type", "hidden");
        new_input.setAttribute("name", key);
        new_input.setAttribute("value", value);
        showing_form.prepend(new_input);
    };
    
};