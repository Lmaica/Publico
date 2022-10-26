from CFuncOs import *

class Funcs_Ganhos(Funcs_Finalizados):
    def __init__(self):
        super().__init__()
        self.Ent_Ganhos4 = None
        self.Ent_Ganhos1 = None
        self.Ent_Ganhos2 = None
        self.Ent_Ganhos3 = None
        self.Ent_Ganhos4 = None
        self.lista_c_clirGanhos = None
        self.Ent_calendario = None
        self.lista_c_clirFinalizados = None
        self.lista_c_clirPendentes = None
        self.entraCarro = None
        self.entra1Carro = None
        self.entra2Carro = None
        self.entra3Carro = None
        self.entra4Carro = None
        self.entra5Carro = None
        self.entra6Carro = None
        self.entra7Carro = None
        self.entra8Carro = None

        self.tVpes1 = None
        self.tVpes = None
        self.entrada_codigo = None
        self.entrada_por = None

        self.entrada_pesas = None
        self.entrada_uni = None
        self.entrada_v_uni = None
        self.entrada_t_uni = None
        self.entrada_pesas1 = None
        self.entrada_uni1 = None
        self.entrada_v_uni1 = None
        self.entrada_t_uni1 = None
        self.entrada_pesas2 = None
        self.entrada_uni2 = None
        self.entrada_v_uni2 = None
        self.entrada_t_uni2 = None
        self.entrada_pesas3 = None
        self.entrada_uni3 = None
        self.entrada_v_uni3 = None
        self.entrada_t_uni3 = None
        self.entrada_pesas4 = None
        self.entrada_uni4 = None
        self.entrada_v_uni4 = None
        self.entrada_t_uni4 = None
        self.entrada_pesas5 = None
        self.entrada_uni5 = None
        self.entrada_v_uni5 = None
        self.entrada_t_uni5 = None
        self.entrada_pesas6 = None
        self.entrada_uni6 = None
        self.entrada_v_uni6 = None
        self.entrada_t_uni6 = None
        self.entrada_pesas7 = None
        self.entrada_uni7 = None
        self.entrada_v_uni7 = None
        self.entrada_t_uni7 = None
        self.entrada_pesas8 = None
        self.entrada_uni8 = None
        self.entrada_v_uni8 = None
        self.entrada_t_uni8 = None
        self.entrada_pesas9 = None
        self.entrada_uni9 = None
        self.entrada_v_uni9 = None
        self.entrada_t_uni9 = None
        self.entrada_pesas10 = None
        self.entrada_uni10 = None
        self.entrada_v_uni10 = None
        self.entrada_t_uni10 = None
        self.entrada_pesas11 = None
        self.entrada_uni11 = None
        self.entrada_v_uni11 = None
        self.entrada_t_uni11 = None
        self.entrada_pesas12 = None
        self.entrada_uni12 = None
        self.entrada_v_uni12 = None
        self.entrada_t_uni12 = None
        self.entrada_pesas13 = None
        self.entrada_uni13 = None
        self.entrada_v_uni13 = None
        self.entrada_t_uni13 = None
        self.entrada_pesas14 = None
        self.entrada_uni14 = None
        self.entrada_v_uni14 = None
        self.entrada_t_uni14 = None
        self.entrada_pesas15 = None
        self.entrada_uni15 = None
        self.entrada_v_uni15 = None
        self.entrada_t_uni15 = None
        self.entrada_pesas16 = None
        self.entrada_uni16 = None
        self.entrada_v_uni16 = None
        self.entrada_t_uni16 = None
        self.entrada_pesas17 = None
        self.entrada_uni17 = None
        self.entrada_v_uni17 = None
        self.entrada_t_uni17 = None
        self.entrada_pesas18 = None
        self.entrada_uni18 = None
        self.entrada_v_uni18 = None
        self.entrada_t_uni18 = None
        self.entrada_pesas19 = None
        self.entrada_uni19 = None
        self.entrada_v_uni19 = None
        self.entrada_t_uni19 = None

        self.PesasTotal = None
        self.Retifica = None
        self.M_O = None
        self.TotalTotal = None
    def Variavel_Ganhos(self):
        self.ent_for = self.Ent_Ganhos.get()
        self.ent_for1 = self.Ent_Ganhos1.get().replace(',','.')
        self.ent_for2 = self.Ent_Ganhos2.get().replace(',','.')
        self.ent_for3 = self.Ent_Ganhos3.get().replace(',','.')
        self.ent_for4 = self.Ent_Ganhos4.get().replace(',','.')
    def LimparGanhos(self):
        self.Ent_Ganhos.delete(0,tk.END)
        self.Ent_Ganhos1.delete(0,tk.END)
        self.Ent_Ganhos2.delete(0,tk.END)
        self.Ent_Ganhos3.delete(0,tk.END)
        self.Ent_Ganhos4.delete(0,tk.END)
    def Variavel_Somas(self):
        self.Valor = self.Ent_soma.get()
        self.Valor1 = self.Ent_soma1.get()
    def LimparSomas(self):
        self.Ent_soma.delete(0,tk.END)
        self.Ent_soma1.delete(0, tk.END)
    def AtualizeLista_Ganhos(self):
        try:
            self.lista_c_clirGanhos.delete(*self.lista_c_clirGanhos.get_children())
            self.ConequitarBancoFinalizados()
            lista_Carro = self.x.execute("""SELECT numero_pedido,cliente,telefone,placa,forma_paga
            ,total_OS,gasto_pesas,gasto_retifica,gasto_outros,valor_recebido,ganho,data FROM dados_finalizados
             ORDER BY data DESC;""")
            for i in lista_Carro:
                self.lista_c_clirGanhos.insert("", tk.END,
                                               values=(i[0], i[1], i[2], i[3], i[4], 'R$ ' + i[5].replace('.', ',')
                                                       , 'R$ ' + i[6].replace('.', ','),
                                                       'R$ ' + i[7].replace('.', ','),
                                                       'R$ ' + i[8].replace('.', ','),
                                                       'R$ ' + i[9].replace('.', ','),
                                                       'R$ ' + i[10].replace('.', ','), i[11]))

            self.DesconequitarBancoFinalizados()
            self.LimparSomas()
            self.Caixa()
        except:
            pass
    def BuscarTelefoneGanhos(self):
        self.LimparSomas()
        self.telefone = self.entrada1.get()
        self.lista_c_clirGanhos.delete(*self.lista_c_clirGanhos.get_children())
        self.ConequitarBancoFinalizados()
        DadosCarro = self.x.execute(f'SELECT numero_pedido,cliente,telefone,placa,forma_paga,total_OS,gasto_pesas'
                                    f',gasto_retifica,gasto_outros,valor_recebido,ganho,data '
                                    f'FROM dados_finalizados WHERE telefone LIKE'
                                    f'"%{self.telefone.strip().replace(" ", "").replace("-", "")}%"'
                                    f'ORDER BY data DESC;')
        self.Somares = []
        self.Somares1 = []
        for i in DadosCarro:
            self.Somares.append(float(i[9]))
            self.Somares1.append(float(i[10]))
            self.lista_c_clirGanhos.insert("", tk.END,
                                           values=(i[0], i[1], i[2], i[3], i[4], 'R$ ' + i[5].replace('.', ',')
                                                   , 'R$ ' + i[6].replace('.', ','),
                                                   'R$ ' + i[7].replace('.', ','),
                                                   'R$ ' + i[8].replace('.', ','),
                                                   'R$ ' + i[9].replace('.', ','),
                                                   'R$ ' + i[10].replace('.', ','), i[11]))
        self.DesconequitarBancoFinalizados()
        self.somado = sum(self.Somares)
        self.somado1 = sum(self.Somares1)
        self.somado_for = str('{:.2f}'.format(self.somado))
        self.somado_for1 = str('{:.2f}'.format(self.somado1))
        self.Ent_soma.insert(tk.END,self.somado_for)
        self.Ent_soma1.insert(tk.END,self.somado_for1)
    def BuscarDataGanhos(self):
        self.LimparSomas()
        self.datapri = f'{self.dataprima[6:11]}-{self.dataprima[3:5]}-{self.dataprima[0:2]}'
        self.datapri1 = f'{self.dataprima1[6:11]}-{self.dataprima1[3:5]}-{self.dataprima1[0:2]}'
        self.lista_c_clirGanhos.delete(*self.lista_c_clirGanhos.get_children())
        self.ConequitarBancoFinalizados()
        DadosCarro = self.x.execute(f'SELECT numero_pedido,cliente,telefone,placa,forma_paga,total_OS,gasto_pesas'
                                    f',gasto_retifica,gasto_outros,valor_recebido,ganho,data'
                                    f' FROM dados_finalizados WHERE data BETWEEN '
                                    f'"{self.datapri}" AND "{self.datapri1}"'
                                    f'ORDER BY data DESC;')

        self.Somares = []
        self.Somares1 = []
        for i in DadosCarro:
            self.Somares.append(float(i[9]))
            self.Somares1.append(float(i[10]))
            self.lista_c_clirGanhos.insert("", tk.END,
                                           values=(i[0], i[1], i[2], i[3], i[4], 'R$ ' + i[5].replace('.', ',')
                                                   , 'R$ ' + i[6].replace('.', ','),
                                                   'R$ ' + i[7].replace('.', ','),
                                                   'R$ ' + i[8].replace('.', ','),
                                                   'R$ ' + i[9].replace('.', ','),
                                                   'R$ ' + i[10].replace('.', ','), i[11]))
        self.DesconequitarBancoFinalizados()
        self.somado = sum(self.Somares)
        self.somado1 = sum(self.Somares1)
        self.somado_for = str('{:.2f}'.format(self.somado))
        self.somado_for1 = str('{:.2f}'.format(self.somado1))
        self.Ent_soma.insert(tk.END, self.somado_for)
        self.Ent_soma1.insert(tk.END, self.somado_for1)
    def BuscarCodigoGanhos(self):
        self.LimparSomas()
        self.codigo = self.entrada2.get()
        self.lista_c_clirGanhos.delete(*self.lista_c_clirGanhos.get_children())
        self.ConequitarBancoFinalizados()
        DadosCarro = self.x.execute(f'SELECT numero_pedido,cliente,telefone,placa,forma_paga,total_OS,gasto_pesas'
                                    f',gasto_retifica,gasto_outros,valor_recebido,ganho,data '
                                    f'FROM dados_finalizados WHERE numero_cliente LIKE '
                                    f'"%{self.codigo.strip().replace(" ", "").replace("-", "")}%"'
                                    f'ORDER BY data DESC;')

        self.Somares = []
        self.Somares1 = []
        for i in DadosCarro:
            self.Somares.append(float(i[9]))
            self.Somares1.append(float(i[10]))
            self.lista_c_clirGanhos.insert("", tk.END,
                                           values=(i[0], i[1], i[2], i[3], i[4], 'R$ ' + i[5].replace('.', ',')
                                                   , 'R$ ' + i[6].replace('.', ','),
                                                   'R$ ' + i[7].replace('.', ','),
                                                   'R$ ' + i[8].replace('.', ','),
                                                   'R$ ' + i[9].replace('.', ','),
                                                   'R$ ' + i[10].replace('.', ','), i[11]))
        self.DesconequitarBancoFinalizados()
        self.somado = sum(self.Somares)
        self.somado1 = sum(self.Somares1)
        self.somado_for = str('{:.2f}'.format(self.somado))
        self.somado_for1 = str('{:.2f}'.format(self.somado1))
        self.Ent_soma.insert(tk.END, self.somado_for)
        self.Ent_soma1.insert(tk.END, self.somado_for1)
    def BuscarPlacaGanhos(self):
        self.LimparSomas()
        self.placa = self.entrada3.get()
        self.lista_c_clirGanhos.delete(*self.lista_c_clirGanhos.get_children())
        self.ConequitarBancoFinalizados()
        self.x.execute("""SELECT numero_pedido,cliente,telefone,placa,forma_paga
        ,total_OS,gasto_pesas,gasto_retifica,gasto_outros,valor_recebido,ganho,data FROM dados_finalizados
         ORDER BY data ASC;""")
        DadosCarro = self.x.execute(f'SELECT numero_pedido,cliente,telefone,placa,numero_cliente,total_OS,gasto_pesas'
                                    f',gasto_retifica,gasto_outros,valor_recebido,ganho,data '
                                    f'FROM dados_finalizados WHERE placa LIKE '
                                    f'"%{self.placa.strip().upper().replace(" ", "").replace("-", "")}%"'
                                    f'ORDER BY data DESC;')

        self.Somares = []
        self.Somares1 = []
        for i in DadosCarro:
            self.Somares.append(float(i[9]))
            self.Somares1.append(float(i[10]))
            self.lista_c_clirGanhos.insert("", tk.END,
                                           values=(i[0], i[1], i[2], i[3], i[4], 'R$ ' + i[5].replace('.', ',')
                                                   , 'R$ ' + i[6].replace('.', ','),
                                                   'R$ ' + i[7].replace('.', ','),
                                                   'R$ ' + i[8].replace('.', ','),
                                                   'R$ ' + i[9].replace('.', ','),
                                                   'R$ ' + i[10].replace('.', ','), i[11]))
        self.DesconequitarBancoFinalizados()
        self.somado = sum(self.Somares)
        self.somado1 = sum(self.Somares1)
        self.somado_for = str('{:.2f}'.format(self.somado))
        self.somado_for1 = str('{:.2f}'.format(self.somado1))
        self.Ent_soma.insert(tk.END, self.somado_for)
        self.Ent_soma1.insert(tk.END, self.somado_for1)
    def AbrirGanhos(self,event):
        self.LimparGanhos()
        self.ConequitarBancoFinalizados()
        self.lista_c_clirGanhos.selection()
        for n in self.lista_c_clirGanhos.selection():
            col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12= self.lista_c_clirGanhos.item(n, 'values')
            Dados = self.x.execute(f'SELECT numero_pedido,gasto_pesas,gasto_retifica,gasto_outros,valor_recebido'
                                   f' oid FROM dados_finalizados WHERE numero_pedido = {col1}')
            for i in Dados:
                self.Ent_Ganhos.insert(tk.END,i[0])
                self.Ent_Ganhos1.insert(tk.END, i[1])
                self.Ent_Ganhos2.insert(tk.END, i[2])
                self.Ent_Ganhos3.insert(tk.END, i[3])
                self.Ent_Ganhos4.insert(tk.END, i[4])

        self.DesconequitarBancoFinalizados()
    def ColocardataGanhos(self):
        self.dataprima = self.calendario.get_date()
        self.Ent_calendario.delete(0,tk.END)
        self.Ent_calendario.insert(tk.END, self.dataprima)
        self.dataprima1 = self.calendario1.get_date()
        self.Ent_calendario1.delete(0,tk.END)
        self.Ent_calendario1.insert(tk.END, self.dataprima1)
        self.BuscarDataGanhos()
    def ModificarGanhos(self):
        try:
            self.DataModificada()
            self.Variavel_Ganhos()
            self.valor_saidas = [self.ent_for1, self.ent_for2, self.ent_for3]
            self.sumi = []
            self.ent_for_float4 = float(self.ent_for4)
            for s, w in enumerate(self.valor_saidas):
                if w == '':
                    x = w.replace('', '0')
                    self.sumi.append(float(x))
                else:
                    self.sumi.append(float(w))
            self.so = sum(self.sumi)
            self.paraobanco = []
            self.somas_rec_sai = (self.ent_for_float4 - self.so)
            for a, i in enumerate(self.valor_saidas):
                if i == '':
                    x = i.replace('', '0')
                    self.paraobanco.append('{:.2f}'.format(float(x)))
                else:
                    self.paraobanco.append('{:.2f}'.format(float(i)))
            self.DadosForma = self.paraobanco[0]
            self.DadosForma1 = self.paraobanco[1]
            self.DadosForma2 = self.paraobanco[2]
            self.ent_for_f4 = ('{:.2f}'.format(float(self.ent_for_float4)))
            self.somas_rec_sai_form = ('{:.2f}'.format(float(self.somas_rec_sai)))
            self.ConequitarBancoFinalizados()
            self.x.execute(f"""UPDATE dados_finalizados SET gasto_pesas = ?,gasto_retifica = ?,gasto_outros = ?,
            valor_recebido = ?, ganho = ? WHERE numero_pedido = ?""",
                           (
                           self.DadosForma, self.DadosForma1, self.DadosForma2, self.ent_for_f4, self.somas_rec_sai_form
                           , self.ent_for))
            self.DesconequitarBancoFinalizados()
            self.LimparGanhos()
            self.aviso.destroy()
            self.AtualizeLista_Ganhos()
        except:
            pass
    def Escolha_Modificar_Ganhos(self):
        if self.Ent_Ganhos.get() == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!ERRO NUMERO DA O.S!!!')
            self.jMensagem.place(x=70, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir os dados para Modificar!')
            self.j2Mensagem.place(x=40, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.cabesario_fo = ("Arial Black", "9")
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_fo, text='!VOCÊ REALMENTE'
                                                                               ' QUER MODIFICAR ESSE PEDIDO!')
            self.jMensagem.place(x=15, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='Está ação não poderar ser desfeita!')
            self.j2Mensagem.place(x=70, y=50)
            self.simbotam = tk.Button(self.aviso, text='SIM', font='Ariel', command=self.ModificarGanhos)
            self.simbotam.place(x=70, y=90, width=100, height=40)
            self.naobotam = tk.Button(self.aviso, text='NÃO', font='Ariel', command=self.aviso.destroy)
            self.naobotam.place(x=220, y=90, width=100, height=40)


class Funcs_Saidas(Funcs_Ganhos):
    def __init__(self):
        super().__init__()
        self.lista_c_clirSaida = None
        self.Ent_Svalor = None
        self.Ent_Svalor1 = None
        self.Ent_Svalor2 = None
        self.Ent_Svalor3 = None
        self.Ent_Svalor4 = None
        self.Ent_Svalor5 = None
        self.Ent_Svalor6 = None
        self.Ent_Svalor7 = None
        self.Ent_Svalor8 = None
        self.Ent_Saida = None
        self.Ent_Saida1 = None
        self.Ent_Saida2 = None
        self.Ent_Saida3 = None
        self.Ent_Saida4 = None
        self.Ent_Saida5 = None
        self.Ent_Saida6 = None
    def Variavel_saidas(self):
        self.entra_criar = self.Ent_Saida.get()
        self.entra_criar1 = self.Ent_Saida1.get().upper()
        self.entra_criar2 = self.Ent_Saida2.get().upper()
        self.entra_criar3 = self.Ent_Saida3.get().upper()
        self.entra_criar4 = self.Ent_Saida4.get().upper()
        self.entra_criar5 = self.Ent_Saida5.get().replace(',','.')
        self.entra_criar6 = self.Ent_Saida6.get().replace(',','.')
    def Limpar_criar_saida(self):
        self.Ent_Saida.delete(0, tk.END)
        self.Ent_Saida1.delete(0, tk.END)
        self.Ent_Saida3.delete(0, tk.END)
        self.Ent_Saida4.delete(0, tk.END)
        self.Ent_Saida5.delete(0, tk.END)
        self.Ent_Saida6.delete(0, tk.END)
    def Limpar_valores_saida(self):
        self.Ent_Svalor.delete(0, tk.END)
        self.Ent_Svalor1.delete(0, tk.END)
        self.Ent_Svalor2.delete(0, tk.END)
        self.Ent_Svalor3.delete(0, tk.END)
        self.Ent_Svalor4.delete(0, tk.END)
        self.Ent_Svalor5.delete(0, tk.END)
        self.Ent_Svalor6.delete(0, tk.END)
        self.Ent_Svalor7.delete(0, tk.END)
        self.Ent_Svalor8.delete(0, tk.END)
    def ConequitarBancoSaida(self):
        self.pasta_bancos()
        self.conexao = sqlite3.connect('Banco_saida.db')
        self.c = self.conexao.cursor()
    def DesconequitarBancoSaida(self):
        self.conexao.commit()
        self.conexao.close()
        os.chdir(diretorio)
    def CriarSaida(self):
        if self.Ent_Saida6.get() == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!VALOR NÃO INSIRIDO!!!')
            self.jMensagem.place(x=70, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o valor pago!')
            self.j2Mensagem.place(x=70, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif self.Ent_Saida2.get() == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!TIPO NÃO INSIRIDO!!!')
            self.jMensagem.place(x=70, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o tipo de Gasto!')
            self.j2Mensagem.place(x=40, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)


        else:
            self.Variavel_saidas()
            self.DataModificada()
            self.valor_saidas = [self.entra_criar5, self.entra_criar6]
            self.sumi = []
            for s, w in enumerate(self.valor_saidas):
                if w == '':
                    x = w.replace('', '0')
                    self.sumi.append(float(x))
                else:
                    self.sumi.append(float(w))
            self.so = sum(self.sumi)
            self.paraobanco = []
            for a, i in enumerate(self.valor_saidas):
                if i == '':
                    x = i.replace('', '0')
                    self.paraobanco.append('{:.2f}'.format(float(x)))
                else:
                    self.paraobanco.append('{:.2f}'.format(float(i)))
            self.so = sum(self.sumi)
            self.DadosForma = self.paraobanco[0]
            self.DadosForma1 = self.paraobanco[1]
            self.ConequitarBancoSaida()
            self.c.execute("""INSERT INTO saida(pago_por,tipo_gasto,gasto_com,local,valor_nota,valor_pago,data)
                           VALUES(?,?,?,?,?,?,?);""",
                           (self.entra_criar1, self.entra_criar2, self.entra_criar3, self.entra_criar4,
                            self.DadosForma, self.DadosForma1, self.data1))
            self.DesconequitarBancoSaida()
            self.Limpar_valores_saida()
            self.Limpar_criar_saida()
            self.AtualizeLista_Saida()
    def AtualizeLista_Saida(self):
        try:
            self.lista_c_clirSaida.delete(*self.lista_c_clirSaida.get_children())
            self.ConequitarBancoSaida()
            lista_Carro = self.c.execute("""SELECT numero_saida,pago_por,tipo_gasto,gasto_com,local,valor_nota,
            valor_pago,data FROM saida ORDER BY data DESC;""")
            for i in lista_Carro:
                self.lista_c_clirSaida.insert("", tk.END,
                                              values=(i[0], i[1], i[2], i[3], i[4], 'R$ ' + i[5].replace('.', ',')
                                                      , 'R$ ' + i[6].replace('.', ','), i[7]))

            self.DesconequitarBancoSaida()
            self.Limpar_criar_saida()
            self.Limpar_valores_saida()
            self.Caixa()
        except:
            pass
    def AbrirSaida(self,event):
        self.Limpar_criar_saida()
        self.Limpar_valores_saida()
        self.ConequitarBancoSaida()
        self.lista_c_clirSaida.selection()
        for n in self.lista_c_clirSaida.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.lista_c_clirSaida.item(n,'values')
            Dados = self.c.execute(f'SELECT numero_saida,pago_por,tipo_gasto,gasto_com,local,valor_nota,valor_pago'
                                   f' oid FROM saida WHERE numero_saida = {col1}')
            for i in Dados:
                self.Ent_Saida.insert(tk.END, i[0])
                self.Ent_Saida1.insert(tk.END, i[1])
                self.Ent_Saida2.set(f'{i[2]}')
                self.Ent_Saida3.insert(tk.END, i[3])
                self.Ent_Saida4.insert(tk.END, i[4])
                self.Ent_Saida5.insert(tk.END, i[5])
                self.Ent_Saida6.insert(tk.END, i[6])

        self.DesconequitarBancoSaida()
    def Escolha_apagar_Saida(self):
        if self.Ent_Saida.get() == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!NUMERO DA SAIDA NÃO INSIRIDO!!!')
            self.jMensagem.place(x=20, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o numero da saida!')
            self.j2Mensagem.place(x=60, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_voltar, text='!VOCÊ REALMENTE'
                                                                                   ' QUER APAGAR ESSE SAIDA!')
            self.jMensagem.place(x=15, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='Está ação não poderar ser desfeita!')
            self.j2Mensagem.place(x=70, y=50)
            self.simbotam = tk.Button(self.aviso, text='SIM', font='Ariel', command=self.DeletaSaida)
            self.simbotam.place(x=70, y=90, width=100, height=40)
            self.naobotam = tk.Button(self.aviso, text='NÃO', font='Ariel', command=self.aviso.destroy)
            self.naobotam.place(x=220, y=90, width=100, height=40)
    def DeletaSaida(self):
        try:
            self.Variavel_saidas()
            self.ConequitarBancoSaida()
            self.c.execute(f"""DELETE FROM saida WHERE numero_saida = '{self.entra_criar}'""")

            self.DesconequitarBancoSaida()
            self.Limpar_valores_saida()
            self.Limpar_criar_saida()
            self.AtualizeLista_Saida()
            self.aviso.destroy()
        except:
            pass
    def ModificarSaida(self):
        if self.Ent_Saida6.get() == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!VALOR NÃO INSIRIDO!!!')
            self.jMensagem.place(x=70, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o valor pago!')
            self.j2Mensagem.place(x=70, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif self.Ent_Saida2.get() == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!TIPO NÃO INSIRIDO!!!')
            self.jMensagem.place(x=70, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o tipo de Gasto!')
            self.j2Mensagem.place(x=40, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.Variavel_saidas()
            self.ConequitarBancoSaida()
            self.valor_saidas = [self.entra_criar5, self.entra_criar6]
            self.sumi = []
            for s, w in enumerate(self.valor_saidas):
                if w == '':
                    x = w.replace('', '0')
                    self.sumi.append(float(x))
                else:
                    self.sumi.append(float(w))
            self.so = sum(self.sumi)
            self.paraobanco = []
            for a, i in enumerate(self.valor_saidas):
                if i == '':
                    x = i.replace('', '0')
                    self.paraobanco.append('{:.2f}'.format(float(x)))
                else:
                    self.paraobanco.append('{:.2f}'.format(float(i)))
            self.so = sum(self.sumi)
            self.DadosForma = self.paraobanco[0]
            self.DadosForma1 = self.paraobanco[1]
            self.c.execute(f"""UPDATE saida SET pago_por = ?,tipo_gasto = ?,gasto_com = ?,local = ?,
            valor_nota = ?,valor_pago = ? WHERE numero_saida = ?""",
                           (self.entra_criar1, self.entra_criar2, self.entra_criar3, self.entra_criar4,
                            self.DadosForma, self.DadosForma1, self.entra_criar))
            self.DesconequitarBancoSaida()
            self.Limpar_valores_saida()
            self.Limpar_criar_saida()
            self.AtualizeLista_Saida()
            self.aviso.destroy()
    def Escolha_Modificar_Saida(self):
        if self.Ent_Saida.get() == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!NUMERO DA SAIDA NÃO INSIRIDO!!!')
            self.jMensagem.place(x=20, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o numero da saida!')
            self.j2Mensagem.place(x=60, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.cabesario_fo = ("Arial Black", "9")
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_fo, text='!VOCÊ REALMENTE'
                                                                               ' QUER MODIFICAR ESSE SAIDA!')
            self.jMensagem.place(x=15, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='Está ação não poderar ser desfeita!')
            self.j2Mensagem.place(x=70, y=50)
            self.simbotam = tk.Button(self.aviso, text='SIM', font='Ariel', command=self.ModificarSaida)
            self.simbotam.place(x=70, y=90, width=100, height=40)
            self.naobotam = tk.Button(self.aviso, text='NÃO', font='Ariel', command=self.aviso.destroy)
            self.naobotam.place(x=220, y=90, width=100, height=40)
    def BuscarDataSaida(self):
        self.Limpar_valores_saida()
        self.datapri = f'{self.dataprima[6:11]}-{self.dataprima[3:5]}-{self.dataprima[0:2]}'
        self.datapri1 = f'{self.dataprima1[6:11]}-{self.dataprima1[3:5]}-{self.dataprima1[0:2]}'
        self.lista_c_clirSaida.delete(*self.lista_c_clirSaida.get_children())
        self.ConequitarBancoSaida()
        DadosCarro = self.c.execute(f"""SELECT numero_saida,pago_por,tipo_gasto,gasto_com,local,valor_nota,valor_pago,
        data FROM saida WHERE data BETWEEN '{self.datapri}' AND '{self.datapri1}' ORDER BY data DESC;""")


        self.Somares = []
        self.Somares1 = []
        self.Somares2 = []
        self.Somares3 = []
        self.Somares4 = []
        self.Somares5 = []
        self.Somares6 = []
        self.Somares7 = []
        self.Somares8 = []

        for i in DadosCarro:
            self.lista_c_clirSaida.insert("", tk.END,
                                                values=(i[0], i[1], i[2], i[3], i[4], 'R$ ' + i[5].replace('.', ',')
                                                        ,'R$ ' + i[6].replace('.', ','),i[7]))
            if i[2] == 'SALARIO':
                self.Somares.append(float(i[6]))
            elif i[2] == 'PRODUTOS':
                self.Somares1.append(float(i[6]))
            elif i[2] == 'FERAMENTAS':
                self.Somares2.append(float(i[6]))
            elif i[2] == 'ALUGUEL':
                self.Somares3.append(float(i[6]))
            elif i[2] == 'QUEBRA DE CAIXA':
                self.Somares4.append(float(i[6]))
            elif i[2] == 'GARANTIAS':
                self.Somares5.append(float(i[6]))
            elif i[2] =='AGUA':
                self.Somares6.append(float(i[6]))
            elif i[2] =='LUZ':
                self.Somares7.append(float(i[6]))
            elif i[2] =='OUTROS':
                self.Somares8.append(float(i[6]))

        self.DesconequitarBancoSaida()

        self.somado = sum(self.Somares)
        self.somado1 = sum(self.Somares1)
        self.somado2 = sum(self.Somares2)
        self.somado3 = sum(self.Somares3)
        self.somado4 = sum(self.Somares4)
        self.somado5 = sum(self.Somares5)
        self.somado6 = sum(self.Somares6)
        self.somado7 = sum(self.Somares7)
        self.somado8 = sum(self.Somares8)
        self.somado_for = str('{:.2f}'.format(self.somado)).replace('.',',')
        self.somado_for1 = str('{:.2f}'.format(self.somado1)).replace('.',',')
        self.somado_for2 = str('{:.2f}'.format(self.somado2)).replace('.',',')
        self.somado_for3 = str('{:.2f}'.format(self.somado3)).replace('.',',')
        self.somado_for4 = str('{:.2f}'.format(self.somado4)).replace('.',',')
        self.somado_for5 = str('{:.2f}'.format(self.somado5)).replace('.',',')
        self.somado_for6 = str('{:.2f}'.format(self.somado6)).replace('.',',')
        self.somado_for7 = str('{:.2f}'.format(self.somado7)).replace('.',',')
        self.somado_for8 = str('{:.2f}'.format(self.somado8)).replace('.',',')
        self.Ent_Svalor.insert(tk.END, self.somado_for)
        self.Ent_Svalor1.insert(tk.END, self.somado_for1)
        self.Ent_Svalor2.insert(tk.END, self.somado_for2)
        self.Ent_Svalor3.insert(tk.END, self.somado_for3)
        self.Ent_Svalor4.insert(tk.END, self.somado_for4)
        self.Ent_Svalor5.insert(tk.END, self.somado_for5)
        self.Ent_Svalor6.insert(tk.END, self.somado_for6)
        self.Ent_Svalor7.insert(tk.END, self.somado_for7)
        self.Ent_Svalor8.insert(tk.END, self.somado_for8)
    def ColocardataSaida(self):
        self.dataprima = self.calendario.get_date()
        self.Ent_calendario.delete(0,tk.END)
        self.Ent_calendario.insert(tk.END, self.dataprima)
        self.dataprima1 = self.calendario1.get_date()
        self.Ent_calendario1.delete(0,tk.END)
        self.Ent_calendario1.insert(tk.END, self.dataprima1)
        self.BuscarDataSaida()
    def Caixa(self):
        self.CAIXA.delete(0,tk.END)
        self.Somares = []
        self.Somares1 = []
        self.ConequitarBancoFinalizados()
        DadosEntrada = self.x.execute(f'SELECT ganho FROM dados_finalizados ')
        for i in DadosEntrada:
            self.Somares.append(float(i[0]))
        self.DesconequitarBancoFinalizados()
        self.ConequitarBancoSaida()
        DadosSaida = self.c.execute(f"""SELECT valor_pago FROM saida """)
        for i in DadosSaida:
            self.Somares1.append(float(i[0]))
        self.DesconequitarBancoSaida()
        self.somado = sum(self.Somares)
        self.somado1 = sum(self.Somares1)
        self.Subitraido = (self.somado - self.somado1)
        self.somado_for = str(' {:.2f}'.format(self.Subitraido)).replace('.',',')
        self.CAIXA.insert(tk.END, self.somado_for)

