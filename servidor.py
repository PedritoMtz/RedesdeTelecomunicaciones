import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #El socket como variable global para poder ser utilizado por todos los metodos
    print "Socket Creado :D"
    s.bind(("127.0.0.1", 9999))
    print "Servidor Listo para recibir informacion :D \n"
except socket.error:
    print "No se pudo crear el Socket :("

def main():
    Dir = ""
    Archivo = open("Datos.dat", "w")

    while True:
        msj = s.recvfrom(1024) #La varible msj recibe el mensaje y la direccion de quien envio este mensaje
        Direccion = msj[1] #Esta variable almacena la direccion del remitente 
        Texto = msj[0] #Esta variable almacena el mensaje
        if Dir != Direccion: #Si se detecta una nueva direccion imprime la direccion de este
            print "Informacion recibida de --> "+str(Direccion)
            Archivo.write("\n")

        Dir = Direccion
        Archivo.write(Texto)
        
        s.sendto(str("Informacion Recibida :) muchas gracias"), Direccion)
    Archivo.close()

main()
