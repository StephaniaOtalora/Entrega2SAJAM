let mascotaTipo;
let mascotaCuidado;

async function readJson() {
  let response = await fetch(
    "https://gist.githubusercontent.com/NicolasAbo17/a69b6e8ed9f372dbc5dbfb5759b836a8/raw/paseadores.json"
  );
  let data = await response.json();
  return data;
}

readJson().then((archivo) => {
  archivo.forEach((mascota) => {
    var tarjetas = document.getElementsByClassName("cards")[0];

    mascota.cuidados.forEach((cuidado) => {
      tarjetas.innerHTML += `<div class ="container-fluid" id="${
        mascota.mascota + cuidado.tipo + "Cards"
      }"> </div>`;
      var tarjetasPaseadores = document.getElementById(
        mascota.mascota + cuidado.tipo + "Cards"
      );

      cuidado.paseadores.forEach((paseador) => {
        const card = document.createElement("div");
        card.classList = "card-body ";
        let comentarios =
          "<h5>Anónimo:</h5><p>" +
          paseador.comentarios.join("</p><h5>Anónimo:</h5><p>") +
          "</p>";

        // Construct card content
        const content = `
          <div class="paseadorcard mb-3 container-fluid h-auto">
            <div class="row">
              <div class="col-md-4">
                <img src="${paseador.foto}" class="w-100 paseadorFoto mt-4">
              </div>
              <div class="col-md-8">
                <div class="paseadorinfo card-block px-3 mt-4">
                  <h4 class="card-title">${paseador.nombre}</h4>
                  <p class="card-text">Ubicación: ${paseador.ciudad}. </p>
                  <p class="card-text">Tiempo de experiencia: ${paseador.experiencia}. </p>
                  <p class="card-text">Sobre mi: ${paseador.descripcion}.</p>
                  <p class="card-text">Rating: ${paseador.valoracion} estrellas.</p>
                  <div class="row justify-content-center mt-5">
                    <div class="col mb-3">
                    <a class="btncards" data-toggle="modal" data-target="#ModalContacto${paseador.nombre}">Contactar</a>
                    </div>
                    <div class="col">

                    <a class="btncards" data-toggle="modal" data-target="#MasInfo${paseador.nombre}">Comentarios sobre ${paseador.nombre}</a>
                    </div>

                    <!-- Modal -->
                    <div class="modal fade " id="ModalContacto${paseador.nombre}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                      <div class="modal-dialog " role="document">
                        <div class="modal-content beigeBackground cafe">
                          <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLabel ">Gracias por tu interés</h5>
                            <button type="button" class="btn close" data-dismiss="modal" aria-label="Close">
                              <span aria-hidden="true">&times;</span>
                            </button>
                          </div>
                          <div class="modal-body ">
                            Nuestro equipo enviará tu información a ${paseador.nombre} para que pronto se contacte contigo. Gracias por confiar en nosotros!
                          </div>
                          <div class="modal-footer">
                          </div>
                        </div>
                      </div>
                    </div>
                    


                    <!-- Modal -->
                    <div class="modal fade " id="MasInfo${paseador.nombre}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                      <div class="modal-dialog " role="document">
                        <div class="modal-content beigeBackground cafe">
                          <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLabel ">Comentarios sobre ${paseador.nombre}</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                              <span aria-hidden="true">&times;</span>
                            </button>
                          </div>
                          <div class="modal-body ">
                          ${comentarios}
                          </div>
                          <div class="modal-footer">
                          </div>
                        </div>
                      </div>
                    </div>

                  </div>
                </div>
              </div>
            </div>
          </div>`;
        tarjetasPaseadores.innerHTML += content;
      });
      document.getElementById(
        mascota.mascota + cuidado.tipo + "Cards"
      ).hidden = true;
    });
  });
  mascotaTipo = "Perros";
  mascotaCuidado = "Residencia";
  document.getElementById("PerrosResidenciaCards").hidden = false;
});
function cambiarPaseadores(tipo, cuidado) {
  document.getElementById(mascotaTipo + mascotaCuidado + "Cards").hidden = true;
  mascotaTipo = tipo;
  mascotaCuidado = cuidado;
  console.log(mascotaTipo + mascotaCuidado + "Cards");
  document.getElementById(
    mascotaTipo + mascotaCuidado + "Cards"
  ).hidden = false;
}
