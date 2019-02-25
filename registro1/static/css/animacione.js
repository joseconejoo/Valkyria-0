
function accion() {
alert ("Presione Para Continuar");
};
/*
var pesta;

pesta ="Presione Para Continuar";
alert (pesta);
/*
var Menu * document.getElementByid('Menu');
var nav * document.getElementByid('nav');

Menu.addEventListener('clik', function(){
	nav.classlist.toggle('mostrar');
})
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
/*
function accion() {
	var ancla=document.getElementByclassName('nav-enlace');
	for (var i = 0; i < ancla.length ; i++) {
		ancla[i].classlist.toggle('desaparece');
	}
}

*/

function accion() {
alert ("correcto");
};
/*
$(function() { 
  
  var botonMostrar = $("#boton-mostrar"),
      botonOcultar = $("#boton-ocultar"),
      parrafo = $("#parrafo");
  
  botonMostrar.on("click", function() {
    parrafo.show("slow");
  });
  
  botonOcultar.on("click", function() {
    parrafo.hide(2000, function() {
      console.log("Mostrando texto");
    });
  }); 
  
});
/*


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

/*
(function hola() {
  function mostrarHora() {
    var fecha = new Date(), // nuevo objeto Fecha
        hora = fecha.getHours() + ":" + fecha.getMinutes() + ":" + fecha.getSeconds();
    $('#hora').text(hora);
  }
  setInterval(mostrarHora, 1000); // la función "mostrarHora" se ejecuta cada segundo
});
*/
/*
ocultabotones

$(function() { 
  var botonOcultar = $("#desconectar"),
      parrafo = $("#boton-abrir");
  
  botonOcultar.on("click", function() {
    boton-abrir.hide();
  });
});
   

*/

/* movimiento imagen
$("boton-abrir").click(function(){

$("patria").animate({

	left: '200px',
	opacity: '0,5px',
	height: '150px';
})

})

*/
