console.log("Código desarrollado por Vito Genovese para la BNE, visita https://infofortis.com")

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
            <input  type="text" class="form-control v" placeholder="Valor" onkeydown="set_filter(this)" id="set_me">
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

let fields = [];

const set_download_link =  (button) => {
    const csv_a = document.querySelector("#d_csv");
    const json_a = document.querySelector("#d_json");
    let url = window.location.href;
    url = url.replace("web/?dataset=", "api/");
    url = url.replace("&", "?");
    if (fields.length > 0) {
        url = url.replace("?view=human", "");
        url = url.replace("?view=marc", "");
        url = url.replace("?view=", "");
        url = url.replace("&", "?");
        csv_a.href = url + "&fields=" + fields.join(",")  + ".csv";
        json_a.href = url  + "&fields=" + fields.join(",") + ".json";
    } else {
        csv_a.href = url + ".csv";
        json_a.href = url  + ".json";
    };


};

const populate_filters = () => {
    const get_args = _ =>
        [...new URLSearchParams(window.location.href.split('?')[1])].reduce(
            (a, [k, v]) => ((a[k] = v), a),
            {}
        );
    let args = get_args();
    const view_i = Object.keys(args).indexOf("view");
    document.querySelector("#view").value =  ["marc", "human"].indexOf(Object.values(args).at(view_i))  >= 0? Object.values(args).at(view_i): "";
    delete args.view;
    if (Object.keys(args).length == 0) {
        document.querySelector("#view").value =  "human";
        return;
    };
    if (!args) {
        return;
    };
    Object.entries(args).forEach((arg, i) => {
        [k,v] = arg;
        if (i > 1 && k != "is_from_web") add_filter();
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

populate_filters();

const set_name_filters = () => {
    for (let filter of document.getElementsByClassName("v")) {
        set_filter(filter);
    };
};

set_name_filters();

const get_headers = () => {
    const view = document.querySelector("#view").value;
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

const show_data = () => {
    try  {
        document.querySelector("#data").value;
    } catch {
        return;
    };
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
    const new_fields = get_headers();
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
    show_data();
};


const remove_col = (button) => {
    cls_name = button.className.split(" ").at(-1);
    const headers = get_headers();
    headers.splice(headers.indexOf(cls_name),1);
    if (fields.length > 0) {
        fields.splice(fields.indexOf(cls_name),1);
    } else {
        fields = headers;
    };
    console.log(fields); 
    button.parentElement.parentElement.remove()
    elements = Array(...document.getElementsByClassName(cls_name));
    elements.forEach((element) => {
        element.remove();
    });
    // console.log(headers);
};

document.onkeydown= (event) => {
    const key = event.key;
    if (document.activeElement.type == "text") {
        return;
    }
    if (key == "v") {
        document.querySelector("#view").focus();
    } else if (key == "d") {
        document.querySelector("#dataset").focus();
    } else if (key == "r") {
        document.querySelector("#results").focus();
    } else if (key == "f") {
        document.querySelector("#original_filter").focus();
        document.querySelector("#original_filter").value = "";
    } else if (key == "a") {
        document.querySelector("#add_filter").focus();

    };
};