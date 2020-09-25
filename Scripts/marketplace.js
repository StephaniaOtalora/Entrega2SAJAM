url_perros =
  "https://gist.githubusercontent.com/EstebanCardenas/b007a57e4b8b1642b28205d208e06b72/raw/181775b9d1275611b35c3e162e90b2c28bb23a9d/p_perros.json";
url_gatos =
  "https://gist.githubusercontent.com/EstebanCardenas/13c69a0b9ba7980710f65d8b6eed111d/raw/7e722a2a6e06a4033b89b21e36f4c5ec9ac42806/p_gatos.json";
url_otros = "https://gist.githubusercontent.com/EstebanCardenas/deaaba292da78c03dbddb82263649cf1/raw/c2b0933430a953932138eb65bbf218a889166216/p_otros.json";

const info = document.getElementById("info");
const n_items = document.getElementById("n_items");
var carrito = [];
var items = 0;

function changeContent(url, filter) {
  info.innerHTML = ""
  fetch(url)
    .then((response) => response.json())
    .then((json) => {
      for (let o of json) {
        if (filter.includes(o["categoria"])) {
          let content = `<div class="card col-xs-12 col-md-6 col-lg-3">\
          <img src="${o["foto"]}" class="card-img-top" alt="${o["nombre"]}">\
          <div class="card-body">\
            <h5 class="card-title">${o["nombre"]}</h5>\
            <p class="card-text"><strong>Descripcion:</strong> ${o["descripcion"]}</p>\
            <p class="card-text"><strong>Precio:</strong> $${o["precio"]}</p>\
            <p class="card-text"><strong>Calificación:</strong> ${o["calificacion"]} estrellas</p>\
            <button onclick="agregarProd('${o["precio"]}', '${o["nombre"]}')" class="btn">AGREGAR</button>
          </div>\
          </div>`;
          info.innerHTML += content;
        }
      }
    });
}

changeContent(url_perros, ["Comida", "Juguetes", "Salud y bienestar"])

//event listeners
const p_perros = document.getElementById("perros_but")
p_perros.addEventListener("click", () => {
  changeContent(url_perros, ["Comida", "Juguetes", "Salud y bienestar"])
})

const p_gatos = document.getElementById("gatos_but")
p_gatos.addEventListener("click", () => {
  changeContent(url_gatos, ["Comida", "Juguetes", "Salud y bienestar"])
})

const p_otros = document.getElementById("otros_but")
p_otros.addEventListener("click", () => {
  changeContent(url_otros, [""])
})

function agregarProd(precio, nombre) {
  item = carrito.find(item => item.nombre === nombre);
  if (item == undefined) {
    carrito.push({ "nombre": nombre, "precio": precio, "cantidad": 1 });
  }
  else {
    item.cantidad += 1;
  }
  items++;
  if (items == 1)
    n_items.innerHTML = `1 item`;
  else {
    n_items.innerHTML = `${items} items`
  }
}

Array.from(document.getElementById("f_perros").children).forEach((el) => {
  el.addEventListener("click", () => {
    let filter = el.innerHTML.toLowerCase()
    filter = filter.charAt(0).toUpperCase() + filter.slice(1)
    changeContent(url_perros, [filter])
  })
})

Array.from(document.getElementById("f_gatos").children).forEach((el) => {
  el.addEventListener("click", () => {
    let filter = el.innerHTML.toLowerCase()
    filter = filter.charAt(0).toUpperCase() + filter.slice(1)
    changeContent(url_gatos, [filter])
  })
})

function cargarCarrito() {
  var element = document.querySelector(".carritoBody");
  var parent = element.parentNode
  parent.removeChild(element);
  element = document.createElement("tbody");
  element.classList.add("carritoBody");
  parent.appendChild(element);
  var total = 0;
  for (var i = 0; i < carrito.length; i++) {
    const tr = document.createElement("tr")
    const td1 = document.createElement("td");
    td1.innerText = carrito[i].nombre;
    const td2 = document.createElement("td");
    td2.innerText = carrito[i].precio;
    const td3 = document.createElement("td");
    td3.innerText = carrito[i].cantidad;
    const td4 = document.createElement("td");
    td4.innerText = "$" + carrito[i].cantidad * carrito[i].precio;
    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tr.appendChild(td4);
    element.appendChild(tr);
    total += carrito[i].cantidad * carrito[i].precio;
  }
  const totalHTML = document.querySelector(".total");
  totalHTML.innerText = "Total: $" + total;
}
function cancelarPedido() {
  location.reload();
  carrito = [];
  n_items.innerHTML = "0 artículos";
}