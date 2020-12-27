# Protocolos.

1. **¿Qué es el protocolo TCP?**

     **Protocolo de Control de Transmisión**. Está orientado a la conexión, o sea, los datos pueden enviarse de forma bidireccional una vez establecida la conexión.

    **Es usado para transferir la mayoría de los tipos de datos, como archivos
     y páginas web o transferencias bancarias**.

2. **¿Qué es el protocolo UDP?**

    **Protocolo de Datagramas de Usuario**. Protocolo de nivel de transporte basado en el intercambio de datagramas. Permite el envío de datagramas a través de la red sin que haya establecido previamente una conexión.

    **Es usado para streaming (Spotify/Netflix)**.

3. **¿Qué es el protocolo ICMP?**   

    **Protocolo de Control de Mensajes de Internet**. Es utilizado para enviar
     mensajes de error e información operativa indicando, por ejemplo, que un
servicio determidado no está disponible o que un router o host no puede ser
localizado.

    **Es usado para envíar mensajes de error**.

4. **¿Qué es el protocolo FTP? (puerto 21)**   

    **Protocolo de Transferencia de Archivos**. Protocolo de red para la
     transeferencia de archivos entre sistemas conectados a una red TCP. 

    **Basado en la arquitectura cliente-servidor**.

5. **¿Qué es el protocolo POP? (puerto 110)**  

    **Protocolo de Oficina de Correos**. Es utilizado por programas de e-mail
     locales para recibir e-mails desde un servidor remoto a través de una
conexión TCP/IP.

6. **¿Qué es el protocolo TFTP? (puerto 69)**   

    **Trivial File Transfer Protocol**. Un protocolo cliente-servidor muy
     simple que regula la transferencia de archivos en redes informáticas.

7. **¿Qué es el protocolo HTTP? (puerto 80)**   

    **Protocolo de Transferencia de Hipertexto**. Protocolo de comunicación que
     permite las transferencias de información en la World Wide Web.

8. **¿Qué es PDU?**   

    **Unidad de Datos de Protocolo**. Se utilizan para el intercambio de datos
     entre unidades disparejas, dentro de una capa del modelo OSI.

9. **¿Qué es IP?**   

    **Internet Protocol**. Es una serie de números que ayudan a identificar la
     computadora en internet.
    
    **IPv4**: 32 bits (192.168.1.1)   
    **IPv6**: 128 bits (fe80::da30:c9b2:f04d:c875)

10. **¿Qué es DHCP? (puerto 67)**   

    **Protocolo de Configuración Dinámica de Host**. Protocolo de red de tipo
     cliente-servidor mediante el cual un servidor DHCP asigna dimanicamente
una dirección IP y otros parámetros de configuración de red a cada dispositivo
en una red para que puedan comunicarse con otras redes IP.

11. **¿Qué es Telnet? (puerto 23)**   

    Permite acceder a otra máquina para manejarla remotamente como si
estuvieramos sentados delante de ella.

12. **¿Qué es SSH? (puerto 22)**   

    **Secure Shell**. Su principal función es el acceso remoto a un servidor
     por medio de un canal seguro en el que toda la información está cifrada.   

13. **¿Qué es SMTP? (puerto 25)**   

    **Protocolo para Transferencia Simple de Correo**. Es utilizado para el
     intercambio de mensajes de correo electrónico entre computadoras u otros
dispositivos. 

14. **¿Qué es DNS? (puerto 53)**   

    **Sistema de Nombre de Dominio**. Un sistema basada en una base de datos
     que sirve para resolver nombres en las redes, es decir, para conocer la
dirección IP de la máquina donde está alojado el dominio al que queremos
acceder.

# Normas de cables.

1. **¿Cuál es la norma EIA/TIA 568?**   

    Esta norma establece dos estandares (A y B) para el cableado ethernet
10base-T, determinando qué color corresponde a cada pin del conector RJ-45.

