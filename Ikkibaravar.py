from tkinter import *
from tkinter.messagebox import *
#gui taraf
oyna = Tk ()
oyna.geometry("350x250")
oyna.resizable(0, 0)
oyna.title("Bankdagi pul")

necha_marta = Entry(oyna,bd=1,width=15)
necha_marta.place(x=160,y=30)
necha_marta_label = Label(oyna,text = "Necha marta ko'paysin?").place(x=20,y=30)

bankdagi_pul = Entry(oyna,bd=1,width=30)
bankdagi_pul.place(x=100,y=60)
pul_qiymat = StringVar()
bankdagi_pul_label = Label(oyna,textvariable=pul_qiymat).place(x=20,y=60)
pul_qiymat.set("Bankdagi Pul")

pul_foizi = Entry(oyna,bd=1,width=30)
pul_foizi.place(x=100,y=90)
pul_foiz = StringVar()
pul_foizi_label = Label(oyna,textvariable=pul_foiz).place(x=20,y=90)
pul_foiz.set("Foiz")

#programmani mag'zi
def hisobla():
    S = int(bankdagi_pul.get())#qoyilgan pul
    p = int(pul_foizi.get())#foiz
    n = int(necha_marta.get())#necha marta 
    k=1
    result=0
    while result < n*S:
       k = k+0.00001
       result = S*(((p+100)/100)**k)
    k=round(k)
    result=round(result,2)
    print(result)
    result_pul.set("Hozirgi Pul:"+str(result)+"O'tgan Oy:"+str(k))
#pastdagi labelcha ;-)    
result_pul = StringVar()
result_label = Label(oyna,textvariable=result_pul).place(x=40,y=180)
result_pul.set("Hozi Javob chiqadi")

go = Button(oyna, text="Hisoblash", width=15, height=2,command=hisobla).place(x=120, y=120)


oyna.mainloop ()
