let usuario;

async function fetchData() {
  response = await fetch("Usuarios/Usuarios.json");
  json = await response.json();
  return json;
}

// eslint-disable-next-line no-unused-vars
async function login() {
  let correo = document.getElementById("correo").value;

  let contrasena = document.getElementById("contrasena").value;

  data = await fetchData();

  usuario = data.filter((usuario) => usuario.email === correo)[0];
  if (usuario != null) {
    if (usuario.contrasena === contrasena) {
      let r = document.getElementById("Registro");
      clean(r);
      let p = document.createElement("p");
      p.textContent = "Bienvenid@ " + usuario.first_name;
      r.appendChild(p);
      location.href = "InicioSesion/indexConInicio.html";
    } else {
      // eslint-disable-next-line no-alert
      alert("Contraseña inválida vuelvalo a intentar");
    }
  } else {
    // eslint-disable-next-line no-alert
    alert("El usuario no se esta registrado");
  }
}

function clean(container) {
  let last;
  while ((last = container.lastChild)) {
    container.removeChild(last);
  }
}
// eslint-disable-next-line no-unused-vars
async function registrarse() {
  let n = document.getElementById("nombre").value;
  let a = document.getElementById("apellido").value;
  let i = document.getElementById("inputState").value;
  let cr = document.getElementById("correo1").value;
  let c = document.getElementById("contrasena1").value;

  usuario = await fetchData();
  if (n != null && a != null && cr != null && c != null && i != "Elije") {
    existe = false;
    for (o in usuario) {
      if (usuario[o].email == cr && !existe) {
        existe = true;
        // eslint-disable-next-line no-alert
        alert("El correo ya tiene una cuenta existente");
      }
    }
    if (!existe) {
      // eslint-disable-next-line no-alert
      alert("Gracias por crear una cuenta");
      location.href = "InicioSesion/indexConInicio.html";
    }
  } else {
    // eslint-disable-next-line no-alert
    alert("Por favor llene todos los campos");
  }
}