![](https://2.bp.blogspot.com/--R9Q5mp2gdo/TZk10u6oLhI/AAAAAAAAAAw/dL7f2sV4rME/s1600/cable-de-red-normas-t568a-t568b_1%255B1%255D.gif)   

2. **¿Qué es el RJ-45?**   

    Es una interfaz física utilizada para conectar redes de computadoras con
cableado estructurado. **Posee 8 pines** o conexiones electricas, que
normalmente se usan como extremos de cable de par trenzado (UTP).

3. **¿Qué es UTP?**   

    **Unshielded Twisted Pair**. Es utilizado en el cableado telefónico y como
     cable de red de computadora para área local (LAN).

4. **¿Qué es RJ-11?**   

    Es el conector utilizado en las redes de telefonía, se refiere exactamente
al conector que se une al cable telefónico y tiene 6 posiciones con 4 contactos
centrales por los 4 hilos del cable telefónico.

# Capas de OSI (Open System Interconnection)   

![](https://www.textoscientificos.com/imagenes/redes/xtcp-ip-osi.gif.pagespeed.ic.y7ij6ZXT9C.png)

# Capas de PDU (Unidad de Datos de Protocolo)

![](https://txdatos.files.wordpress.com/2011/02/11.png)

# Tipos de redes

1. **¿Qué es una red?**   

    Es un conjunto de máquinas de ordenadores interconectados entre sí mediante
cable o por otros medios inalámbricos.

2. **¿Cuáles son los objetivos de una red?**   

    - Compartir recursos: archivos, impresoras.
    - Transferir información entre ordenadores: e-mail, www, etc..

3. **¿Cuáles son los tipos de redes?**  

    - **LAN**: Local Area Network. Redes de Área Local.
    - **MAN**: Metropolitan Area Network. Redes de Área Metropolitana.
    - **WAN**: Wide Area Network. Redes de Área Extendida.   

    Según el sistema jerárquico de red utilizada, se clasifican en:
      
      - Redes cliente-servidor.
      - Redes punto   punto.
  
4. **¿Qué son las redes cliente-servidor?**   

    Son redes en las que uno o más ordenadores (servidores) son los que
controlan y proporcionan recursos y servicios a otros (clientes).

5. **¿Qué son las redes punto a punto?**   

    Son las que todos los ordenadores tienen el mismo status en la red que
deciden qué recursos y servicios dan al resto. En la red punto a punto cada
cliente puede ser también servidor y un servidor puede ser cliente.

6. **¿Cuáles son los componentes de una red local?**   

    - Estación de trabajo (clientes).
    - Servidores.
    - Tarjetas de red (NIC).
    - Cableado o medios inalámbricos (Antenas).
    - Dispositivos distribuidores: HUB, Switch, Router.
    - Sistema operativo de red.
    - Recursos compartidos: Impresora de red, archivos y aplicaciones.

7. **¿Qué es una tarjeta de red?**   

    También conocida como **NIC (Network Interface Card)**, se instalan dentro
del ordenador y son las que hacen posible la conexión del PC con la red.
Traducen la información que circula por el cable/ondas de la red al lenguaje
que entiende el ordenador.

8. **Menciona los tipos de cableado**   

    - Coaxial.
    - Fibra óptica.
    - Par trenzado.

9. **¿Qué es el HUB?**

    Es un dispositivo que sirve para conectar múltiples dispositivos mediante
cables cruzados o fibra óptica y haciéndolos funcionar como un único segmento
de red.

**Trabaja en Half-Duplex**.

10. **¿Qué es un switch?**   

    Utiliza una arquitectura store-and-forward, es decir, almacena la trama de
datos en un pequeño búffer para posteriormente reenvíarla a su destino
correcto.

**Trabaja en Full-Duplex**.

11. **¿Cuál es la diferencia entre HUB y SWITCH?**   

La diferencia es que el **HUB envía todos los datos que recibe a todos** los
puertos y el **switch lo envía sólo al puerto del equipo correcto**.

12. **Según la IEEE a qué se le conoce como el estándar 802.11**   

    Es la manera formal/apropiada de llamar a las redes WiFi/inalámbricas.

13. **Según la IEEE a qué se le conoce como el estándar 802.3**

    Es la manera formal/apropiada de llamar a las redes alámbricas/por cable.

14. **¿Qué es la MAC?**   

    **Media Access Control**. Es un identificador de 48 bits que corresponde de
     forma única a una tarjeta o dispositivos de red.

15. **¿Qué es MUA?**   

    **Agente de Usuario de Correo**.

16. **¿Qué es MTA?**   

    **Agente que Transfiere el Correo**.

17. **¿Qué es MDA?**   

    **Agente de Entrega de Correo**.

18. **¿Qué es Full-Duplex?**   

    El dispositivo no tiene que esperar para envíar tramas. Puede envíar
y recibir al mismo tiempo.

19. **¿Qué es Half-Duplex?**   

    El dispositivo debe esperar para envíar si está en ese momento recibiendo
tramas, es decir, no puede envíar y recibir al mismo tiempo.
  
20. **¿Qué es el Bridge?**   

    Un dispositivo de interconexión de redes de computadoras que almacena las
direcciones MAC de los dispositivos.   
