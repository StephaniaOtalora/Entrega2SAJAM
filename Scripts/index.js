var usuario;

async function fetchData() {
  response = await fetch("Usuarios/Usuarios.json");
  json = await response.json();
  return json;
}

async function login() {
  let correo = document.getElementById("correo").value;
  console.log(correo);

  let contrasena = document.getElementById("contrasena").value;
  console.log(contrasena);

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
      alert("Contraseña inválida vuelvalo a intentar");
    }
  } else {
    alert("El usuario no se esta registrado");
  }
  console.log(data);
}

function clean(container) {
  let last;
  while ((last = container.lastChild)) container.removeChild(last);
}
async function registrarse() {
  let n = document.getElementById("nombre").value;
  let a = document.getElementById("apellido").value;
  let i = document.getElementById("inputState").value;
  let cr = document.getElementById("correo1").value;
  let c = document.getElementById("contrasena1").value;
  console.log("nombre: " + n);
  console.log("apellido: " + a);
  console.log("correo: " + cr);
  console.log("contraseña: " + c);
  console.log("Genero: " + i);
  usuario = await fetchData();
  if (n != null && a != null && cr != null && c != null && i != "Elije") {
    existe = false;
    for (o in usuario) {
      if (usuario[o].email == cr && !existe) {
        existe = true;
        alert("El correo ya tiene una cuenta existente")
      }
    }
    if (!existe) {
      alert("Gracias por crear una cuenta");
      location.href = "InicioSesion/indexConInicio.html";
    }
  }
  else {
    alert("Por favor llene todos los campos");
  }
}