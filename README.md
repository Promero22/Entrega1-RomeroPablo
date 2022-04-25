## Readme para el testeo de la pagina
***
La Pagina utiliza el formato MTV y CRUD para los formularios.

Credenciales Admin:
User: promero
pass: Coder_123

Credenciales Usuarios:
User: Vicky2
pass: probando

User: Marcos
pass: probando

1. Al ingresar al "Inicio" se encontraran con que es necesario estar Logueado para ver el Inicio (@login_required), al hacerlo se encontraran con una "Bienvenida" a la Home del CMP con la Imagen de Avatar si la misma esta cargada.

2. Alli encontraran los vinculos que se presentaran en todas las paginas al estar definidos en "padre.html":
* Barra Superior (header): 
** Titulo de "Centro Medico Privado" en la parte arriba izquierda -> "Inicio" (Inicio)
** Home -> "Inicio" (Inicio)
** Nuestros Profesionales -> "PList" (profesional/list')
** Especialidades -> "EList" (especialidad/list)
** Sucursales -> "SList" (sucursal/list)
** Login -> "Login" (/login)
** Registrate -> "Register" (/register)
** About us -> "Abot" (/about)

* Barra Inferior (footer):
** Home -> "Inicio" (Inicio)
** Profesionales -> "PList" (profesional/list')
** Especialidades -> "EList" (especialidad/list)
** Sucursales -> "SList" (sucursal/list)
** Admin -> Admin (http://127.0.0.1:8000/admin)
** About us -> "Abot" (/about)
** Buscar -> (/busquedaEspecialidad)
** Sumar un Avatar -> "AgregarAvatar" ("agregarAvatar")
** Index -> "Index" (/index)

3. Tendran un cuadro de busqueda donde se podra ingresar el numero de una de las "Especialidades" para buscarla y que regrese el formulario con la informacion de la Especialidad.
** Busca tu especialidad -> (buscar/)

4. Tambien se puede realizar la busqueda ingresando al link "Buscar" en la barra inferior de las paginas, este redirigira a (/busquedaEspecialidad) donde podran realizar la busqueda de una especialidad por el numero.

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

8. Logueados podran ver donde estaba el boton de Login, un saludos y el usuario logueado, junto a los botones de "Ver Perfil" y "Logout" (logout), que desloguea al usuario y lo informa en una pagina de mensaje. 

9. Si se selecciona "Ver Perfil" (userDetalle) podran ver los datos ingresados del usuario actual, USUARIO, NOMBRE, APELLIDO y CORREO, tambien habra 2 botones. "Editar Perfil" y "Regresar" (inicio)
** Si se selecciona "Editar Perfil" (editarPerfil), se podra modificar el MAIL, APELLIDO y NOMBRE del usuario logueado, el campo de CONTRASEÑA Y REPETIR CONTRASEÑA esta como readonly y no pueden modificarse.

11. En el header si no se esta logueado tambien se mostrara el boton de "Registrate" (register).
Si se selecciona el mismo seran redirigidos a al formulario de registro donde se deberan ingresar USERNAME, MAIL, CONTRASEÑA y REPETIR CONTRASEÑA y al presionar el boton de "Registrate!", se creara el registro y el usuario sera redirigido a una pagina con un mensaje de registro exitoso.
** El usuario registrado no cuenta con Avatar, Nombre o Apellido.

12. Para la carga del avatar un usuario Logueado puede seleccionar "Sumar un Avatar" (agregarAvatar) en el NavBar del footer.
** Alli podra seleccionar su Usuario y luego presionar el boton "Seleccionar Archivo" que abrira una popup para poder seleccionar la imagen deseada. Una vez cargada la misma sera visible en el Inicio sobre el mensaje de saludo.

13. El link al "About us" (about) en el header y en footer redirigen a una pagina con informacion del creador de la pagina (yo).

14. El link a la pagina de Index, redirige a una pagina en la que se encuentran listadas las paginas creadas y un boton para regresar el indice.

15. los usuarios administradores podran desde el Admin realizar el ABM de usuarios, registros para los 3 modelos, Avatars y grupos.

VIDEO: 
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/_vJ-bJAwRzw/0.jpg)](https://www.youtube.com/watch?v=_vJ-bJAwRzw)
  
***
Pablo Romero 04-2022
END
