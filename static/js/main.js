function comprobar(esto){
	fecha=esto.value.split("/");
	if(fecha.length<3 || fecha[2].length<4){
	
	return false;
	}
	
    fechaPuesta=new Date(fecha[2],fecha[1]-1,fecha[0]);
	fechaActual=new Date();
	if(fechaPuesta<=fechaActual){
	alert("Debe poner una fecha posterior!!");
	esto.focus();
	}
	}