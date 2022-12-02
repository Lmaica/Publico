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
            self.conexao = sqlite3.connect('Banco_serviços_pendentes.db')

            self.c = self.conexao.cursor()

            self.c.execute('''CREATE TABLE dados_serviços(
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
                  peças1 text,
                  uni1 text,
                  valor_peças1 text,
                  peças2 text,
                  uni2 text,
                  valor_peças2 text,
                  peças3 text,
                  uni3 text,
                  valor_peças3 text,
                  peças4 text,
                  uni4 text,
                  valor_peças4 text,
                  peças5 text,
                  uni5 text,
                  valor_peças5 text,
                  peças6 text,
                  uni6 text,
                  valor_peças6 text,
                  peças7 text,
                  uni7 text,
                  valor_peças7 text,
                  peças8 text,
                  uni8 text,
                  valor_peças8 text,
                  peças9 text,
                  uni9 text,
                  valor_peças9 text,
                  peças10 text,
                  uni10 text,
                  valor_peças10 text,
                  peças11 text,
                  uni11 text,
                  valor_peças11 text,
                  peças12 text,
                  uni12 text,
                  valor_peças12 text,
                  peças13 text,
                  uni13 text,
                  valor_peças13 text,
                  peças14 text,
                  uni14 text,
                  valor_peças14 text,
                  peças15 text,
                  uni15 text,
                  valor_peças15 text,
                  peças16 text,
                  uni16 text,
                  valor_peças16 text,
                  peças17 text,
                  uni17 text,
                  valor_peças17 text,
                  peças18 text,
                  uni18 text,
                  valor_peças18 text,
                  peças19 text,
                  uni19 text,
                  valor_peças19 text,
                  peças20 text,
                  uni20 text,
                  valor_peças20 text,                  
                  retifica text,
                  M_O text,
                  total_peças text,
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
                  peças1 text,
                  uni1 text,
                  valor_peças1 text,
                  peças2 text,
                  uni2 text,
                  valor_peças2 text,
                  peças3 text,
                  uni3 text,
                  valor_peças3 text,
                  peças4 text,
                  uni4 text,
                  valor_peças4 text,
                  peças5 text,
                  uni5 text,
                  valor_peças5 text,
                  peças6 text,
                  uni6 text,
                  valor_peças6 text,
                  peças7 text,
                  uni7 text,
                  valor_peças7 text,
                  peças8 text,
                  uni8 text,
                  valor_peças8 text,
                  peças9 text,
                  uni9 text,
                  valor_peças9 text,
                  peças10 text,
                  uni10 text,
                  valor_peças10 text,
                  peças11 text,
                  uni11 text,
                  valor_peças11 text,
                  peças12 text,
                  uni12 text,
                  valor_peças12 text,
                  peças13 text,
                  uni13 text,
                  valor_peças13 text,
                  peças14 text,
                  uni14 text,
                  valor_peças14 text,
                  peças15 text,
                  uni15 text,
                  valor_peças15 text,
                  peças16 text,
                  uni16 text,
                  valor_peças16 text,
                  peças17 text,
                  uni17 text,
                  valor_peças17 text,
                  peças18 text,
                  uni18 text,
                  valor_peças18 text,
                  peças19 text,
                  uni19 text,
                  valor_peças19 text,
                  peças20 text,
                  uni20 text,
                  valor_peças20 text,                  
                  retifica text,
                  M_O text,
                  total_peças text,
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

