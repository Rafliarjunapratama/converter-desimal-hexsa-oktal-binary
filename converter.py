from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.geometry("800x800")
root.title("Converter Desimal")

img= (Image.open("7.jpg"))
resized_image= img.resize((190,180), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

def hilang_enter(i):
		Engtry.delete(0,'end')
def keluar_enter(i):
	if Engtry.get() == "":
		Engtry.insert(0,"\t         Masukan Nilai Desimal ")
		Engtry.bind("<FocusIn>",hilang_enter)
		
def hilang_enter1(i):
		Engtry.delete(0,'end')
def keluar_enter1(i):
	if Engtry.get() == "":
		Engtry.insert(0,"\t         Masukan Nilai Binary ")
		Engtry.bind("<FocusIn>",hilang_enter)
		
def hilang_enter2(i):
		Engtry.delete(0,'end')
def keluar_enter2(i):
	if Engtry.get() == "":
		Engtry.insert(0,"\t         Masukan Nilai Hexsa ")
		Engtry.bind("<FocusIn>",hilang_enter)
		
def hilang_enter3(i):
		Engtry.delete(0,'end')
def keluar_enter3(i):
	if Engtry.get() == "":
		Engtry.insert(0,"\t         Masukan Nilai Octal ")
		Engtry.bind("<FocusIn>",hilang_enter)
		
def def1_menux():
	prame = Frame(frame_samping,bg="#FFFFFF")
	lakbel1 = Label(prame,font=('Consolas 10 bold'),text="Desimal Converter",bg="#FFFFFF")
	lakbel1.pack(pady=10)
	global Engtry
	lbil1 = Label(prame,text="Nilai Desimal :",font=("default",4),bg="#FFFFFF")
	lbil1.pack(anchor=NW)
	
	Engtry = Entry(prame,width=38,font=("default", 5 ),bg="#FFFFFF",highlightthickness=2,highlightbackground="black")
	Engtry.pack(ipady=10)
	Engtry.insert(0,"\t     Masukan Nilai Desimal ")
	Engtry.bind("<FocusIn>",hilang_enter)
	Engtry.bind("<FocusOut>",keluar_enter)
	
	
	tombol = Button(prame,text="  Sumbit ",command=def1_proses)
	tombol.config(bd=0, font=("Bold",5),bg="#FFFFFF",fg="#1b1b1b",highlightthickness=2,highlightbackground="#1b1b1b",activebackground="#1b1b1b",activeforeground="#FFFFFF",width=2)
	tombol.pack(pady=20)
	
	prame.pack()
	
def def1_proses():
	prame = Frame(frame_samping,bg="#FFFFFF")

	#binary
	int_engtry = int(Engtry.get())
	variabel_proses_binary = bin(int_engtry)
	inisialisasi_string_binary = str(variabel_proses_binary)
	
	#octal
	variabel_proses_octal = oct(int_engtry)
	inisialisasi_string_octal = str(variabel_proses_octal)
	
	#hexsa
	variabel_proses_hexsa = hex(int_engtry)
	inisialisasi_string_hexsa = str(variabel_proses_hexsa)
	
	#binary output
	Hasil_proses_binary = inisialisasi_string_binary.replace("0b","")
	Hasil_proses_binary1 = "Binary Convert : "+Hasil_proses_binary
	Hasil_proses_binary2 = Label(prame,text=Hasil_proses_binary1,font=("'Consolas",6,"bold"),bg="#FFFFFF",highlightthickness=2,highlightbackground="#1b1b1b",width=30)
	Hasil_proses_binary2.pack(ipady=3)
	
	#octal output
	Hasil_proses_octal = inisialisasi_string_octal.replace("0o","")
	Hasil_proses_octal1 = "Octal Convert : "+Hasil_proses_octal
	Hasil_proses_octal2 = Label(prame,text=Hasil_proses_octal1,font=("'Consolas",6,"bold"),bg="#FFFFFF",highlightthickness=2,highlightbackground="#1b1b1b",width=30)
	Hasil_proses_octal2.pack(pady=15,ipady=3)
	
	#hexsa output
	Hasil_proses_hexsa = inisialisasi_string_hexsa.replace("0x","")
	Hasil_proses_hexsa1 = "Hexsa Convert : "+Hasil_proses_hexsa
	Hasil_proses_hexsa2 = Label(prame,text=Hasil_proses_hexsa1,font=("'Consolas",6,"bold"),bg="#FFFFFF",highlightthickness=2,highlightbackground="#1b1b1b",width=30)
	Hasil_proses_hexsa2.pack(pady=15,ipady=3)
	prame.pack()

#// binery
def def2_menux():
	prame = Frame(frame_samping,bg="#FFFFFF")
	lakbel1 = Label(prame,font=('Consolas 10 bold'),text="Binary Converter",bg="#FFFFFF")
	lakbel1.pack(pady=10)
	global Engtry
	lbil1 = Label(prame,text="Nilai Binary :",font=("default",4),bg="#FFFFFF")
	lbil1.pack(anchor=NW)
	
	Engtry = Entry(prame,width=38,font=("default", 5 ),bg="#FFFFFF",highlightthickness=2,highlightbackground="black")
	Engtry.pack(ipady=10)
	Engtry.insert(0,"\t     Masukan Nilai Binary ")
	Engtry.bind("<FocusIn>",hilang_enter1)
	Engtry.bind("<FocusOut>",keluar_enter1)
	
	
	tombol = Button(prame,text="  Sumbit ",command=def2_proses)
	tombol.config(bd=0, font=("Bold",5),bg="#FFFFFF",fg="#1b1b1b",highlightthickness=2,highlightbackground="#1b1b1b",activebackground="#1b1b1b",activeforeground="#FFFFFF",width=2)
	tombol.pack(pady=20)
	
	prame.pack()
	
def def2_proses():
	prame = Frame(frame_samping,bg="#FFFFFF")

	#Desimal
	int_engtry = int(Engtry.get(),2)
	inisialisasi_string_Desimal = str(int_engtry)
	
	#octal
	variabel_proses_octal = oct(int_engtry)
	inisialisasi_string_octal = str(variabel_proses_octal)
	
	#hexsa
	variabel_proses_hexsa = hex(int_engtry)
	inisialisasi_string_hexsa = str(variabel_proses_hexsa)
	
	#Desimal output
	Hasil_proses_Desimal = inisialisasi_string_Desimal.replace("0b","")
	Hasil_proses_Desimal1 = "Desimal Convert : "+Hasil_proses_Desimal
	Hasil_proses_Desimal2 = Label(prame,text=Hasil_proses_Desimal1,font=("'Consolas",6,"bold"),bg="#FFFFFF",highlightthickness=2,highlightbackground="#1b1b1b",width=30)
	Hasil_proses_Desimal2.pack(ipady=3)
	
	#octal output
	Hasil_proses_octal = inisialisasi_string_octal.replace("0o","")
	Hasil_proses_octal1 = "Octal Convert : "+Hasil_proses_octal
	Hasil_proses_octal2 = Label(prame,text=Hasil_proses_octal1,font=("'Consolas",6,"bold"),bg="#FFFFFF",highlightthickness=2,highlightbackground="#1b1b1b",width=30)
	Hasil_proses_octal2.pack(pady=15,ipady=3)
	
	#hexsa output
	Hasil_proses_hexsa = inisialisasi_string_hexsa.replace("0x","")
	Hasil_proses_hexsa1 = "Hexsa Convert : "+Hasil_proses_hexsa
	Hasil_proses_hexsa2 = Label(prame,text=Hasil_proses_hexsa1,font=("'Consolas",6,"bold"),bg="#FFFFFF",highlightthickness=2,highlightbackground="#1b1b1b",width=30)
	Hasil_proses_hexsa2.pack(pady=15,ipady=3)
	prame.pack()

#//hexsa

def def3_menux():
	prame = Frame(frame_samping,bg="#FFFFFF")
	lakbel1 = Label(prame,font=('Consolas 10 bold'),text="Hexsa Converter",bg="#FFFFFF")
	lakbel1.pack(pady=10)
	global Engtry
	lbil1 = Label(prame,text="Nilai Hexsa :",font=("default",4),bg="#FFFFFF")
	lbil1.pack(anchor=NW)
	
	Engtry = Entry(prame,width=38,font=("default", 5 ),bg="#FFFFFF",highlightthickness=2,highlightbackground="black")
	Engtry.pack(ipady=10)
	Engtry.insert(0,"\t     Masukan Nilai Hexsa ")
	Engtry.bind("<FocusIn>",hilang_enter2)
	Engtry.bind("<FocusOut>",keluar_enter2)
	
	
	tombol = Button(prame,text="  Sumbit ",command=def3_proses)
	tombol.config(bd=0, font=("Bold",5),bg="#FFFFFF",fg="#1b1b1b",highlightthickness=2,highlightbackground="#1b1b1b",activebackground="#1b1b1b",activeforeground="#FFFFFF",width=2)
	tombol.pack(pady=20)
	
	prame.pack()
	
def def3_proses():
	prame = Frame(frame_samping,bg="#FFFFFF")

	#Desimal
	int_engtry = int(Engtry.get(),16)
	inisialisasi_string_Desimal = str(int_engtry)
	
	#octal
	variabel_proses_octal = oct(int_engtry)
	inisialisasi_string_octal = str(variabel_proses_octal)
	
	#Binary
	variabel_proses_binary = bin(int_engtry)
	inisialisasi_string_binary = str(variabel_proses_binary)
	
	#Desimal output
	Hasil_proses_Desimal = inisialisasi_string_Desimal.replace("0b","")
	Hasil_proses_Desimal1 = "Desimal Convert : "+Hasil_proses_Desimal
	Hasil_proses_Desimal2 = Label(prame,text=Hasil_proses_Desimal1,font=("'Consolas",6,"bold"),bg="#FFFFFF",highlightthickness=2,highlightbackground="#1b1b1b",width=30)
	Hasil_proses_Desimal2.pack(ipady=3)
	
	#octal output
	Hasil_proses_octal = inisialisasi_string_octal.replace("0o","")
	Hasil_proses_octal1 = "Octal Convert : "+Hasil_proses_octal
	Hasil_proses_octal2 = Label(prame,text=Hasil_proses_octal1,font=("'Consolas",6,"bold"),bg="#FFFFFF",highlightthickness=2,highlightbackground="#1b1b1b",width=30)
	Hasil_proses_octal2.pack(pady=15,ipady=3)
	
	#Binary output
	Hasil_proses_Binary = inisialisasi_string_binary.replace("0b","")
	Hasil_proses_Binary1 = "Binary Convert : "+Hasil_proses_Binary
	Hasil_proses_Binary2 = Label(prame,text=Hasil_proses_Binary1,font=("'Consolas",6,"bold"),bg="#FFFFFF",highlightthickness=2,highlightbackground="#1b1b1b",width=30)
	Hasil_proses_Binary2.pack(pady=15,ipady=3)
	prame.pack()
	
#//Octal
def def4_menux():
	prame = Frame(frame_samping,bg="#FFFFFF")
	lakbel1 = Label(prame,font=('Consolas 10 bold'),text="Octal Converter",bg="#FFFFFF")
	lakbel1.pack(pady=10)
	global Engtry
	lbil1 = Label(prame,text="Nilai Octal :",font=("default",4),bg="#FFFFFF")
	lbil1.pack(anchor=NW)
	
	Engtry = Entry(prame,width=38,font=("default", 5 ),bg="#FFFFFF",highlightthickness=2,highlightbackground="black")
	Engtry.pack(ipady=10)
	Engtry.insert(0,"\t     Masukan Nilai Octal ")
	Engtry.bind("<FocusIn>",hilang_enter3)
	Engtry.bind("<FocusOut>",keluar_enter3)
	
	
	tombol = Button(prame,text="  Sumbit ",command=def4_proses)
	tombol.config(bd=0, font=("Bold",5),bg="#FFFFFF",fg="#1b1b1b",highlightthickness=2,highlightbackground="#1b1b1b",activebackground="#1b1b1b",activeforeground="#FFFFFF",width=2)
	tombol.pack(pady=20)
	
	prame.pack()
	
def def4_proses():
	prame = Frame(frame_samping,bg="#FFFFFF")

	#Desimal
	int_engtry = int(Engtry.get(),8)
	inisialisasi_string_Desimal = str(int_engtry)
	
	#hexsa
	variabel_proses_hexsa = hex(int_engtry)
	inisialisasi_string_hexsa = str(variabel_proses_hexsa)
	
	#Binary
	variabel_proses_binary = bin(int_engtry)
	inisialisasi_string_binary = str(variabel_proses_binary)
	
	#Desimal output
	Hasil_proses_Desimal = inisialisasi_string_Desimal.replace("0b","")
	Hasil_proses_Desimal1 = "Desimal Convert : "+Hasil_proses_Desimal
	Hasil_proses_Desimal2 = Label(prame,text=Hasil_proses_Desimal1,font=("'Consolas",6,"bold"),bg="#FFFFFF",highlightthickness=2,highlightbackground="#1b1b1b",width=30)
	Hasil_proses_Desimal2.pack(ipady=3)
	
	#Hexsa output
	Hasil_proses_hexsa = inisialisasi_string_hexsa.replace("0x","")
	Hasil_proses_hexsa1 = "Hexsa Convert : "+Hasil_proses_hexsa
	Hasil_proses_hexsa2 = Label(prame,text=Hasil_proses_hexsa1,font=("'Consolas",6,"bold"),bg="#FFFFFF",highlightthickness=2,highlightbackground="#1b1b1b",width=30)
	Hasil_proses_hexsa2.pack(pady=15,ipady=3)
	#Binary output
	Hasil_proses_Binary = inisialisasi_string_binary.replace("0b","")
	Hasil_proses_Binary1 = "Binary Convert : "+Hasil_proses_Binary
	Hasil_proses_Binary2 = Label(prame,text=Hasil_proses_Binary1,font=("'Consolas",6,"bold"),bg="#FFFFFF",highlightthickness=2,highlightbackground="#1b1b1b",width=30)
	Hasil_proses_Binary2.pack(pady=15,ipady=3)
	prame.pack()
	
def hapus():
	for frame in frame_samping.winfo_children():
		frame.destroy()
def menu(menux):
	hapus()
	menux()

		
frame_123 = Frame(root,bg="#0059FF")

canvas1= Canvas(frame_123, width= 220, height= 220,bg="#0059FF",highlightthickness=0)
canvas1.pack()
canvas1.create_image(15,5, anchor=NW, image=new_image)
lakbel = Label(frame_123,font=('Consolas 4 bold'),text="Kelompok 3",bg="#0059FF",fg="white")
lakbel.place(x=46, y=200)

frame_556 = Frame(frame_123,bg="#FFFFFF")
frame_556.place(x=0, y=249)
frame_556.configure(width=220,height=2)

buton = Button(frame_123,text="Desimal \t  ",bd=0, font=("Bold",5),bg="#0059FF",fg="#E4E4E4",height=1,highlightthickness=0,activebackground="#FFFFFF",activeforeground="#0059FF",command=lambda : menu(def1_menux))
buton.place(x=0, y=250)

frame_556 = Frame(frame_123,bg="#FFFFFF")
frame_556.place(x=0, y=315)
frame_556.configure(width=220,height=2)

buton1 = Button(frame_123,text=" Binary   \t    ",bd=0, font=("Bold",5),bg="#0059FF",fg="#E4E4E4",height=1,highlightthickness=0,activebackground="#FFFFFF",activeforeground="#0059FF",command=lambda : menu(def2_menux))
buton1.place(x=0, y=316)

frame_556 = Frame(frame_123,bg="#FFFFFF")
frame_556.place(x=0, y=380)
frame_556.configure(width=220,height=2)

buton2= Button(frame_123,text=" Hexsa  \t ",bd=0, font=("Bold",5),bg="#0059FF",fg="#E4E4E4",height=1,highlightthickness=0,activebackground="#FFFFFF",activeforeground="#0059FF",command=lambda : menu(def3_menux))
buton2.place(x=0, y=381)

frame_556 = Frame(frame_123,bg="#FFFFFF")
frame_556.place(x=0, y=448)
frame_556.configure(width=220,height=2)

buton2= Button(frame_123,text=" Oktal  \t ",bd=0, font=("Bold",5),bg="#0059FF",fg="#E4E4E4",height=1,highlightthickness=0,activebackground="#FFFFFF",activeforeground="#0059FF",command=lambda : menu(def4_menux))
buton2.place(x=0, y=450)

frame_556 = Frame(frame_123,bg="#FFFFFF")
frame_556.place(x=0, y=515)
frame_556.configure(width=220,height=2)

frame_123.pack(side=LEFT)
frame_123.pack_propagate(False)
frame_123.configure(width=220,height=800)

frame_samping = Frame(root,highlightbackground="white",highlightthickness=2,bg="#FFFFFF")

frame_samping.pack(side=LEFT)
frame_samping.pack_propagate(False)
frame_samping.configure(width=700,height=800)
def1_menux()
root.mainloop()