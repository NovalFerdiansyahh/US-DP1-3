from tkinter import *

root = Tk()
root.title("Konversi Bilangan")

# Function for Clearing screen
def clear_screen():
    output.delete(0, END)
    input_field.delete(0, END)

# Function for Decimal Conversion
def desimal():
    output.delete(0, END)
    try:
        angka = int(input_field.get())
    except ValueError:
        output.insert(0, "Bilangan Tidak Sesuai!")
        return
    bineri = bin(angka).replace("0b","")
    oktal = oct(angka).replace("0o","")
    heks = hex(angka).replace("0x","")
    
    output.insert(0, "Decimal: " + str(angka) + ", Biner: " + str(bineri) + ", Oktal: " + str(oktal) + ", Hexa: " + str(heks))

# Function for Binary Conversion
def biner():
    output.delete(0, END)
    try:
        angka = int(input_field.get(), 2)
    except ValueError:
        output.insert(0, "Bilangan Tidak Sesuai!")
        return
    oktal = oct(angka).replace("0o","")
    heks = hex(angka).replace("0x","")
    
    output.insert(0, "Decimal: " + str(angka) + ", Biner: " + str(input_field.get()) + ", Oktal: " + str(oktal) + ", Hexa: " + str(heks))

# Function for Octal Conversion
def oktal():
    output.delete(0, END)
    try:
        angka = int(input_field.get(), 8)
    except ValueError:
        output.insert(0, "Bilangan Tidak Sesuai!")
        return
    biner = bin(angka).replace("0b","")
    heks = hex(angka).replace("0x","")
    
    output.insert(0, "Decimal: " + str(angka) + ", Biner: " + str(biner) + ", Oktal: " + str(input_field.get()) + ", Hexa: " + str(heks))

# Function for Hexadecimal Conversion
def hexadecimal():
    output.delete(0, END)
    try:
        angka = int(input_field.get(), 16)
    except ValueError:
        output.insert(0, "Bilangan Tidak Sesuai!")
        return
    biner = bin(angka).replace("0b","")
    oktal = oct(angka).replace("0o","")
    
    output.insert(0, "Decimal: " + str(angka) + ", Biner: " + str(biner) + ", Oktal: " + str(oktal) + ", Hexa: " + str(input_field.get()))

# Function for ASCII Conversion
def str_to_ascii():
    output.delete(0, END)
    string = input_field.get()
    ascii_code = [ord(c) for c in string]
    output.insert(0, "ASCII code: " + str(ascii_code))


# Create Labels
label1 = Label(root, text="Konversi Bilangan", font=("Arial Bold", 20))
label2 = Label(root, text="Masukkan Bilangan:")
label3 = Label(root, text="Hasil Konversi:")

# Create Input Field
input_field = Entry(root, width=50)

# Create Output Field
output = Entry(root, width=50)

# Create Buttons
button1 = Button(root, text="Konversi Desimal", width=20, pady=8, command=desimal)
button2 = Button(root, text="Konversi Biner", width=20, pady=8, command=biner)
button3 = Button(root, text="Konversi Oktal", width=20, pady=8, command=oktal)
button4 = Button(root, text="Konversi Hexadecimal", width=20, pady=8, command=hexadecimal)
button5 = Button(root, text="Convert to ASCII", width=20, pady=8, command=str_to_ascii)
button6 = Button(root, text="Clear", width=20, pady=8, command=clear_screen)

#place labels
label1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
label2.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky='w')
label3.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky='w')

#place input fields
input_field.grid(row=2, column=0,columnspan=3, padx=10, pady=5, sticky='e')

#place output fields
output.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky='e')

#place buttons
button1.grid(row=5, column=1, pady=10, )
button2.grid(row=5, column=2, pady=10, )
button3.grid(row=6, column=1, pady=10, )
button4.grid(row=6, column=2, pady=10, )
button5.grid(row=7, column=1, pady=10, )
button6.grid(row=7, column=2, pady=10, )

# Set label2 and label3 to center alignment
label2.config(anchor='center')
label3.config(anchor='center')


root.mainloop()
