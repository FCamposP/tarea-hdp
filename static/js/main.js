//  inicio de js FC



function habilitarRecurso(){
    var selectRecurso=document.getElementById('selectRecurso');
    var btnRecurso=document.getElementById('btnRecurso');
    if(selectRecurso==""){
        btnRecurso.disabled=true
    }
    else{
    }
    cargarEjemplares();
}

function cargarEjemplares(){

    var id_re=document.getElementById('selectRecurso').value;

    $.ajax({
        data:{'id_re':id_re},
        url:'/constructora/prueba/',
        type:'GET',
        success: function(data){
            console.log(data);
            var html="";
            html+=" <option></option>";
            for (var i=0; i<data.length;i++){
               
            html+="<option value=\""+data[i].pk+"\">"+data[i].fields.nombreEjemplar+"</option>";
        } 
        $('#selectEjemplar').html(html);      
 
        }
    });
}

function empleadosAsignados(){
    var id_emp=document.getElementById('selectEmpleado').value;
    var id_pues=document.getElementById('selectPuesto').value;
    var salario=document.getElementById('salario').value;
    $.ajax({
        data:{'id_pro':id_pro,'id_emp':id_emp,'id_pues':id_pues,'salario':salario},
        url:'/constructora/agregarEmpleado/',
        type:'GET',
        success: function(data){
            var html="";
            html+=" <table class="+"table"+">"+
            "<thead class="+"thead-dark"+">"+
            "<tr>"+
            "<th scope="+"col" +"style="+"width:%"+">#</th>"+
            "<th scope="+"col" +"style="+"width:%"+">Tipo Recurso</th>"+
            "<th scope="+"col" +"style="+"width:%"+">Nombre</th>"+
            "<th scope="+"col" +"style="+"width:%"+">Asignación</th>"+
            " <th scope="+"col" +"style="+"width:%"+">Salario</th>"+
            "</tr>"+
            " </thead>"+
            "<tbody>";
         
            for (var i=0; i<data.a.length;i++){
                
               html+="<tr>"+
               "<td>"+(i+1)+"</td>"+
               "<td>Empleado</td>"+
               "<td>"+ data.e[i]+"</td>"+
               "<td>"+data.a[i]+"</td>"+
               "<td>"+data.salario[i]+ "</td>"
               "</tr>";
            }
            html+=" </tbody>"+
            " </table>";
            $('#tablaa ').html(html); 
            
        }
        
          
        
    });
    alert('sii'); 
}

    //Pagina Solicitar Recursos

function CambioTipoRecurso(){

    var opcion=document.getElementById('selectTipoRecurso').value;

    $.ajax({
        data:{'opcion':opcion},
        url:'/constructora/ConseguirTipoRecurso/',
        type:'GET',
        success: function(data){
          
            var html="";
            html+=" <option></option>";

            if(opcion=='1'){
                for (var i=0; i<data.length;i++){
               if(data[i].fields.nombrePuesto!='Encargado')
               {
                html+="<option value=\""+data[i].pk+"\">"+data[i].fields.nombrePuesto+"</option>";

               }
                } 
                $('#selectRecDisponible ').html(html); 
              
            }

            if(opcion=='2'){
                for (var i=0; i<data.length;i++){
 
                html+="<option value=\""+data[i].pk+"\">"+data[i].fields.nombreRecurso+"</option>";

                } 
                $('#selectRecDisponible ').html(html); 
              
            }

            if(opcion=='3'){
                for (var i=0; i<data.length;i++){

                html+="<option value=\""+data[i].pk+"\">"+data[i].fields.nombreHerramienta+"</option>";

                } 
                $('#selectRecDisponible ').html(html); 
              
            } //fin if 3
  
        }
    });

}
function SolicitarRecurso(){

    var opcion=document.getElementById('selectTipoRecurso').value;
    var elemento=document.getElementById('selectRecDisponible').value;
    var cantidad=document.getElementById('cantidadSolicitar').value;
    
  //  var cantidad=document.getElementById('cantidadHerramientaSolicitar').value;
   // alert(cantidad);
    $.ajax({
        data:{'elemento':elemento,'opcion':opcion},
        url:'/constructora/conseguirElemento/',
        type:'GET',
        success: function(data){
            console.log(data);
       
            var html="";

            if(opcion=='1'){
              
                html+="<tr  id=\""+ data[0].fields.codigoPuesto  +"\" style=  \"text-align: center\">"+

                "<td>  Puesto</td>"+
                "<td>"+ data[0].fields.codigoPuesto  +"</td>"+
                "<td>"+ data[0].fields.nombrePuesto +"</td>"+
                "<td>"+ data[0].fields.descripcionPuesto +"</td>"+
                "<td><input style=\"display:none;\" name=\""+ data[0].fields.codigoPuesto  +"\" value="+cantidad+"  > "+ cantidad +"</td>"+
                "<td>   <a class=\"btn btn-danger\"name=\""+ data[0].fields.codigoPuesto  +"\" onclick=\"eliminarRecurso(this.name)\" >Eliminar</a>   </td>"+

                "</tr>";

                $('#tbodyPuesto').after(html);
            }

            if(opcion=='2'){
                html+="<tr  id=\""+ data[0].pk   +"\" style=  \"text-align: center\">"+

                "<td>  Maquinaria </td>"+
                "<td>"+ data[0].pk  +"</td>"+
                "<td>"+ data[0].fields.nombreRecurso +"</td>"+
                "<td>"+ data[0].fields.descripcionRecurso +"</td>"+
                "<td><input style=\"display:none;\" name=\""+ data[0].pk   +"\" value="+cantidad+"  > "+ cantidad +"</td>"+
                "<td>   <a class=\"btn btn-danger\"name=\""+ data[0].pk  +"\" onclick=\"eliminarRecurso(this.name)\" >Eliminar</a>   </td>"+

                "</tr>";
                $('#tbodyPuesto2').after(html);
            }

            if(opcion=='3'){
                html+="<tr  id=\""+ data[0].pk   +"\" style=  \"text-align: center\">"+

                "<td>  Herramienta </td>"+
                "<td>"+ data[0].pk   +"</td>"+
                "<td>"+ data[0].fields.nombreHerramienta +"</td>"+
                "<td>"+ data[0].fields.descripcionHerramienta +"</td>"+
                "<td><input style=\"display:none;\" name=\""+ data[0].pk   +"\" value="+cantidad+"  > "+ cantidad +"</td>"+
                "<td>   <a class=\"btn btn-danger\"name=\""+ data[0].pk   +"\" onclick=\"eliminarRecurso(this.name)\" >Eliminar</a>   </td>"+

                "</tr>";
                $('#tbodyPuesto3').after(html);
            } //fin if 3
  
        }
    });
  
}

function eliminarRecurso(name){
  console.log(name);
  document.getElementById(name).remove();
}

function MostrarEjemplares(){

    var id_re=document.getElementById('reasignarEjemplar').value;

    $.ajax({
        data:{'id_re':id_re},
        url:'/constructora/ReasignarEjemplar/',
        type:'GET',
        success: function(data){
            console.log(data);
            var html="";
            html+=" <option></option>";
            for (var i=0; i<data.length;i++){
               
            html+="<option value=\""+data[i].pk+"\">"+data[i].fields.nombreEjemplar+"</option>";
        } 
        $('#selectEjemplar1').html(html);      
 
        }
    });
}

// fin de js FC