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

            
        }
        
          
        
    });

}

// fin de js FC