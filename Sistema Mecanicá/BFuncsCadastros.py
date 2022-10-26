from AFuncGlobal import *

class Funcs_clintes(PastasBAncos):
    def __init__(self):
        super().__init__()
        self.cabesario_voltar = None
        self.cabesario_font = None
        self.c_janela = None
        self.diretorio = None
        self.os = None
        self.lista_c_clir = None
        self.entrada = None
        self.entrada1 = None
        self.entrada2 = None
        self.entrada3 = None
        self.entrada4 = None
        self.entrada5 = None
        self.entrada6 = None
        self.entrada7 = None
        self.entrada8 = None
    def LimpaEnterClientes(self):
        self.entrada.delete(0, tk.END)
        self.entrada1.delete(0, tk.END)
        self.entrada2.delete(0, tk.END)
        self.entrada3.delete(0, tk.END)
        self.entrada4.delete(0, tk.END)
        self.entrada5.delete(0, tk.END)
        self.entrada6.delete(0, tk.END)
        self.entrada7.delete(0, tk.END)
        self.entrada8.delete(0, tk.END)
    def VariaveiClientes(self):
        self.NumeroTemClinte = self.entrada.get()
        self.nome = self.entrada1.get().strip().title().replace(' ', '_')
        self.telefone = self.entrada2.get().replace(' ', '').replace('-', '').replace('(', '').replace(')','')
        self.telefone2 = self.entrada3.get().replace(' ', '').replace('-', '').replace('(', '').replace(')','')
        self.nacimento = self.entrada4.get().strip().replace(' ', '/').replace('-', '/')
        self.cpf = self.entrada5.get().strip().replace(' ', '').replace('-', '')
        self.cep = self.entrada6.get().strip().replace(' ', '').replace('-', '')
        self.numero_casa = self.entrada7.get().strip().replace(' ', '').replace('-', '')
        self.complemento = self.entrada8.get().strip().title().replace(' ', '_')
    def ConequitarBancoClinetes(self):
        self.pasta_bancos()
        self.conexao_clientes = sqlite3.connect('Banco_clientes.db')
        self.c = self.conexao_clientes.cursor()
    def DesconequitarBancoClientes(self):
        self.conexao_clientes.commit()
        self.conexao_clientes.close()
        os.chdir(diretorio)
    def AddClinete(self):
        self.VariaveiClientes()
        self.pasta_bancos()
        conn = sqlite3.connect('Banco_clientes.db')
        cursor = conn.cursor()
        cursor.execute('SELECT *, oid FROM dados_clientes')
        tes = cursor.fetchall()
        for i, a in enumerate(tes):
            numero = (a[1])
            cliente = (a[0])
            numero_cliente = (a[8])
            if self.telefone.strip().replace(' ', '').replace('-', '').replace('(', '').replace(')', '') == numero:
                self.Mensagenscaixa()
                self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!TELEFONE JÁ CADASTRADO!!!')
                self.jMensagem.place(x=40, y=10)
                self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text=f'O Telefone {numero}\nPertence ao'
                                                                          f' o cliente\n {cliente}\n'
                                                                          f'O codigo do cliente {numero_cliente}!')
                self.j2Mensagem.place(x=5, y=40)
                self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
                self.jbotam.place(x=280, y=90, width=100, height=40)
                return
        conn.commit()
        conn.close()
        max = self.telefone[:10]
        mix = self.telefone[11:].replace('', 'A')
        if self.entrada1.get() == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!NOME NÃO INSIRIDO!!!')
            self.jMensagem.place(x=80, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o nome do cliente!')
            self.j2Mensagem.place(x=50, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif self.telefone <= max:
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!ERRO NO NUMERO!!!')
            self.jMensagem.place(x=80, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='O numero de telefone está pequeno de mais!\nDigi'
                                                                      'te o numero com 11 digitos.exp (51999999999).')
            self.j2Mensagem.place(x=10, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif mix != 'A':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!ERRO NO NUMERO!!!')
            self.jMensagem.place(x=80, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='O numero de telefone esta grande de mais!\nDigi'
                                                                      'te o numero com 11 digitos.exp (51999999999).')
            self.j2Mensagem.place(x=10, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.ConequitarBancoClinetes()

            self.c.execute("""INSERT INTO dados_clientes (cliente,telefone,telefone_2,data_nacimento,
            cpf,cep,numero_casa,complemento) VALUES (?,?,?,?,?,?,?,?)""",
                           (self.nome, self.telefone, self.telefone2, self.nacimento,
                            self.cpf, self.cep, self.numero_casa, self.complemento))
            self.DesconequitarBancoClientes()

            self.AtualizeLista_clientes()
            self.LimpaEnterClientes()
            os.chdir(diretorio)
    def AtualizeLista_clientes(self):
        self.lista_c_clir.delete(*self.lista_c_clir.get_children())
        self.ConequitarBancoClinetes()
        lista_clientes = self.c.execute("""SELECT numero_cliente,cliente,telefone,telefone_2,data_nacimento,cpf
        ,cep,numero_casa,complemento FROM dados_clientes ORDER BY numero_cliente DESC;""")
        for i in lista_clientes:
            self.lista_c_clir.insert("", tk.END,values=i)
        self.DesconequitarBancoClientes()
    def SelencionarCliente(self,event):
        self.LimpaEnterClientes()
        self.lista_c_clir.selection()

        for n in self.lista_c_clir.selection():
            col1,col2,col3,col4,col5,col6,col7,col8,col9 = self.lista_c_clir.item(n, 'values')
            self.entrada.insert(tk.END,col1)
            self.entrada1.insert(tk.END, col2)
            self.entrada2.insert(tk.END, col3)
            self.entrada3.insert(tk.END, col4)
            self.entrada4.insert(tk.END, col5)
            self.entrada5.insert(tk.END, col6)
            self.entrada6.insert(tk.END, col7)
            self.entrada7.insert(tk.END, col8)
            self.entrada8.insert(tk.END, col9)
    def Escolha_apagar(self):
        if self.entrada.get() == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!CLIENTE NÃO INSIRIDO!!!')
            self.jMensagem.place(x=70, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o numero do cliente!')
            self.j2Mensagem.place(x=60, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_voltar, text='!VOCÊ REALMENTE'
                                                                                   ' QUER APAGAR ESSE CLIENTE!')
            self.jMensagem.place(x=15, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='Está ação não poderar ser desfeita!')
            self.j2Mensagem.place(x=70, y=50)
            self.simbotam = tk.Button(self.aviso, text='SIM', font='Ariel', command=self.DeletaClinte)
            self.simbotam.place(x=70, y=90, width=100, height=40)
            self.naobotam = tk.Button(self.aviso, text='NÃO', font='Ariel', command=self.aviso.destroy)
            self.naobotam.place(x=220, y=90, width=100, height=40)
    def DeletaClinte(self):
        try:
            self.VariaveiClientes()
            self.ConequitarBancoClinetes()
            self.c.execute(f"""DELETE FROM dados_clientes WHERE numero_cliente = {self.NumeroTemClinte} """)

            self.DesconequitarBancoClientes()
            self.LimpaEnterClientes()
            self.AtualizeLista_clientes()
            self.aviso.destroy()
        except:
            pass
        finally:
            os.chdir(diretorio)
    def Escolha_modificar(self):
        if self.entrada.get() == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!CLIENTE NÃO INSIRIDO!!!')
            self.jMensagem.place(x=70, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o numero do cliente!')
            self.j2Mensagem.place(x=60, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_voltar, text='!VOCÊ REALMENTE!\n'
                                                                                   ' !QUER MODIFICAR ESSE CLIENTE!')
            self.jMensagem.place(x=70, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='Está ação não poderar ser desfeita!')
            self.j2Mensagem.place(x=70, y=60)
            self.simbotam = tk.Button(self.aviso, text='SIM', font='Ariel', command=self.ModificarClintes)
            self.simbotam.place(x=70, y=90, width=100, height=40)
            self.naobotam = tk.Button(self.aviso, text='NÃO', font='Ariel', command=self.aviso.destroy)
            self.naobotam.place(x=220, y=90, width=100, height=40)
    def ModificarClintes(self):
        self.VariaveiClientes()
        self.ConequitarBancoClinetes()
        self.c.execute(f"""UPDATE dados_clientes SET cliente = ?
        ,telefone = ?,telefone_2 = ?,data_nacimento = ?
        ,cpf = ?,cep = ?,numero_casa = ?,complemento = ?
         WHERE numero_cliente = ?""",
                       (self.nome.strip().title().replace(' ', '_')
                        ,self.telefone.strip().replace(' ', '').replace('-', '').replace('(', '').replace(')', ''),
                        self.telefone2.strip().replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
                        ,self.nacimento.strip().replace(' ', '/').replace('-', '/')
                        ,self.cpf.strip().replace(' ', '').replace('-', '')
                        ,self.cep.strip().replace(' ', '').replace('-', '')
                        ,self.numero_casa.strip().replace(' ', '').replace('-', '')
                        ,self.complemento.strip().title().replace(' ', '_'),self.NumeroTemClinte))
        self.DesconequitarBancoClientes()
        self.AtualizeLista_clientes()
        self.LimpaEnterClientes()
        self.aviso.destroy()
    def Buscar_cliente(self):
        self.coluna = self.Ent_Busca.get().replace('Nome','cliente').replace('Telefone','telefone')\
            .replace('CPF','cpf').replace('N/Cliente','numero_cliente')
        self.linha = self.Entrada_busca.get()
        self.lista_c_clir.delete(*self.lista_c_clir.get_children())
        self.ConequitarBancoClinetes()
        self.c.execute("""SELECT numero_cliente,cliente,telefone,telefone_2,data_nacimento,cpf
        ,cep,numero_casa,complemento FROM dados_clientes ORDER BY cliente ASC;""")
        DadosCliente = self.c.execute(f'SELECT numero_cliente,cliente,telefone,telefone_2,data_nacimento'
                                      f',cpf,cep,numero_casa,complemento FROM dados_clientes WHERE '
                                      f'{self.coluna} LIKE "%{self.linha}%" ORDER BY numero_cliente DESC;')

        for i in DadosCliente:
            self.lista_c_clir.insert("", tk.END,values=i)

        self.DesconequitarBancoClientes()



class Funcs_Carro(Funcs_clintes):
    def __init__(self):
        super().__init__()
        self.codigo_carro =None
        self.fonte_buton = None
        self.fonte_entra = None
        self.fonte_titlo = None
        self.codigo = None
        self.nome = None
        self.telefone = None
        self.diretorio = None
        self.cr_janela = None
        self.os = None
        self.lista_c_clirCarro = None
        self.entradaCarro = None
        self.entrada1Carro = None
        self.entrada2Carro = None
        self.entrada3Carro = None
        self.entrada4Carro = None
        self.entrada5Carro = None
        self.entrada6Carro = None
        self.entrada7Carro = None
        self.entrada8Carro = None
        self.entrada = None
        self.entrada1 = None
        self.entrada2 = None
        self.entrada3 = None
        self.entrada4 = None
        self.entrada5 = None
        self.entrada6 = None
        self.entrada7 = None
        self.entrada8 = None
    def Var_cli(self):
        self.NumeroTemClinte = self.entrada.get()
        self.nome = self.entrada1.get()
        self.telefone = self.entrada2.get()
    def limpar_cli(self):
        self.entrada.delete(0,tk.END)
        self.entrada1.delete(0,tk.END)
        self.entrada2.delete(0,tk.END)
    def Bus_cli(self):
        self.coluna = self.Ent_Busca.get().replace('Nome','cliente').replace('Telefone','telefone')\
            .replace('CPF','cpf').replace('N/Cliente','numero_cliente')
        self.linha = self.Entrada_busca.get()
        self.limpar_cli()
        self.lista_c_clir.delete(*self.lista_c_clir.get_children())
        self.Var_cli()
        self.ConequitarBancoClinetes()
        self.c.execute("""SELECT numero_cliente,cliente,telefone,telefone_2,data_nacimento,cpf
        ,cep,numero_casa,complemento FROM dados_clientes ORDER BY cliente ASC;""")
        DadosCliente = self.c.execute(f'SELECT numero_cliente,cliente,telefone,telefone_2,data_nacimento'
                                      f',cpf,cep,numero_casa,complemento FROM dados_clientes WHERE '
                                      f'{self.coluna} LIKE "%{self.linha}%" ORDER BY numero_cliente DESC;')

        for i in DadosCliente:
            self.lista_c_clir.insert("", tk.END,values=i)
        self.DesconequitarBancoClientes()
    def CriarUmCarro(self,event):
        self.pasta_bancos()
        self.lista_c_clirCarro.selection()

        for n in self.lista_c_clir.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.lista_c_clir.item(n, 'values')
            self.entrada.insert(tk.END, col1)
            self.entrada1.insert(tk.END, col2)
            self.entrada2.insert(tk.END, col3)
            self.codigo = self.entrada.get()
            self.nome = self.entrada1.get()
            self.telefone = self.entrada2.get()
        self.lista_c_clirCarro.selection()

        self.VariaveiCarro()

        self.ConequitarBancoClinetes()

        self.c.execute("""INSERT INTO dados_carro (cliente,telefone,marca,modelo,ano,motor,placa,km,numero_cliente)
                VALUES(?,?,?,?,?,?,?,?,?)""",
                       (self.nome,
                        self.telefone,
                        self.marca,
                        self.modelo,
                        self.ano,
                        self.motor,
                        self.placa,
                        self.km,
                        self.codigo,))
        self.DesconequitarBancoClientes()

        self.AtualizeLista_Carro()
        self.LimpaEnterCarro()
        self.Sel_Cliente.destroy()
        os.chdir(diretorio)
    def LimpaEnterCarro(self):
        self.codigo_carro.delete(0,tk.END)
        self.entradaCarro.delete(0, tk.END)
        self.entrada1Carro.delete(0, tk.END)
        self.entrada2Carro.delete(0, tk.END)
        self.entrada3Carro.delete(0, tk.END)
        self.entrada4Carro.delete(0, tk.END)
        self.entrada5Carro.delete(0, tk.END)
    def VariaveiCarro(self):
        self.n_carro = self.codigo_carro.get()
        self.placa = self.entradaCarro.get().strip().upper().replace(' ', '').replace('-', '')
        self.marca = self.entrada1Carro.get().strip().upper().replace(' ', '_')
        self.modelo = self.entrada2Carro.get().strip().title().replace(' ', '_')
        self.ano = self.entrada3Carro.get().strip()
        self.motor = self.entrada4Carro.get().strip().replace(',', '.').replace(' ', '.')
        self.km = self.entrada5Carro.get().strip().replace(' ', '-')
    def AddCarro(self):
        self.VariaveiCarro()
        if self.placa == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!PLACA NÃO INSIRIDO!!!')
            self.jMensagem.place(x=80, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir a placa do carro!')
            self.j2Mensagem.place(x=70, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif self.modelo == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!MODELO NÃO INSIRIDO!!!')
            self.jMensagem.place(x=80, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o modelo do carro!')
            self.j2Mensagem.place(x=70, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.pasta_bancos()
            conn8 = sqlite3.connect('Banco_clientes.db')
            cursor8 = conn8.cursor()

            cursor8.execute('SELECT *, oid FROM dados_carro')
            tes1 = cursor8.fetchall()

            for i, a in enumerate(tes1):
                numero = (a[6])
                carro = (a[3])
                cliente = (a[0])
                numero_cliente = (a[8])
                if self.placa == numero:
                    self.Mensagenscaixa()
                    self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!PLACA JÁ CADASTRADO!!!')
                    self.jMensagem.place(x=70, y=10)
                    self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text=f'A placa {numero}\nPertence ao um'
                                                                              f' {carro},\nDo cliente {cliente}\n'
                                                                              f'O codigo do cliente {numero_cliente}!')
                    self.j2Mensagem.place(x=5, y=40)
                    self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
                    self.jbotam.place(x=280, y=90, width=100, height=40)
                    return
            conn8.commit()
            conn8.close()
            os.chdir(diretorio)
            self.Sel_Cliente = tk.Toplevel()
            self.Sel_Cliente.title('Maicá manutenção Automotiva')
            self.Sel_Cliente.iconbitmap(self.diretorio + '\Imagens\icone.ico')
            self.Sel_Cliente.geometry('800x550')
            self.Sel_Cliente.resizable(False, False)
            self.Sel_Cliente.configure(background='#1e0000')
            self.Sel_Cliente.transient(self.cr_janela)
            self.Sel_Cliente.focus_force()
            self.Sel_Cliente.grab_set()

            self.quadradoCarro = tk.Frame(self.Sel_Cliente)
            self.quadradoCarro.place(x=5, y=5, width=790, height=415)

            self.quadrado2 = tk.Frame(self.Sel_Cliente)
            self.quadrado2.place(x=5, y=425, width=790, height=120)

            self.lista_c_clir = ttk.Treeview(self.Sel_Cliente, height=600,
                                             columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6,col7',
                                                      'col8', 'col9', 'col10'))
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

            self.barra_lado = ttk.Scrollbar(self.Sel_Cliente, orient='vertical', command=self.lista_c_clir.yview)
            self.lista_c_clir.configure(yscrollcommand=self.barra_lado.set)
            self.barra_lado.place(x=760, y=72, width=30, height=343)

            self.barra_baixo = ttk.Scrollbar(self.Sel_Cliente, orient='horizontal',
                                             command=self.lista_c_clir.xview)
            self.lista_c_clir.configure(xscrollcommand=self.barra_baixo.set)
            self.barra_baixo.place(x=10, y=385, width=750, height=30)

            self.entrada = tk.Entry(self.Sel_Cliente, font=self.fonte_entra)
            self.entrada.place(x=900, y=500, width=150)
            self.entrada1 = tk.Entry(self.Sel_Cliente, font=self.fonte_entra)
            self.entrada1.place(x=900, y=500, width=250)
            self.entrada2 = tk.Entry(self.Sel_Cliente, font=self.fonte_entra)
            self.entrada2.place(x=900, y=500, width=150)

            self.Escrita = tk.Label(self.Sel_Cliente, font='Ariel', text='Buscar por:').place(x=510, y=425)
            self.Ent_Busca = tk.StringVar(self.Sel_Cliente)
            self.tipv = ('Nome', 'Telefone', 'N/Cliente', 'CPF')
            self.Ent_Busca.set('Nome')
            self.pormenu = tk.OptionMenu(self.Sel_Cliente, self.Ent_Busca, *self.tipv)
            self.pormenu.configure(bg="white", foreground="black")
            self.pormenu.place(x=510, y=445, width=100, height=30)

            self.buscar = tk.Button(self.Sel_Cliente, text="BUSCAR", font=self.fonte_buton, bg="black",
                                    foreground="white", command=self.Bus_cli)
            self.buscar.place(x=685, y=425, width=100, height=20)

            self.Entrada_busca = tk.Entry(self.Sel_Cliente, font=self.fonte_entra)
            self.Entrada_busca.place(x=635, y=450, width=150)

            self.criarCarro = tk.Button(self.Sel_Cliente, text="CANCELAR", font=self.fonte_buton, bg="black",
                                        foreground="white", command=self.Sel_Cliente.destroy)
            self.criarCarro.place(x=10, y=430, width=150, height=40)

            self.AtualizeLista_clientes()
            self.lista_c_clir.bind("<Double-1>", self.CriarUmCarro)
    def AtualizeLista_Carro(self):
        self.lista_c_clirCarro.delete(*self.lista_c_clirCarro.get_children())
        self.ConequitarBancoClinetes()
        lista_Carro = self.c.execute("""SELECT cliente,telefone,placa,marca,modelo,
        ano,motor,km,numero_cliente,numero_carro,numero_carro FROM dados_carro ORDER BY numero_carro DESC;""")
        for i in lista_Carro:
            self.lista_c_clirCarro.insert("", tk.END,values=i)
        self.DesconequitarBancoClientes()
    def SelencionarCarro(self,event):
        self.LimpaEnterCarro()
        self.lista_c_clirCarro.selection()
        for n in self.lista_c_clirCarro.selection():
            col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11 = self.lista_c_clirCarro.item(n, 'values')
            self.entradaCarro.insert(tk.END,col3)
            self.entrada1Carro.insert(tk.END, col4)
            self.entrada2Carro.insert(tk.END, col5)
            self.entrada3Carro.insert(tk.END, col6)
            self.entrada4Carro.insert(tk.END, col7)
            self.entrada5Carro.insert(tk.END, col8)
            self.codigo_carro.insert(tk.END, col10)
    def Escolha_apagar_Carro(self):
        if self.codigo_carro.get() == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!CARRO NÃO INSIRIDO!!!')
            self.jMensagem.place(x=70, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o carro!')
            self.j2Mensagem.place(x=90, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_voltar, text='!VOCÊ REALMENTE'
                                                                                   ' QUER APAGAR ESSE CARRO!')
            self.jMensagem.place(x=15, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='Está ação não poderar ser desfeita!')
            self.j2Mensagem.place(x=70, y=50)
            self.simbotam = tk.Button(self.aviso, text='SIM', font='Ariel', command=self.DeletaCarro)
            self.simbotam.place(x=70, y=90, width=100, height=40)
            self.naobotam = tk.Button(self.aviso, text='NÃO', font='Ariel', command=self.aviso.destroy)
            self.naobotam.place(x=220, y=90, width=100, height=40)
    def DeletaCarro(self):
        try:
            self.VariaveiCarro()
            self.ConequitarBancoClinetes()
            self.c.execute(f"""DELETE FROM dados_carro WHERE numero_carro = '{self.n_carro}'""")

            self.DesconequitarBancoClientes()
            self.LimpaEnterCarro()
            self.AtualizeLista_Carro()
            self.aviso.destroy()
        except:
            pass
        finally:
            os.chdir(diretorio)
    def Escolha_modificar_carro(self):
        if self.codigo_carro.get() == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!CARRO NÃO INSIRIDO!!!')
            self.jMensagem.place(x=70, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o carro!')
            self.j2Mensagem.place(x=90, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_voltar, text='!VOCÊ REALMENTE'
                                                                                   ' QUER MODIFICAR ESSE CARRO!')
            self.jMensagem.place(x=10, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='Está ação não poderar ser desfeita!')
            self.j2Mensagem.place(x=70, y=50)
            self.simbotam = tk.Button(self.aviso, text='SIM', font='Ariel', command=self.ModificarCarro)
            self.simbotam.place(x=70, y=90, width=100, height=40)
            self.naobotam = tk.Button(self.aviso, text='NÃO', font='Ariel', command=self.aviso.destroy)
            self.naobotam.place(x=220, y=90, width=100, height=40)
    def ModificarCarro(self):
        self.VariaveiCarro()
        self.ConequitarBancoClinetes()
        self.c.execute(f"""UPDATE dados_carro SET marca = ?
        ,modelo = ?,ano = ?,motor = ?
        ,placa = ?,km = ?
         WHERE numero_carro = ?""",
                       (self.marca.strip().upper().replace(' ', '_')
                        ,self.modelo.strip().title().replace(' ', '_')
                        ,self.ano.strip().replace(' ', '-')
                        ,self.motor.strip().replace(',', '.').replace(' ', '.')
                        ,self.placa.strip().upper().replace('-', '').replace(' ', '')
                        ,self.km.strip().replace(' ', '-')
                        ,self.n_carro))
        self.DesconequitarBancoClientes()
        self.AtualizeLista_Carro()
        self.LimpaEnterCarro()
        self.aviso.destroy()
    def Buscar_Carro(self):
        self.modelo = self.entrada2Carro.get()
        self.lista_c_clirCarro.delete(*self.lista_c_clirCarro.get_children())
        self.ConequitarBancoClinetes()
        self.c.execute("""SELECT cliente,telefone,placa,marca,modelo,
        ano,motor,km,numero_cliente,numero_carro FROM dados_carro ORDER BY modelo ASC;""")
        DadosCarro = self.c.execute(f'SELECT cliente,telefone,placa,marca,modelo,ano,motor,km,numero_cliente,'
                                    f'numero_carro,numero_carro FROM dados_carro WHERE modelo LIKE '
                                      f'"%{self.modelo.strip().title().replace(" ", "_")}%"'
                                    f'ORDER BY numero_carro DESC;')

        for i in DadosCarro:
            self.lista_c_clirCarro.insert("", tk.END,values=i)
        self.DesconequitarBancoClientes()
