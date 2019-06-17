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
   var btnRecurso=document.getElementById('btnRecurso');
   var selectHerra=document.getElementById('selectHerra');
   var inputCantidad=document.getElementById('inputCantidad');
   var btnHerra=document.getElementById('btnHerra');
    if(sel==""){
        selectRecurso.disabled=true
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



function habilitarEjemplares(){
    var btnRecurso=document.getElementById('btnRecurso');
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

function habilitarRecurso(){
    
    var selectRecurso=document.getElementById('selectRecurso');
    var btnRecurso=document.getElementById('btnRecurso');
    if(selectRecurso==""){
        btnRecurso.disabled=true
    }
    else{
    }
    AsignarEmpleado();
}

function AsignarEmpleado(){

    var id_re=document.getElementById('selectRecurso').value;

    $.ajax({
        data:{'id_re':id_re},
        url:'/constructora/prueba/',
        type:'GET',
        success: function(data){
         
            var html="";
            html+=" <option></option>";
            for (var i=0; i<data.length;i++){
               
            html+="<option value="+"data[i].fields.codigoEjemplar"+">"+data[i].fields.nombreEjemplar+"</option>";
        } 
        $('#ejemplaresT').html(html);      
 
        }
    });
}

// fin de js FC