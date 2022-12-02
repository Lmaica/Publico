from EFuncPosVenda import *

class InicioPrograma(FuncMensagens):
    def __init__(self, master):
        super().__init__()
        self.i_janela = master
        self.diretorio = os.getcwd()
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.imag = tk.PhotoImage(file=self.diretorio + '\Imagens\M_D.png')
        self.LbImag = tk.Label(image=self.imag)
        self.LbImag.place(width=719,height=530)
        self.i_janela.title('Maicá Manutenção Automotiva')
        self.i_janela.iconbitmap(self.diretorio +'\Imagens\icone.ico')
        self.i_janela.geometry('719x530')
        self.i_janela.resizable(False,False)
        self.i_janela.attributes('-alpha', 2.5)

        self.fonte_buton = ("Times New Roman CE", "15")

        self.botao = tk.Button(text="CRIAR O.S", font=self.fonte_buton, bg="black", foreground="white"
                               ,command=self.OsJanela)
        self.botao.place(x=10, y=10, width=220, height=50, )
        self.botao1 = tk.Button(text="ADICIONAR SERVIÇO", font=self.fonte_buton, bg="black", foreground="white"
                               , command=self.InicilServiços)
        self.botao1.place(x=10, y=70, width=220, height=50,)
        self.botao2 = tk.Button(text="CARROS", font=self.fonte_buton, bg="black", foreground="white"
                                ,command=self.CarroJanela)
        self.botao2.place(x=250, y=10, width=220, height=50)
        self.botao3 = tk.Button(text="CLIENTES", font=self.fonte_buton, bg="black", foreground="white"
                                ,command=self.ClientesJanela)
        self.botao3.place(x=480, y=10, width=220, height=50)
        self.botao4 = tk.Button(text="VENDAS PENDENTES", font=self.fonte_buton, bg="black", foreground="white",
                                command=self.PendetesJanela)
        self.botao4.place(x=130, y=300, width=220, height=50)
        self.botao5 = tk.Button(text="VENDAS FINALIZADAS", font=self.fonte_buton, bg="black", foreground="white",
                                command=self.FinalizadosJanela)
        self.botao5.place(x=360, y=300, width=220, height=50)
        self.botao5 = tk.Button(text="ENVIOS AUTOMATICOS", font=self.fonte_buton, bg="black", foreground="white",
                                command=self.InicilSecuPosVenda)
        self.botao5.place(x=210, y=375, width=275, height=50)
        self.botao7 = tk.Button(text="RENDIMENTOS", font=self.fonte_buton, bg="black", foreground="white",
                                command=self.GanhosJanela)
        self.botao7.place(x=130, y=450, width=220, height=50)
        self.botao8 = tk.Button(text="SAIDAS DE CAIXA", font=self.fonte_buton, bg="black", foreground="white",
                                command=self.SaidaJanela)
        self.botao8.place(x=360, y=450, width=220, height=50)

    def ClientesJanela(self):
        self.InicioJanela()
        self.cr_janela.geometry('800x600')
        self.ValidarEntr()
        self.SelesaoClientes()
        self.Fontes()
        self.quadrado2 = tk.Frame(self.cr_janela)
        self.quadrado2.place(x=5,y=425,width=790,height=170)

        self.texto = tk.Label(self.cr_janela,text='CLIENTES',font=self.cabesario_font)
        self.texto.place(x=350, y=10)

        self.voltar = tk.Button(self.cr_janela,text="<VOLTAR", font=self.cabesario_voltar, bg="white",
                                foreground="black",command=self.cr_janela.destroy)
        self.voltar.place(x=10, y=10, width=80, height=30)

        self.escrita = tk.Label(self.cr_janela,text='Codigo Cliente',font=self.fonte_titlo)
        self.escrita.place(x=20,y=480)
        self.entrada = tk.Entry(self.cr_janela,font=self.fonte_entra)
        self.entrada.place(x=20,y=500,width=150)

        self.escrita1 = tk.Label(self.cr_janela,text='Nome Cliente',font=self.fonte_titlo)
        self.escrita1.place(x=190,y=480)
        self.entrada1 = tk.Entry(self.cr_janela,font=self.fonte_entra)
        self.entrada1.place(x=190,y=500,width=250)
        self.escrita2 = tk.Label(self.cr_janela,text='WhatsApp',font=self.fonte_titlo)
        self.escrita2.place(x=460,y=480)
        self.entrada2 = tk.Entry(self.cr_janela,validate='key',validatecommand=self.SonumeroTelefone,
                                 font=self.fonte_entra)
        self.entrada2.place(x=460,y=500,width=150)
        self.escrita3 = tk.Label(self.cr_janela,text='2° Telefone',font=self.fonte_titlo)
        self.escrita3.place(x=630,y=480)
        self.entrada3 = tk.Entry(self.cr_janela,validate='key',validatecommand=self.SonumeroTelefone,
                                 font=self.fonte_entra)
        self.entrada3.place(x=630,y=500,width=150)
        self.escrita4 = tk.Label(self.cr_janela,text='Data Nacimento',font=self.fonte_titlo)
        self.escrita4.place(x=10,y=530)
        self.entrada4 = tk.Entry(self.cr_janela,font=self.fonte_entra)
        self.entrada4.place(x=10,y=550,width=100)
        self.escrita5 = tk.Label(self.cr_janela,text='CPF',font=self.fonte_titlo)
        self.escrita5.place(x=130,y=530)
        self.entrada5 = tk.Entry(self.cr_janela,font=self.fonte_entra)
        self.entrada5.place(x=130,y=550,width=150)
        self.escrita6 = tk.Label(self.cr_janela,text='CEP',font=self.fonte_titlo)
        self.escrita6.place(x=300,y=530)
        self.entrada6 = tk.Entry(self.cr_janela,font=self.fonte_entra)
        self.entrada6.place(x=300,y=550,width=120)
        self.escrita7 = tk.Label(self.cr_janela,text='Numero "Casa"',font=self.fonte_titlo)
        self.escrita7.place(x=450,y=530)
        self.entrada7 = tk.Entry(self.cr_janela,font=self.fonte_entra)
        self.entrada7.place(x=450,y=550,width=100)
        self.escrita8 = tk.Label(self.cr_janela,text='Complemento',font=self.fonte_titlo)
        self.escrita8.place(x=590,y=530)
        self.entrada8 = tk.Entry(self.cr_janela,font=self.fonte_entra)
        self.entrada8.place(x=590,y=550,width=200)

        self.criar = tk.Button(self.cr_janela,text="CRIAR\nNOVO CLIENTE", font=self.fonte_buton, bg="black",
                                foreground="white",command=self.AddClinete)
        self.criar.place(x=130, y=430, width=150, height=40)
        self.editar = tk.Button(self.cr_janela,text="EDITAR\nCLIENTE", font=self.fonte_buton, bg="black",
                                foreground="white",command=self.Escolha_modificar)
        self.editar.place(x=290, y=430, width=100, height=40)
        self.excluir = tk.Button(self.cr_janela,text="EXCLUIR\nCLIENTE", font=self.fonte_buton, bg="black",
                                foreground="white",command=self.Escolha_apagar)
        self.excluir.place(x=400, y=430, width=100, height=40)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='Buscar por:').place(x=510,y=425)
        self.Ent_Busca = tk.StringVar(self.cr_janela)
        self.tipv = ('Nome','Telefone','N/Cliente','CPF')
        self.Ent_Busca.set('Nome')
        self.pormenu = tk.OptionMenu(self.cr_janela,self.Ent_Busca,*self.tipv)
        self.pormenu.configure(bg="white",foreground="black")
        self.pormenu.place(x=510,y=445,width=100, height=30)

        self.buscar = tk.Button(self.cr_janela,text="BUSCAR", font=self.fonte_buton, bg="black",
                                foreground="white",command = self.Buscar_cliente)
        self.buscar.place(x=685, y=425, width=100, height=20)

        self.Entrada_busca = tk.Entry(self.cr_janela,font=self.fonte_entra)
        self.Entrada_busca.place(x=635,y=450,width=150)

        self.limpar = tk.Button(self.cr_janela,text="Limpar", font=self.cabesario_voltar, bg="white", foreground="black"
                                ,command=self.LimpaEnterClientes)
        self.limpar.place(x=35, y=440, width=80, height=30)
        self.AtualizeLista_clientes()
        self.lista_c_clir.bind("<Double-1>",self.SelencionarCliente)
    def SelesaoClientes(self):
        self.Fontes()
        self.quadrado = tk.Frame(self.cr_janela)
        self.quadrado.place(x=5,y=5,width=790,height=415)

        self.lista_c_clir = ttk.Treeview(self.cr_janela, height=600,
                                  columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6,col7',
                                           'col8', 'col9','col10'))
        self.lista_c_clir.heading('#0', text='')
        self.lista_c_clir.heading('#1', text='Codigo')
        self.lista_c_clir.heading('#2', text='Nome')
        self.lista_c_clir.heading('#3', text='Fone Whats')
        self.lista_c_clir.heading('#4', text='2° Telefone')
        self.lista_c_clir.heading('#5', text='Nacimento')
        self.lista_c_clir.heading('#6', text='CPF')
        self.lista_c_clir.heading('#7', text='CEP')
        self.lista_c_clir.heading('#8', text='Numero "Casa"')
        self.lista_c_clir.heading('#9', text='Complemento')
        self.lista_c_clir.column('#0', width=0)
        self.lista_c_clir.column('#1', width=50)
        self.lista_c_clir.column('#2', width=150)
        self.lista_c_clir.column('#3', width=100)
        self.lista_c_clir.column('#4', width=100)
        self.lista_c_clir.column('#5', width=100)
        self.lista_c_clir.column('#6', width=100)
        self.lista_c_clir.column('#7', width=100)
        self.lista_c_clir.column('#8', width=100)
        self.lista_c_clir.column('#9', width=150)
        self.lista_c_clir.place(x=10, y=45, width=780, height=345)

        self.barra_lado = ttk.Scrollbar(self.cr_janela, orient='vertical',command=self.lista_c_clir.yview)
        self.lista_c_clir.configure(yscrollcommand=self.barra_lado.set)
        self.barra_lado.place(x=760, y=72, width=30, height=343)

        self.barra_baixo = ttk.Scrollbar(self.cr_janela, orient='horizontal',
                                              command=self.lista_c_clir.xview)
        self.lista_c_clir.configure(xscrollcommand=self.barra_baixo.set)
        self.barra_baixo.place(x=10, y=385, width=750, height=30)

    def CarroJanela(self):
        self.InicioJanela()
        self.SelesaoCarro()
        self.Fontes()

        self.escritaCarro = tk.Label(self.cr_janela,text='Placa do Carro',font=self.fonte_titlo)
        self.escritaCarro.place(x=20,y=480)
        self.entradaCarro = tk.Entry(self.cr_janela,font=self.fonte_entra)
        self.entradaCarro.place(x=20,y=500,width=120)
        self.escrita1Carro = tk.Label(self.cr_janela,text='Marca do Carro',font=self.fonte_titlo)
        self.escrita1Carro.place(x=148,y=480)
        self.entrada1Carro = tk.Entry(self.cr_janela,font=self.fonte_entra)
        self.entrada1Carro.place(x=148,y=500,width=120)
        self.escrita2Carro = tk.Label(self.cr_janela,text='Modelo do Carro',font=self.fonte_titlo)
        self.escrita2Carro.place(x=276,y=480)
        self.entrada2Carro = tk.Entry(self.cr_janela,font=self.fonte_entra)
        self.entrada2Carro.place(x=276,y=500,width=120)
        self.escrita3Carro = tk.Label(self.cr_janela,text='Ano do Carro',font=self.fonte_titlo)
        self.escrita3Carro.place(x=404,y=480)
        self.entrada3Carro = tk.Entry(self.cr_janela,font=self.fonte_entra)
        self.entrada3Carro.place(x=404,y=500,width=120)
        self.escrita4Carro = tk.Label(self.cr_janela,text='Motor do Carro',font=self.fonte_titlo)
        self.escrita4Carro.place(x=532,y=480)
        self.entrada4Carro = tk.Entry(self.cr_janela,font=self.fonte_entra)
        self.entrada4Carro.place(x=532,y=500,width=120)
        self.escrita5Carro = tk.Label(self.cr_janela,text='Km do Carro',font=self.fonte_titlo)
        self.escrita5Carro.place(x=660,y=480)
        self.entrada5Carro = tk.Entry(self.cr_janela,font=self.fonte_entra)
        self.entrada5Carro.place(x=660,y=500,width=120)

        self.codigo_carro = tk.Entry(self.cr_janela,font=self.fonte_entra)
        self.codigo_carro.place(x=800,y=800,width=1)

        self.criarCarro = tk.Button(self.cr_janela,text="CRIAR\nNOVO CARRO", font=self.fonte_buton, bg="black",
                                foreground="white",command=self.AddCarro)
        self.criarCarro.place(x=140, y=430, width=150, height=40)
        self.buscarCarro = tk.Button(self.cr_janela,text="BUSCAR\nPOR MODELO", font=self.fonte_buton, bg="black",
                                foreground="white",command=self.Buscar_Carro)
        self.buscarCarro.place(x=320, y=430, width=100, height=40)
        self.editarCarro = tk.Button(self.cr_janela,text="EDITAR\nCARRO", font=self.fonte_buton, bg="black",
                                foreground="white",command=self.Escolha_modificar_carro)
        self.editarCarro.place(x=440, y=430, width=100, height=40)
        self.excluirCarro = tk.Button(self.cr_janela,text="EXCLUIR\nCARRO", font=self.fonte_buton, bg="black",
                                foreground="white",command=self.Escolha_apagar_Carro)
        self.excluirCarro.place(x=560, y=430, width=100, height=40)

        self.limparCarro = tk.Button(self.cr_janela,text="Limpar", font=self.cabesario_voltar,
                                     bg="white", foreground="black",command=self.LimpaEnterCarro)
        self.limparCarro.place(x=35, y=440, width=80, height=30)
        self.AtualizeLista_Carro()
        self.lista_c_clirCarro.bind("<Double-1>",self.SelencionarCarro)
    def SelesaoCarro(self):
        self.Fontes()
        self.quadradoCarro = tk.Frame(self.cr_janela)
        self.quadradoCarro.place(x=5,y=5,width=790,height=415)

        self.lista_c_clirCarro = ttk.Treeview(self.cr_janela, height=600,
                                  columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6,col7',
                                           'col8', 'col9','col10','col11'))
        self.lista_c_clirCarro.heading('#0', text='')
        self.lista_c_clirCarro.heading('#1', text='Nome Cliente')
        self.lista_c_clirCarro.heading('#2', text='Fone Whats')
        self.lista_c_clirCarro.heading('#3', text='Placa')
        self.lista_c_clirCarro.heading('#4', text='Marca ')
        self.lista_c_clirCarro.heading('#5', text='Modelo')
        self.lista_c_clirCarro.heading('#6', text='Ano')
        self.lista_c_clirCarro.heading('#7', text='Motor')
        self.lista_c_clirCarro.heading('#8', text='Km')
        self.lista_c_clirCarro.heading('#9', text='Codigo Cliente')
        self.lista_c_clirCarro.heading('#10', text='Codigo Carro')
        self.lista_c_clirCarro.column('#0', width=0)
        self.lista_c_clirCarro.column('#1', width=150)
        self.lista_c_clirCarro.column('#2', width=100)
        self.lista_c_clirCarro.column('#3', width=100)
        self.lista_c_clirCarro.column('#4', width=100)
        self.lista_c_clirCarro.column('#5', width=100)
        self.lista_c_clirCarro.column('#6', width=100)
        self.lista_c_clirCarro.column('#7', width=100)
        self.lista_c_clirCarro.column('#8', width=100)
        self.lista_c_clirCarro.column('#9', width=150)
        self.lista_c_clirCarro.column('#10', width=100)
        self.lista_c_clirCarro.place(x=10, y=45, width=780, height=345)

        self.barra_ladoCarro = ttk.Scrollbar(self.cr_janela, orient='vertical',command=self.lista_c_clirCarro.yview)
        self.lista_c_clirCarro.configure(yscrollcommand=self.barra_ladoCarro.set)
        self.barra_ladoCarro.place(x=760, y=72, width=30, height=343)

        self.barra_baixoCarro = ttk.Scrollbar(self.cr_janela, orient='horizontal',
                                              command=self.lista_c_clirCarro.xview)
        self.lista_c_clirCarro.configure(xscrollcommand=self.barra_baixoCarro.set)
        self.barra_baixoCarro.place(x=10, y=385, width=750, height=30)

        self.textoCarro = tk.Label(self.cr_janela,text='CARROS',font=self.cabesario_font)
        self.textoCarro.place(x=350, y=10)

        self.voltarCarro = tk.Button(self.cr_janela,text="<VOLTAR", font=self.cabesario_voltar,
                                     bg="white", foreground="black",command=self.cr_janela.destroy)
        self.voltarCarro.place(x=10, y=10, width=80, height=30)

        self.quadrado2Carro = tk.Frame(self.cr_janela)
        self.quadrado2Carro.place(x=5,y=425,width=790,height=120)

    def OsJanela(self):
        self.os_janela = tk.Toplevel()
        self.ValorArumado()
        self.os_janela.title('Maicá manutenção Automotiva')
        self.os_janela.iconbitmap(self.diretorio + '\Imagens\icone.ico')
        self.os_janela.geometry('1020x550')
        self.os_janela.resizable(False, False)
        self.os_janela.configure(background='#1e0000')
        self.os_janela.transient(self.i_janela)
        self.os_janela.focus_force()
        self.os_janela.grab_set()
        self.Fontes()

        self.quadrado = tk.Frame(self.os_janela)
        self.quadrado.place(x=5,y=5,width=770,height=540)

        self.quadrado = tk.Frame(self.os_janela)
        self.quadrado.place(x=780,y=5,width=235,height=540)

        self.textoCarro = tk.Label(self.os_janela,text='CARROS',font='Arial')
        self.textoCarro.place(x=860, y=5)
        self.Abrir_W = tk.Button(self.os_janela, text="Falar Whats", font=self.fonte_buton, bg="black",
                                 foreground="white", width=7, command=self.AbrirWhats)
        self.Abrir_W.place(x=920, y=30,width=80,height=25)
        self.escriCarro = tk.Label(self.os_janela,text='Nome do Cliente',font=self.fonte_titlo)
        self.escriCarro.place(x=800,y=40)
        self.entraCarro = tk.Entry(self.os_janela,font=self.fonte_entra)
        self.entraCarro.place(x=800,y=60,width=200)
        self.escri1Carro = tk.Label(self.os_janela,text='Telefone do Cliente',font=self.fonte_titlo)
        self.escri1Carro.place(x=800,y=90)
        self.entra1Carro = tk.Entry(self.os_janela,font=self.fonte_entra,validate='key',
                                    validatecommand=self.SonumeroTelefoneOs)
        self.entra1Carro.place(x=800,y=110,width=200)
        self.escri2Carro = tk.Label(self.os_janela,text='Placa do Carro',font=self.fonte_titlo)
        self.escri2Carro.place(x=800,y=190)
        self.entra2Carro = tk.Entry(self.os_janela,font=self.fonte_entra)
        self.entra2Carro.place(x=800,y=210,width=200)
        self.escri3Carro = tk.Label(self.os_janela,text='Marca do Carro',font=self.fonte_titlo)
        self.escri3Carro.place(x=800,y=240)
        self.entra3Carro = tk.Entry(self.os_janela,font=self.fonte_entra)
        self.entra3Carro.place(x=800,y=260,width=200)
        self.escri4Carro = tk.Label(self.os_janela,text='Modelo do Carro',font=self.fonte_titlo)
        self.escri4Carro.place(x=800,y=290)
        self.entra4Carro = tk.Entry(self.os_janela,font=self.fonte_entra)
        self.entra4Carro.place(x=800,y=310,width=200)
        self.escri5Carro = tk.Label(self.os_janela,text='Ano do Carro',font=self.fonte_titlo)
        self.escri5Carro.place(x=800,y=340)
        self.entra5Carro = tk.Entry(self.os_janela,font=self.fonte_entra)
        self.entra5Carro.place(x=800,y=360,width=200)
        self.escri6Carro = tk.Label(self.os_janela,text='Motor do Carro',font=self.fonte_titlo)
        self.escri6Carro.place(x=800,y=390)
        self.entra6Carro = tk.Entry(self.os_janela,font=self.fonte_entra)
        self.entra6Carro.place(x=800,y=410,width=200)
        self.escri7Carro = tk.Label(self.os_janela,text='Km do Carro',font=self.fonte_titlo)
        self.escri7Carro.place(x=800,y=440)
        self.entra7Carro = tk.Entry(self.os_janela,font=self.fonte_entra)
        self.entra7Carro.place(x=800,y=460,width=200)
        self.escri8Carro = tk.Label(self.os_janela,text='Numero do Cliente',font=self.fonte_titlo)
        self.escri8Carro.place(x=800,y=140)
        self.entra8Carro = tk.Entry(self.os_janela,font=self.fonte_entra)
        self.entra8Carro.place(x=800,y=160,width=200)

        self.Fun_esCarro = tk.Button(self.os_janela,text="TROCAR CARRO", font=self.fonte_buton, bg="black",
                                    foreground="white",width=15,command=self.AddCarroPedido)
        self.Fun_esCarro.place(x=830,y=500)

        self.P_escrita = tk.Label(self.os_janela, text='%',font=self.fonte_entra)
        self.P_escrita.place(x=410,y=15)

        self.entrada_por = tk.Entry(self.os_janela,font=self.fonte_entra,width=4,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_por.place(x=430,y=15)

        self.Abrir_W = tk.Button(self.os_janela,text="WhatsApp", font=self.fonte_buton, bg="black",
                                    foreground="white",width=7,command=self.abrir_arquivo_whats)
        self.Abrir_W.place(x=230,y=10)

        self.Abrir_impr = tk.Button(self.os_janela,text="IMPRIMIR", font=self.fonte_buton, bg="black",
                                    foreground="white",width=7,command=self.abrir_arquivo_imprimir)
        self.Abrir_impr.place(x=310,y=10)

        self.Fun_Somar = tk.Button(self.os_janela,text="LIMPAR TUDO", font=self.fonte_buton, bg="black",
                                    foreground="white",width=13,command=self.LimparPesas)
        self.Fun_Somar.place(x=530,y=10)

        self.Fun_Somar = tk.Button(self.os_janela,text="SOMAR", font=self.fonte_buton, bg="black",
                                    foreground="white",width=13,command=self.Somar)
        self.Fun_Somar.place(x=655,y=40)

        self.Fun_Somar = tk.Button(self.os_janela,text="SOMAR COM\n PORCENTAGEM", font=self.fonte_buton, bg="black",
                                    foreground="white",width=13,command=self.MesagemPorcentagem)
        self.Fun_Somar.place(x=655,y=110)

        self.F_Buscar = tk.Button(self.os_janela,text="BUSCAR/\nFINALIZADOS", font=self.fonte_buton, bg="black",
                                    foreground="white",width=13,command=self.AbrirFinalizadosPorOS)
        self.F_Buscar.place(x=655,y=200)
        self.P_Buscar = tk.Button(self.os_janela,text="BUSCAR/\nPENDENTES", font=self.fonte_buton, bg="black",
                                    foreground="white",width=13,command=self.AbrirPorOS)
        self.P_Buscar.place(x=655,y=250)
        self.Fun_modificar = tk.Button(self.os_janela,text="MODIFICAR\nO.S", font=self.fonte_buton, bg="black",
                                    foreground="white",width=13,command=self.Escolha_Modificar_Pendentes)
        self.Fun_modificar.place(x=655,y=300)
        self.Fun_Excluir = tk.Button(self.os_janela,text="EXCLUIR\nO.S", font=self.fonte_buton, bg="black",
                                    foreground="white",width=13,command=self.Escolha_apagar_Pendentes)
        self.Fun_Excluir.place(x=655,y=350)
        self.F_salvar = tk.Button(self.os_janela,text="FINALIZAR", font=self.fonte_buton, bg="black",
                                    foreground="white",width=13,command=self.JanelaFechamento)
        self.F_salvar.place(x=655,y=440)
        self.P_salvar = tk.Button(self.os_janela,text="SALVAR/\nPENDENTE", font=self.fonte_buton, bg="black",
                                    foreground="white",width=13,command=self.CriarOS_Pendende)
        self.P_salvar.place(x=655,y=480)

        self.P_escrita = tk.Label(self.os_janela, text='Numero O.S',font=self.fonte_entra)
        self.P_escrita.place(x=15,y=10)
        self.entrada_codigo = tk.Entry(self.os_janela,font=self.fonte_entra,width=10)
        self.entrada_codigo.place(x=110,y=10)

        self.quadrado1 = tk.Frame(self.os_janela)
        self.quadrado1.place(x=5,y=50,width=645,height=350)

        self.cava = tk.Canvas(self.quadrado1)
        self.cava.pack(side=tk.LEFT,fill=tk.BOTH,expand=1)

        self.barra_ladoOs = ttk.Scrollbar(self.quadrado1,orient='vertical',command=self.cava.yview)
        self.barra_ladoOs.pack(side=tk.RIGHT,fill=tk.Y)
        self.cava.configure(yscrollcommand=self.barra_ladoOs.set)
        self.cava.bind('<Configure>',lambda e:self.cava.configure(scrollregion = self.cava.bbox(tk.ALL)))

        self.quadradoframe = tk.Frame(self.cava)
        self.cava.create_window((0,0),window=self.quadradoframe,anchor='nw')

        self.P_escrita = tk.Label(self.quadradoframe, text='NOME PEÇAS',font=self.fonte_entra)
        self.P_escrita.grid(row =2,column=1,padx=5,pady=5,columnspan =2)
        self.U_escrita = tk.Label(self.quadradoframe, text='UNI',font=self.fonte_entra)
        self.U_escrita.grid(row =2,column=3,padx=5,pady=5)
        self.VU_escrita = tk.Label(self.quadradoframe, text='VALOR UNI',font=self.fonte_entra)
        self.VU_escrita.grid(row = 2,column=4,columnspan =2,padx=5,pady=5)
        self.VT_escrita = tk.Label(self.quadradoframe, text='VALOR TOTAL',font=self.fonte_entra)
        self.VT_escrita.grid(row = 2,column=6,columnspan =2,padx=5,pady=5)

        self.numero_p = tk.Label(self.quadradoframe, text='1)',font=self.fonte_entra)
        self.numero_p.grid(row=3, column=1, padx=5, pady=5)
        self.entrada_pesas = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=30)
        self.entrada_pesas.grid(row = 3,column=2,padx =5,pady =5)
        self.entrada_uni = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni.grid(row = 3,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 3,column=4,padx=5,pady=5)
        self.entrada_v_uni = tk.Entry(self.quadradoframe , font=self.fonte_entra,width=8)
        self.entrada_v_uni.grid(row = 3,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 3,column=6,padx=5,pady=5)
        self.entrada_t_uni = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=8)
        self.entrada_t_uni.grid(row = 3,column=7,padx =5,pady =5)

        self.numero_p1 = tk.Label(self.quadradoframe , text='2)',font=self.fonte_entra)
        self.numero_p1.grid(row=4, column=1, padx=5, pady=5)
        self.entrada_pesas1 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=30)
        self.entrada_pesas1.grid(row = 4,column=2,padx =5,pady =5)
        self.entrada_uni1 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni1.grid(row = 4,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 4,column=4,padx=5,pady=5)
        self.entrada_v_uni1 = tk.Entry(self.quadradoframe , font=self.fonte_entra,width=8)
        self.entrada_v_uni1.grid(row = 4,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 4,column=6,padx=5,pady=5)
        self.entrada_t_uni1 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=8)
        self.entrada_t_uni1.grid(row = 4,column=7,padx =5,pady =5)

        self.numero_p2 = tk.Label(self.quadradoframe, text='3)',font=self.fonte_entra)
        self.numero_p2.grid(row=5, column=1, padx=5, pady=5)
        self.entrada_pesas2 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=30)
        self.entrada_pesas2.grid(row = 5,column=2,padx =5,pady =5)
        self.entrada_uni2 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni2.grid(row = 5,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 5,column=4,padx=5,pady=5)
        self.entrada_v_uni2 = tk.Entry(self.quadradoframe , font=self.fonte_entra,width=8)
        self.entrada_v_uni2.grid(row = 5,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 5,column=6,padx=5,pady=5)
        self.entrada_t_uni2 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=8)
        self.entrada_t_uni2.grid(row = 5,column=7,padx =5,pady =5)

        self.numero_p3 = tk.Label(self.quadradoframe , text='4)',font=self.fonte_entra)
        self.numero_p3.grid(row=6, column=1, padx=5, pady=5)
        self.entrada_pesas3 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=30)
        self.entrada_pesas3.grid(row = 6,column=2,padx =5,pady =5)
        self.entrada_uni3 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni3.grid(row = 6,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 6,column=4,padx=5,pady=5)
        self.entrada_v_uni3 = tk.Entry(self.quadradoframe , font=self.fonte_entra,width=8)
        self.entrada_v_uni3.grid(row = 6,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 6,column=6,padx=5,pady=5)
        self.entrada_t_uni3 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=8)
        self.entrada_t_uni3.grid(row = 6,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.quadradoframe, text='5)',font=self.fonte_entra)
        self.numero_p.grid(row=7, column=1, padx=5, pady=5)
        self.entrada_pesas4 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=30)
        self.entrada_pesas4.grid(row = 7,column=2,padx =5,pady =5)
        self.entrada_uni4 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni4.grid(row = 7,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 7,column=4,padx=5,pady=5)
        self.entrada_v_uni4 = tk.Entry(self.quadradoframe, font=self.fonte_entra,width=8)
        self.entrada_v_uni4.grid(row = 7,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 7,column=6,padx=5,pady=5)
        self.entrada_t_uni4 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=8)
        self.entrada_t_uni4.grid(row = 7,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.quadradoframe, text='6)',font=self.fonte_entra)
        self.numero_p.grid(row=8, column=1, padx=5, pady=5)
        self.entrada_pesas5 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=30)
        self.entrada_pesas5.grid(row = 8,column=2,padx =5,pady =5)
        self.entrada_uni5 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni5.grid(row = 8,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 8,column=4,padx=5,pady=5)
        self.entrada_v_uni5 = tk.Entry(self.quadradoframe, font=self.fonte_entra,width=8)
        self.entrada_v_uni5.grid(row = 8,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 8,column=6,padx=5,pady=5)
        self.entrada_t_uni5 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=8)
        self.entrada_t_uni5.grid(row = 8,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.quadradoframe, text='7)',font=self.fonte_entra)
        self.numero_p.grid(row=9, column=1, padx=5, pady=5)
        self.entrada_pesas6 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=30)
        self.entrada_pesas6.grid(row = 9,column=2,padx =5,pady =5)
        self.entrada_uni6 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni6.grid(row = 9,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 9,column=4,padx=5,pady=5)
        self.entrada_v_uni6 = tk.Entry(self.quadradoframe, font=self.fonte_entra,width=8)
        self.entrada_v_uni6.grid(row = 9,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 9,column=6,padx=5,pady=5)
        self.entrada_t_uni6 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=8)
        self.entrada_t_uni6.grid(row = 9,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.quadradoframe, text='8)',font=self.fonte_entra)
        self.numero_p.grid(row=10, column=1, padx=5, pady=5)
        self.entrada_pesas7 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=30)
        self.entrada_pesas7.grid(row = 10,column=2,padx =5,pady =5)
        self.entrada_uni7 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni7.grid(row = 10,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 10,column=4,padx=5,pady=5)
        self.entrada_v_uni7 = tk.Entry(self.quadradoframe, font=self.fonte_entra,width=8)
        self.entrada_v_uni7.grid(row = 10,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 10,column=6,padx=5,pady=5)
        self.entrada_t_uni7 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=8)
        self.entrada_t_uni7.grid(row = 10,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.quadradoframe, text='9)',font=self.fonte_entra)
        self.numero_p.grid(row=11, column=1, padx=5, pady=5)
        self.entrada_pesas8 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=30)
        self.entrada_pesas8.grid(row = 11,column=2,padx =5,pady =5)
        self.entrada_uni8 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni8.grid(row = 11,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 11,column=4,padx=5,pady=5)
        self.entrada_v_uni8 = tk.Entry(self.quadradoframe, font=self.fonte_entra,width=8)
        self.entrada_v_uni8.grid(row = 11,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 11,column=6,padx=5,pady=5)
        self.entrada_t_uni8= tk.Entry(self.quadradoframe,font=self.fonte_entra,width=8)
        self.entrada_t_uni8.grid(row = 11,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.quadradoframe, text='10)',font=self.fonte_entra)
        self.numero_p.grid(row=12, column=1, padx=5, pady=5)
        self.entrada_pesas9 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=30)
        self.entrada_pesas9.grid(row = 12,column=2,padx =5,pady =5)
        self.entrada_uni9 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni9.grid(row = 12,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 12,column=4,padx=5,pady=5)
        self.entrada_v_uni9 = tk.Entry(self.quadradoframe, font=self.fonte_entra,width=8)
        self.entrada_v_uni9.grid(row = 12,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 12,column=6,padx=5,pady=5)
        self.entrada_t_uni9 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=8)
        self.entrada_t_uni9.grid(row = 12,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.quadradoframe, text='11)',font=self.fonte_entra)
        self.numero_p.grid(row=13, column=1, padx=5, pady=5)
        self.entrada_pesas10 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=30)
        self.entrada_pesas10.grid(row = 13,column=2,padx =5,pady =5)
        self.entrada_uni10 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni10.grid(row = 13,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 13,column=4,padx=5,pady=5)
        self.entrada_v_uni10 = tk.Entry(self.quadradoframe, font=self.fonte_entra,width=8)
        self.entrada_v_uni10.grid(row = 13,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 13,column=6,padx=5,pady=5)
        self.entrada_t_uni10 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=8)
        self.entrada_t_uni10.grid(row = 13,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.quadradoframe, text='12)',font=self.fonte_entra)
        self.numero_p.grid(row=14, column=1, padx=5, pady=5)
        self.entrada_pesas11 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=30)
        self.entrada_pesas11.grid(row = 14,column=2,padx =5,pady =5)
        self.entrada_uni11 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni11.grid(row = 14,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 14,column=4,padx=5,pady=5)
        self.entrada_v_uni11 = tk.Entry(self.quadradoframe, font=self.fonte_entra,width=8)
        self.entrada_v_uni11.grid(row = 14,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 14,column=6,padx=5,pady=5)
        self.entrada_t_uni11 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=8)
        self.entrada_t_uni11.grid(row = 14,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.quadradoframe, text='13)',font=self.fonte_entra)
        self.numero_p.grid(row=15, column=1, padx=5, pady=5)
        self.entrada_pesas12 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=30)
        self.entrada_pesas12.grid(row = 15,column=2,padx =5,pady =5)
        self.entrada_uni12 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni12.grid(row = 15,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 15,column=4,padx=5,pady=5)
        self.entrada_v_uni12 = tk.Entry(self.quadradoframe, font=self.fonte_entra,width=8)
        self.entrada_v_uni12.grid(row = 15,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 15,column=6,padx=5,pady=5)
        self.entrada_t_uni12 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=8)
        self.entrada_t_uni12.grid(row = 15,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.quadradoframe, text='14)',font=self.fonte_entra)
        self.numero_p.grid(row=16, column=1, padx=5, pady=5)
        self.entrada_pesas13 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=30)
        self.entrada_pesas13.grid(row = 16,column=2,padx =5,pady =5)
        self.entrada_uni13 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni13.grid(row = 16,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 16,column=4,padx=5,pady=5)
        self.entrada_v_uni13 = tk.Entry(self.quadradoframe, font=self.fonte_entra,width=8)
        self.entrada_v_uni13.grid(row = 16,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe, text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 16,column=6,padx=5,pady=5)
        self.entrada_t_uni13 = tk.Entry(self.quadradoframe,font=self.fonte_entra,width=8)
        self.entrada_t_uni13.grid(row = 16,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.quadradoframe, text='15)',font=self.fonte_entra)
        self.numero_p.grid(row=17, column=1, padx=5, pady=5)
        self.entrada_pesas14 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=30)
        self.entrada_pesas14.grid(row = 17,column=2,padx =5,pady =5)
        self.entrada_uni14 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni14.grid(row = 17,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 17,column=4,padx=5,pady=5)
        self.entrada_v_uni14 = tk.Entry(self.quadradoframe , font=self.fonte_entra,width=8)
        self.entrada_v_uni14.grid(row = 17,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 17,column=6,padx=5,pady=5)
        self.entrada_t_uni14 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=8)
        self.entrada_t_uni14.grid(row = 17,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.quadradoframe, text='16)',font=self.fonte_entra)
        self.numero_p.grid(row=18, column=1, padx=5, pady=5)
        self.entrada_pesas15 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=30)
        self.entrada_pesas15.grid(row = 18,column=2,padx =5,pady =5)
        self.entrada_uni15 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni15.grid(row = 18,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 18,column=4,padx=5,pady=5)
        self.entrada_v_uni15 = tk.Entry(self.quadradoframe , font=self.fonte_entra,width=8)
        self.entrada_v_uni15.grid(row = 18,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 18,column=6,padx=5,pady=5)
        self.entrada_t_uni15 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=8)
        self.entrada_t_uni15.grid(row = 18,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.quadradoframe, text='17)',font=self.fonte_entra)
        self.numero_p.grid(row=19, column=1, padx=5, pady=5)
        self.entrada_pesas16 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=30)
        self.entrada_pesas16.grid(row = 19,column=2,padx =5,pady =5)
        self.entrada_uni16 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni16.grid(row = 19,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 19,column=4,padx=5,pady=5)
        self.entrada_v_uni16 = tk.Entry(self.quadradoframe , font=self.fonte_entra,width=8)
        self.entrada_v_uni16.grid(row = 19,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 19,column=6,padx=5,pady=5)
        self.entrada_t_uni16 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=8)
        self.entrada_t_uni16.grid(row = 19,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.quadradoframe, text='18)',font=self.fonte_entra)
        self.numero_p.grid(row=20, column=1, padx=5, pady=5)
        self.entrada_pesas17 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=30)
        self.entrada_pesas17.grid(row = 20,column=2,padx =5,pady =5)
        self.entrada_uni17 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni17.grid(row = 20,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 20,column=4,padx=5,pady=5)
        self.entrada_v_uni17 = tk.Entry(self.quadradoframe , font=self.fonte_entra,width=8)
        self.entrada_v_uni17.grid(row = 20,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 20,column=6,padx=5,pady=5)
        self.entrada_t_uni17 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=8)
        self.entrada_t_uni17.grid(row = 20,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.quadradoframe, text='19)',font=self.fonte_entra)
        self.numero_p.grid(row=21, column=1, padx=5, pady=5)
        self.entrada_pesas18 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=30)
        self.entrada_pesas18.grid(row = 21,column=2,padx =5,pady =5)
        self.entrada_uni18 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni18.grid(row = 21,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 21,column=4,padx=5,pady=5)
        self.entrada_v_uni18 = tk.Entry(self.quadradoframe , font=self.fonte_entra,width=8)
        self.entrada_v_uni18.grid(row = 21,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 21,column=6,padx=5,pady=5)
        self.entrada_t_uni18 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=8)
        self.entrada_t_uni18.grid(row = 21,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.quadradoframe, text='20)',font=self.fonte_entra)
        self.numero_p.grid(row=22, column=1, padx=5, pady=5)
        self.entrada_pesas19 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=30)
        self.entrada_pesas19.grid(row = 22,column=2,padx =5,pady =5)
        self.entrada_uni19 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=3,
                                    validate='key',validatecommand=self.SonumeroTelefoneOs)
        self.entrada_uni19.grid(row = 22,column=3,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 22,column=4,padx=5,pady=5)
        self.entrada_v_uni19 = tk.Entry(self.quadradoframe , font=self.fonte_entra,width=8)
        self.entrada_v_uni19.grid(row = 22,column=5,padx =5,pady =5)
        self.Rs_escrita = tk.Label(self.quadradoframe , text='R$',font=self.fonte_entra)
        self.Rs_escrita.grid(row = 22,column=6,padx=5,pady=5)
        self.entrada_t_uni19 = tk.Entry(self.quadradoframe ,font=self.fonte_entra,width=8)
        self.entrada_t_uni19.grid(row = 22,column=7,padx =5,pady =5)

        self.numero_p = tk.Label(self.os_janela, text=f'{"RETIFICA":^88}',font=self.fonte_entra)
        self.numero_p.place(x=5,y=410)
        self.Rs_escrita = tk.Label(self.os_janela, text='R$',font=self.fonte_entra)
        self.Rs_escrita.place(x=500,y=410)
        self.Retifica = tk.Entry(self.os_janela,font=self.fonte_entra,width=8)
        self.Retifica.place(x=535,y=410)

        self.numero_p = tk.Label(self.os_janela, text=f'{"M.O":^90}', font=self.fonte_entra)
        self.numero_p.place(x=5,y=440)
        self.Rs_escrita = tk.Label(self.os_janela, text='R$',font=self.fonte_entra)
        self.Rs_escrita.place(x=500,y=440)
        self.M_O = tk.Entry(self.os_janela,font=self.fonte_entra,width=8)
        self.M_O.place(x=535,y=440)

        self.numero_p = tk.Label(self.os_janela, text=f'{"TOTAL PEÇAS":^80}',font=self.fonte_entra)
        self.numero_p.place(x=5,y=470)
        self.Rs_escrita = tk.Label(self.os_janela, text='R$',font=self.fonte_entra)
        self.Rs_escrita.place(x=500,y=470)
        self.PesasTotal = tk.Entry(self.os_janela,font=self.fonte_entra,width=8)
        self.PesasTotal.place(x=535,y=470)

        self.numero_p = tk.Label(self.os_janela, text=f'{"VALOR TOTAL":^80}',font=self.fonte_entra)
        self.numero_p.place(x=5,y=500)
        self.Rs_escrita = tk.Label(self.os_janela, text='R$',font=self.fonte_entra)
        self.Rs_escrita.place(x=500,y=500)
        self.TotalTotal = tk.Entry(self.os_janela,font=self.fonte_entra,width=8)
        self.TotalTotal.place(x=535,y=500)
        #self.AddCarroPedido()

    def PendetesJanela(self):
        self.InicioJanela()
        self.Fontes()

        self.quadradoPendentes = tk.Frame(self.cr_janela)
        self.quadradoPendentes.place(x=5,y=5,width=790,height=415)

        self.texto = tk.Label(self.cr_janela,text='PENDENTES',font=self.cabesario_font)
        self.texto.place(x=350, y=10)

        self.voltar = tk.Button(self.cr_janela,text="<VOLTAR", font=self.cabesario_voltar, bg="white",
                                foreground="black",command=self.cr_janela.destroy)
        self.voltar.place(x=10, y=10, width=80, height=30)

        self.lista_c_clirPendentes = ttk.Treeview(self.quadradoPendentes, height=600,
                                  columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6,col7',
                                           'col8', 'col9','col10','col11'))
        self.lista_c_clirPendentes.heading('#0', text='')
        self.lista_c_clirPendentes.heading('#1', text='N/O.S')
        self.lista_c_clirPendentes.heading('#2', text='Nome do Cliente')
        self.lista_c_clirPendentes.heading('#3', text='Whts')
        self.lista_c_clirPendentes.heading('#4', text='Placa')
        self.lista_c_clirPendentes.heading('#5', text='Codigo Clinte')
        self.lista_c_clirPendentes.heading('#6', text='Retifica')
        self.lista_c_clirPendentes.heading('#7', text='M_O')
        self.lista_c_clirPendentes.heading('#8', text='Total_peças')
        self.lista_c_clirPendentes.heading('#9', text='Total Valor OS')
        self.lista_c_clirPendentes.heading('#10', text='Data e Hora')
        self.lista_c_clirPendentes.column('#0', width=0)
        self.lista_c_clirPendentes.column('#1', width=50)
        self.lista_c_clirPendentes.column('#2', width=100)
        self.lista_c_clirPendentes.column('#3', width=100)
        self.lista_c_clirPendentes.column('#4', width=100)
        self.lista_c_clirPendentes.column('#5', width=100)
        self.lista_c_clirPendentes.column('#6', width=100)
        self.lista_c_clirPendentes.column('#7', width=100)
        self.lista_c_clirPendentes.column('#8', width=100)
        self.lista_c_clirPendentes.column('#9', width=150)
        self.lista_c_clirPendentes.column('#10', width=180)
        self.lista_c_clirPendentes.place(x=10, y=40, width=775, height=345)

        self.barra_lado = ttk.Scrollbar(self.cr_janela, orient='vertical',command=self.lista_c_clirPendentes.yview)
        self.lista_c_clirPendentes.configure(yscrollcommand=self.barra_lado.set)
        self.barra_lado.place(x=760, y=72, width=30, height=343)

        self.barra_baixo = ttk.Scrollbar(self.cr_janela, orient='horizontal',
                                              command=self.lista_c_clirPendentes.xview)
        self.lista_c_clirPendentes.configure(xscrollcommand=self.barra_baixo.set)
        self.barra_baixo.place(x=10, y=385, width=750, height=30)

        self.quadrado2Pendentes = tk.Frame(self.cr_janela)
        self.quadrado2Pendentes.place(x=5,y=425,width=790,height=120)

        self.criarCarro = tk.Button(self.cr_janela,text="Buscar\nPor Telefone", font=self.fonte_buton, bg="black",
                                    foreground="white",command=self.BuscarTelefonePendentes)
        self.criarCarro.place(x=30, y=440, width=150, height=50)
        self.entrada1 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.entrada1.place(x=30,y=500,width=150)
        self.criarCarro = tk.Button(self.cr_janela,text="Buscar Por\n Codigo do Cliente",font=self.fonte_buton,
                                    bg="black",foreground="white",command=self.BuscarCodigoPendentes)
        self.criarCarro.place(x=200, y=440, width=170, height=50)
        self.entrada2 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.entrada2.place(x=200,y=500,width=170)
        self.criarCarro = tk.Button(self.cr_janela,text="Buscar\nPor Placa", font=self.fonte_buton, bg="black",
                                    foreground="white",command=self.BuscarPlacaPendetes)
        self.criarCarro.place(x=390, y=440, width=150, height=50)
        self.entrada3 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.entrada3.place(x=390,y=500,width=150)

        self.AtualizeLista_Pendentes()
        self.lista_c_clirPendentes.bind("<Double-1>", self.AbrirPendentes)

    def FinalizadosJanela(self):
        self.InicioJanela()
        self.cr_janela.geometry('800x650')
        self.Fontes()
        self.ValidarEntr()
        self.quadradoFinalizados = tk.Frame(self.cr_janela)
        self.quadradoFinalizados.place(x=5,y=5,width=790,height=415)

        self.texto = tk.Label(self.cr_janela,text='FINALIZADOS',font=self.cabesario_font)
        self.texto.place(x=350, y=10)

        self.voltar = tk.Button(self.cr_janela,text="<VOLTAR", font=self.cabesario_voltar, bg="white",
                                foreground="black",command=self.cr_janela.destroy)
        self.voltar.place(x=10, y=10, width=80, height=30)

        self.lista_c_clirFinalizados = ttk.Treeview(self.quadradoFinalizados, height=600,
                                  columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6,col7',
                                           'col8', 'col9','col10','col11'))
        self.lista_c_clirFinalizados.heading('#0', text='')
        self.lista_c_clirFinalizados.heading('#1', text='N/O.S')
        self.lista_c_clirFinalizados.heading('#2', text='Nome do Cliente')
        self.lista_c_clirFinalizados.heading('#3', text='Whts')
        self.lista_c_clirFinalizados.heading('#4', text='Placa')
        self.lista_c_clirFinalizados.heading('#5', text='Codigo Clinte')
        self.lista_c_clirFinalizados.heading('#6', text='Retifica')
        self.lista_c_clirFinalizados.heading('#7', text='M_O')
        self.lista_c_clirFinalizados.heading('#8', text='Total_peças')
        self.lista_c_clirFinalizados.heading('#9', text='Total Valor OS')
        self.lista_c_clirFinalizados.heading('#10', text='Data e Hora')
        self.lista_c_clirFinalizados.column('#0', width=0)
        self.lista_c_clirFinalizados.column('#1', width=50)
        self.lista_c_clirFinalizados.column('#2', width=100)
        self.lista_c_clirFinalizados.column('#3', width=100)
        self.lista_c_clirFinalizados.column('#4', width=100)
        self.lista_c_clirFinalizados.column('#5', width=100)
        self.lista_c_clirFinalizados.column('#6', width=100)
        self.lista_c_clirFinalizados.column('#7', width=100)
        self.lista_c_clirFinalizados.column('#8', width=100)
        self.lista_c_clirFinalizados.column('#9', width=150)
        self.lista_c_clirFinalizados.column('#10', width=180)

        self.lista_c_clirFinalizados.place(x=10, y=40, width=775, height=345)

        self.barra_lado = ttk.Scrollbar(self.cr_janela, orient='vertical',command=self.lista_c_clirFinalizados.yview)
        self.lista_c_clirFinalizados.configure(yscrollcommand=self.barra_lado.set)
        self.barra_lado.place(x=760, y=72, width=30, height=343)

        self.barra_baixo = ttk.Scrollbar(self.cr_janela, orient='horizontal',
                                              command=self.lista_c_clirFinalizados.xview)
        self.lista_c_clirFinalizados.configure(xscrollcommand=self.barra_baixo.set)
        self.barra_baixo.place(x=10, y=385, width=750, height=30)

        self.quadrado2Pendentes = tk.Frame(self.cr_janela)
        self.quadrado2Pendentes.place(x=5, y=425, width=790, height=220)

        self.criarCarro = tk.Button(self.cr_janela, text="Buscar Por\n Codigo do Cliente", font=self.fonte_buton,
                                    bg="black", foreground="white", command=self.BuscarCodigoFinalizados)
        self.criarCarro.place(x=165, y=440, width=170, height=50)
        self.entrada2 = tk.Entry(self.cr_janela, font=self.fonte_buton)
        self.entrada2.place(x=165, y=500, width=170)
        self.criarCarro = tk.Button(self.cr_janela, text="Buscar\nPor Telefone", font=self.fonte_buton, bg="black",
                                    foreground="white", command=self.BuscarTelefoneFinalizados)
        self.criarCarro.place(x=10, y=440, width=150, height=50)
        self.entrada1 = tk.Entry(self.cr_janela, font=self.fonte_buton)
        self.entrada1.place(x=10, y=500, width=150)
        self.criarCarro = tk.Button(self.cr_janela, text="Buscar\nPor Placa", font=self.fonte_buton, bg="black",
                                    foreground="white", command=self.BuscarPlacaFinalizados)
        self.criarCarro.place(x=10, y=540, width=150, height=50)
        self.entrada3 = tk.Entry(self.cr_janela, font=self.fonte_buton)
        self.entrada3.place(x=10, y=600, width=150)

        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='Data Inicial').place(x=350, y=430)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='Data Final').place(x=570, y=430)

        self.calendario = tc.Calendar(self.cr_janela, locale='pt_br')
        self.calendario.place(x=350, y=450, width=200, height=180)
        self.calendario1 = tc.Calendar(self.cr_janela, locale='pt_br')
        self.calendario1.place(x=570, y=450, width=200, height=180)

        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='Data Inicial').place(x=165, y=520)
        self.Ent_calendario = tk.Entry(self.cr_janela, font=self.fonte_buton)
        self.Ent_calendario.place(x=165, y=540, width=170)

        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='Data Final').place(x=165, y=560)
        self.Ent_calendario1 = tk.Entry(self.cr_janela, font=self.fonte_buton)
        self.Ent_calendario1.place(x=165, y=580, width=170)

        self.calendarioData = tk.Button(self.cr_janela, text='Buscar Por Data', bg="black",
                                        foreground="white", command=self.Colocardata)
        self.calendarioData.place(x=165, y=600, width=170)

        self.AtualizeLista_Finalizados()
        self.lista_c_clirFinalizados.bind("<Double-1>", self.AbrirFinalizados)

    def GanhosJanela(self):
        self.InicioJanela()
        self.cr_janela.geometry('1100x650')
        self.Fontes()
        self.ValidarEntr()

        self.quadradoGanhos = tk.Frame(self.cr_janela)
        self.quadradoGanhos.place(x=5,y=5,width=790,height=415)

        self.texto = tk.Label(self.cr_janela,text='RENDIMENTOS',font=self.cabesario_font)
        self.texto.place(x=350, y=10)

        self.voltar = tk.Button(self.cr_janela,text="<VOLTAR", font=self.cabesario_voltar, bg="white",
                                foreground="black",command=self.cr_janela.destroy)
        self.voltar.place(x=10, y=10, width=80, height=30)

        self.lista_c_clirGanhos = ttk.Treeview(self.quadradoGanhos, height=600,
                                  columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6,col7',
                                           'col8', 'col9','col10','col11','col12','col13'))
        self.lista_c_clirGanhos.heading('#0', text='')
        self.lista_c_clirGanhos.heading('#1', text='N/O.S')
        self.lista_c_clirGanhos.heading('#2', text='Nome do Cliente')
        self.lista_c_clirGanhos.heading('#3', text='Whts')
        self.lista_c_clirGanhos.heading('#4', text='Placa')
        self.lista_c_clirGanhos.heading('#5', text='Forma de pagamento')
        self.lista_c_clirGanhos.heading('#6', text='Total Valor OS')
        self.lista_c_clirGanhos.heading('#7', text='Gasto em Peças')
        self.lista_c_clirGanhos.heading('#8', text='Gastos em Retifica')
        self.lista_c_clirGanhos.heading('#9', text='Gastos em outros')
        self.lista_c_clirGanhos.heading('#10', text='Valor Recebido')
        self.lista_c_clirGanhos.heading('#11', text='Ganho')
        self.lista_c_clirGanhos.heading('#12', text='Data e Hora')
        self.lista_c_clirGanhos.column('#0', width=0)
        self.lista_c_clirGanhos.column('#1', width=50)
        self.lista_c_clirGanhos.column('#2', width=100)
        self.lista_c_clirGanhos.column('#3', width=100)
        self.lista_c_clirGanhos.column('#4', width=100)
        self.lista_c_clirGanhos.column('#5', width=100)
        self.lista_c_clirGanhos.column('#6', width=100)
        self.lista_c_clirGanhos.column('#7', width=100)
        self.lista_c_clirGanhos.column('#8', width=100)
        self.lista_c_clirGanhos.column('#9', width=150)
        self.lista_c_clirGanhos.column('#10', width=150)
        self.lista_c_clirGanhos.column('#11', width=150)
        self.lista_c_clirGanhos.column('#12', width=180)
        self.lista_c_clirGanhos.place(x=10, y=40, width=775, height=345)

        self.barra_lado = ttk.Scrollbar(self.cr_janela, orient='vertical',command=self.lista_c_clirGanhos.yview)
        self.lista_c_clirGanhos.configure(yscrollcommand=self.barra_lado.set)
        self.barra_lado.place(x=760, y=72, width=30, height=343)

        self.barra_baixo = ttk.Scrollbar(self.cr_janela, orient='horizontal',
                                              command=self.lista_c_clirGanhos.xview)
        self.lista_c_clirGanhos.configure(xscrollcommand=self.barra_baixo.set)
        self.barra_baixo.place(x=10, y=385, width=750, height=30)

        self.quadrado2Pendentes = tk.Frame(self.cr_janela)
        self.quadrado2Pendentes.place(x=5,y=425,width=1090,height=220)

        self.Escrit = tk.Label(self.cr_janela,font=self.cabesario_font1,text='SOMA DOS VALORES\nREFERENTE A BUSCA ')
        self.Escrit.place(x=835,y=430)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='Valores Recebido').place(x=850,y=485)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=820, y=505)
        self.Ent_soma = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_soma.place(x=850,y=505,width=170)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='Valor Rendimento').place(x=850,y=535)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=820, y=555)
        self.Ent_soma1 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_soma1.place(x=850,y=555,width=170)

        self.Escrita = tk.Label(self.cr_janela,font=self.cabesario_font1,text='VALOR EM CAIXA').place(x=850,y=585)
        self.Escrita = tk.Label(self.cr_janela, font=self.cabesario_font1, text='R$').place(x=820, y=610)
        self.CAIXA = tk.Entry(self.cr_janela,font=self.cabesario_font1)
        self.CAIXA.place(x=850,y=610,width=170)

        self.criarCarro = tk.Button(self.cr_janela,text="Buscar Por\n Codigo do Cliente",font=self.fonte_buton,
                                    bg="black",foreground="white",command=self.BuscarCodigoGanhos)
        self.criarCarro.place(x=165, y=440, width=170, height=50)
        self.entrada2 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.entrada2.place(x=165,y=500,width=170)
        self.criarCarro = tk.Button(self.cr_janela,text="Buscar\nPor Telefone", font=self.fonte_buton, bg="black",
                                    foreground="white",command=self.BuscarTelefoneGanhos)
        self.criarCarro.place(x=10, y=440, width=150, height=50)
        self.entrada1 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.entrada1.place(x=10,y=500,width=150)
        self.criarCarro = tk.Button(self.cr_janela,text="Buscar\nPor Placa", font=self.fonte_buton, bg="black",
                                    foreground="white",command=self.BuscarPlacaGanhos)
        self.criarCarro.place(x=10, y=540, width=150, height=50)
        self.entrada3 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.entrada3.place(x=10,y=600,width=150)

        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='Data Inicial').place(x=350, y=430)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='Data Final').place(x=570, y=430)
        self.calendario = tc.Calendar(self.cr_janela,locale='pt_br')
        self.calendario.place(x=350,y=450,width=200, height=180)
        self.calendario1 = tc.Calendar(self.cr_janela,locale='pt_br')
        self.calendario1.place(x=570,y=450,width=200, height=180)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='Data Inicial').place(x=165,y=520)
        self.Ent_calendario = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_calendario.place(x=165,y=540,width=170)

        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='Data Final').place(x=165, y=560)
        self.Ent_calendario1 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_calendario1.place(x=165,y=580,width=170)

        self.calendarioData = tk.Button(self.cr_janela, text= 'Buscar Por Data',bg="black",
                                    foreground="white",command=self.ColocardataGanhos)
        self.calendarioData.place(x=165, y=600, width=170)

        self.quadrado3 = tk.Frame(self.cr_janela)
        self.quadrado3.place(x=800,y=5,width=295,height=415)

        self.Escrita = tk.Label(self.cr_janela, font=self.cabesario_font1, text='MODIFICAR RENDIMENTOS')\
            .place(x=835, y=10)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='N/Pedido').place(x=810,y=40)
        self.Ent_Ganhos = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Ganhos.place(x=810,y=65,width=100)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='Valor Gasto em Peças').place(x=865,y=100)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=840, y=125)
        self.Ent_Ganhos1 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Ganhos1.place(x=870,y=125,width=170)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='Valor Gasto em Retifica').place(x=865,y=150)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=840, y=175)
        self.Ent_Ganhos2 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Ganhos2.place(x=870,y=175,width=170)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='Valor Gasto em Outros').place(x=865,y=200)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=840, y=225)
        self.Ent_Ganhos3 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Ganhos3.place(x=870,y=225,width=170)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='Valor Recebido').place(x=890,y=260)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=840, y=290)
        self.Ent_Ganhos4 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Ganhos4.place(x=870,y=290,width=170)

        self.criar = tk.Button(self.cr_janela,text="Modificar",font=self.fonte_entra1,
                                    bg="black",foreground="white",command=self.Escolha_Modificar_Ganhos)
        self.criar.place(x=860, y=340, width=170, height=50)

        self.AtualizeLista_Ganhos()
        self.lista_c_clirGanhos.bind("<Double-1>", self.AbrirGanhos)

    def SaidaJanela(self):
        self.InicioJanela()
        self.cr_janela.geometry('1055x650')
        self.Fontes()
        self.ValidarEntr()

        self.quadradoGanhos = tk.Frame(self.cr_janela)
        self.quadradoGanhos.place(x=5,y=5,width=790,height=415)

        self.texto = tk.Label(self.cr_janela,text='SAIDAS',font=self.cabesario_font)
        self.texto.place(x=350, y=10)

        self.voltar = tk.Button(self.cr_janela,text="<VOLTAR", font=self.cabesario_voltar, bg="white",
                                foreground="black",command=self.cr_janela.destroy)
        self.voltar.place(x=10, y=10, width=80, height=30)

        self.lista_c_clirSaida = ttk.Treeview(self.quadradoGanhos, height=600,
                                  columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6,col7',
                                           'col8', 'col9'))
        self.lista_c_clirSaida.heading('#0', text='')
        self.lista_c_clirSaida.heading('#1', text='N/Saida')
        self.lista_c_clirSaida.heading('#2', text='Pago Por')
        self.lista_c_clirSaida.heading('#3', text='Tipo de gasto')
        self.lista_c_clirSaida.heading('#4', text='Gasto Com')
        self.lista_c_clirSaida.heading('#5', text='Local')
        self.lista_c_clirSaida.heading('#6', text='Valor da nota')
        self.lista_c_clirSaida.heading('#7', text='Valor Pago')
        self.lista_c_clirSaida.heading('#8', text='Data e Hora')
        self.lista_c_clirSaida.column('#0', width=0)
        self.lista_c_clirSaida.column('#1', width=50)
        self.lista_c_clirSaida.column('#2', width=100)
        self.lista_c_clirSaida.column('#3', width=100)
        self.lista_c_clirSaida.column('#4', width=100)
        self.lista_c_clirSaida.column('#5', width=100)
        self.lista_c_clirSaida.column('#6', width=100)
        self.lista_c_clirSaida.column('#7', width=100)
        self.lista_c_clirSaida.column('#8', width=180)

        self.lista_c_clirSaida.place(x=10, y=40, width=775, height=345)

        self.barra_lado = ttk.Scrollbar(self.cr_janela, orient='vertical',command=self.lista_c_clirSaida.yview)
        self.lista_c_clirSaida.configure(yscrollcommand=self.barra_lado.set)
        self.barra_lado.place(x=760, y=72, width=30, height=343)

        self.barra_baixo = ttk.Scrollbar(self.cr_janela, orient='horizontal',
                                              command=self.lista_c_clirSaida.xview)
        self.lista_c_clirSaida.configure(xscrollcommand=self.barra_baixo.set)
        self.barra_baixo.place(x=10, y=385, width=750, height=30)

        self.quadrado2 = tk.Frame(self.cr_janela)
        self.quadrado2.place(x=5,y=425,width=1045,height=220)

        self.Escrit = tk.Label(self.cr_janela,font=self.cabesario_font1,text='SOMA DOS VALORES REFERENTE A BUSCA')
        self.Escrit.place(x=40,y=430)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='SALARIOS').place(x=40,y=470)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=10, y=495)
        self.Ent_Svalor = tk.Entry(self.cr_janela,font=self.cabesario_font2)
        self.Ent_Svalor.place(x=40,y=495,width=100)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='PRODUTOS').place(x=40,y=520)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=10, y=545)
        self.Ent_Svalor1 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Svalor1.place(x=40,y=545,width=100)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='FERRAMENTAS').place(x=20,y=570)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=10, y=595)
        self.Ent_Svalor2 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Svalor2.place(x=40,y=595,width=100)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='ALUGUEIS').place(x=190,y=470)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=160, y=495)
        self.Ent_Svalor3 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Svalor3.place(x=190,y=495,width=100)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='QUEBRA DE CAIXA').place(x=155,y=520)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=160, y=545)
        self.Ent_Svalor4 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Svalor4.place(x=190,y=545,width=100)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='GARANTIAS').place(x=190,y=570)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=160, y=595)
        self.Ent_Svalor5 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Svalor5.place(x=190,y=595,width=100)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='AGUA').place(x=360,y=470)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=310, y=495)
        self.Ent_Svalor6 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Svalor6.place(x=340,y=495,width=100)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='LUZ').place(x=365,y=520)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=310, y=545)
        self.Ent_Svalor7 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Svalor7.place(x=340,y=545,width=100)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='OUTROS').place(x=350,y=570)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=310, y=595)
        self.Ent_Svalor8 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Svalor8.place(x=340,y=595,width=100)

        self.Escrita = tk.Label(self.cr_janela,font=self.cabesario_font1,text='VALOR EM CAIXA').place(x=445,y=430)
        self.Escrita = tk.Label(self.cr_janela, font=self.cabesario_font1, text='R$').place(x=450, y=460)
        self.CAIXA = tk.Entry(self.cr_janela,font=self.cabesario_font1)
        self.CAIXA.place(x=480,y=460,width=100)

        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='Data Inicial').place(x=610, y=425)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='Data Final').place(x=830, y=425)
        self.calendario = tc.Calendar(self.cr_janela,locale='pt_br')
        self.calendario.place(x=610,y=450,width=200, height=180)
        self.calendario1 = tc.Calendar(self.cr_janela,locale='pt_br')
        self.calendario1.place(x=830,y=450,width=200, height=180)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='Data Inicial').place(x=495,y=510)
        self.Ent_calendario = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_calendario.place(x=495,y=530,width=100)

        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='Data Final').place(x=495, y=550)
        self.Ent_calendario1 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_calendario1.place(x=495,y=570,width=100)

        self.calendarioData = tk.Button(self.cr_janela, text='Buscar Por Data',bg="black",
                                    foreground="white",command=self.ColocardataSaida)
        self.calendarioData.place(x=495, y=600, width=100)

        self.quadrado3 = tk.Frame(self.cr_janela)
        self.quadrado3.place(x=800,y=5,width=250,height=415)

        self.criar = tk.Button(self.cr_janela,text="Criar",font=self.cabesario_voltar,
                                    bg="black",foreground="white",command=self.CriarSaida)
        self.criar.place(x=940, y=40, width=100, height=30)

        self.Escrita = tk.Label(self.cr_janela, font=self.cabesario_font1, text='CRIAR E MODIFICAR SAIDA')\
            .place(x=810, y=6)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='N/Saida').place(x=810,y=30)
        self.Ent_Saida = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Saida.place(x=810,y=55,width=100)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='Pago Por:').place(x=830,y=80)
        self.Ent_Saida1 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Saida1.place(x=830,y=105,width=170)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='Tipo de Gasto:').place(x=825,y=130)
        self.Ent_Saida2 = tk.StringVar(self.cr_janela)
        self.tipv = ('SALARIO','PRODUTOS','FERAMENTAS','ALUGUEL','QUEBRA DE CAIXA','GARANTIAS','AGUA','LUZ','OUTROS')
        self.pormenu = tk.OptionMenu(self.cr_janela,self.Ent_Saida2,*self.tipv)
        self.pormenu.configure(bg="white",foreground="black")
        self.pormenu.place(x=830,y=150,width=170)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='Gasto Com:').place(x=825,y=180)
        self.Ent_Saida3 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Saida3.place(x=830,y=205,width=170)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='Local:').place(x=825,y=230)
        self.Ent_Saida4 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Saida4.place(x=830,y=255,width=170)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='Valor da Nota').place(x=825,y=280)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=810, y=305)
        self.Ent_Saida5 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Saida5.place(x=840,y=305,width=170)

        self.Escrita = tk.Label(self.cr_janela,font='Ariel',text='Valor Pago').place(x=825,y=330)
        self.Escrita = tk.Label(self.cr_janela, font='Ariel', text='R$').place(x=810, y=355)
        self.Ent_Saida6 = tk.Entry(self.cr_janela,font=self.fonte_buton)
        self.Ent_Saida6.place(x=840,y=355,width=170)

        self.criar = tk.Button(self.cr_janela,text="Modificar",font=self.cabesario_voltar,
                                    bg="black",foreground="white",command=self.Escolha_Modificar_Saida)
        self.criar.place(x=810, y=385, width=100, height=30)

        self.criar = tk.Button(self.cr_janela,text="Excluir",font=self.cabesario_voltar,
                                    bg="black",foreground="white",command=self.Escolha_apagar_Saida)
        self.criar.place(x=940, y=385, width=100, height=30)


        self.AtualizeLista_Saida()
        self.lista_c_clirSaida.bind("<Double-1>", self.AbrirSaida)
        #Intengrando Sistem Pos Venda

    def InicilSecuPosVenda(self):
        self.TelaSecundari()
        self.FrameSecu()
        self.SuperiorPosVenda0()
        self.LateralPosVenda()
        self.InferiorPosVenda1()
        self.AtualizeLista_PosVenda()
    def TelaSecundari(self):
        self.FontsCoresTamanhos()
        self.Secundaria = tk.Toplevel()
        self.Secundaria.title('Maicá Manutenção Automotiva')
        self.Secundaria.iconbitmap(self.diretorio + '\Imagens\icone.ico')
        self.Secundaria.geometry('1100x650')
        self.Secundaria.resizable(False, False)
        self.Secundaria.configure(background=self.CorDeFundo)
        self.Secundaria.transient(self.i_janela)
        self.Secundaria.focus_force()
        self.Secundaria.grab_set()
    def FrameSecu(self):
        self.FontsCoresTamanhos()
        self.quadrado = tk.Frame(self.Secundaria,background=self.CorFram)
        self.quadrado.place(x=5, y=5, width=790, height=415)

        self.quadrado1 = tk.Frame(self.Secundaria,background=self.CorFram)
        self.quadrado1.place(x=5,y=425,width=790,height=220)

        self.quadrado2 = tk.Frame(self.Secundaria,background=self.CorFram)
        self.quadrado2.place(x=800,y=5,width=295,height=640)
    def SuperiorPosVenda0(self):
        self.FontsCoresTamanhos()
        self.Ent_Hor = tk.StringVar(self.Secundaria)
        self.tipv = ('OFF','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00',
                     '22:00','00:00')
        self.pormenu = tk.OptionMenu(self.Secundaria,self.Ent_Hor,*self.tipv)
        self.pormenu.configure(background=self.CorFram,foreground="white")
        self.pormenu.place(x=10,y=10,width=70)

        self.texto = tk.Label(self.Secundaria, text='Agendar Horario \nPara desligar o computador',
                              background=self.CorFram,foreground=self.CorLetraEscrit, font=('Ariel','8'))
        self.texto.place(x=80, y=5)

        self.texto = tk.Label(self.Secundaria, text='ENVIOS', background=self.CorFram,
                              foreground=self.CorLetraEscrit, font=self.FontSecu)
        self.texto.place(x=250, y=5)

        self.te = tk.Label(self.Secundaria, text='1°Horario\nDe Envio',
                              background=self.CorFram,foreground=self.CorLetraEscrit, font=('Ariel','8'))
        self.te.place(x=400, y=5)

        self.Ent_Hor1 = tk.StringVar(self.Secundaria)
        self.tipv1 = ('OFF','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00',
                      '18:00','19:00','20:00','21:00',)
        self.pormenu1 = tk.OptionMenu(self.Secundaria,self.Ent_Hor1,*self.tipv1)
        self.pormenu1.configure(background=self.CorFram,foreground="white")
        self.pormenu1.place(x=460,y=10,width=70)

        self.te = tk.Label(self.Secundaria, text='2°Horario\nDe Envio',
                              background=self.CorFram,foreground=self.CorLetraEscrit, font=('Ariel','8'))
        self.te.place(x=540, y=5)

        self.Ent_Hor2 = tk.StringVar(self.Secundaria)
        self.tipv2 = ('OFF','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00',
                      '17:00','18:00','19:00','20:00','21:00',)
        self.pormenu2 = tk.OptionMenu(self.Secundaria,self.Ent_Hor2,*self.tipv2)
        self.pormenu2.configure(background=self.CorFram,foreground="white")
        self.pormenu2.place(x=600,y=10,width=70)

        self.Salvado = tk.StringVar()
        self.Salvado.set('Agendar Horarios')

        self.Botao = tk.Button(self.Secundaria, textvariable=self.Salvado,font=('Ariel','10'), bg=self.CorFundoBotao,
                               foreground=self.CorLetraBotao, command=self.ModificarHorario)
        self.Botao.place(x=680, y=10, width=110)

        self.lista = ttk.Treeview(self.Secundaria, height=600,
                                              columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6,col7','col8',
                                                       'col9','col10'))
        self.lista.heading('#0', text='')
        self.lista.heading('#1', text='N/Envio')
        self.lista.heading('#2', text='Nome Cliente')
        self.lista.heading('#3', text='Fone Whats')
        self.lista.heading('#4', text='N/Cliente')
        self.lista.heading('#5', text='Criada na Data')
        self.lista.heading('#6', text='Data a Executar')
        self.lista.heading('#7', text='Mensagem_1')
        self.lista.heading('#8', text='Mensagem_2')
        self.lista.heading('#9', text='Mensagem_3')
        self.lista.column('#0', width=0)
        self.lista.column('#1', width=80)
        self.lista.column('#2', width=150)
        self.lista.column('#3', width=100)
        self.lista.column('#4', width=100)
        self.lista.column('#5', width=100)
        self.lista.column('#6', width=80)
        self.lista.column('#7', width=400)
        self.lista.column('#8', width=400)
        self.lista.column('#9', width=400)
        self.lista.place(x=10, y=45, width=780, height=345)

        self.barra_lado = ttk.Scrollbar(self.Secundaria, orient='vertical',command=self.lista.yview)
        self.lista.configure(yscrollcommand=self.barra_lado.set)
        self.barra_lado.place(x=760, y=72, width=30, height=343)

        self.barra_baixo = ttk.Scrollbar(self.Secundaria, orient='horizontal',
                                              command=self.lista.xview)
        self.lista.configure(xscrollcommand=self.barra_baixo.set)
        self.barra_baixo.place(x=10, y=385, width=750, height=30)
        self.ColocarHorario()
        self.lista.bind("<Double-1>", self.Abrir_Pos_Venda)
    def InferiorPosVenda1(self):
        self.FontsCoresTamanhos()

        self.Escrit = tk.Label(self.Secundaria,font=self.FontSecu,background=self.CorFram,
                               foreground=self.CorLetraEscrit,text='MENSAGENS A ENVIAR')
        self.Escrit.place(x=130,y=425)

        self.Botao = tk.Button(self.Secundaria, text='Criar\nMensagem',font=('Ariel','10'), bg=self.CorFundoBotao,
                               foreground=self.CorLetraBotao, command=self.Gerar_Mensagens)
        self.Botao.place(x=420, y=430, width=80)

        self.Botao = tk.Button(self.Secundaria, text='Buscar\nMensagem',font=('Ariel','10'), bg=self.CorFundoBotao,
                               foreground=self.CorLetraBotao, command=self.InicilMensagens)
        self.Botao.place(x=510, y=430, width=80)

        self.Botao = tk.Button(self.Secundaria, text='Modificar\nMensagem',font=('Ariel','10'), bg=self.CorFundoBotao,
                               foreground=self.CorLetraBotao, command=self.Escolha_Modificar_Mensagens)
        self.Botao.place(x=600, y=430, width=80)

        self.Botao = tk.Button(self.Secundaria, text='Excluir\nMensagem',font=('Ariel','10'), bg=self.CorFundoBotao,
                               foreground=self.CorLetraBotao, command=self.Escolha_apagar_Mensagens)
        self.Botao.place(x=690, y=430, width=80)

        self.Escrit = tk.Label(self.Secundaria,font=self.FontSecu2,background=self.CorFram,
                               foreground=self.CorLetraEscrit1,text='N/Men...')
        self.Escrit.place(x=20,y=425)
        self.CM = tk.Entry(self.Secundaria,font=(10))
        self.CM.place(x=20,y=445,width=60)

        self.Escrit = tk.Label(self.Secundaria,font=self.FontSecu1,background=self.CorFram,
                               foreground=self.CorLetraEscrit1,text='Mensagens 1')
        self.Escrit.place(x=20,y=465)
        self.Ent_Mensagem = tk.Entry(self.Secundaria,font=self.FontEntras)
        self.Ent_Mensagem.place(x=20,y=495,width=770)


        self.Escrit = tk.Label(self.Secundaria,font=self.FontSecu1,background=self.CorFram,
                               foreground=self.CorLetraEscrit1,text='Mensagens 2')
        self.Escrit.place(x=20,y=525)
        self.Ent_Mensagem1 = tk.Entry(self.Secundaria,font=self.FontEntras)
        self.Ent_Mensagem1.place(x=20,y=555,width=770)

        self.Escrit = tk.Label(self.Secundaria,font=self.FontSecu1,background=self.CorFram,
                               foreground=self.CorLetraEscrit1,text='Mensagens 3')
        self.Escrit.place(x=20,y=580)
        self.Ent_Mensagem2 = tk.Entry(self.Secundaria,font=self.FontEntras)
        self.Ent_Mensagem2.place(x=20,y=610,width=770)
    def LateralPosVenda(self):
        self.ValidandoTelSec()
        self.FontsCoresTamanhos()
        self.Escrita = tk.Label(self.Secundaria, font=self.FontSecu
                                ,background=self.CorFram,foreground=self.CorLetraEscrit,text='INCERIR POS VENDA')
        self.Escrita.place(x=805, y=10)

        self.Botao = tk.Button(self.Secundaria, text='CRIAR', font=self.FontBotao1, bg=self.CorFundoBotao,
                               foreground=self.CorLetraBotao,command=self.Gerar_Pos_Vendas)
        self.Botao.place(x=875, y=50, width=self.LarBotIni1, height=self.AutBotIni1)

        self.Botao = tk.Button(self.Secundaria, text='MODIFICAR', font=self.FontBotao1, bg=self.CorFundoBotao,
                               foreground=self.CorLetraBotao,command=self.Escolha_Modificar_PosVenda)
        self.Botao.place(x=805, y=100, width=self.LarBotIni1, height=self.AutBotIni1)

        self.Botao = tk.Button(self.Secundaria, text='EXCLUIR', font=self.FontBotao1, bg=self.CorFundoBotao,
                               foreground=self.CorLetraBotao,command=self.Escolha_apagar_PosVenda)
        self.Botao.place(x=950, y=100, width=self.LarBotIni1, height=self.AutBotIni1)

        self.Botao = tk.Button(self.Secundaria, text='INCIRIR/\nCLIENTE', font=self.FontBotao1, bg=self.CorFundoBotao,
                               foreground=self.CorLetraBotao,command=self.AddEmPosVenda)
        self.Botao.place(x=875, y=150, width=self.LarBotIni1, height=self.AutBotIni1)

        self.Botao = tk.Button(self.Secundaria, text='Limpar Dados', font=self.FontBotao1, bg=self.CorFundoBotao,
                               foreground=self.CorLetraBotao, command=self.Limpar_Pos_Venda)
        self.Botao.place(x=990, y=200)


        self.Escrita = tk.Label(self.Secundaria,font='Ariel',text='N/Pos Venda',background=self.CorFram,
                                foreground=self.CorLetraEscrit1)
        self.Escrita.place(x=845,y=235)
        self.Ent = tk.Entry(self.Secundaria,font=self.FontEntras)
        self.Ent.place(x=845,y=260,width=100)

        self.Escrita = tk.Label(self.Secundaria,font='Ariel',text='N/Clientes',background=self.CorFram,
                                foreground=self.CorLetraEscrit1)
        self.Escrita.place(x=955,y=235)
        self.Ent1 = tk.Entry(self.Secundaria,font=self.FontEntras)
        self.Ent1.place(x=955,y=260,width=100)

        self.Escrita = tk.Label(self.Secundaria,font='Ariel',text='Nome do Cliente',background=self.CorFram,
                                foreground=self.CorLetraEscrit1)
        self.Escrita.place(x=865,y=285)
        self.Ent2 = tk.Entry(self.Secundaria,font=self.FontEntras)
        self.Ent2.place(x=865,y=310,width=170)

        self.Escrita = tk.Label(self.Secundaria,font='Ariel',text='WhatsApp',background=self.CorFram,
                                foreground=self.CorLetraEscrit1)
        self.Escrita.place(x=865,y=335)
        self.Ent3 = tk.Entry(self.Secundaria,font=self.FontEntras,validate='key',
                             validatecommand=self.SonumeroTelefoneSec)
        self.Ent3.place(x=865,y=360,width=170)

        self.Botao = tk.Button(self.Secundaria, text='Colocar Data', font=self.FontBotao2, bg=self.CorFundoBotao,
                               foreground=self.CorLetraBotao,command=self.ColocardataPos)
        self.Botao.place(x=950, y=425, width=120, height=25)

        self.Escrita = tk.Label(self.Secundaria, font='Ariel', text='Data De Excusão',background=self.CorFram,
                                foreground=self.CorLetraEscrit1)
        self.Escrita.place(x=805, y=400)

        self.Ent4 = tk.Entry(self.Secundaria, font=self.FontEntras)
        self.Ent4.place(x=805, y=425, width=130)

        self.calendario = tc.Calendar(self.Secundaria, locale='pt_br')
        self.calendario.place(x=850, y=455, width=200, height=180)

    def InicilMensagens(self):
        self.TelaSecundariMensagens()
        self.FrameSecuMensagens()
        self.SuperiorMensagens0()
        self.AtualizeLista_Mensagens()
    def TelaSecundariMensagens(self):
        self.FontsCoresTamanhos()
        self.SecundariaM = tk.Toplevel()
        self.SecundariaM.title('Maicá Manutenção Automotiva')
        self.SecundariaM.iconbitmap(self.diretorio + '\Imagens\icone.ico')
        self.SecundariaM.geometry('800x425')
        self.SecundariaM.resizable(False, False)
        self.SecundariaM.configure(background=self.CorDeFundo)
        self.SecundariaM.transient(self.Secundaria)
        self.SecundariaM.focus_force()
        self.SecundariaM.grab_set()
    def FrameSecuMensagens(self):
        self.FontsCoresTamanhos()
        self.quadrado = tk.Frame(self.SecundariaM,background=self.CorFram)
        self.quadrado.place(x=5, y=5, width=790, height=415)
    def SuperiorMensagens0(self):
        self.FontsCoresTamanhos()

        self.texto = tk.Label(self.SecundariaM, text='MENSAGENS', background=self.CorFram,
                              foreground=self.CorLetraEscrit, font=self.FontSecu)
        self.texto.place(x=330, y=10)

        self.listaM = ttk.Treeview(self.SecundariaM, height=600,
                                              columns=('col1', 'col2', 'col3', 'col4'))
        self.listaM.heading('#0', text='')
        self.listaM.heading('#1', text='N/Mensagem')
        self.listaM.heading('#2', text='Mensagem_1')
        self.listaM.heading('#3', text='Mensagem_2')
        self.listaM.heading('#4', text='Mensagem_3')
        self.listaM.column('#0', width=0)
        self.listaM.column('#1', width=80)
        self.listaM.column('#2', width=400)
        self.listaM.column('#3', width=400)
        self.listaM.column('#4', width=400)
        self.listaM.place(x=10, y=45, width=780, height=345)

        self.barra_ladoM = ttk.Scrollbar(self.SecundariaM, orient='vertical',command=self.listaM.yview)
        self.listaM.configure(yscrollcommand=self.barra_ladoM.set)
        self.barra_ladoM.place(x=760, y=72, width=30, height=343)

        self.barra_baixoM = ttk.Scrollbar(self.SecundariaM, orient='horizontal',
                                              command=self.listaM.xview)
        self.listaM.configure(xscrollcommand=self.barra_baixoM.set)
        self.barra_baixoM.place(x=10, y=385, width=750, height=30)

        self.listaM.bind("<Double-1>", self.Abrir_Mensagens)

    def InicilServiços(self):
        self.TelaServiços()
        self.FrameServiços()
        self.SuperiorServiços()
        self.Aba1Serviços()
    def TelaServiços(self):
        self.FontsCoresTamanhos()
        self.Secundaria = tk.Toplevel()
        self.Secundaria.title('Maicá Manutenção Automotiva')
        self.Secundaria.iconbitmap(self.diretorio + '\Imagens\icone.ico')
        self.Secundaria.geometry('1100x650')
        self.Secundaria.resizable(False, False)
        self.Secundaria.configure(background=self.CorDeFundo)
        self.Secundaria.transient(self.i_janela)
        self.Secundaria.focus_force()
        self.Secundaria.grab_set()
    def FrameServiços(self):
        self.FontsCoresTamanhos()
        self.quadrado = tk.Frame(self.Secundaria,background=self.CorFram)
        self.quadrado.place(x=5, y=5, width=1090, height=640)
    def SuperiorServiços(self):
        self.Fontes()
        self.abas = ttk.Notebook(self.quadrado)

        self.abas.place(x=0,y=0, width=1090, height=640)

        self.aba1 = tk.Frame(self.abas)
        self.aba2 = tk.Frame(self.abas)
        self.abas.add(self.aba1, text='Serviços')
        self.abas.add(self.aba2, text='Adicionar')
        self.aba1.configure(background='DarkRed')
        self.aba2.configure(background='DarkRed')

        self.style.configure("TNotebook.Tab",
                             foreground='black',
                             font=('Calbri',15))
    def Aba1Serviços(self):
        self.lista = ttk.Treeview(self.aba1, height=600,
                                              columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6,col7','col8',
                                                       'col9','col10'))
        self.lista.heading('#0', text='')
        self.lista.heading('#1', text='N/Serviço')
        self.lista.heading('#2', text='Descrição')
        self.lista.heading('#3', text='Aplicação')
        self.lista.heading('#4', text='')
        self.lista.heading('#5', text='Criada na Data')
        self.lista.heading('#6', text='Data a Executar')
        self.lista.heading('#7', text='Mensagem_1')
        self.lista.heading('#8', text='Mensagem_2')
        self.lista.heading('#9', text='Mensagem_3')
        self.lista.column('#0', width=0)
        self.lista.column('#1', width=80)
        self.lista.column('#2', width=150)
        self.lista.column('#3', width=100)
        self.lista.column('#4', width=100)
        self.lista.column('#5', width=100)
        self.lista.column('#6', width=80)
        self.lista.column('#7', width=400)
        self.lista.column('#8', width=400)
        self.lista.column('#9', width=400)
        self.lista.place(x=10, y=45, width=780, height=345)

        self.barra_lado = ttk.Scrollbar(self.aba1, orient='vertical',command=self.lista.yview)
        self.lista.configure(yscrollcommand=self.barra_lado.set)
        self.barra_lado.place(x=760, y=72, width=30, height=343)

        self.barra_baixo = ttk.Scrollbar(self.aba1, orient='horizontal',
                                              command=self.lista.xview)
        self.lista.configure(xscrollcommand=self.barra_baixo.set)
        self.barra_baixo.place(x=10, y=385, width=750, height=30)

    def InicioJanela(self):
        self.cr_janela = tk.Toplevel()
        self.cr_janela.title('Maicá Manutenção Automotiva')
        self.cr_janela.iconbitmap(self.diretorio + '\Imagens\icone.ico')
        self.cr_janela.geometry('800x550')
        self.cr_janela.resizable(False, False)
        self.cr_janela.configure(background='#1e0000')
        self.cr_janela.transient(self.i_janela)
        self.cr_janela.focus_force()
        self.cr_janela.grab_set()
    def Fontes(self):
        self.cabesario_font = ("Arial Black", "13")
        self.fonte_titlo = ("Arial Black Italia", "10")
        self.fonte_entra1 = ("Arial ", "15")
        self.fonte_entra = ("Arial Black ", "12")
        self.fonte_buton = ("Arial", "10")
        self.cabesario_voltar = ("Arial Black", "10")
        self.cabesario_font1 = ("Arial Black", "11")
        self.cabesario_font2 = ("Arial", "11")
    def ValidarEntr(self):
        self.SonumeroTelefone = (self.cr_janela.register(self.ValidasaoTelefone),'%P')
    def ValorArumado(self):
        self.SonumeroTelefoneOs = (self.os_janela.register(self.ValidasaoTelefone),'%P')
    def ValidandoTelSec(self):
        self.SonumeroTelefoneSec = (self.Secundaria.register(self.ValidasaoTelefone),'%P')
    def FontsCoresTamanhos(self):
        # Fonts
        self.FontSecu = ('Akzidenz Grotesk', 18,"bold")
        self.FontBotao = ('Akzidenz Grotesk', '14')
        self.FontBotao1 = ('Akzidenz Grotesk', '10')
        self.FontBotao2 = ('Akzidenz Grotesk', '10')
        self.FontSecu1 = ("Arial", 16, "bold", "italic")
        self.FontSecu2 = ("Arial", 10, "bold", "italic")
        self.FontEntras =('Akzidenz Grotesk', 13,"bold")
        self.FontMsg = ("Arial", 16, "bold", "italic")
        # Cores
        self.CorFram = ('#8B0000')
        self.CorFundoBotao = ('Black')
        self.CorLetraBotao = ('white')
        self.CorLetraEscrit = ('white')
        self.CorLetraEscrit1 = ('white')
        self.CorDeFundo = ('white')
        # Tamanhos
        self.LarBotIni = 200
        self.AutBotIni = 60
        self.LarBotIni1 = 140
        self.AutBotIni1 = 40

fora = PastasBAncos()
fora.criar_pasta_banco()
fora.criar_lisa_clientes()
fora.criar_lisa_carro()
fora.criar_lista_pendentes()
fora.criar_banco_finalizados()
fora.criar_saida()
fora.Criar_Pos_Vendas()
fora.Criar_Mensagens()

if __name__ == '__main__':
    inicil = tk.Tk()
    InicioPrograma(inicil)
    inicil.mainloop()