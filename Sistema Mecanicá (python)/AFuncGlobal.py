from Modolos import *

diretorio = os.getcwd()

class Validadors():
    def ValidasaoTelefone(self, text):
        if text == '': return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 100000000000


class PastasBAncos(Validadors):
    def __init__(self):
        self.os = None
    def DataModificada(self):
        self.data1 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.data2 = datetime.now().strftime('%d/%m/%Y %H:%M')
        self.dataP1 = datetime.now().strftime('%Y-%m-%d')
        self.dataP2 = datetime.now().strftime('%d/%m/%Y')
    def criar_pasta_banco(self):
        self.DataModificada()
        try:
            os.mkdir('Bancos de dados')
            os.makedirs('O.S/Nota')
            os.makedirs('O.S/Nota_p_maquina')
            os.chdir(diretorio)
        except:
            pass
        finally:
            os.chdir(diretorio)
    def pasta_bancos(self):
        try:
            os.chdir('Bancos de dados')
        except:
            pass
    def pasta_nota(self):
        self.DataModificada()
        try:
            os.chdir('O.S')
            os.chdir('Nota_p_maquina')
        except:
            pass
    def pasta_W_s(self):
        self.DataModificada()
        try:
            os.chdir('O.S')
            os.chdir('Nota')
        except:
            pass
    def criar_lisa_clientes(self):
        try:
            self.pasta_bancos()
            self.conexao_clientes = sqlite3.connect('Banco_clientes.db')
            self.c = self.conexao_clientes.cursor()

            self.c.execute('''CREATE TABLE dados_clientes(
                          cliente text,
                          telefone text,
                          telefone_2 text,
                          data_nacimento text,
                          cpf text,
                          cep text,
                          numero_casa text,
                          complemento text,
                          numero_cliente INTEGER PRIMARY KEY
                          );

                    ''')

            self.conexao_clientes.commit()
            self.conexao_clientes.close()
            os.chdir(diretorio)
        except:
            os.chdir(diretorio)
    def criar_lisa_carro(self):
        try:
            self.pasta_bancos()
            self.conexao = sqlite3.connect('Banco_clientes.db')
            self.cr = self.conexao.cursor()

            self.cr.execute('''CREATE TABLE dados_carro(
                          cliente text,
                          telefone text,
                          marca text,
                          modelo text,
                          ano text,
                          motor text,
                          placa text,
                          km text,
                          numero_cliente text,
                          numero_carro INTEGER PRIMARY KEY
                          );
                    ''')

            self.conexao.commit()
            self.conexao.close()
            os.chdir(diretorio)
        except:
            os.chdir(diretorio)
    def criar_lista_pendentes(self):
        try:
            self.pasta_bancos()
            self.conexao = sqlite3.connect('Banco_servi??os_pendentes.db')

            self.c = self.conexao.cursor()

            self.c.execute('''CREATE TABLE dados_servi??os(
                  numero_pedido INTEGER PRIMARY KEY,
                  cliente text,
                  telefone text,
                  numero_cliente text,
                  placa text,
                  marca text,
                  modelo text,
                  ano text,
                  motor text,
                  km text,
                  pe??as1 text,
                  uni1 text,
                  valor_pe??as1 text,
                  pe??as2 text,
                  uni2 text,
                  valor_pe??as2 text,
                  pe??as3 text,
                  uni3 text,
                  valor_pe??as3 text,
                  pe??as4 text,
                  uni4 text,
                  valor_pe??as4 text,
                  pe??as5 text,
                  uni5 text,
                  valor_pe??as5 text,
                  pe??as6 text,
                  uni6 text,
                  valor_pe??as6 text,
                  pe??as7 text,
                  uni7 text,
                  valor_pe??as7 text,
                  pe??as8 text,
                  uni8 text,
                  valor_pe??as8 text,
                  pe??as9 text,
                  uni9 text,
                  valor_pe??as9 text,
                  pe??as10 text,
                  uni10 text,
                  valor_pe??as10 text,
                  pe??as11 text,
                  uni11 text,
                  valor_pe??as11 text,
                  pe??as12 text,
                  uni12 text,
                  valor_pe??as12 text,
                  pe??as13 text,
                  uni13 text,
                  valor_pe??as13 text,
                  pe??as14 text,
                  uni14 text,
                  valor_pe??as14 text,
                  pe??as15 text,
                  uni15 text,
                  valor_pe??as15 text,
                  pe??as16 text,
                  uni16 text,
                  valor_pe??as16 text,
                  pe??as17 text,
                  uni17 text,
                  valor_pe??as17 text,
                  pe??as18 text,
                  uni18 text,
                  valor_pe??as18 text,
                  pe??as19 text,
                  uni19 text,
                  valor_pe??as19 text,
                  pe??as20 text,
                  uni20 text,
                  valor_pe??as20 text,                  
                  retifica text,
                  M_O text,
                  total_pe??as text,
                  total_OS text,
                  data text
                  );

            ''')

            self.conexao.commit()
            self.conexao.close()
            os.chdir(diretorio)
        except:
            os.chdir(diretorio)
    def criar_banco_finalizados(self):
        try:
            self.pasta_bancos()
            conexao = sqlite3.connect('Banco_finalizados.db')

            c = conexao.cursor()

            c.execute('''CREATE TABLE dados_finalizados(
                  numero_pedido text,
                  cliente text,
                  telefone text,
                  numero_cliente text,
                  placa text,
                  marca text,
                  modelo text,
                  ano text,
                  motor text,
                  km text,
                  pe??as1 text,
                  uni1 text,
                  valor_pe??as1 text,
                  pe??as2 text,
                  uni2 text,
                  valor_pe??as2 text,
                  pe??as3 text,
                  uni3 text,
                  valor_pe??as3 text,
                  pe??as4 text,
                  uni4 text,
                  valor_pe??as4 text,
                  pe??as5 text,
                  uni5 text,
                  valor_pe??as5 text,
                  pe??as6 text,
                  uni6 text,
                  valor_pe??as6 text,
                  pe??as7 text,
                  uni7 text,
                  valor_pe??as7 text,
                  pe??as8 text,
                  uni8 text,
                  valor_pe??as8 text,
                  pe??as9 text,
                  uni9 text,
                  valor_pe??as9 text,
                  pe??as10 text,
                  uni10 text,
                  valor_pe??as10 text,
                  pe??as11 text,
                  uni11 text,
                  valor_pe??as11 text,
                  pe??as12 text,
                  uni12 text,
                  valor_pe??as12 text,
                  pe??as13 text,
                  uni13 text,
                  valor_pe??as13 text,
                  pe??as14 text,
                  uni14 text,
                  valor_pe??as14 text,
                  pe??as15 text,
                  uni15 text,
                  valor_pe??as15 text,
                  pe??as16 text,
                  uni16 text,
                  valor_pe??as16 text,
                  pe??as17 text,
                  uni17 text,
                  valor_pe??as17 text,
                  pe??as18 text,
                  uni18 text,
                  valor_pe??as18 text,
                  pe??as19 text,
                  uni19 text,
                  valor_pe??as19 text,
                  pe??as20 text,
                  uni20 text,
                  valor_pe??as20 text,                  
                  retifica text,
                  M_O text,
                  total_pe??as text,
                  total_OS text,
                  forma_paga text,
                  valor_recebido text,
                  gasto_pesas text,
                  gasto_retifica text,
                  gasto_outros text,
                  ganho text,
                  data text
                  );

            ''')

            conexao.commit()
            conexao.close()
        except:
            pass
        finally:
            os.chdir(diretorio)
    def criar_saida(self):
        try:
            self.pasta_bancos()

            self.conexao = sqlite3.connect('Banco_saida.db')

            self.c = self.conexao.cursor()

            self.c.execute('''CREATE TABLE saida(
            numero_Saida INTEGER PRIMARY KEY,
            pago_por text,
            tipo_gasto text,
            gasto_com text,
            local text,
            valor_nota text,
            valor_pago text,
            data text
            );

            ''')

            self.conexao.commit()
            self.conexao.close()

            os.chdir(diretorio)
        except:
            os.chdir(diretorio)
    def Criar_Pos_Vendas(self):
        try:
            self.pasta_bancos()

            self.conexao = sqlite3.connect('Banco_Pos_Venda.db')

            self.c = self.conexao.cursor()

            self.c.execute('''CREATE TABLE pos_venda(
            numero_pos_venda INTEGER PRIMARY KEY,
            nome text,
            whats text,
            numero_cliente text,
            data_criada text,
            data_executar text,
            mensagem1 text,
            mensagem2 text,
            mensagem3 text
            );

            ''')

            self.conexao.commit()
            self.conexao.close()

            os.chdir(diretorio)
        except:
            os.chdir(diretorio)
    def Criar_Mensagens(self):
        try:
            self.pasta_bancos()

            self.conexao = sqlite3.connect('Banco_mensagens.db')

            self.c = self.conexao.cursor()

            self.c.execute('''CREATE TABLE mensagens(
            numero_mensagens INTEGER PRIMARY KEY,
            mensagem1 text,
            mensagem2 text,
            mensagem3 text
            );

            ''')

            self.conexao.commit()
            self.conexao.close()

            os.chdir(diretorio)
        except:
            os.chdir(diretorio)
    def Mensagenscaixa(self):
        self.aviso = tk.Toplevel()
        self.aviso.title('ALERTA!')
        self.aviso.iconbitmap(self.diretorio + '\Imagens\icone.ico')
        self.aviso.geometry('390x140')
        self.aviso.configure(background='#CC1100')
        self.aviso.resizable(False, False)
        self.aviso.transient(self.c_janela)
        self.aviso.focus_force()
        self.aviso.grab_set()
        self.quadrado = tk.Frame(self.aviso)
        self.quadrado.place(x=5, y=5, width=380, height=130)

