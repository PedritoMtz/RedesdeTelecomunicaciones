import socket

direccion = "127.0.0.1"
puerto = 9999

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.connect((direccion, puerto))
    print "Solicitando Conexion -----------"

except socket.error:
    print "No pudo conseguir el socket"

def main():
    #while True:
    mensaje = raw_input("Mensaje a Enviar al Servidor --> ")
    print mensaje

    paquete(mensaje)
    recibir()

#Obtener longitud de un texto
def paquete(mensaje):
    Lista = list(mensaje)
    Tamano = len(Lista)
    Paquete = 2
    bandera = 1
    c = 0
    menlist = ""

    for i in Lista:
        menlist = menlist + i
        c = c + 1
        if c == Paquete:
            enviar(menlist)
            c = 0
            menlist = ""
        if ((Tamano % 2) != 0) and (i == Lista[Tamano - 1]):
            enviar(menlist)
            menlist = ""

def enviar(mensaje):
    s.sendto(mensaje, (direccion, puerto)) #Envio el mensaje al servidor

def recibir():
    Msjserv = s.recvfrom(1024)
    Msj = Msjserv[0]

    print "Mensaje del Servidor --> "+str(Msj)

main()
