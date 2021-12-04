""""
Gato

1. Tener un menu con 3 opciones
    Intrucciones
    Jugar
    Salir

2. Al jugar
    Tener un tablero
    Imprimir el tablero
    Empezar tirando X
    Validar que el espacio este libre
    Validar que aun no haya un ganador
    Validar que no sea empate
    Tira la compu
    Validar que el espacio este libre
    Validar que aun no haya un ganador
    Validar que no sea empate
"""
import random



#Empieza el juego
def jugar():
    
#crea la matriz
    def crear (a, b):
        matriz=[]
        for i in range(a):
            matriz.append([])
            for j in range(b):
                matriz[i].append('_')
        return matriz
    
#Hace que el tablero sea de 3x3
    def tablero (matriz):
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                print ("%2s" % matriz[i][j], end= ' ')
            print()
            
#Valida que el numero que elegiste este entre 1-9      
    def validarturno(): 
        print()
        print("Jugador X tire")
        pos = int(input("¿Dónde quiere tirar?: "))
        while pos < 0 or pos > 9:
            print()
            print("Esa no es una posición valida")
            pos = int(input("¿Dónde quiere tirar?: "))
        return pos


# La funcion que se usa si el usuario quiere poner una posicion que ya esta ocupada
    def turnos2 (m):
        print()
        x = 'X'
        print("Jugador X tire")
        pos = int(input("¿Dónde quiere tirar?: "))
        while pos < 0 or pos > 9:
            print()
            print("Esa no es una posición valida")
            pos = int(input("¿Dónde quiere tirar?: "))
        validacion(m, pos, x)
    
#Pone las X o O en el tablero
    def modifica_celda(m, r, c, x):
        if m[r][c] == '_':
            m[r][c] = x
        
        else:      
            if x == 'O':
                tiro_compu(m)
        
            elif x == 'X':
                print("Esa posición ya esta ocupada")
                turnos2(m)    
        return m
 
#Convierte el numero que dio el usuario a coordenadas
    def validacion(m, pos, x):
        if pos == 1:
            r = 0
            c = 0
        elif pos == 2:
            r = 0
            c = 1
        elif pos == 3:
            r = 0
            c = 2
        elif pos == 4:
            r = 1
            c = 0
        elif pos == 5:
            r = 1
            c = 1
        elif pos == 6:
            r = 1
            c = 2
        elif pos == 7:
            r = 2
            c = 0
        elif pos == 8:
            r = 2
            c = 1
        elif pos == 9:
            r = 2
            c = 2
    
        modifica_celda(m, r, c, x)
        
#Verifica que no haya un empate    
    def empate(m):
        cont = 0
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] != '_':
                    cont = cont + 1
                    if cont == 9:
                        return "empate"
                
#Valida si ya hay un ganador
    def ganador (m):
#SI GANA EL JUGADOR
        if 'X' == m[0][0] and 'X' == m[0][1] and 'X' == m[0][2]:
            return "gano"
        elif 'X' == m[1][0] and 'X' == m[1][1] and 'X' == m[1][2]:
            return "gano"
        elif 'X' == m[2][0] and 'X' == m[2][1] and 'X' == m[2][2]:
            return "gano"
        elif 'X' == m[0][0] and 'X' == m[1][0] and 'X' == m[2][0]:
            return "gano"
        elif 'X' == m[0][1] and 'X' == m[1][1] and 'X' == m[2][1]:
            return "gano"
        elif 'X' == m[0][2] and 'X' == m[1][2] and 'X' == m[2][2]:
            return "gano"
        elif 'X' == m[0][0] and 'X' == m[1][1] and 'X' == m[2][2]:
            return "gano"
        elif 'X' == m[2][0] and 'X' == m[1][1] and 'X' == m[0][2]:
            return "gano"
#CUANDO GANA LA COMPU
        if 'O' == m[0][0] and 'O' == m[0][1] and 'O' == m[0][2]:
            return "gano"
        elif 'O' == m[1][0] and 'O' == m[1][1] and 'O' == m[1][2]:
           return "gano"
        elif 'O' == m[2][0] and 'O' == m[2][1] and 'O' == m[2][2]:
            return "gano"
        elif 'O' == m[0][0] and 'O' == m[1][0] and 'O' == m[2][0]:
            return "gano"
        elif 'O' == m[0][1] and 'O' == m[1][1] and 'O' == m[2][1]:
            return "gano"
        elif 'O' == m[0][2] and 'O' == m[1][2] and 'O' == m[2][2]:
            return "gano"
        elif 'O' == m[0][0] and 'O' == m[1][1] and 'O' == m[2][2]:
            return "gano"
        elif 'O' == m[2][0] and 'O' == m[1][1] and 'O' == m[0][2]:
            return "gano"

#Genera el tiro de la compu      
    def tiro_compu(m):
        x ='O'
        tc = random.randint(1,9)
        validacion(m,tc,x)
        
#Es el main, llegan valores y manda los valores a las funciones
    def mainjuego():
    
        m = crear(3, 3)   
        continua = True
        while continua == True:
        
            pos = validarturno()

            x = 'X'
            validacion (m, pos, x)#aqui mismo mandas la validacion a modifica_celda
            tablero(m)
                
    
            mes = ganador(m)
            if mes == "gano":
                print()
                print("Felicidades ha ganado")
                print("Ganador jugador 'X'")
                break
            
#Si el jugador gana para el juego
            
            emp = empate(m)
            if emp == "empate":
                print()
                print("GATO")
                print("EMPATE")
                break
    
        
            print()
            print("Tiro de la computadora '0'")
            print()
            tiro_compu(m)
            tablero(m)

        
            mes = ganador(m)
            if mes == "gano":
                print()
                print("Ha perdido, suertre en la próxima")
                print("Ganador jugador 'O'")
                break   
#Si la compu gana, para el juego
            
    mainjuego()
    
print("BIENVENDIO A GATO")
#Es el menu
def menu():
    print()
    print("MENU")
    print("1. ¿Cómo se juega?")
    print("2. Jugar")
    print("3. Salir")
    print()

def main():
    continuar = True
    while continuar == True:
#Hace que el menu se repita hasta que selecciones la opcion de salir
        menu()
        opcion = int(input("¿Qué quieres hacer?: "))
        if opcion == 1:
            file = open("Intruccionesgato.txt", "r")
            ins = file.read()
            print(ins)
            file.close()
            
        
        elif opcion == 2 :
            file = open("Jugar.txt", "r")
            ins = file.read()
            print(ins)
            file.close()
            
            jugar()
            break
            
        elif opcion == 3:
            print("Gracias, nos vemos pronto!")
            continuar = False
            
            
        else:
            print("Elige una opcion valida")
            
main()



"""
CASOS PRUEBA: (Los casos son totalmente aleatorios)

Input: 2 (¿Qué quieres hacer?)
Input : 1 (¿Dónde quiere tirar?)
Output: Tiro de la compu que es aleatorio
Input : 9 (¿Dónde quiere tirar?)
Output: Tiro de la compu que es aleatorio
Input : 2 (¿Dónde quiere tirar?)
Output: Tiro de la compu que es aleatorio
Input : 2 (¿Dónde quiere tirar?)
Output: Esa posición ya esta ocupada
Input : 5 (¿Dónde quiere tirar?)
Output: Felicidades ha ganado
        Ganador jugador 'X'
        
"""