from customtkinter import*

window = CTk()
window.geometry("500x500")
window.title("puuuuuuuuk")
window.configure(fg_color="red")

knopka = CTkButton(window, text="click")
knopka.pack()

nadpus = CTkLabel(window, text="text")
nadpus.pack

window.mainloop()