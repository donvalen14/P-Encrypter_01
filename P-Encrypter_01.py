from tkinter import Tk, Label, Entry, Button, mainloop
from pyperclip import copy

# Bearded Theme Monokai Black

window = Tk()
window.geometry("650x500+430+150")
window.title("Encrypter [Versión 1.5]")
listE, listD = list([" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","Ç",'"',"K","L","M","N","O","P","Q","€","R","S","T","U","V","¨","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","á","é","í","ó","ú","Á","É","Í","Ó","Ú","!",'J',"#","$","%","&","/","(",")","=","ç","'","?","\\","¿","¡",",","<",">","|","°","ª","¬","+","*","{","}","[","]",";",":",".","-","_","^","ñ","Ñ","@","º","`","´","~","·"]), list(["<","Ñ", "p", "L", "#", "!", "o","i", "k","K","l","P","ñ","O","7","1","9","5",'"',"í","%","&","/","(","ó",")","=","?","¿","'","¡","\\","a","q","A","¨","Q","e","Á","é","É","r","R","ª","t","T","y","Y","j","J","m","M","n","N","b","c","B","C","v","x","z","V","Z","X","s","d","f","g","D","G","F","h","H","u","U","á","^","€","~","ç","$","Í","8","Ó","ú","Ú","3","4","6","2","|","[","}","]",";",":","-","{","_","*","`","+","´","@"," ",".","º","0",">","E","I","Ç","S","W","w",",","¬","·","°"])
labels = []

def addLabel(textL, xL, yL, fgL):
    name = Label(window, text= textL, fg= fgL)
    name.place(x=xL,y=yL)
    labels.append(name)
updateL = lambda index, newText : labels[index].config(text=newText)
addLabel('>>Introdusca el texto que desea encriptar<<', 160, 10, None) # Label 0
intr = Entry(window, bg="white",fg="black")
intr.place(x=83,y=40,width=500)

def work(text, lista1, lista2):
    result = ""
    for letter in text:
        try:
            if letter in lista1:
                np = lista1.index(letter)
                letter = lista2[np]
            elif letter not in lista1:
                lista1.append(letter)
                nle = lista1.index(letter)
                letter = lista2[nle]
        except IndexError:
            letter += '(Caracter no válido)'
        result += letter
    return result

copyF = lambda text: copy(text)
def addButton(textB, fgB, commandB, xB, yB):
    name = Button(window, text = textB , fg = fgB, command = commandB)
    name.place(x=xB,y=yB)

addLabel(f'', 175, 120, 'blue') # Label 1
def click():
    updateL(1,f'El texto "{intr.get()}" fue encriptado exitosamente')
    mensaje_encrypt = work(intr.get(),listE,listD)
    encryptE = Entry(window, bg = "white", fg="black")
    encryptE.insert(0,mensaje_encrypt)
    encryptE.place(x=83,y=150,width=500)
    addButton('Copy', 'black', lambda : copyF(mensaje_encrypt), 265, 172)

buttom = Button(window,text="Encrypt", command= click)
buttom.place(x=265,y=80)
addLabel('>>Introdusca el texto que desea desencriptar<<', 160, 200, None) # Label 2
intrD = Entry(window,bg="white",fg="black")
intrD.place(x=83,y=240,width=500)
addLabel('', 83, 320, 'blue') # Label 3

def clickD():
    updateL(3, f'El texto "{intrD.get()}" fue desencriptado exitosamente')
    intrDe = Entry(window, bg="white",fg="black")
    intrDe.place(x=83,y=350,width=500)
    messageDecrypt = work(intrD.get(), listD, listE)
    intrDe.insert(0,messageDecrypt)
    copyD = lambda text: copy(text)
    addButton('Copy', 'black', lambda : copyD(messageDecrypt), 265, 375)
buttonD = Button(window,text="Decrypt", command= clickD)

buttonD.place(x=265,y=270)
window.mainloop()
