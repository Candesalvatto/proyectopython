Esta es la web BY NETA, es un e-comerce de productos de belleza. 
La web cuenta con distintas secciones:
-Un nav para acceder a las distintas partes de la web, iconos de Iniciar sesion,  Cerrar sesion y carrito de compras. (cerrar Sesion y carrito solo se pueden ver cuando el usuario inicia sesion)
- Inicio con informacion general, y varios links para acceder desde alli (ademas del nav) a las partes de la web
-Footer con 2 links para ir a iniciar sesion o registrarse
-Acerca de mi (informacion sobre la fundadora de la empresa y links a sus redes originales)
-Seccion productos, dividida en ACCESORIOS, AUTOBRONCEANTES Y BRUMAS. En cada una de ella respectivos productos. Si el usuario no inicio sesion, puede ver los productos, acceder al detalle pero si lo quiere comprar lo redirige a iniciar sesión. Una vez iniciada la sesión puede comprarlo y vera su producto plasmado en el carrito de compras.
-Manual de uso con informacion adicionales de cómo colocar los productos con videos explicativos.
-Registro de usuario
-Inicio de sesion. Una vez el usuario iniciado sesión se verá su nombre en el nav junto con la opcion de salir o de ver el carrito de compras. Cuando el usuario clickea su nombre puede acceder a su perfil con todos sus datos registrados, el cual puede verlos, editar sus datos y cambiar la contraseña.
-Carrito de compras muestra un mensaje que esta vacio en caso de no haber agregado productos, todos los productos que se compren van a aparecer en un listado con la información del día en que se compro, la cantidad, qué producto es y la opción de poder eliminarlo del carrito. En la parte de arriba cuenta con una barra de búsqueda de sus productos del carrito, si se busca un producto que no está aparece un mensaje de que no se encontro su busqueda y sino, muestra filtrado el producto buscado.
-Los formularios para agregar un producto a las listas de productos sólo los puede ver y acceder el usuario admin, osea el superuser. El cual puede agregar, modificar un existente o eliminarlo.

Puntos de la entrega:
-Herencia de templates en varios de ellos, los que no tienen herencia es sólo por cambios a los estilos que no podia modificar. Los template base que extendi estan en la carpeta templates y son: 'store.html' y 'template.html'.
-git ignore con las especificaciones correspondientes.
-archivo requirements.txt
-Clases basadas en vista: hay en app carrito(borrar producto), tienda(editar producto) y cuenta(cambiar contraseña).
-decoradores en la vista del carrito
