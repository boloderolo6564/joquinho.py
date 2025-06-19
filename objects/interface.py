import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  
class interface:
    def __init__(self,root,usuario,store,data_save,rebirth):
        self.root = root
        self.usuario = usuario
        self.store = store
        self.data_save = data_save
        self.rebirth = rebirth

        self.frame_principal = tk.Frame(root,bg="#1C1616")
        self.frame_principal.pack(fill="both", expand=True)

        self.frame_lateral = tk.Frame(self.frame_principal, width=200,bg="#46D4D1")
        self.frame_lateral.pack(side="right", fill="y")

        self.canvas = tk.Canvas(self.frame_lateral, width=180, bg="#46D4D1")
        self.scrollbar = tk.Scrollbar(self.frame_lateral, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#46D4D1")

        self.barra = tk.Label(self.frame_principal,bg="#4D00FF")
        self.barra.place(x=0, y=0, width=400, height=35)

        self.scrollable_frame.bind(
                "<Configure>",
                lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")


        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", self.on_configure)

        self.window_id = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.storename = tk.Label(self.frame_lateral,text="STORE",bg="#659291")
        self.storename.place(x=400, y=0, width=200, height=35)

        self.listastore(self.data_save)

        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)

        self.label = tk.Label(self.frame_principal,bg="#46D4D1",)
        self.label.place(x=0, y=0, width=136, height=35)

        self.button = tk.Button(self.frame_principal, text='Click-me',bg = "#26A8DB",activebackground= "#46D4D1",relief="raised",bd=5,  command=lambda:self.clicar(self.data_save ))
        self.button.place(x=136, y=153, width=139, height=120)

        self.buttonRebirth = tk.Button(self.frame_principal,text = "REBIRTH", bg = "#659291", command=lambda:self.confirmar_rebirth(self.data_save))
        self.buttonRebirth.place(x=0, y=35, width=66, height=35)

        self.labelstore = tk.Label(self.frame_principal,text= "STORE -->",bg="#46D4D1",)
        self.labelstore.place(x=304, y=0, width=96, height=35)
       
        self.atualizarpontos()
        pass
    def confirmar_rebirth(self,data_save):
        resposta = messagebox.askyesno("Rebirth", f"You need {data_save["Rebirth"]["require"]:.1f} points to Rebirth. Do you want to proceed?")
        if resposta:
            if (self.rebirth.verificarebirth(self,data_save)):
                this_save = self.usuario.rebirthupgrade(data_save)
                if(this_save is not None):
                    data_save = self.rebirth.aumentarequire(self,this_save)
                    if(data_save):
                        messagebox.showinfo("Rebirth","Rebirth was successful")
                        self.atualizarpontos()
                        self.atualizarstore()
                    else: 
                        messagebox.showinfo("Rebirth","ERROR!!!!")
                else: 
                    messagebox.showinfo("Rebirth","ERROR")
            else: 
                messagebox.showinfo("Rebirth", "Not enough points")
        else:
            print("user denied.")

    def clicar(self,data_save):
        self.usuario.adicionarpontos(data_save)

    def listastore(self,data_save):
        self.caixabuttons = []
        for index, (item, price,power) in enumerate(zip(data_save["store"]["itens"], data_save["store"]["price"],data_save["store"]["addpower"])):
            index +=1
            label = tk.Label(self.scrollable_frame, text=f"{item} +{power}", bg="#d0ffd0")
            label.grid(row=index, column=0, sticky="ew", padx=5, pady=5)
            buttonstore = tk.Button(self.scrollable_frame, text=f"{price:.1f}",command=lambda p=data_save,i=item :self.compra(p,i))
            buttonstore.grid(row=index, column=1, sticky="ew", padx=5, pady=5)
            self.caixabuttons.append((buttonstore,item))

    def atualizarstore(self,):
        
        for botao, item in self.caixabuttons:
            try:
                index = self.data_save["store"]["itens"].index(item)
                novo_preco = self.data_save["store"]["price"][index]
                botao.config(text=f"{novo_preco:.1f}")
            except ValueError:
                continue  
        self.root.after(1000, self.atualizarstore)
    def atualizarpontos(self,):
        self.data_save = self.usuario.carregardados()
        self.label.config(text=f"Points: {self.data_save["user"]["points"]:.1f}")
        self.root.after(200, self.atualizarpontos)
        
    def on_configure(self,event):
        self.canvas_width = event.width
        self.canvas.itemconfig(self.window_id, width=self.canvas_width)

    def compra(self,data_save,item):
        index = self.store.buy(self.data_save,item)
        if(index is not None):
            self.usuario.upgrade(self.data_save,index)
            self.atualizarstore()
        else:
            messagebox.showinfo("STORE","Not enough points")
    def atualizardados(self,):
        self.root.after(200, self.atualizarpontos)