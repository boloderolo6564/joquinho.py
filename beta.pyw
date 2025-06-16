from function import *
import tkinter as tk


def atualizar_pontos():
    data_save = ler()
    label.config(text=f"Pontos: {data_save["usuario"]['clique']}")
    root.after(1000, atualizar_pontos)

root = tk.Tk()
root.title("joquinho.py")
root.geometry("600x400")
root.configure(bg="#1C1616")
root.resizable(False, False)

data_save = ler()

frame_principal = tk.Frame(root)
frame_principal.pack(fill="both", expand=True)


barra = tk.Label(frame_principal,bg="#4D00FF")
barra.place(x=0, y=0, width=400, height=35)

label = tk.Label(frame_principal,)
label.place(x=0, y=0, width=66, height=35)

frame_lateral = tk.Frame(frame_principal, width=200,bg="#4D00FF")
frame_lateral.pack(side="right", fill="y")


# Canvas e Scrollbar só dentro da parte lateral
canvas = tk.Canvas(frame_lateral, width=180, bg="#4D00FF")
scrollbar = tk.Scrollbar(frame_lateral, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#4D00FF")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

for index,(i,b) in enumerate(zip(data_save["store"]["itens"],data_save["store"]["price"])):
    tk.Label(scrollable_frame, text=f"{i}", bg="#d0ffd0").grid(row= index,column=1,)
    tk.Button(scrollable_frame, text=f"{b}").grid(row= index,column=2,)

atualizar_pontos()

label = tk.Label(frame_principal,bg="#46D4D1",)
label.place(x=0, y=0, width=66, height=35)

button = tk.Button(frame_principal,bg="#26A8DB", text='Clique-me', command=lambda:clicado(data_save))
button.place(x=136, y=153, width=139, height=120)

root.mainloop()




