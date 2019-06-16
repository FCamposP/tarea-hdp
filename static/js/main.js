//  inicio de js FC

function resetearpaginaAsignacion(){
    var selEmpl=document.getElementById('selectEmpleado');
    var selPues=document.getElementById('selectPuesto');
    var btnEmpl=document.getElementById('btnEmpleado');


    selEmpl.disabled=true
    selPues.disabled=true
    btnEmpl.disabled=true
}

function habilitarProyecto(){
   var sel=document.getElementById('selectProyecto').value;
   var emple=document.getElementById('selectEmpleado');
   var pues=document.getElementById('selectPuesto');
   var btnEmpleado=document.getElementById('btnEmpleado');
   var selectRecurso=document.getElementById('selectRecurso');
   var selectEjemplar=document.getElementById('selectEjemplar');
   var btnRecurso=document.getElementById('btnRecurso');
   var selectHerra=document.getElementById('selectHerra');
   var inputCantidad=document.getElementById('inputCantidad');
   var btnHerra=document.getElementById('btnHerra');
    if(sel==""){
        selectRecurso.disabled=true
        selectEjemplar.disabled=true
        btnRecurso.disabled=true
        selectHerra.disabled=true
        inputCantidad.disabled=true
        btnHerra.disabled=true

        emple.disabled=true
        btnEmpleado.disabled=true
        pues.disabled=true
    }
    else{
        emple.disabled=false;
        selectRecurso.disabled=false
        selectHerra.disabled=false
    }
}

function   habilitarEmpleado(){
    var opcion=document.getElementById('selectEmpleado').value;
    var pues=document.getElementById('selectPuesto');
    var btnEmpleado=document.getElementById('btnEmpleado');
    if(opcion==""){
        btnEmpleado.disabled=true
        pues.disabled=true
    }
    else{
        pues.disabled=false  
    }
}

function habilitarPuesto(){
    var pues=document.getElementById('selectPuesto').value;
    var btnEmpleado=document.getElementById('btnEmpleado');
    if(pues==""){
        btnEmpleado.disabled=true
    }
    else{
        btnEmpleado.disabled=false
    }
}

function habilitarRecurso(){
    var selectRecurso=document.getElementById('selectRecurso');
    var selectEjemplar=document.getElementById('selectEjemplar');
    var btnRecurso=document.getElementById('btnRecurso');
    if(selectRecurso==""){
        selectEjemplar.disabled=true
        btnRecurso.disabled=true
    }
    else{
        selectEjemplar.disabled=false
    }
}

function habilitarEjemplares(){
    var selectEjemplar=document.getElementById('selectEjemplar');
    var btnRecurso=document.getElementById('btnRecurso');

    if(selectEjemplar==""){
        btnRecurso.disabled=true;
    }
    else{
        btnRecurso.disabled=false;
    }
}

function HabilitarHerra(){
    var selectHerra=document.getElementById('selectHerra');
    var inputCantidad=document.getElementById('inputCantidad');
    var btnHerra=document.getElementById('btnHerra');    

    if(selectHerra==""){
        inputCantidad.disabled=true;
        btnHerra.disabled=true
    }
    else{
        inputCantidad.disabled=false;
        btnHerra.disabled=false;
    }

}
// fin de js FC