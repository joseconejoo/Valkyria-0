
/*

login
let passwordDB = contra
let input = usuario
let resultado== input ==passwordDB;
if.... (resultado == true) {
	alert ( login correcto);
	}
	else  {
	alert( usuario incoreto
	}
*/


function accion() {
alert ("hola");
};



/*
reloj
*/
function ActualizarHora(){
    var fecha = new Date();
    var segundos = fecha.getSeconds();
    var minutos = fecha.getMinutes();
    var horas = fecha.getHours();

    var elementoHoras = document.getElementById("pHoras");
    var elementoMinutos = document.getElementById("pMinutos");
    var elementoSegundos = document.getElementById("pSegundos");
    var pSaludo = document.getElementById("contSaludo");

    elementoHoras.textContent = horas;
    elementoMinutos.textContent = minutos;
    elementoSegundos.textContent = segundos;
    

    if (horas >= 8 && minutos >= 1 && horas < 12) {
        pSaludo.textContent = "Buenos Días";
    }
    if (horas >= 12 && minutos >= 1 && horas < 19) {
        pSaludo.textContent = "Buenas Tardes";
    }
    if (horas >= 19 && minutos >= 1) {
        pSaludo.textContent = "Buenas Noches";
    }
}

setInterval(ActualizarHora,1000);




/* movimiento imagen
$("boton-abrir").click(function(){

$("patria").animate({

	left: '200px',
	opacity: '0,5px',
	height: '150px';
})

})

*/

function mostrar() {
    document.getElementById("sidebar").style.width = "300px";
    document.getElementById("M_boton-abrir").style.marginLeft = "300px";
    document.getElementById("abrir").style.display = "none";
    document.getElementById("cerrar").style.display = "inline";
}

function ocultar() {
    document.getElementById("sidebar").style.width = "0";
    document.getElementById("M_boton-abrir").style.marginLeft = "0";
    document.getElementById("abrir").style.display = "inline";
    document.getElementById("cerrar").style.display = "none";
}
