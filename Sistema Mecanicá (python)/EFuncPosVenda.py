from DFuncFinalizado import *

class FuncPosVenda(Funcs_Saidas):
    def ConequitarBancoPosVenda(self):
        self.pasta_bancos()
        self.conexao = sqlite3.connect('Banco_Pos_Venda.db')
        self.c = self.conexao.cursor()

    def DesconequitarBancoPosVenda(self):
        self.conexao.commit()
        self.conexao.close()
        os.chdir(diretorio)

    def Variavel_Pos_Venda(self):
        self.msg = self.Ent_Mensagem.get()
        self.msg1 = self.Ent_Mensagem1.get()
        self.msg2 = self.Ent_Mensagem2.get()
        self.ent = self.Ent.get()
        self.ent1 = self.Ent1.get()
        self.ent2 = self.Ent2.get().strip().title().replace(' ', '_')
        self.ent3 = self.Ent3.get().replace(' ', '').replace('-', '').replace('(', '').replace(')','')
        self.ent4 = self.Ent4.get().replace('/', '-')

    def VariavelHorarios(self):
        self.horaD = self.Ent_Hor.get()
        self.horaE1 = self.Ent_Hor1.get()
        self.horaE2 = self.Ent_Hor2.get()

    def Limpar_Pos_Venda(self):
        self.CM.delete(0, tk.END)
        self.Ent.delete(0, tk.END)
        self.Ent1.delete(0, tk.END)
        self.Ent2.delete(0, tk.END)
        self.Ent3.delete(0, tk.END)
        self.Ent4.delete(0, tk.END)
        self.Ent_Mensagem.delete(0, tk.END)
        self.Ent_Mensagem1.delete(0, tk.END)
        self.Ent_Mensagem2.delete(0, tk.END)

    def ColocardataPos(self):
        self.dataprima = self.calendario.get_date()
        self.Ent4.delete(0,tk.END)
        self.Ent4.insert(tk.END, self.dataprima)

    def Gerar_Pos_Vendas(self):
        self.DataModificada()
        self.Variavel_Pos_Venda()
        max = self.ent3[:10]
        nacimento = str(self.ent4).replace('-','/')
        mox = nacimento[:9]
        mix = nacimento[10:].replace('', 'A')
        if self.ent4 == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NA DATA!!!')
            self.jMensagem.place(x=80, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='A Data Para Executar Tem que ser informada!')
            self.j2Mensagem.place(x=30, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif nacimento <= mox:
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NA DATA!!!')
            self.jMensagem.place(x=80, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='Algo de errado com a data de execução!')
            self.j2Mensagem.place(x=40, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif mix != 'A':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NA DATA!!!')
            self.jMensagem.place(x=80, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='Algo de errado com a data de execução!')
            self.j2Mensagem.place(x=40, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif nacimento[2] != '/':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NA DATA!!!')
            self.jMensagem.place(x=80, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='Algo de errado com a data de execução!')
            self.j2Mensagem.place(x=40, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif nacimento[5] != '/':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NA DATA!!!')
            self.jMensagem.place(x=80, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='Algo de errado com a data de execução!')
            self.j2Mensagem.place(x=40, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif self.ent2 == 'Todos':
            if self.msg == '':
                self.Mensagenscaixa()
                self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NA MESAGEM!!!')
                self.jMensagem.place(x=70, y=10)
                self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='É nesessario colocar ao menos uma Mensagem!')
                self.j2Mensagem.place(x=25, y=45)
                self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
                self.jbotam.place(x=140, y=90, width=100, height=40)
            else:
                self.ConequitarBancoClinetes()
                self.c.execute("""SELECT numero_cliente,cliente,telefone,telefone_2,data_nacimento,cpf
                        ,cep,numero_casa,complemento FROM dados_clientes;""")
                self.tes = self.c.fetchall()
                self.DesconequitarBancoClientes()
                for a,i in enumerate(self.tes) :
                    self.DatBanco = self.ent4[6:] + self.ent4[2:6] + self.ent4[0:2]
                    self.ConequitarBancoPosVenda()
                    self.c.execute("""INSERT INTO pos_venda(nome,whats,numero_cliente,data_criada,data_executar,mensagem1,
                    mensagem2,mensagem3)VALUES(?,?,?,?,?,?,?,?);""",
                                   (i[1], i[2], i[0], self.dataP2, self.DatBanco
                                    , self.msg, self.msg1, self.msg2))
                    self.DesconequitarBancoPosVenda()
                self.Limpar_Pos_Venda()
                self.AtualizeLista_PosVenda()

        elif self.ent2 == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NO NOME!!!')
            self.jMensagem.place(x=80, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='O Nome do Cliente não foi inserido!')
            self.j2Mensagem.place(x=50, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif self.ent3 <= max:
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NO NUMERO!!!')
            self.jMensagem.place(x=70, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='O numero de telefone está pequeno de mais!\nDigi'
                                                                      'te o numero com 11 digitos.exp (51999999999).')
            self.j2Mensagem.place(x=10, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif self.msg == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NA MESAGEM!!!')
            self.jMensagem.place(x=70, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='É nesessario colocar ao menos uma Mensagem!')
            self.j2Mensagem.place(x=25, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.DatBanco = self.ent4[6:]+self.ent4[2:6]+self.ent4[0:2]
            self.Variavel_Pos_Venda()
            self.ConequitarBancoPosVenda()
            self.c.execute("""INSERT INTO pos_venda(nome,whats,numero_cliente,data_criada,data_executar,mensagem1,
            mensagem2,mensagem3)VALUES(?,?,?,?,?,?,?,?);""",
                           (self.ent2, self.ent3, self.ent1, self.dataP2, self.DatBanco
                            , self.msg, self.msg1, self.msg2))
            self.DesconequitarBancoPosVenda()
            self.Limpar_Pos_Venda()
            self.AtualizeLista_PosVenda()

    def AtualizeLista_PosVenda(self):
        self.lista.delete(*self.lista.get_children())
        self.ConequitarBancoPosVenda()
        list = self.c.execute("""SELECT numero_pos_venda,nome,whats,numero_cliente,data_criada,data_executar,
        mensagem1,mensagem2,mensagem3 FROM pos_venda ORDER BY data_executar DESC;""")
        for i in list:
            self.IData = i[5].replace('-', '/')
            if i[5] == 'ERRO!(certifique se que essa mensagem foi enviada)':
                self.lista.insert("", tk.END, values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
            else:
                self.ParaMostrar = self.IData[8:] + self.IData[4:8] + self.IData[0:4]
                self.lista.insert("", tk.END, values=(i[0], i[1], i[2], i[3], i[4], self.ParaMostrar, i[6], i[7], i[8]))

        self.DesconequitarBancoPosVenda()

    def Abrir_Pos_Venda(self,event):
        self.Limpar_Pos_Venda()
        self.Variavel_Pos_Venda()
        self.ConequitarBancoPosVenda()
        self.lista.selection()
        for n in self.lista.selection():
            col1,col2,col3,col4,col5,col6,col7,col8,col9= self.lista.item(n, 'values')
            Dados = self.c.execute(f'SELECT numero_pos_venda,nome,whats,numero_cliente,data_criada,data_executar,'
                                   f'mensagem1,mensagem2,mensagem3 FROM pos_venda WHERE numero_pos_venda = {col1}')
            for i in Dados:
                self.IData = i[5].replace('-', '/')
                self.ParaMostrar = self.IData[8:] + self.IData[4:8] + self.IData[0:4]
                self.Ent.insert(tk.END, i[0])
                self.Ent1.insert(tk.END, i[3])
                self.Ent2.insert(tk.END, i[1])
                self.Ent3.insert(tk.END, i[2])
                self.Ent4.insert(tk.END, self.ParaMostrar)
                self.Ent_Mensagem.insert(tk.END, i[6])
                self.Ent_Mensagem1.insert(tk.END, i[7])
                self.Ent_Mensagem2.insert(tk.END, i[8])
        self.DesconequitarBancoPosVenda()

    def Escolha_apagar_PosVenda(self):
        if self.Ent.get() == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!MENAGEM NÃO INSIRIDO!!!')
            self.jMensagem.place(x=40, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir a Mensagem!')
            self.j2Mensagem.place(x=70, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!VOCÊ REALMENTE QUER!\n'
                                                                          '!APAGAR ESSE MENSAGEM!')
            self.jMensagem.place(x=50, y=5)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='Está ação não poderar ser desfeita!')
            self.j2Mensagem.place(x=70, y=60)
            self.simbotam = tk.Button(self.aviso, text='SIM', font='Ariel', command=self.DeletaPosVenda)
            self.simbotam.place(x=70, y=90, width=100, height=40)
            self.naobotam = tk.Button(self.aviso, text='NÃO', font='Ariel', command=self.aviso.destroy)
            self.naobotam.place(x=220, y=90, width=100, height=40)

    def DeletaPosVenda(self):
        try:
            self.Variavel_Pos_Venda()
            self.ConequitarBancoPosVenda()
            self.c.execute(f"""DELETE FROM pos_venda WHERE numero_pos_venda = '{self.ent}'""")

            self.DesconequitarBancoPosVenda()
            self.Limpar_Pos_Venda()
            self.AtualizeLista_PosVenda()
            self.aviso.destroy()
        except:
            pass

    def Escolha_Modificar_PosVenda(self):
        self.DataModificada()
        self.Variavel_Pos_Venda()
        max = self.ent3[:10]
        nacimento = str(self.ent4).replace('-','/')
        mox = nacimento[:9]
        mix = nacimento[10:].replace('', 'A')
        if self.ent4 == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NA DATA!!!')
            self.jMensagem.place(x=80, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='A Data Para Executar Tem que ser informada!')
            self.j2Mensagem.place(x=30, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif nacimento[2] != '/':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NA DATA!!!')
            self.jMensagem.place(x=80, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='Algo de errado com a data de execução!')
            self.j2Mensagem.place(x=40, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif nacimento[5] != '/':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NA DATA!!!')
            self.jMensagem.place(x=80, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='Algo de errado com a data de execução!')
            self.j2Mensagem.place(x=40, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif nacimento <= mox:
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NA DATA!!!')
            self.jMensagem.place(x=80, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='Algo de errado com a data de execução!')
            self.j2Mensagem.place(x=40, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif mix != 'A':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NA DATA!!!')
            self.jMensagem.place(x=80, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='Algo de errado com a data de execução!')
            self.j2Mensagem.place(x=40, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif self.ent2 == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NO NOME!!!')
            self.jMensagem.place(x=80, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='O Nome do Cliente não foi inserido!')
            self.j2Mensagem.place(x=50, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif self.ent3 <= max:
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NO NUMERO!!!')
            self.jMensagem.place(x=70, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='O numero de telefone está pequeno de mais!\nDigi'
                                                                      'te o numero com 11 digitos.exp (51999999999).')
            self.j2Mensagem.place(x=10, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif self.msg == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NA MESAGEM!!!')
            self.jMensagem.place(x=70, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='É nesessario colocar ao menos uma Mensagem!')
            self.j2Mensagem.place(x=25, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!VOCÊ REALMENTE QUER!\n'
                                                                          '!MODIFICAR ESSE MENSAGEM!')
            self.jMensagem.place(x=50, y=5)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='Está ação não poderar ser desfeita!')
            self.j2Mensagem.place(x=70, y=60)
            self.simbotam = tk.Button(self.aviso, text='SIM', font='Ariel', command=self.ModificarPosVenda)
            self.simbotam.place(x=70, y=90, width=100, height=40)
            self.naobotam = tk.Button(self.aviso, text='NÃO', font='Ariel', command=self.aviso.destroy)
            self.naobotam.place(x=220, y=90, width=100, height=40)

    def ModificarPosVenda(self):
        self.DataModificada()
        self.Variavel_Pos_Venda()
        self.DatBanco = self.ent4[6:] + self.ent4[2:6] + self.ent4[0:2]
        self.ConequitarBancoPosVenda()
        self.c.execute(f"""UPDATE pos_venda SET nome = ?,whats = ?,numero_cliente = ?,data_criada = ?,
        data_executar = ?, mensagem1 = ?,mensagem2 = ?,mensagem3 = ? WHERE numero_pos_venda = ?""",
                       (self.ent2, self.ent3, self.ent1, self.dataP2, self.DatBanco
                            , self.msg, self.msg1, self.msg2,self.ent))
        self.DesconequitarBancoPosVenda()
        self.AtualizeLista_PosVenda()
        self.Limpar_Pos_Venda()
        self.aviso.destroy()

    def ColocarHorario(self):
        self.pasta_bancos()
        arquivo = open('HorarioExeção.txt', 'r')
        arquivo2 = open('HorarioExeção2.txt', 'r')
        arquivo3 = open('HorarioExeção3.txt', 'r')
        linha = arquivo.read()
        linha2 = arquivo2.read()
        linha3 = arquivo3.read()
        arquivo.close()
        arquivo2.close()
        arquivo3.close()
        os.chdir(diretorio)
        self.Ent_Hor2.set(f'{linha}')
        self.Ent_Hor1.set(f'{linha2}')
        self.Ent_Hor.set(f'{linha3}')

    def ModificarHorario(self):
        self.pasta_bancos()
        self.VariavelHorarios()
        with open('HorarioExeção.txt', 'w+') as arquivo:
                arquivo.write(self.horaE2)
        with open('HorarioExeção2.txt', 'w+') as arquivo:
                arquivo.write(self.horaE1)
        with open('HorarioExeção3.txt', 'w+') as arquivo:
                arquivo.write(self.horaD)
        os.chdir(diretorio)

        self.Salvado.set('HORA SALVA')

    def Incluir(self,event):
        self.Ent1.delete(0, tk.END)
        self.Ent2.delete(0, tk.END)
        self.Ent3.delete(0, tk.END)
        for n in self.lista_c_clir.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.lista_c_clir.item(n, 'values')
            self.Ent1.insert(tk.END, col1)
            self.Ent2.insert(tk.END, col2)
            self.Ent3.insert(tk.END, col3)

        self.Sel_Cliente.destroy()

    def AddEmPosVenda(self):
        self.Sel_Cliente = tk.Toplevel()
        self.Sel_Cliente.title('Maicá manutenção Automotiva')
        self.Sel_Cliente.iconbitmap(self.diretorio + '\Imagens\icone.ico')
        self.Sel_Cliente.geometry('800x550')
        self.Sel_Cliente.resizable(False, False)
        self.Sel_Cliente.configure(background='#1e0000')
        self.Sel_Cliente.transient(self.Secundaria)
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
        self.lista_c_clir.bind("<Double-1>", self.Incluir)


class FuncMensagens(FuncPosVenda):
    def ConequitarBancoMensagens(self):
        self.pasta_bancos()
        self.conexao = sqlite3.connect('Banco_mensagens.db')
        self.c = self.conexao.cursor()

    def DesconequitarBancoMensagens(self):
        self.conexao.commit()
        self.conexao.close()
        os.chdir(diretorio)

    def Variavel_Mensagens(self):
        self.cm = self.CM.get()
        self.msg = self.Ent_Mensagem.get()
        self.msg1 = self.Ent_Mensagem1.get()
        self.msg2 = self.Ent_Mensagem2.get()

    def Limpar_Mensagens(self):
        self.CM.delete(0, tk.END)
        self.Ent_Mensagem.delete(0, tk.END)
        self.Ent_Mensagem1.delete(0, tk.END)
        self.Ent_Mensagem2.delete(0, tk.END)

    def Gerar_Mensagens(self):
        self.DataModificada()
        self.Variavel_Mensagens()
        if self.msg == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!ERRO NA MENSAGEM!!!')
            self.jMensagem.place(x=70, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Arial', text='É nesessario colocar ao menos uma Mensagem!')
            self.j2Mensagem.place(x=25, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.Variavel_Pos_Venda()
            self.ConequitarBancoMensagens()
            self.c.execute("""INSERT INTO mensagens(mensagem1,mensagem2,mensagem3)VALUES(?,?,?);""",
                           (self.msg, self.msg1, self.msg2))
            self.DesconequitarBancoMensagens()
            self.Limpar_Mensagens()

    def AtualizeLista_Mensagens(self):
        self.listaM.delete(*self.listaM.get_children())
        self.ConequitarBancoMensagens()
        list = self.c.execute("""SELECT numero_mensagens,mensagem1,mensagem2,mensagem3
         FROM mensagens""")
        for i in list:
            self.listaM.insert("", tk.END, values=(i[0],i[1],i[2],i[3]))

        self.DesconequitarBancoMensagens()

    def Abrir_Mensagens(self,event):
        self.Limpar_Mensagens()
        self.Variavel_Mensagens()
        self.ConequitarBancoMensagens()
        self.listaM.selection()
        for n in self.listaM.selection():
            col1,col2,col3,col4= self.listaM.item(n, 'values')
            Dados = self.c.execute(f'SELECT numero_mensagens,mensagem1,mensagem2,mensagem3'
                                   f' FROM mensagens WHERE numero_mensagens = {col1}')
            for i in Dados:
                self.CM.insert(tk.END, i[0])
                self.Ent_Mensagem.insert(tk.END, i[1])
                self.Ent_Mensagem1.insert(tk.END, i[2])
                self.Ent_Mensagem2.insert(tk.END, i[3])
        self.DesconequitarBancoPosVenda()
        self.SecundariaM.destroy()

    def Escolha_apagar_Mensagens(self):
        self.Variavel_Mensagens()
        if self.cm == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!MENAGEM NÃO INSIRIDO!!!')
            self.jMensagem.place(x=40, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir a Mensagem!')
            self.j2Mensagem.place(x=70, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!VOCÊ REALMENTE QUER!\n'
                                                                          '!APAGAR ESSE MENSAGEM!')
            self.jMensagem.place(x=50, y=5)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='Está ação não poderar ser desfeita!')
            self.j2Mensagem.place(x=70, y=60)
            self.simbotam = tk.Button(self.aviso, text='SIM', font='Ariel', command=self.DeletaMensagens)
            self.simbotam.place(x=70, y=90, width=100, height=40)
            self.naobotam = tk.Button(self.aviso, text='NÃO', font='Ariel', command=self.aviso.destroy)
            self.naobotam.place(x=220, y=90, width=100, height=40)

    def DeletaMensagens(self):
        self.Variavel_Mensagens()
        self.ConequitarBancoMensagens()
        self.c.execute(f"""DELETE FROM mensagens WHERE numero_mensagens = '{self.cm}'""")

        self.DesconequitarBancoMensagens()
        self.Limpar_Mensagens()
        self.aviso.destroy()

    def Escolha_Modificar_Mensagens(self):
        self.Variavel_Mensagens()
        if self.cm == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!!!MENAGEM NÃO INSIRIDO!!!')
            self.jMensagem.place(x=40, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir a Mensagem!')
            self.j2Mensagem.place(x=70, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.FontMsg, text='!VOCÊ REALMENTE QUER!\n'
                                                                          '!MODIFICAR ESSE MENSAGEM!')
            self.jMensagem.place(x=50, y=5)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='Está ação não poderar ser desfeita!')
            self.j2Mensagem.place(x=70, y=60)
            self.simbotam = tk.Button(self.aviso, text='SIM', font='Ariel', command=self.ModificarMensagens)
            self.simbotam.place(x=70, y=90, width=100, height=40)
            self.naobotam = tk.Button(self.aviso, text='NÃO', font='Ariel', command=self.aviso.destroy)
            self.naobotam.place(x=220, y=90, width=100, height=40)

    def ModificarMensagens(self):
        self.DataModificada()
        self.Variavel_Mensagens()
        self.ConequitarBancoMensagens()
        self.c.execute(f"""UPDATE mensagens SET mensagem1 = ?,mensagem2 = ?,mensagem3 = ? WHERE numero_mensagens = ?""",
                       (self.msg, self.msg1, self.msg2,self.cm))
        self.DesconequitarBancoMensagens()
        self.Limpar_Mensagens()
        self.aviso.destroy()