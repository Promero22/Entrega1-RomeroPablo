## Readme para el testo de la pagina
***
La Pagina utiliza el formato MTV y CRUD para los formularios.

Credenciales Admin:
User: promero
pass: Coder_123

1. Al ingresar al "Inicio" se encontraran con una "Bienvenida" a la Home del CMP.

2. Alli encontraran los vinculos que se presentaran en todas las paginas al estar definidos en "padre.html":
* Barra Superior (header): 
** Titulo de "Centro Medico Privado" en la parte arriba izquierda -> "Inicio" (Inicio)
** Home -> "Inicio" (Inicio)
** Nuestros Profesionales -> "PList" (profesional/list')
** Especialidades -> "EList" (especialidad/list)
** Sucursales -> "SList" (sucursal/list)
** Login Admin -> Admin (http://127.0.0.1:8000/admin)
* Barra Inferior (footer):
** Home -> "Inicio" (Inicio)
** Profesionales -> "PList" (profesional/list')
** Especialidades -> "EList" (especialidad/list)
** Sucursales -> "SList" (sucursal/list)

3. Tendran un cuadro de busqueda donde se podra ingresar el numero de una de las "Especialidades" para buscarla y que regrese el formulario con la informacion de la Especialidad.
** Busca tu especialidad -> (buscar/)

4. Tambien se puede realizar la busqueda ingresando al link "Buscar" en la barra inferior de las paginas, este redirigira a (/busquedaEspecialidad) donde podran ralizar la busqueda de una especialidad por el numero.

5. Si se ingresa al listado de "Profesionales" por alguno de los vinculos, se mostrara el listado de Profesionales actuales en la bd, mostrando el NOMBRE, el APELLIDO y la ESPECIALIDAD. Desde alli se podra seleccionar:
** Ver -> Redirige a (r'^(?P<pk>\d+)$') desde alli se podra ver los datos del profesional seleccionado
** Editar -> Redirige a (r'^editar/(?P<pk>\d+)$') desde alli se podran editar los datos del profesional en el formulario y guardarlos
** Borrar -> Redirige a (r'^borrar/(?P<pk>\d+)$'), se mostrara un mensaje antes de borrar el usuario y si se acepta se borrara el registro
** Nuevo -> Redirige a (r'^nuevo$') desde alli se podra completar el formulario para la creacion de un nuevo registro
** Volver -> Vuelve al Inicio

6. Si se ingresa al listado de "Especialidades" por alguno de los vinculos, se mostrara el listado de Especialidades actuales en la bd, mostrando el NOMBRE y el NUMERO. Desde alli se podra seleccionar:
** Ver -> Redirige a (especialidad/<int:pk>) desde alli se podra ver los datos del registro seleccionado
** Editar -> Redirige a (especialidad/editar/<int:pk>) desde alli se podran editar los datos de la especialidad en el formulario y guardarlos
** Borrar -> Redirige a (especialidad/eliminar/<int:pk>), se mostrara un mensaje antes de borrar el registro y si se acepta se borrara el mismo
** Nuevo -> Redirige a (especialidad/nuevo) desde alli se podra completar el formulario para la creacion de un nuevo registro
** Volver -> Vuelve al Inicio

7. Si se ingresa al listado de "Sucursales" por alguno de los vinculos, se mostrara el listado de Sucursales actuales en la bd, mostrando el NOMBRE y la DIRECCION. Desde alli se podra seleccionar:
** Ver -> Redirige a (sucursal/<int:pk>) desde alli se podra ver los datos del registro seleccionado
** Editar -> Redirige a (sucursal/editar/<int:pk>) desde alli se podran editar los datos de la sucursal en el formulario y guardarlos
** Borrar -> Redirige a (sucursal/eliminar/<int:pk>), se mostrara un mensaje antes de borrar el registro y si se acepta se borrara el mismo
** Nuevo -> Redirige a (sucursal/nuevo) desde alli se podra completar el formulario para la creacion de un nuevo registro
** Volver -> Vuelve al Inicio

8. Desde el Admin podran crearse nuevos usuarios y registros para los 3 modelos.

***
END