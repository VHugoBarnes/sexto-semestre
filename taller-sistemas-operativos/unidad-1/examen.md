# Guía Tema I

## Sistemas operativos por su estructura.

1. **Estructura Monolítica**: No permite el manejo de recursos. Está
estructurada por modulos que se agrupan por separado, mediante un ligador.

2. **Estrcutura Jerárquica**: Las partes que lo integran se organizan por medio
de niveles de importancia.

3. **Máquina Virtual**: Se presenta una interfaz a cada proceso mostrando una
máquiena que parece identica a la máquina real subyacente. Se suelen estár
unidos con el resto de sistema: la multiprogramación y la máquina extendida.

4. **Cliente-Servidor (Micro-Kernel)**: Sirve para toda clase de aplicaciones
y el prósito es general, cumpliendo así con las mismas actividades de los otros
sistemas operativos.

5. **Subnúcleo**: Designado a establecer comunicación entre los clientes
y servidores. Los procesos pueden ser tanto servidores como clientes y a su
vez, el cliente como el servidor para otros procesos.

## Sistemas operativos por la forma que ofrecen sus servicios.

1. **Sistema operativo de red**: Interactua con otras computadoras por un medio
de transmisión, transfiere archivos, ejecuta comandos remotos y otras tareas.

2. **Sistema operativo distribuído**: Incluye los mismos servicios que un
sistema operativo de red, incluye o añade recursos (impresoras, unidades de
respaldo, memoria, procesos y unidad central de proceso) en una sola máquina
virtual. 


## Procesos y multiprogramación.

Un **proceso** en un sistema multiprogramado o de tiempo compartido es una
**imagen en memoria** de un programa, junto con toda la información relacionada
 con el estado de su ejecución. 

Un **programa** es una entidad pasiva, una lista de instrucciones o es una
entidad activa que define la activación que tendrá el sistema. 

En contraposición con los procesos en un sistema por lotes se habla de
**tareas**. Una **tarea** requiere menos estructura. Tipicamente basta con
 guardar la información relacionada con la contabilidad de los recursos
empleados. 

Una tarea **no es interrumpida** en el transcurso de su ejecución.

### Estados de un proceso.

1. **Nuevo**: Se solicita al S.O. la creación de un proceso. Sus recursos
y estructuras están siendo creadas.

2. **Listo**: Es el inicio o continuación de su ejecución. El sistema aún no le
ha asignado un procesador.

3. **En ejecución**: El proceso está siendo ejecutado en ese momento. Sus
instrucciones están siendo procesadas.

4. **Bloqueado**: En espera de algún evento.

5. **Zombie**: Ha finalizado su ejecución pero se debe limpiar de la lista.

6. **Terminado**: Terminó de ejecutarse y sus estructuras están a la espera de
ser limpiadas.

## VPS (Virtual Private Server).

Ofrece un ambiente parcialmente aislado junto con un mayor control y la
capacidad de hacer cosas más avanzadas en un sitio web.

El espacio en el servidor se divide en contenedores.

Un **Servidor dedicado** ofrece privacidad, seguridad y recursos de dicados, no
se tiene que competir por un ancho de banda, velocidad y espacio de
almacenamiento.

La mayoría de los propietarios de los sitios web para principiantes empiezan
con un plan de alojamiento compartido. Estos están diseñados para sitios que no
exigen demasiado.

La parte importante del **VPS** es la **Virtualización**. El anfitrión divide
un servidor en varios servidores virtuales más pequelos, cada uno con su parte
de RAM y espacio de disco duro.

### Ventajas del VPS.

- Se puede configurar en pocos minutos.
- Tiende a ser más confiable que el alojamiento compartido.
- Puede crear y eliminar sitios a voluntad.
- Cada sitio tiene su panel de control.
- El software puede ser instalado y modificado y puede ser más seguro.

### Desventajas del VPS.

- Necesitas saber un poco sobre administración de servidores.
- El costo es algo elevado.
- Uno administrado puede parecer una opción barata, pero la fijación de un
fallo sale caro.
- La elección de un plan puede ser complicado.

## Virtualización.

Virtualizar consiste en proveer algo que no está ahí aunque parezca estarlo.
Más especificamente, presentar a un sistema de elementos que se comparten
igual que un componente físico sin que exista.

- **Host**: El hardware real que ofrece el mecanismo de virtualización.
- **Guest**: Sistema o aplicaciones que se ejecutan en el entorno virtualizado.

## Emulación.

La emulación consta de **realizar una replica una arquitectura de hardware al
completo** (procesador, juego de instrucciones, hardware, etc.) Un ejemplo son
los **emuladores de videojuegos como el GameBoy o Nintendo 64**.

## Virtualización asistida por hardware.

Este tipo de virtualización **utiliza una capa intermedia de virtualización**
(el hypervisor) que media entre hosts físicos y máquinas virtuales. Además,
**incluye código para emular el hardware subyacente para las m.v.** (Esto
 permite ejecutar cualquier sistema sin modificar, siempre que soporte el
hardware subyacente).

## Paravirtualización.

Se basa en lo mismo que la virtualización asistida por hardware, con la
diferencia de que **no incluye el código de emulación de hardware** e introduce
modificaciones en los sistemas operativos.

## Paravirtualización y Software Libre.

Existe el problema en la paravirtualización de que para poder realizarla, se
debe tener acceso a la arquitectura de hardware y poder manipular y modificar
su código fuente.

En tanto, el trabajo para lograr la paravirtualización de un sistema operativo
libre como Linux, FreeBSD puede ser libremente distribuido. No solo eso, sino
que el esfuerzo para realizar la adaptación puede compartirse entre
desarrolladores de todo el mundo.
