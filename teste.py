from function import *
import tkinter as tk

def on_configure(event):
    canvas_width = event.width
    canvas.itemconfig(window_id, width=canvas_width)

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

frame_lateral = tk.Frame(frame_principal, width=200,bg="#46D4D1")
frame_lateral.pack(side="right", fill="y")

canvas = tk.Canvas(frame_lateral, width=180, bg="#46D4D1")
scrollbar = tk.Scrollbar(frame_lateral, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#46D4D1")

barra = tk.Label(frame_principal,bg="#4D00FF")
barra.place(x=0, y=0, width=400, height=35)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.bind("<Configure>", on_configure)

window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

storename = tk.Label(frame_lateral,text="STORE",bg="#659291")
storename.place(x=400, y=0, width=200, height=35)

for index, (item, price) in enumerate(zip(data_save["store"]["itens"], data_save["store"]["price"])):
    index +=1
    label = tk.Label(scrollable_frame, text=item, bg="#d0ffd0")
    label.grid(row=index, column=0, sticky="ew", padx=5, pady=5)
    button = tk.Button(scrollable_frame, text=price)
    button.grid(row=index, column=1, sticky="ew", padx=5, pady=5)



scrollable_frame.grid_columnconfigure(0, weight=1)
scrollable_frame.grid_columnconfigure(1, weight=1)



label = tk.Label(frame_principal,bg="#46D4D1",)
label.place(x=0, y=0, width=66, height=35)

button = tk.Button(frame_principal,bg="#26A8DB", text='Clique-me', command=lambda:clicado(data_save))
button.place(x=136, y=153, width=139, height=120)

atualizar_pontos()
root.mainloop()




