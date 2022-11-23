# Proyecto Final de Ezequiel Nunzio, Sebastian Padilla y Tomas Goldenhorn.

### Pasos a seguir:
#### 1- Clonar el repositorio
#### 2- Ejecutar el entorno virtual (venv\Scripts\activate)
#### 3- Ejecutar el proyecto (python manape.py runserver)


### Que encontrarás dentro

#### El proyecto consta de un home funcional con unos botones, los cuales permiten buscar y agregar datos a la DB (base de datos).
#### Los botones de crear conducen a un formulario para agregar lo deseado a la DB y al presionar enviar sera redireccionado al home.
#### Mientras que los botones de buscar mostrarán un listado actualizado de lo que contiene ese request a la DB.

### Modelos:
#### Empleado con atributos de nombre, apellido, email, puesto, dni
#### Profesor con atributos de nombre, apellido, email, profesion
#### Curso con atributos de nombre, comision

### Funcionalidad del Formulario de Creación
#### Ejemplo: creación de un Empleado

#### Al llenar los campos del formulario con los datos correspondientes y apretar el botón de ENVIAR, se crea un formulario vacío dentro del servidor. Luego se comprueba que los datos sean válidos. En caso que los sean, se limpian los datos, se guarda un empleado nuevo con sus atributos cargados en la DB y se redirecciona al home. En caso contrario se crea un formulario en blanco y se repite el proceso.

### Funcionalidad del Formulario de Búsqueda
#### Ejemplo: búsqueda de Empleado

#### El formulario admite búsqueda por DNI. El dni ingresado (al menos un número ya que no está programado que sea un dni válido) se envía en el request como valor para la clave 'dni' de un diccionario QueryDict. Dentro del servidor se verifica que el dni esté en el diccionario, luego procede a buscar en la DB los empleados que tengan el dni buscado y los mismos se registran en una lista. Si hay empleados en la lista se muestran en pantalla cada uno, en caso contrario muestra la leyenda 'No hay datos'. 






