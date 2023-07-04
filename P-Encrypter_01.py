from tkinter import *

#primera lista enla que estan todos los caracteres
listE = list([" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","Ç",'"',"K","L","M","N","O","P","Q","€","R","S","T","U","V","¨","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","á","é","í","ó","ú","Á","É","Í","Ó","Ú","!",'J',"#","$","%","&","/","(",")","=","ç","'","?","\\","¿","¡",",","<",">","|","°","ª","¬","+","*","{","}","[","]",";",":",".","-","_","^","ñ","Ñ","@","º","`","´","·","~"])

#segunda lista en la que estan los mismos caracteres pero desordenados
listD = list(["<","Ñ", "p", "L", "#", "!", "o","i", "k","K","l","P","ñ","O","7","1","9","5",'"',"í","%","&","/","(","ó",")","=","?","¿","'","¡","\\","a","q","A","¨","Q","e","Á","é","É","r","R","ª","t","T","y","Y","j","J","m","M","n","N","b","c","B","C","v","x","z","V","Z","X","s","d","f","g","D","G","F","h","H","u","U","á","^","€","~","ç","$","Í","8","Ó","ú","Ú","","3","4","6","2","|","[","}","]",";",":","-","{","_","`","*","+","´","@"," ",".","º","0",">","E","I","Ç","S","W","w",",","¬","·","°"])
window = Tk()
window.geometry("650x500+430+150")
window.title("Encrypter [Versión 1.4]")

#label
inf = Label(window, text = ">>Introdusca el texto que desea encriptar<<")
inf.place(x=83,y=10)

#Entry en el que la persona escribe el texto que quiere encriptar
intr = Entry(window, bg="white",fg="black")
intr.place(x=83,y=40,width=500)

#def que hace la funcion de encriptar (la descripción dice como funciona esto)
def encrypt(text):
    result = ""
    for letter in text:
        if letter in listE:
            np = listE.index(letter)
            letter = listD[np]
            textE = letter
            #print(dir(set(listE)))
        elif not(letter in listE):
            listE.append(letter)
            nle = listE.index(letter)
            letter = listD[nle]
            textE = letter
        else:
            letter = letter
        result += textE
    return result


#este def es lo que se activa cuando la persona le da click, lo que hace es encriptar el texto ingresado e insertarlo en otro Entry
def click():
    text = Label(window, text=f'El texto "{intr.get()}" fue encriptado exitosamente', fg="lime")
    text.place(x=175,y=120)

    mensaje_encrypt = encrypt(intr.get())

    encryptE = Entry(window, bg = "white", width=50, fg="black")
    encryptE.insert(0,mensaje_encrypt)
    encryptE.place(x=83,y=150,width=500)


#Button para encriptar el texto ingresado
buttom = Button(window,text="Encrypt", command= click)
buttom.place(x=265,y=80)


#<----------------------------------------------------------DECRYPTER---------------------------------------------------------------------->#

#creo una variable con el texto que el usuario escribe pero ya encriptado, se guarda en esta variable
messageEncrypt = encrypt(intr.get())


#El def que hace la funcion de desencriptar
def decrypt(text):
    result = ""
    for letter in text:
        if letter in listD:
            np = listD.index(letter)
            letter = listE[np]
            textD = letter
        else:
            textD = letter
        result += textD
    return result

infD = Label(window,text=">>Introdusca el texto que desea desencriptar<<")
infD.place(x=160,y=200)

#Entry donde la persona escribe lo que quiere desencriptar
intrD = Entry(window,bg="white",fg="black")
intrD.place(x=83,y=240,width=500)

#La  funcion que se activa al hacer click en el boton "Decrypt" osea desencriptar
def clickD():
    textD = Label(window,text=f'El texto "{intrD.get()}" fue desencriptado exitosamente', fg="lime")
    textD.place(x=83,y=320)

    intrDe = Entry(window, bg="white",fg="black")
    intrDe.place(x=83,y=350,width=500)

    messageDecrypt = decrypt(intrD.get())

    intrDe.insert(0,messageDecrypt)

#Botton para desencriptar
buttonD = Button(window,text="Decrypt", command= clickD)
buttonD.place(x=265,y=280)

window.mainloop()
