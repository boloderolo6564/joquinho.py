import tkinter as tk

class interface:
    def __init__(self,root,usuario,store,data_save):
        self.root = root
        self.usuario = usuario
        self.store = store
        self.data_save = data_save

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

        self.listastore(data_save)

        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)

        self.label = tk.Label(self.frame_principal,bg="#46D4D1",)
        self.label.place(x=0, y=0, width=66, height=35)

        self.button = tk.Button(self.frame_principal,bg="#26A8DB", text='Clique-me', command=lambda:self.clicar(data_save))
        self.button.place(x=136, y=153, width=139, height=120)

        self.atualizarpontos()

        pass
    def clicar(self,data_save):
        self.usuario.adicionarpontos(data_save)
        self.usuario.carregardados()

    def listastore(self,data_save):
        self.caixabuttons = []
        for index, (item, price) in enumerate(zip(data_save["store"]["itens"], data_save["store"]["price"])):
            index +=1
            label = tk.Label(self.scrollable_frame, text=item, bg="#d0ffd0")
            label.grid(row=index, column=0, sticky="ew", padx=5, pady=5)
            buttonstore = tk.Button(self.scrollable_frame, text=price,command=lambda p=data_save,i=item :self.compra(p,i))
            buttonstore.grid(row=index, column=1, sticky="ew", padx=5, pady=5)
            self.caixabuttons.append((buttonstore,item))

    def atualizarstore(self,):
        data_save = self.usuario.carregardados()
        
        for botao, item in self.caixabuttons:
            try:
                index = data_save["store"]["itens"].index(item)
                novo_preco = data_save["store"]["price"][index]
                botao.config(text=novo_preco)
            except ValueError:
                continue  
        self.root.after(1000, self.atualizarstore)
    def atualizarpontos(self,):
        data_save = self.usuario.carregardados()
        self.label.config(text=f"Pontos: {data_save["usuario"]["clique"]}")
        self.root.after(200, self.atualizarpontos)

    def on_configure(self,event):
        self.canvas_width = event.width
        self.canvas.itemconfig(self.window_id, width=self.canvas_width)

    def compra(self,data_save,item):
        index = self.store.buy(data_save,item)
        if(index is not None):
            self.usuario.upgrade(data_save,index)
            self.atualizarstore()
        else:
            print("pontos insuficientes")
        












