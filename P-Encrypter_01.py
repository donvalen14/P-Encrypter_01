from tkinter import Tk, Label, Entry, Button, mainloop
from pyperclip import copy

#tengo que explicar esto?
window = Tk()
window.geometry("650x500+430+150")
window.title("Encrypter [Versión 1.4]")

#Las 2 listas, la primera 'listE' Todos los caracteres que se pueden usar en el programa. La segunda 'listD' Lo mismo pero desordenado.
listE, listD = list([" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","Ç",'"',"K","L","M","N","O","P","Q","€","R","S","T","U","V","¨","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","á","é","í","ó","ú","Á","É","Í","Ó","Ú","!",'J',"#","$","%","&","/","(",")","=","ç","'","?","\\","¿","¡",",","<",">","|","°","ª","¬","+","*","{","}","[","]",";",":",".","-","_","^","ñ","Ñ","@","º","`","´","·","~"]), list(["<","Ñ", "p", "L", "#", "!", "o","i", "k","K","l","P","ñ","O","7","1","9","5",'"',"í","%","&","/","(","ó",")","=","?","¿","'","¡","\\","a","q","A","¨","Q","e","Á","é","É","r","R","ª","t","T","y","Y","j","J","m","M","n","N","b","c","B","C","v","x","z","V","Z","X","s","d","f","g","D","G","F","h","H","u","U","á","^","€","~","ç","$","Í","8","Ó","ú","Ú","","3","4","6","2","|","[","}","]",";",":","-","{","_","`","*","+","´","@"," ",".","º","0",">","E","I","Ç","S","W","w",",","¬","·","°"])

#una funcion para simplificar la creacion de labels
def addLabel(textL, xL, yL, fgL):
    name = Label(window, text= textL, fg= fgL)
    name.place(x=xL,y=yL)

#tengo que explicar esto?
addLabel('>>Introdusca el texto que desea encriptar<<', 160, 10, None)

#tengo que explicar esto?
intr = Entry(window, bg="white",fg="black")
intr.place(x=83,y=40,width=500)

#Ok esta es la funcion que lo hace todo, lo demas es adorno. Resumido: Recibe un texto 'text' que es la palabra que se va a encriptar/desencriptar.
#Depende de si 'lista1' es 'listE' y 'lista2' es 'listD' y vicebersa. 
def work(text, lista1, lista2):
    #tengo que explicar que es 'result'???
    result = ""
    #bucle for por cada letra de la palabra que sera encriptada/desencriptada
    for letter in text:
        #dentro de un try por si acaso
        try:
            #tengo q explicar este if?
            if letter in lista1:
                #se guarda en 'np' la posicion en la que esta 'letter' en la 'lista1'.
                np = lista1.index(letter)
                #entre muchas comillas encripta la letra y pasa a ser el caracter de la otra lista que esta en su misma posicion osea...
                #si 'letter' es 'd' y 'd' esta en la posicion 4 en 'lista1' entonces lo cambia por el caracter de 'lista2' en la posicion 4 que seria '#'
                #y en el caso de desencriptacion simplemente cambia el valor de 'lista1' por el de 'lista2' y vicebersa.
                letter = lista2[np]
            #si 'letter' no esta en 'lista1' se le agrega a 'lista1' el caracter desconocido
            elif letter not in lista1:
                #sinceramente no se que quizo hacer mi yo del pasado pero esto de aca no le encuentro sentido, dejenlo ahi o saquenlo (no creo que alguien lea esto)
                lista1.append(letter)
                nle = lista1.index(letter)
                letter = lista2[nle]
        #no voy a explicar esto
        except IndexError:
            letter += '(Caracter no válido)'
        #despues de todo a 'result' se le agrega cada letra de la palabra que seria encriptada/desencriptada
        result += letter
    #tengo q explicar esto
    return result

#funcion para copiar :/
copyF = lambda text: copy(text)

#funcion para simplificar la creacion de botones... no c xq hago esto nadie va a leer esto, estoy aburrido doy verguenza y soy un fracaso
def addButton(textB, fgB, commandB, xB, yB):
    name = Button(window, text = textB , fg = fgB, command = commandB)
    name.place(x=xB,y=yB)

#no tengo ganas de comentar esto ademas no creo q haga falta
def click():
    #j4w34grg
    addLabel(f'El texto "{intr.get()}" fue encriptado exitosamente', 175, 120, 'blue')

    #wrjgw30r
    mensaje_encrypt = work(intr.get(),listE,listD)
    #wirw9'0    G
    encryptE = Entry(window, bg = "white", fg="black")
    encryptE.insert(0,mensaje_encrypt)
    encryptE.place(x=83,y=150,width=500)
    #eogrvjqerg
    addButton('Copy', 'black', lambda : copyF(mensaje_encrypt), 265, 172)

#tampoco quiero comentar lo q sigue 
buttom = Button(window,text="Encrypt", command= click)
buttom.place(x=265,y=80)
#<----------------------------------------------------------DECRYPTER---------------------------------------------------------------------->#
#iwjg9qrw3g
addLabel('>>Introdusca el texto que desea desencriptar<<', 160, 200, None)
#jgr3j3w
intrD = Entry(window,bg="white",fg="black")
intrD.place(x=83,y=240,width=500)
#no creo q tenga q explicar esto no?
def clickD():
    #invadan polonia
    addLabel(f'El texto "{intrD.get()}" fue desencriptado exitosamente', 83, 320, 'blue')
    intrDe = Entry(window, bg="white",fg="black")
    intrDe.place(x=83,y=350,width=500)
    #1939
    messageDecrypt = work(intrD.get(), listD, listE)
    #revivan el sacro imperio romano germánico
    intrDe.insert(0,messageDecrypt)
    copyD = lambda text: copy(text)
    #revivan el imperio azteca
    addButton('Copy', 'black', lambda : copyD(messageDecrypt), 265, 375)
#bolivia no deberia existir
buttonD = Button(window,text="Decrypt", command= clickD)
buttonD.place(x=265,y=270)
#1889
window.mainloop()
