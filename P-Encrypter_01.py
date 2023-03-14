from tkinter import *

listE = list([" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I",'"',"K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","á","é","í","ó","ú","Á","É","Í","Ó","Ú","!",'J',"#","$","%","&","/","(",")","=","'","?","\\","¿","¡",",","<",">","|","°","¬","+","*","~","{","}","[","]",";",":",".","-","_","^","ñ","Ñ","@"])

listD = list(["<","Ñ", "p", "L", "#", "!", "o","i", "k","K","l","P","ñ","O","7","1","9","5",'"',"í","%","&","/","(","ó",")","=","?","¿","'","¡","\\","a","q","A","Q","e","Á","é","É","r","R","t","T","y","Y","j","J","m","M","n","N","b","c","B","C","v","x","z","V","Z","X","s","d","f","g","D","G","F","h","H","u","U","á","^","$","Í","8","Ó","ú","Ú","\\","3","4","6","2","|","¬","ŋ","ł","↓","ŧ","ø","~","[","}","]",";",":","-","{","_","`","*","+","´","@","“","»","æ","«","ĸ","€","↓"])

window = Tk()
window.geometry("650x500+430+150")
window.title("Encrypter")

#label
inf = Label(window, text = ">>Introdusca el texto que desea encriptar<<")
inf.place(x=170,y=10)

#Entry major
intr = Entry(window, bg="white",fg="black")
intr.place(x=83,y=40,width=500)

#box encrypter
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


#box click button
def click():
    text = Label(window, text=f'El texto "{intr.get()}" fue encriptado exitosamente', fg="lime")
    text.place(x=175,y=120)

    mensaje_encrypt = encrypt(intr.get())

    encryptE = Entry(window, bg = "white", width=50, fg="black")
    encryptE.insert(0,mensaje_encrypt)
    encryptE.place(x=83,y=150,width=500)


#Button
buttom = Button(window,text="Encrypt", command= click)
buttom.place(x=265,y=80)


#<----------------------------------------------------------DECRYPTER---------------------------------------------------------------------->#

messageEncrypt = encrypt(intr.get())


#BOX DECRYPT
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

intrD = Entry(window,bg="white",fg="black")
intrD.place(x=83,y=240,width=500)

def clickD():
    textD = Label(window,text=f'El texto "{intrD.get()}" fue desencriptado exitosamente', fg="lime")
    textD.place(x=160,y=320)

    intrDe = Entry(window, bg="white",fg="black")
    intrDe.place(x=83,y=350,width=500)

    messageDecrypt = decrypt(intrD.get())

    intrDe.insert(0,messageDecrypt)


buttonD = Button(window,text="Decrypt", command= clickD)
buttonD.place(x=265,y=280)

window.mainloop()

