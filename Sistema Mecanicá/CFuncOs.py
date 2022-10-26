from BFuncsCadastros import *


class Funcs_os(Funcs_Carro):
    def __init__(self):
        super().__init__()
        self.cabesario_font1 = None
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
    def ConequitarBancoPendentes(self):
        self.pasta_bancos()
        self.conexao = sqlite3.connect('Banco_serviços_pendentes.db')
        self.c = self.conexao.cursor()
    def DesconequitarBancoPendetes(self):
        self.conexao.commit()
        self.conexao.close()
        os.chdir(diretorio)
    def LimparOsCarro(self):
        self.entraCarro.delete(0,tk.END)
        self.entra1Carro.delete(0,tk.END)
        self.entra2Carro.delete(0,tk.END)
        self.entra3Carro.delete(0,tk.END)
        self.entra4Carro.delete(0,tk.END)
        self.entra5Carro.delete(0,tk.END)
        self.entra6Carro.delete(0,tk.END)
        self.entra7Carro.delete(0,tk.END)
        self.entra8Carro.delete(0,tk.END)
    def Variavel_Os(self):
        self.codigo_os = self.entrada_codigo.get()
        self.porcentagem = self.entrada_por.get()

        self.pasa = self.entrada_pesas.get().strip().title()
        self.Upesa = self.entrada_uni.get()
        self.vUpesa = self.entrada_v_uni.get().replace(',', '.')
        self.tVpesa = self.entrada_t_uni.get().replace(',', '.')
        self.pasa1 = self.entrada_pesas1.get().strip().title()
        self.Upesa1 = self.entrada_uni1.get()
        self.vUpesa1 = self.entrada_v_uni1.get().replace(',', '.')
        self.tVpesa1 = self.entrada_t_uni1.get().replace(',', '.')
        self.pasa2 = self.entrada_pesas2.get().strip().title()
        self.Upesa2 = self.entrada_uni2.get()
        self.vUpesa2 = self.entrada_v_uni2.get().replace(',', '.')
        self.tVpesa2 = self.entrada_t_uni2.get().replace(',', '.')
        self.pasa3 = self.entrada_pesas3.get().strip().title()
        self.Upesa3 = self.entrada_uni3.get()
        self.vUpesa3 = self.entrada_v_uni3.get().replace(',', '.')
        self.tVpesa3 = self.entrada_t_uni3.get().replace(',', '.')
        self.pasa4 = self.entrada_pesas4.get().strip().title()
        self.Upesa4 = self.entrada_uni4.get()
        self.vUpesa4 = self.entrada_v_uni4.get().replace(',', '.')
        self.tVpesa4 = self.entrada_t_uni4.get().replace(',', '.')
        self.pasa5 = self.entrada_pesas5.get().strip().title()
        self.Upesa5 = self.entrada_uni5.get()
        self.vUpesa5 = self.entrada_v_uni5.get().replace(',', '.')
        self.tVpesa5 = self.entrada_t_uni5.get().replace(',', '.')
        self.pasa6 = self.entrada_pesas6.get().strip().title()
        self.Upesa6 = self.entrada_uni6.get()
        self.vUpesa6 = self.entrada_v_uni6.get().replace(',', '.')
        self.tVpesa6 = self.entrada_t_uni6.get().replace(',', '.')
        self.pasa7 = self.entrada_pesas7.get().strip().title()
        self.Upesa7 = self.entrada_uni7.get()
        self.vUpesa7 = self.entrada_v_uni7.get().replace(',', '.')
        self.tVpesa7 = self.entrada_t_uni7.get().replace(',', '.')
        self.pasa8 = self.entrada_pesas8.get().strip().title()
        self.Upesa8 = self.entrada_uni8.get().strip()
        self.vUpesa8 = self.entrada_v_uni8.get().replace(',', '.')
        self.tVpesa8 = self.entrada_t_uni8.get().replace(',', '.')
        self.pasa9 = self.entrada_pesas9.get().strip().title()
        self.Upesa9 = self.entrada_uni9.get()
        self.vUpesa9 = self.entrada_v_uni9.get().replace(',', '.')
        self.tVpesa9 = self.entrada_t_uni9.get().replace(',', '.')
        self.pasa10 = self.entrada_pesas10.get().strip().title()
        self.Upesa10 = self.entrada_uni10.get()
        self.vUpesa10 = self.entrada_v_uni10.get().replace(',', '.')
        self.tVpesa10 = self.entrada_t_uni10.get().replace(',', '.')
        self.pasa11 = self.entrada_pesas11.get().strip().title()
        self.Upesa11 = self.entrada_uni11.get()
        self.vUpesa11 = self.entrada_v_uni11.get().replace(',', '.')
        self.tVpesa11 = self.entrada_t_uni11.get().replace(',', '.')
        self.pasa12 = self.entrada_pesas12.get().strip().title()
        self.Upesa12 = self.entrada_uni12.get()
        self.vUpesa12 = self.entrada_v_uni12.get().replace(',', '.')
        self.tVpesa12 = self.entrada_t_uni12.get().replace(',', '.')
        self.pasa13 = self.entrada_pesas13.get().strip().title()
        self.Upesa13 = self.entrada_uni13.get()
        self.vUpesa13 = self.entrada_v_uni13.get().replace(',', '.')
        self.tVpesa13 = self.entrada_t_uni13.get().replace(',', '.')
        self.pasa14 = self.entrada_pesas14.get().strip().title()
        self.Upesa14 = self.entrada_uni14.get()
        self.vUpesa14 = self.entrada_v_uni14.get().replace(',', '.')
        self.tVpesa14 = self.entrada_t_uni14.get().replace(',', '.')
        self.pasa15 = self.entrada_pesas15.get().strip().title()
        self.Upesa15 = self.entrada_uni15.get()
        self.vUpesa15 = self.entrada_v_uni15.get().replace(',', '.')
        self.tVpesa15 = self.entrada_t_uni15.get().replace(',', '.')
        self.pasa16 = self.entrada_pesas16.get().strip().title()
        self.Upesa16 = self.entrada_uni16.get()
        self.vUpesa16 = self.entrada_v_uni16.get().replace(',', '.')
        self.tVpesa16 = self.entrada_t_uni16.get().replace(',', '.')
        self.pasa17 = self.entrada_pesas17.get().strip().title()
        self.Upesa17 = self.entrada_uni17.get()
        self.vUpesa17 = self.entrada_v_uni17.get().replace(',', '.')
        self.tVpesa17 = self.entrada_t_uni17.get().replace(',', '.')
        self.pasa18 = self.entrada_pesas18.get().strip().title()
        self.Upesa18 = self.entrada_uni18.get()
        self.vUpesa18 = self.entrada_v_uni18.get().replace(',', '.')
        self.tVpesa18 = self.entrada_t_uni18.get().replace(',', '.')
        self.pasa19 = self.entrada_pesas19.get().strip().title()
        self.Upesa19 = self.entrada_uni19.get()
        self.vUpesa19 = self.entrada_v_uni19.get().replace(',', '.')
        self.tVpesa19 = self.entrada_t_uni19.get().replace(',', '.')

        self.DadosOsCarro = self.entraCarro.get()
        self.DadosOsCarro1 = self.entra1Carro.get()
        self.DadosOsCarro2 = self.entra2Carro.get()
        self.DadosOsCarro3 = self.entra3Carro.get()
        self.DadosOsCarro4 = self.entra4Carro.get()
        self.DadosOsCarro5 = self.entra5Carro.get()
        self.DadosOsCarro6 = self.entra6Carro.get()
        self.DadosOsCarro7 = self.entra7Carro.get()
        self.DadosOsCarro8 = self.entra8Carro.get()

        self.retifica = self.Retifica.get().replace(',', '.')
        self.mo = self.M_O.get().replace(',', '.')
        self.pesas_total = self.PesasTotal.get().replace(',', '.')
        self.totaltotal = self.TotalTotal.get().replace(',', '.')
    def LimparPesas(self):
        self.entrada_codigo.delete(0,tk.END)
        self.entrada_por.delete(0, tk.END)

        self.entrada_pesas.delete(0, tk.END)
        self.entrada_uni.delete(0, tk.END)
        self.entrada_v_uni.delete(0, tk.END)
        self.entrada_t_uni.delete(0, tk.END)
        self.entrada_pesas1.delete(0, tk.END)
        self.entrada_uni1.delete(0, tk.END)
        self.entrada_v_uni1.delete(0, tk.END)
        self.entrada_t_uni1.delete(0, tk.END)
        self.entrada_pesas2.delete(0, tk.END)
        self.entrada_uni2.delete(0, tk.END)
        self.entrada_v_uni2.delete(0, tk.END)
        self.entrada_t_uni2.delete(0, tk.END)
        self.entrada_pesas3.delete(0, tk.END)
        self.entrada_uni3.delete(0, tk.END)
        self.entrada_v_uni3.delete(0, tk.END)
        self.entrada_t_uni3.delete(0, tk.END)
        self.entrada_pesas4.delete(0, tk.END)
        self.entrada_uni4.delete(0, tk.END)
        self.entrada_v_uni4.delete(0, tk.END)
        self.entrada_t_uni4.delete(0, tk.END)
        self.entrada_pesas5.delete(0, tk.END)
        self.entrada_uni5.delete(0, tk.END)
        self.entrada_v_uni5.delete(0, tk.END)
        self.entrada_t_uni5.delete(0, tk.END)
        self.entrada_pesas6.delete(0, tk.END)
        self.entrada_uni6.delete(0, tk.END)
        self.entrada_v_uni6.delete(0, tk.END)
        self.entrada_t_uni6.delete(0, tk.END)
        self.entrada_pesas7.delete(0, tk.END)
        self.entrada_uni7.delete(0, tk.END)
        self.entrada_v_uni7.delete(0, tk.END)
        self.entrada_t_uni7.delete(0, tk.END)
        self.entrada_pesas8.delete(0, tk.END)
        self.entrada_uni8.delete(0, tk.END)
        self.entrada_v_uni8.delete(0, tk.END)
        self.entrada_t_uni8.delete(0, tk.END)
        self.entrada_pesas9.delete(0, tk.END)
        self.entrada_uni9.delete(0, tk.END)
        self.entrada_v_uni9.delete(0, tk.END)
        self.entrada_t_uni9.delete(0, tk.END)
        self.entrada_pesas10.delete(0, tk.END)
        self.entrada_uni10.delete(0, tk.END)
        self.entrada_v_uni10.delete(0, tk.END)
        self.entrada_t_uni10.delete(0, tk.END)
        self.entrada_pesas11.delete(0, tk.END)
        self.entrada_uni11.delete(0, tk.END)
        self.entrada_v_uni11.delete(0, tk.END)
        self.entrada_t_uni11.delete(0, tk.END)
        self.entrada_pesas12.delete(0, tk.END)
        self.entrada_uni12.delete(0, tk.END)
        self.entrada_v_uni12.delete(0, tk.END)
        self.entrada_t_uni12.delete(0, tk.END)
        self.entrada_pesas13.delete(0, tk.END)
        self.entrada_uni13.delete(0, tk.END)
        self.entrada_v_uni13.delete(0, tk.END)
        self.entrada_t_uni13.delete(0, tk.END)
        self.entrada_pesas14.delete(0, tk.END)
        self.entrada_uni14.delete(0, tk.END)
        self.entrada_v_uni14.delete(0, tk.END)
        self.entrada_t_uni14.delete(0, tk.END)
        self.entrada_pesas15.delete(0, tk.END)
        self.entrada_uni15.delete(0, tk.END)
        self.entrada_v_uni15.delete(0, tk.END)
        self.entrada_t_uni15.delete(0, tk.END)
        self.entrada_pesas16.delete(0, tk.END)
        self.entrada_uni16.delete(0, tk.END)
        self.entrada_v_uni16.delete(0, tk.END)
        self.entrada_t_uni16.delete(0, tk.END)
        self.entrada_pesas17.delete(0, tk.END)
        self.entrada_uni17.delete(0, tk.END)
        self.entrada_v_uni17.delete(0, tk.END)
        self.entrada_t_uni17.delete(0, tk.END)
        self.entrada_pesas18.delete(0, tk.END)
        self.entrada_uni18.delete(0, tk.END)
        self.entrada_v_uni18.delete(0, tk.END)
        self.entrada_t_uni18.delete(0, tk.END)
        self.entrada_pesas19.delete(0, tk.END)
        self.entrada_uni19.delete(0, tk.END)
        self.entrada_v_uni19.delete(0, tk.END)
        self.entrada_t_uni19.delete(0, tk.END)

        self.PesasTotal.delete(0, tk.END)
        self.Retifica.delete(0, tk.END)
        self.M_O.delete(0, tk.END)
        self.TotalTotal.delete(0, tk.END)
    def Somar(self):
        self.Variavel_Os()
        try:
            self.entrada_v_uni.delete(0, tk.END)
            self.vUpesafor = ('{:.2f}').format(float(self.vUpesa)).replace('.', ',')
            self.entrada_v_uni.insert(tk.END, self.vUpesafor)
            self.somar_un_pesa = float(self.vUpesa) * int(self.Upesa)
            self.entrada_t_uni.delete(0, tk.END)
            self.somar_un_pesafor = ('{:.2f}').format(self.somar_un_pesa).replace('.', ',')
            self.entrada_t_uni.insert(tk.END, self.somar_un_pesafor)

            self.entrada_v_uni1.delete(0, tk.END)
            self.vUpesafor1 = ('{:.2f}').format(float(self.vUpesa1)).replace('.', ',')
            self.entrada_v_uni1.insert(tk.END, self.vUpesafor1)
            self.somar_un_pesa1 = float(self.vUpesa1) * int(self.Upesa1)
            self.entrada_t_uni1.delete(0, tk.END)
            self.somar_un_pesafor1 = ('{:.2f}').format(self.somar_un_pesa1).replace('.', ',')
            self.entrada_t_uni1.insert(tk.END, self.somar_un_pesafor1)

            self.entrada_v_uni2.delete(0, tk.END)
            self.vUpesafor2 = ('{:.2f}').format(float(self.vUpesa2)).replace('.', ',')
            self.entrada_v_uni2.insert(tk.END, self.vUpesafor2)
            self.somar_un_pesa2 = float(self.vUpesa2) * int(self.Upesa2)
            self.entrada_t_uni2.delete(0, tk.END)
            self.somar_un_pesafor2 = ('{:.2f}').format(self.somar_un_pesa2).replace('.', ',')
            self.entrada_t_uni2.insert(tk.END, self.somar_un_pesafor2)

            self.entrada_v_uni3.delete(0, tk.END)
            self.vUpesafor3 = ('{:.2f}').format(float(self.vUpesa3)).replace('.', ',')
            self.entrada_v_uni3.insert(tk.END, self.vUpesafor3)
            self.somar_un_pesa3 = float(self.vUpesa3) * int(self.Upesa3)
            self.entrada_t_uni3.delete(0, tk.END)
            self.somar_un_pesafor3 = ('{:.2f}').format(self.somar_un_pesa3).replace('.', ',')
            self.entrada_t_uni3.insert(tk.END, self.somar_un_pesafor3)

            self.entrada_v_uni4.delete(0, tk.END)
            self.vUpesafor4 = ('{:.2f}').format(float(self.vUpesa4)).replace('.', ',')
            self.entrada_v_uni4.insert(tk.END, self.vUpesafor4)
            self.somar_un_pesa4 = float(self.vUpesa4) * int(self.Upesa4)
            self.entrada_t_uni4.delete(0, tk.END)
            self.somar_un_pesafor4 = ('{:.2f}').format(self.somar_un_pesa4).replace('.', ',')
            self.entrada_t_uni4.insert(tk.END, self.somar_un_pesafor4)

            self.entrada_v_uni5.delete(0, tk.END)
            self.vUpesafor5 = ('{:.2f}').format(float(self.vUpesa5)).replace('.', ',')
            self.entrada_v_uni5.insert(tk.END, self.vUpesafor5)
            self.somar_un_pesa5 = float(self.vUpesa5) * int(self.Upesa5)
            self.entrada_t_uni5.delete(0, tk.END)
            self.somar_un_pesafor5 = ('{:.2f}').format(self.somar_un_pesa5).replace('.', ',')
            self.entrada_t_uni5.insert(tk.END, self.somar_un_pesafor5)

            self.entrada_v_uni6.delete(0, tk.END)
            self.vUpesafor6 = ('{:.2f}').format(float(self.vUpesa6)).replace('.', ',')
            self.entrada_v_uni6.insert(tk.END, self.vUpesafor6)
            self.somar_un_pesa6 = float(self.vUpesa6) * int(self.Upesa6)
            self.entrada_t_uni6.delete(0, tk.END)
            self.somar_un_pesafor6 = ('{:.2f}').format(self.somar_un_pesa6).replace('.', ',')
            self.entrada_t_uni6.insert(tk.END, self.somar_un_pesafor6)

            self.entrada_v_uni7.delete(0, tk.END)
            self.vUpesafor7 = ('{:.2f}').format(float(self.vUpesa7)).replace('.', ',')
            self.entrada_v_uni7.insert(tk.END, self.vUpesafor7)
            self.somar_un_pesa7 = float(self.vUpesa7) * int(self.Upesa7)
            self.entrada_t_uni7.delete(0, tk.END)
            self.somar_un_pesafor7 = ('{:.2f}').format(self.somar_un_pesa7).replace('.', ',')
            self.entrada_t_uni7.insert(tk.END, self.somar_un_pesafor7)

            self.entrada_v_uni8.delete(0, tk.END)
            self.vUpesafor8 = ('{:.2f}').format(float(self.vUpesa8)).replace('.', ',')
            self.entrada_v_uni8.insert(tk.END, self.vUpesafor8)
            self.somar_un_pesa8 = float(self.vUpesa8) * int(self.Upesa8)
            self.entrada_t_uni8.delete(0, tk.END)
            self.somar_un_pesafor8 = ('{:.2f}').format(self.somar_un_pesa8).replace('.', ',')
            self.entrada_t_uni8.insert(tk.END, self.somar_un_pesafor8)

            self.entrada_v_uni9.delete(0, tk.END)
            self.vUpesafor9 = ('{:.2f}').format(float(self.vUpesa9)).replace('.', ',')
            self.entrada_v_uni9.insert(tk.END, self.vUpesafor9)
            self.somar_un_pesa9 = float(self.vUpesa9) * int(self.Upesa9)
            self.entrada_t_uni9.delete(0, tk.END)
            self.somar_un_pesafor9 = ('{:.2f}').format(self.somar_un_pesa9).replace('.', ',')
            self.entrada_t_uni9.insert(tk.END, self.somar_un_pesafor9)

            self.entrada_v_uni10.delete(0, tk.END)
            self.vUpesafor10 = ('{:.2f}').format(float(self.vUpesa10)).replace('.', ',')
            self.entrada_v_uni10.insert(tk.END, self.vUpesafor10)
            self.somar_un_pesa10 = float(self.vUpesa10) * int(self.Upesa10)
            self.entrada_t_uni10.delete(0, tk.END)
            self.somar_un_pesafor10 = ('{:.2f}').format(self.somar_un_pesa10).replace('.', ',')
            self.entrada_t_uni10.insert(tk.END, self.somar_un_pesafor10)

            self.entrada_v_uni11.delete(0, tk.END)
            self.vUpesafor11 = ('{:.2f}').format(float(self.vUpesa11)).replace('.', ',')
            self.entrada_v_uni11.insert(tk.END, self.vUpesafor11)
            self.somar_un_pesa11 = float(self.vUpesa11) * int(self.Upesa11)
            self.entrada_t_uni11.delete(0, tk.END)
            self.somar_un_pesafor11 = ('{:.2f}').format(self.somar_un_pesa11).replace('.', ',')
            self.entrada_t_uni11.insert(tk.END, self.somar_un_pesafor11)

            self.entrada_v_uni12.delete(0, tk.END)
            self.vUpesafor12 = ('{:.2f}').format(float(self.vUpesa12)).replace('.', ',')
            self.entrada_v_uni12.insert(tk.END, self.vUpesafor12)
            self.somar_un_pesa12 = float(self.vUpesa12) * int(self.Upesa12)
            self.entrada_t_uni12.delete(0, tk.END)
            self.somar_un_pesafor12 = ('{:.2f}').format(self.somar_un_pesa12).replace('.', ',')
            self.entrada_t_uni12.insert(tk.END, self.somar_un_pesafor12)

            self.entrada_v_uni13.delete(0, tk.END)
            self.vUpesafor13 = ('{:.2f}').format(float(self.vUpesa13)).replace('.', ',')
            self.entrada_v_uni13.insert(tk.END, self.vUpesafor13)
            self.somar_un_pesa13 = float(self.vUpesa13) * int(self.Upesa13)
            self.entrada_t_uni13.delete(0, tk.END)
            self.somar_un_pesafor13 = ('{:.2f}').format(self.somar_un_pesa13).replace('.', ',')
            self.entrada_t_uni13.insert(tk.END, self.somar_un_pesafor13)

            self.entrada_v_uni14.delete(0, tk.END)
            self.vUpesafor14 = ('{:.2f}').format(float(self.vUpesa14)).replace('.', ',')
            self.entrada_v_uni14.insert(tk.END, self.vUpesafor14)
            self.somar_un_pesa14 = float(self.vUpesa14) * int(self.Upesa14)
            self.entrada_t_uni14.delete(0, tk.END)
            self.somar_un_pesafor14 = ('{:.2f}').format(self.somar_un_pesa14).replace('.', ',')
            self.entrada_t_uni14.insert(tk.END, self.somar_un_pesafor14)

            self.entrada_v_uni15.delete(0, tk.END)
            self.vUpesafor15 = ('{:.2f}').format(float(self.vUpesa15)).replace('.', ',')
            self.entrada_v_uni15.insert(tk.END, self.vUpesafor15)
            self.somar_un_pesa15 = float(self.vUpesa15) * int(self.Upesa)
            self.entrada_t_uni15.delete(0, tk.END)
            self.somar_un_pesafor15 = ('{:.2f}').format(self.somar_un_pesa15).replace('.', ',')
            self.entrada_t_uni15.insert(tk.END, self.somar_un_pesafor15)

            self.entrada_v_uni16.delete(0, tk.END)
            self.vUpesafor16 = ('{:.2f}').format(float(self.vUpesa16)).replace('.', ',')
            self.entrada_v_uni16.insert(tk.END, self.vUpesafor16)
            self.somar_un_pesa16 = float(self.vUpesa16) * int(self.Upesa16)
            self.entrada_t_uni16.delete(0, tk.END)
            self.somar_un_pesafor16 = ('{:.2f}').format(self.somar_un_pesa16).replace('.', ',')
            self.entrada_t_uni16.insert(tk.END, self.somar_un_pesafor16)

            self.entrada_v_uni17.delete(0, tk.END)
            self.vUpesafor17 = ('{:.2f}').format(float(self.vUpesa17)).replace('.', ',')
            self.entrada_v_uni17.insert(tk.END, self.vUpesafor17)
            self.somar_un_pesa17 = float(self.vUpesa17) * int(self.Upesa17)
            self.entrada_t_uni17.delete(0, tk.END)
            self.somar_un_pesafor17 = ('{:.2f}').format(self.somar_un_pesa17).replace('.', ',')
            self.entrada_t_uni17.insert(tk.END, self.somar_un_pesafor17)

            self.entrada_v_uni18.delete(0, tk.END)
            self.vUpesafor18 = ('{:.2f}').format(float(self.vUpesa18)).replace('.', ',')
            self.entrada_v_uni18.insert(tk.END, self.vUpesafor18)
            self.somar_un_pesa18 = float(self.vUpesa18) * int(self.Upesa18)
            self.entrada_t_uni18.delete(0, tk.END)
            self.somar_un_pesafor18 = ('{:.2f}').format(self.somar_un_pesa18).replace('.', ',')
            self.entrada_t_uni18.insert(tk.END, self.somar_un_pesafor18)

            self.entrada_v_uni19.delete(0, tk.END)
            self.vUpesafor19 = ('{:.2f}').format(float(self.vUpesa19)).replace('.', ',')
            self.entrada_v_uni19.insert(tk.END, self.vUpesafor19)
            self.somar_un_pesa19 = float(self.vUpesa19) * int(self.Upesa19)
            self.entrada_t_uni19.delete(0, tk.END)
            self.somar_un_pesafor19 = ('{:.2f}').format(self.somar_un_pesa19).replace('.', ',')
            self.entrada_t_uni19.insert(tk.END, self.somar_un_pesafor19)

        except:
            pass
        finally:
            os.chdir(diretorio)
        self.SOMARtudo()
    def somabuton(self):
        self.Somar_Porcentagem()
        self.aviso.destroy()
    def MesagemPorcentagem(self):
        if self.entrada_por.get() == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!ERRO NA PORCENTAGEM!!!')
            self.jMensagem.place(x=30, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessário inserir o valor da porcentagem!')
            self.j2Mensagem.place(x=35, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font1, text='!REALMENTE QUER USAR PORCENTAGEM!')
            self.jMensagem.place(x=10, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='Está ação modificara todos os dados,\n'
                                                                      'Ainda quer continuar?')
            self.j2Mensagem.place(x=50, y=50)
            self.simbotam = tk.Button(self.aviso, text='SIM', font='Ariel',
                                      command=self.somabuton)
            self.simbotam.place(x=70, y=90, width=100, height=40)
            self.naobotam = tk.Button(self.aviso, text='NÃO', font='Ariel', command=self.aviso.destroy)
            self.naobotam.place(x=220, y=90, width=100, height=40)
    def Somar_Porcentagem(self):
        try:
            self.cabesario_font = ("Arial Black", "15")
            self.Variavel_Os()
            self.somarpor = (float(self.vUpesa) * int(self.porcentagem) / 100) + float(self.vUpesa)
            self.entrada_v_uni.delete(0, tk.END)
            self.somarporfor = ('{:.2f}').format(self.somarpor).replace('.', ',')
            self.entrada_v_uni.insert(tk.END, self.somarporfor)
            self.somarp = ('{:.2f}').format(self.somarpor)
            self.somar_un_pesa = float(self.somarp) * int(self.Upesa)
            self.entrada_t_uni.delete(0, tk.END)
            self.somar_un_pesafor = ('{:.2f}').format(self.somar_un_pesa).replace('.', ',')
            self.entrada_t_uni.insert(tk.END, self.somar_un_pesafor)

            self.somarpor1 = (float(self.vUpesa1) * int(self.porcentagem) / 100) + float(self.vUpesa1)
            self.entrada_v_uni1.delete(0, tk.END)
            self.somarporfor1 = ('{:.2f}').format(self.somarpor1).replace('.', ',')
            self.entrada_v_uni1.insert(tk.END, self.somarporfor1)
            self.somarp1 = ('{:.2f}').format(self.somarpor1)
            self.somar_un_pesa1 = float(self.somarp1) * int(self.Upesa1)
            self.entrada_t_uni1.delete(0, tk.END)
            self.somar_un_pesafor1 = ('{:.2f}').format(self.somar_un_pesa1).replace('.', ',')
            self.entrada_t_uni1.insert(tk.END, self.somar_un_pesafor1)

            self.somarpor2 = (float(self.vUpesa2) * int(self.porcentagem) / 100) + float(self.vUpesa2)
            self.entrada_v_uni2.delete(0, tk.END)
            self.somarporfor2 = ('{:.2f}').format(self.somarpor2).replace('.', ',')
            self.entrada_v_uni2.insert(tk.END, self.somarporfor2)
            self.somarp2 = ('{:.2f}').format(self.somarpor2)
            self.somar_un_pesa2 = float(self.somarp2) * int(self.Upesa2)
            self.entrada_t_uni2.delete(0, tk.END)
            self.somar_un_pesafor2 = ('{:.2f}').format(self.somar_un_pesa2).replace('.', ',')
            self.entrada_t_uni2.insert(tk.END, self.somar_un_pesafor2)

            self.somarpor3 = (float(self.vUpesa3) * int(self.porcentagem) / 100) + float(self.vUpesa3)
            self.entrada_v_uni3.delete(0, tk.END)
            self.somarporfor3 = ('{:.2f}').format(self.somarpor3).replace('.', ',')
            self.entrada_v_uni3.insert(tk.END, self.somarporfor3)
            self.somarp3 = ('{:.2f}').format(self.somarpor3)
            self.somar_un_pesa3 = float(self.somarp3) * int(self.Upesa3)
            self.entrada_t_uni3.delete(0, tk.END)
            self.somar_un_pesafor3 = ('{:.2f}').format(self.somar_un_pesa3).replace('.', ',')
            self.entrada_t_uni3.insert(tk.END, self.somar_un_pesafor3)

            self.somarpor4 = (float(self.vUpesa4) * int(self.porcentagem) / 100) + float(self.vUpesa4)
            self.entrada_v_uni4.delete(0, tk.END)
            self.somarporfor4 = ('{:.2f}').format(self.somarpor4).replace('.', ',')
            self.entrada_v_uni4.insert(tk.END, self.somarporfor4)
            self.somarp4 = ('{:.2f}').format(self.somarpor4)
            self.somar_un_pesa4 = float(self.somarp4) * int(self.Upesa4)
            self.entrada_t_uni4.delete(0, tk.END)
            self.somar_un_pesafor4 = ('{:.2f}').format(self.somar_un_pesa4).replace('.', ',')
            self.entrada_t_uni4.insert(tk.END, self.somar_un_pesafor4)

            self.somarpor5 = (float(self.vUpesa5) * int(self.porcentagem) / 100) + float(self.vUpesa5)
            self.entrada_v_uni5.delete(0, tk.END)
            self.somarporfor5 = ('{:.2f}').format(self.somarpor5).replace('.', ',')
            self.entrada_v_uni5.insert(tk.END, self.somarporfor5)
            self.somarp5 = ('{:.2f}').format(self.somarpor5)
            self.somar_un_pesa5 = float(self.somarp5) * int(self.Upesa5)
            self.entrada_t_uni5.delete(0, tk.END)
            self.somar_un_pesafor5 = ('{:.2f}').format(self.somar_un_pesa5).replace('.', ',')
            self.entrada_t_uni5.insert(tk.END, self.somar_un_pesafor5)

            self.somarpor6 = (float(self.vUpesa6) * int(self.porcentagem) / 100) + float(self.vUpesa6)
            self.entrada_v_uni6.delete(0, tk.END)
            self.somarporfor6 = ('{:.2f}').format(self.somarpor6).replace('.', ',')
            self.entrada_v_uni6.insert(tk.END, self.somarporfor6)
            self.somarp6 = ('{:.2f}').format(self.somarpor6)
            self.somar_un_pesa6 = float(self.somarp6) * int(self.Upesa6)
            self.entrada_t_uni6.delete(0, tk.END)
            self.somar_un_pesafor6 = ('{:.2f}').format(self.somar_un_pesa6).replace('.', ',')
            self.entrada_t_uni6.insert(tk.END, self.somar_un_pesafor6)

            self.somarpor7 = (float(self.vUpesa7) * int(self.porcentagem) / 100) + float(self.vUpesa7)
            self.entrada_v_uni7.delete(0, tk.END)
            self.somarporfor7 = ('{:.2f}').format(self.somarpor7).replace('.', ',')
            self.entrada_v_uni7.insert(tk.END, self.somarporfor7)
            self.somar_un_pesa7 = self.somarpor7 * int(self.Upesa7)
            self.entrada_t_uni7.delete(0, tk.END)
            self.somar_un_pesafor7 = ('{:.2f}').format(self.somar_un_pesa7).replace('.', ',')
            self.entrada_t_uni7.insert(tk.END, self.somar_un_pesafor7)

            self.somarpor8 = (float(self.vUpesa8) * int(self.porcentagem) / 100) + float(self.vUpesa8)
            self.entrada_v_uni8.delete(0, tk.END)
            self.somarporfor8 = ('{:.2f}').format(self.somarpor8).replace('.', ',')
            self.entrada_v_uni8.insert(tk.END, self.somarporfor8)
            self.somarp8 = ('{:.2f}').format(self.somarpor8)
            self.somar_un_pesa8 = float(self.somarp8) * int(self.Upesa8)
            self.entrada_t_uni8.delete(0, tk.END)
            self.somar_un_pesafor8 = ('{:.2f}').format(self.somar_un_pesa8).replace('.', ',')
            self.entrada_t_uni8.insert(tk.END, self.somar_un_pesafor8)

            self.somarpor9 = (float(self.vUpesa9) * int(self.porcentagem) / 100) + float(self.vUpesa9)
            self.entrada_v_uni9.delete(0, tk.END)
            self.somarporfor9 = ('{:.2f}').format(self.somarpor9).replace('.', ',')
            self.entrada_v_uni9.insert(tk.END, self.somarporfor9)
            self.somarp9 = ('{:.2f}').format(self.somarpor9)
            self.somar_un_pesa9 = float(self.somarp9) * int(self.Upesa9)
            self.entrada_t_uni9.delete(0, tk.END)
            self.somar_un_pesafor9 = ('{:.2f}').format(self.somar_un_pesa9).replace('.', ',')
            self.entrada_t_uni9.insert(tk.END, self.somar_un_pesafor9)

            self.somarpor10 = (float(self.vUpesa10) * int(self.porcentagem) / 100) + float(self.vUpesa10)
            self.entrada_v_uni10.delete(0, tk.END)
            self.somarporfor10 = ('{:.2f}').format(self.somarpor10).replace('.', ',')
            self.entrada_v_uni10.insert(tk.END, self.somarporfor10)
            self.somarp10 = ('{:.2f}').format(self.somarpor10)
            self.somar_un_pesa10 = float(self.somarp10) * int(self.Upesa10)
            self.entrada_t_uni10.delete(0, tk.END)
            self.somar_un_pesafor10 = ('{:.2f}').format(self.somar_un_pesa10).replace('.', ',')
            self.entrada_t_uni10.insert(tk.END, self.somar_un_pesafor10)

            self.somarpor11 = (float(self.vUpesa11) * int(self.porcentagem) / 100) + float(self.vUpesa11)
            self.entrada_v_uni11.delete(0, tk.END)
            self.somarporfor11 = ('{:.2f}').format(self.somarpor11).replace('.', ',')
            self.entrada_v_uni11.insert(tk.END, self.somarporfor11)
            self.somarp11 = ('{:.2f}').format(self.somarpor11)
            self.somar_un_pesa11 = float(self.somarp11) * int(self.Upesa11)
            self.entrada_t_uni11.delete(0, tk.END)
            self.somar_un_pesafor11 = ('{:.2f}').format(self.somar_un_pesa11).replace('.', ',')
            self.entrada_t_uni11.insert(tk.END, self.somar_un_pesafor11)

            self.somarpor12 = (float(self.vUpesa12) * int(self.porcentagem) / 100) + float(self.vUpesa12)
            self.entrada_v_uni12.delete(0, tk.END)
            self.somarporfor12 = ('{:.2f}').format(self.somarpor12).replace('.', ',')
            self.entrada_v_uni12.insert(tk.END, self.somarporfor12)
            self.somarp12 = ('{:.2f}').format(self.somarpor12)
            self.somar_un_pesa12 = float(self.somarp12) * int(self.Upesa12)
            self.entrada_t_uni12.delete(0, tk.END)
            self.somar_un_pesafor12 = ('{:.2f}').format(self.somar_un_pesa12).replace('.', ',')
            self.entrada_t_uni12.insert(tk.END, self.somar_un_pesafor12)

            self.somarpor13 = (float(self.vUpesa13) * int(self.porcentagem) / 100) + float(self.vUpesa13)
            self.entrada_v_uni13.delete(0, tk.END)
            self.somarporfor13 = ('{:.2f}').format(self.somarpor13).replace('.', ',')
            self.entrada_v_uni13.insert(tk.END, self.somarporfor13)
            self.somarp13 = ('{:.2f}').format(self.somarpor13)
            self.somar_un_pesa13 = float(self.somarp13) * int(self.Upesa13)
            self.entrada_t_uni13.delete(0, tk.END)
            self.somar_un_pesafor13 = ('{:.2f}').format(self.somar_un_pesa13).replace('.', ',')
            self.entrada_t_uni13.insert(tk.END, self.somar_un_pesafor13)

            self.somarpor14 = (float(self.vUpesa14) * int(self.porcentagem) / 100) + float(self.vUpesa14)
            self.entrada_v_uni14.delete(0, tk.END)
            self.somarporfor14 = ('{:.2f}').format(self.somarpor14).replace('.', ',')
            self.entrada_v_uni14.insert(tk.END, self.somarporfor14)
            self.somarp14 = ('{:.2f}').format(self.somarpor14)
            self.somar_un_pesa14 = float(self.somarp14) * int(self.Upesa14)
            self.entrada_t_uni14.delete(0, tk.END)
            self.somar_un_pesafor14 = ('{:.2f}').format(self.somar_un_pesa14).replace('.', ',')
            self.entrada_t_uni14.insert(tk.END, self.somar_un_pesafor14)

            self.somarpor15 = (float(self.vUpesa15) * int(self.porcentagem) / 100) + float(self.vUpesa15)
            self.entrada_v_uni15.delete(0, tk.END)
            self.somarporfor15 = ('{:.2f}').format(self.somarpor15).replace('.', ',')
            self.entrada_v_uni15.insert(tk.END, self.somarporfor15)
            self.somarp15 = ('{:.2f}').format(self.somarpor15)
            self.somar_un_pesa15 = float(self.somarp15) * int(self.Upesa15)
            self.entrada_t_uni15.delete(0, tk.END)
            self.somar_un_pesafor15 = ('{:.2f}').format(self.somar_un_pesa15).replace('.', ',')
            self.entrada_t_uni15.insert(tk.END, self.somar_un_pesafor15)

            self.somarpor16 = (float(self.vUpesa16) * int(self.porcentagem) / 100) + float(self.vUpesa16)
            self.entrada_v_uni16.delete(0, tk.END)
            self.somarporfor16 = ('{:.2f}').format(self.somarpor16).replace('.', ',')
            self.entrada_v_uni16.insert(tk.END, self.somarporfor16)
            self.somarp16 = ('{:.2f}').format(self.somarpor16)
            self.somar_un_pesa16 = float(self.somarp16) * int(self.Upesa16)
            self.entrada_t_uni16.delete(0, tk.END)
            self.somar_un_pesafor16 = ('{:.2f}').format(self.somar_un_pesa16).replace('.', ',')
            self.entrada_t_uni16.insert(tk.END, self.somar_un_pesafor16)

            self.somarpor17 = (float(self.vUpesa17) * int(self.porcentagem) / 100) + float(self.vUpesa17)
            self.entrada_v_uni17.delete(0, tk.END)
            self.somarporfor17 = ('{:.2f}').format(self.somarpor17).replace('.', ',')
            self.entrada_v_uni17.insert(tk.END, self.somarporfor17)
            self.somarp17 = ('{:.2f}').format(self.somarpor17)
            self.somar_un_pesa17 = float(self.somarp17) * int(self.Upesa17)
            self.entrada_t_uni17.delete(0, tk.END)
            self.somar_un_pesafor17 = ('{:.2f}').format(self.somar_un_pesa17).replace('.', ',')
            self.entrada_t_uni17.insert(tk.END, self.somar_un_pesafor17)

            self.somarpor18 = (float(self.vUpesa18) * int(self.porcentagem) / 100) + float(self.vUpesa18)
            self.entrada_v_uni18.delete(0, tk.END)
            self.somarporfor18 = ('{:.2f}').format(self.somarpor18).replace('.', ',')
            self.entrada_v_uni18.insert(tk.END, self.somarporfor18)
            self.somarp18 = ('{:.2f}').format(self.somarpor18)
            self.somar_un_pesa18 = float(self.somarp18) * int(self.Upesa18)
            self.entrada_t_uni18.delete(0, tk.END)
            self.somar_un_pesafor18 = ('{:.2f}').format(self.somar_un_pesa18).replace('.', ',')
            self.entrada_t_uni18.insert(tk.END, self.somar_un_pesafor18)

            self.somarpor19 = (float(self.vUpesa19) * int(self.porcentagem) / 100) + float(self.vUpesa19)
            self.entrada_v_uni19.delete(0, tk.END)
            self.somarporfor19 = ('{:.2f}').format(self.somarpor19).replace('.', ',')
            self.entrada_v_uni19.insert(tk.END, self.somarporfor19)
            self.somarp19 = ('{:.2f}').format(self.somarpor19)
            self.somar_un_pesa19 = float(self.somarp19) * int(self.Upesa19)
            self.entrada_t_uni19.delete(0, tk.END)
            self.somar_un_pesafor19 = ('{:.2f}').format(self.somar_un_pesa19).replace('.', ',')
            self.entrada_t_uni19.insert(tk.END, self.somar_un_pesafor19)
        except:
            pass
        finally:
            self.SOMARtudo()
            self.Somar()
    def SOMARtudo(self):
        self.Variavel_Os()

        TotalPlist=[self.tVpesa,self.tVpesa1, self.tVpesa2,self.tVpesa3,self.tVpesa4,self.tVpesa5,self.tVpesa6,
                    self.tVpesa7,self.tVpesa8,self.tVpesa9,self.tVpesa10,self.tVpesa11,self.tVpesa12,self.tVpesa13,
                    self.tVpesa14,self.tVpesa15,self.tVpesa16,self.tVpesa17,self.tVpesa18,self.tVpesa19]
        listPtotal = []
        for i, a in enumerate(TotalPlist):
            if a == '':
                v = a.replace('','0')
                listPtotal.append(float(v))
            else:
                listPtotal.append(float(a))

        TotalPlista = sum(listPtotal)
        self.PesasTotal.delete(0, tk.END)
        self.TPlista = ('{:.2f}').format(TotalPlista).replace('.', ',')
        self.PesasTotal.insert(tk.END,self.TPlista)
        try:
            self.Retifica.delete(0, tk.END)
            self.retifi = ('{:.2f}').format(float(self.retifica)).replace('.', ',')
            self.Retifica.insert(tk.END, self.retifi)
        except:
            pass
        try:
            self.M_O.delete(0, tk.END)
            self.m_O = ('{:.2f}').format(float(self.mo)).replace('.', ',')
            self.M_O.insert(tk.END, self.m_O)
        except:
            pass
        Mo_Retifica = [self.retifica,self.mo,TotalPlista]
        Retifica_Mo = []
        for x,w in enumerate(Mo_Retifica):
            if w == '':
                y = w.replace('','0')
                Retifica_Mo.append(float(y))
            elif w == ' ':
                c = w.replace(' ', '0')
                Retifica_Mo.append(float(c))
            else:
                Retifica_Mo.append(float(w))
        TOTAIS = sum(Retifica_Mo)
        self.TotalTotal.delete(0, tk.END)
        self.TOTAISFOR = ('{:.2f}').format(TOTAIS).replace('.', ',')
        self.TotalTotal.insert(tk.END,self.TOTAISFOR)
    def VarCarro(self,event):
        self.LimparOsCarro()
        self.lista_c_clirCarro.selection()
        for n in self.lista_c_clirCarro.selection():
            col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11 = self.lista_c_clirCarro.item(n, 'values')
            self.entraCarro.insert(tk.END,col1)
            self.entra1Carro.insert(tk.END,col2)
            self.entra2Carro.insert(tk.END, col3)
            self.entra3Carro.insert(tk.END, col4)
            self.entra4Carro.insert(tk.END, col5)
            self.entra5Carro.insert(tk.END, col6)
            self.entra6Carro.insert(tk.END, col7)
            self.entra7Carro.insert(tk.END, col8)
            self.entra8Carro.insert(tk.END, col9)
        self.lista_c_clirCarro.selection()
        self.cr_janela.destroy()
    def AddCarroPedido(self):
        self.InicioJanela()
        self.SelesaoCarro()

        self.criarCarro = tk.Button(self.cr_janela,text="Buscar", font=self.fonte_buton, bg="black",
                                foreground="white",command=self.Buscar_Carro)
        self.criarCarro.place(x=20, y=430, width=150, height=40)
        self.escrita1 = tk.Label(self.cr_janela,text='Marca do Carro',font=self.fonte_titlo)
        self.escrita1.place(x=20,y=480)
        self.entrada2Carro = tk.Entry(self.cr_janela,font=self.fonte_entra)
        self.entrada2Carro.place(x=20,y=500,width=250)
        self.AtualizeLista_Carro()
        self.lista_c_clirCarro.bind("<Double-1>",self.VarCarro)
    def FusaoWrd(self):
        self.Variavel_Os()
        self.ListaP = []
        PL = [self.pasa,self.Upesa,self.vUpesa.replace('.', ','),self.tVpesa.replace('.', ',')]
        PL1 = [self.pasa1,self.Upesa1,self.vUpesa1.replace('.', ','),self.tVpesa1.replace('.', ',')]
        PL2 = [self.pasa2,self.Upesa2,self.vUpesa2.replace('.', ','),self.tVpesa2.replace('.', ',')]
        PL3 = [self.pasa3,self.Upesa3,self.vUpesa3.replace('.', ','),self.tVpesa3.replace('.', ',')]
        PL4 = [self.pasa4,self.Upesa4,self.vUpesa4.replace('.', ','),self.tVpesa4.replace('.', ',')]
        PL5 = [self.pasa5,self.Upesa5,self.vUpesa5.replace('.', ','),self.tVpesa5.replace('.', ',')]
        PL6 = [self.pasa6,self.Upesa6,self.vUpesa6.replace('.', ','),self.tVpesa6.replace('.', ',')]
        PL7 = [self.pasa7,self.Upesa7,self.vUpesa7.replace('.', ','),self.tVpesa7.replace('.', ',')]
        PL8 = [self.pasa8,self.Upesa8,self.vUpesa8.replace('.', ','),self.tVpesa8.replace('.', ',')]
        PL9 = [self.pasa9,self.Upesa9,self.vUpesa9.replace('.', ','),self.tVpesa9.replace('.', ',')]
        PL10 = [self.pasa10,self.Upesa10,self.vUpesa10.replace('.', ','),self.tVpesa10.replace('.', ',')]
        PL11 = [self.pasa11,self.Upesa11,self.vUpesa11.replace('.', ','),self.tVpesa11.replace('.', ',')]
        PL12 = [self.pasa12,self.Upesa12,self.vUpesa12.replace('.', ','),self.tVpesa12.replace('.', ',')]
        PL13 = [self.pasa13,self.Upesa13,self.vUpesa13.replace('.', ','),self.tVpesa13.replace('.', ',')]
        PL14 = [self.pasa14,self.Upesa14,self.vUpesa14.replace('.', ','),self.tVpesa14.replace('.', ',')]
        PL15 = [self.pasa15,self.Upesa15,self.vUpesa15.replace('.', ','),self.tVpesa15.replace('.', ',')]
        PL16 = [self.pasa16,self.Upesa16,self.vUpesa16.replace('.', ','),self.tVpesa16.replace('.', ',')]
        PL17 = [self.pasa17,self.Upesa17,self.vUpesa17.replace('.', ','),self.tVpesa17.replace('.', ',')]
        PL18 = [self.pasa18,self.Upesa18,self.vUpesa18.replace('.', ','),self.tVpesa18.replace('.', ',')]
        PL19 = [self.pasa19,self.Upesa19,self.vUpesa19.replace('.', ','),self.tVpesa19.replace('.', ',')]


        while True:
            if PL[0] == '':
                break
            elif PL[1] == '':
                break
            elif PL[2] == '':
                break
            elif PL[3] == '':
                break
            else:
                self.ListaP.append(PL)
                break
        while True:
            if PL1[0] == '':
                break
            elif PL1[1] == '':
                break
            elif PL1[2] == '':
                break
            elif PL1[3] == '':
                break
            else:
                self.ListaP.append(PL1)
                break
        while True:
            if PL2[0] == '':
                break
            elif PL2[1] == '':
                break
            elif PL2[2] == '':
                break
            elif PL2[3] == '':
                break
            else:
                self.ListaP.append(PL2)
                break
        while True:
            if PL3[0] == '':
                break
            elif PL3[1] == '':
                break
            elif PL3[2] == '':
                break
            elif PL3[3] == '':
                break
            else:
                self.ListaP.append(PL3)
                break
        while True:
            if PL4[0] == '':
                break
            elif PL4[1] == '':
                break
            elif PL4[2] == '':
                break
            elif PL4[3] == '':
                break
            else:
                self.ListaP.append(PL4)
                break
        while True:
            if PL5[0] == '':
                break
            elif PL5[1] == '':
                break
            elif PL5[2] == '':
                break
            elif PL5[3] == '':
                break
            else:
                self.ListaP.append(PL5)
                break
        while True:
            if PL6[0] == '':
                break
            elif PL6[1] == '':
                break
            elif PL6[2] == '':
                break
            elif PL6[3] == '':
                break
            else:
                self.ListaP.append(PL6)
                break
        while True:
            if PL7[0] == '':
                break
            elif PL7[1] == '':
                break
            elif PL7[2] == '':
                break
            elif PL7[3] == '':
                break
            else:
                self.ListaP.append(PL7)
                break
        while True:
            if PL8[0] == '':
                break
            elif PL8[1] == '':
                break
            elif PL8[2] == '':
                break
            elif PL8[3] == '':
                break
            else:
                self.ListaP.append(PL8)
                break
        while True:
            if PL9[0] == '':
                break
            elif PL9[1] == '':
                break
            elif PL9[2] == '':
                break
            elif PL9[3] == '':
                break
            else:
                self.ListaP.append(PL9)
                break
        while True:
            if PL10[0] == '':
                break
            elif PL10[1] == '':
                break
            elif PL10[2] == '':
                break
            elif PL10[3] == '':
                break
            else:
                self.ListaP.append(PL10)
                break
        while True:
            if PL11[0] == '':
                break
            elif PL11[1] == '':
                break
            elif PL11[2] == '':
                break
            elif PL11[3] == '':
                break
            else:
                self.ListaP.append(PL11)
                break
        while True:
            if PL12[0] == '':
                break
            elif PL12[1] == '':
                break
            elif PL12[2] == '':
                break
            elif PL12[3] == '':
                break
            else:
                self.ListaP.append(PL12)
                break

        while True:
            if PL13[0] == '':
                break
            elif PL13[1] == '':
                break
            elif PL13[2] == '':
                break
            elif PL13[3] == '':
                break
            else:
                self.ListaP.append(PL13)
                break

        while True:
            if PL14[0] == '':
                break
            elif PL14[1] == '':
                break
            elif PL14[2] == '':
                break
            elif PL14[3] == '':
                break
            else:
                self.ListaP.append(PL14)
                break

        while True:
            if PL15[0] == '':
                break
            elif PL15[1] == '':
                break
            elif PL15[2] == '':
                break
            elif PL15[3] == '':
                break
            else:
                self.ListaP.append(PL15)
                break

        while True:
            if PL16[0] == '':
                break
            elif PL16[1] == '':
                break
            elif PL16[2] == '':
                break
            elif PL16[3] == '':
                break
            else:
                self.ListaP.append(PL16)
                break

        while True:
            if PL17[0] == '':
                break
            elif PL17[1] == '':
                break
            elif PL17[2] == '':
                break
            elif PL17[3] == '':
                break
            else:
                self.ListaP.append(PL17)
                break

        while True:
            if PL18[0] == '':
                break
            elif PL18[1] == '':
                break
            elif PL18[2] == '':
                break
            elif PL18[3] == '':
                break
            else:
                self.ListaP.append(PL18)
                break

        while True:
            if PL19[0] == '':
                break
            elif PL19[1] == '':
                break
            elif PL19[2] == '':
                break
            elif PL19[3] == '':
                break
            else:
                self.ListaP.append(PL19)
                break
    def abrir_arquivo_whats(self):
        self.Variavel_Os()
        os.chdir(diretorio)
        self.pasta_W_s()
        self.FusaoWrd()
        self.telefone = str(self.DadosOsCarro1)
        max = self.telefone[:10]
        mix = self.telefone[11:].replace('', 'A')
        if self.DadosOsCarro == '':
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
            hd = f'{self.codigo_os:<}\n{self.data2.replace("-", "/"):<}'
            h1 = f'{"MAICÁ":^22}\n{"MANUTEÇAO":^22}\n{"AUTOMOTIVA":^22}'
            h2 = ('=' * 22)
            h3 = (f'{"NOME:" + self.DadosOsCarro:<}\n{"TELEFONE:" + self.DadosOsCarro1:<}\n'
                  f'{"MARCA:" + self.DadosOsCarro3:<}\n{"MODELO:" + self.DadosOsCarro4:<}\n'
                  f'{"ANO:" + self.DadosOsCarro5:<}\n'
                  f'{"MOTOR:" + self.DadosOsCarro6:<}\n{"PLACA:" + self.DadosOsCarro2:<}\n'
                  f'{"KM:" + self.DadosOsCarro7:<}')
            h4 = ('_' * 22)
            h5 = f'{"NOME DA PEÇA":<} \n{"UNI":<} |{"PEÇA UNI":<} |{"TOTAL":<}'
            h6 = ('_' * 22)
            h7 = ' '
            HR = f'{"RETIFICA":<} | {"R$" + self.retifica:<}'.replace('.', ',')
            h8 = f'{"PEÇAS":<} | {"R$" + self.pesas_total:<}'.replace('.', ',')
            h9 = f'{"M O":<} | {"R$" + self.mo:<}'.replace('.', ',')
            h10 = ('_' * 22)
            h11 = f'{"TOTAL":<} | {"R$" + self.totaltotal:<}'.replace('.', ',')

            with open('Arquivo.txt', 'w+') as arquivo:
                for teste in hd, h1, h2, h3, h4, h5, h6:
                    arquivo.write(teste + '\n')
                for i, a in enumerate(self.ListaP):
                    f'{a[1]:<}|{a[0]:<}\n{"R$" + a[2]:<}|{"R$" + a[3]:<}'
                    arquivo.write(str(f'{a[0]:<}\n{a[1]:<} |{"R$" + a[2]:<} |{"R$" + a[3]:<12}') + '\n')
                for teste2 in h7, HR, h8, h9, h10, h11:
                    arquivo.write(teste2 + '\n')

            BuscaArquivo = open('Arquivo.txt', 'r')
            Arquivo = BuscaArquivo.read()

            texto = urllib.parse.quote(f'{Arquivo}')
            link = f"https://wa.me/55{self.DadosOsCarro1}?text={texto}"
            webbrowser.open(link)

            BuscaArquivo.close()
            os.chdir(diretorio)
    def abrir_arquivo_imprimir(self):
        try:
            self.Variavel_Os()
            self.pasta_nota()
            self.FusaoWrd()
            hd = f'{self.codigo_os:<}\n{self.data2.replace("-", "/"):<}'
            h1 = f'{"MAICÁ":^22}\n{"MANUTEÇAO":^22}\n{"AUTOMOTIVA":^22}'
            h2 = ('=' * 22)
            h3 = (f'{"NOME:" + self.DadosOsCarro:<}\n{"TELEFONE:" + self.DadosOsCarro1:<}\n'
                  f'{"MARCA:" + self.DadosOsCarro3:<}\n{"MODELO:" + self.DadosOsCarro4:<}\n'
                  f'{"ANO:" + self.DadosOsCarro5:<}\n'
                  f'{"MOTOR:" + self.DadosOsCarro6:<}\n{"PLACA:" + self.DadosOsCarro2:<}\n'
                  f'{"KM:" + self.DadosOsCarro7:<}')
            h4 = ('_' * 22)
            h5 = f'{"NOME DA PEÇA":<} \n{"UNI":<} |{"PEÇA UNI":<} |{"TOTAL":<}'
            h6 = ('_' * 22)
            h7 = ' '
            HR = f'{"RETIFICA":<} | {"R$" + self.retifica:<}'.replace('.', ',')
            h8 = f'{"PEÇAS":<} | {"R$" + self.pesas_total:<}'.replace('.', ',')
            h9 = f'{"M O":<} | {"R$" + self.mo:<}'.replace('.', ',')
            h10 = ('_' * 22)
            h11 = f'{"TOTAL":<} | {"R$" + self.totaltotal:<}'.replace('.', ',')
            h12 = ' '
            h13 = f'{"CUPOM NÃO FISCAL":^22}'

            with open('Arquivo.txt', 'w+') as arquivo:
                for teste in hd, h1, h2, h3, h4, h5, h6:
                    arquivo.write(teste + '\n')
                for i, a in enumerate(self.ListaP):
                    f'{a[1]:<}|{a[0]:<}\n{"R$" + a[2]:<}|{"R$" + a[3]:<}'
                    arquivo.write(str(f'{a[0]:<}\n{a[1]:<} |{"R$" + a[2]:<} |{"R$" + a[3]:<12}') + '\n')
                for teste2 in h7, HR, h8, h9, h10, h11, h12, h13:
                    arquivo.write(teste2 + '\n')

            os.startfile('Arquivo.txt')

            os.chdir(diretorio)
        except:
            self.Mensagenscaixa()
            self.cabesario_fo = ("Arial Black", "10")
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_fo, text='!!!ERRO!!!')
            self.jMensagem.place(x=150, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='ARQUIVO NÃO ENCONTRADO.')
            self.j2Mensagem.place(x=70, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        finally:
            os.chdir(diretorio)
    def AbrirWhats(self):
        self.Variavel_Os()
        self.telefone = str(self.DadosOsCarro1)
        max = self.telefone[:10]
        mix = self.telefone[11:].replace('', 'A')
        if self.telefone <= max:
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
            link = f"https://wa.me/55{self.DadosOsCarro1}"
            webbrowser.open(link)

    # def abrir_arquivo_whats(self):
    #     self.Variavel_Os()
    #     os.chdir(diretorio)
    #     self.pasta_W_s()
    #     self.FusaoWrd()
    #     hd = f'{self.codigo_os:<32}{self.data2.replace("-", "/"):>26}'
    #     h1 = f'{"MAICÁ MANUTEÇAO AUTOMOTIVA":^59}'
    #     h2 = ('=' * 59)
    #     h3 = (f'{"NOME: " + self.DadosOsCarro:<35}\t{"TELEFONE: " + self.DadosOsCarro1:<22}\n'
    #           f'{"MARCA: " + self.DadosOsCarro3:<19}\t{"MODELO: " + self.DadosOsCarro4:<19}\t'
    #           f'{"ANO: " + self.DadosOsCarro5:<10}\n'
    #           f'{"MOTOR: " + self.DadosOsCarro6:<19}\t{"PLACA: " + self.DadosOsCarro2:<19}\t'
    #           f'{"KM: " + self.DadosOsCarro7:<10}')
    #     h4 = ('_' * 59)
    #     h5 = f'{"PEÇAS":<30}\t{"UNI":>3}\t{"PEÇAS UNI":>10}\t{"TOTAL PEÇAS":>10}'
    #     h6 = ('_' * 59)
    #     h7 = ' '
    #     HR = f'{"RETIFICA":<30}\t{"R$" + self.retifica:>26}'
    #     h9 = f'{"M.O":<30}\t{"R$" + self.mo:>26}'
    #     h8 = f'{"TOTAL PEÇAS":<30}\t{"R$" + self.pesas_total:>26}'
    #     h10 = ('_' * 59)
    #     h11 = f'{"TOTAL":<30}\t{"R$" + self.totaltotal:>26}'
    #     with open('Arquivo.txt', 'w+') as arquivo:
    #         for teste in hd, h1, h2, h3, h4, h5, h6:
    #             arquivo.write(teste + '\n')
    #         for i, a in enumerate(self.ListaP):
    #             f'{a[0]:<30}\t{a[1]:>3}\t{"R$" + a[2]:>10}\t{"R$" + a[3]:>10}'
    #             arquivo.write(str(f'{a[0]:<30}\t{a[1]:>3}\t{"R$" + a[2]:>10}\t{"R$" + a[3]:>10}') + '\n')
    #         for teste2 in h7, HR, h8, h9, h10, h11:
    #             arquivo.write(teste2 + '\n')
    #
    #
    #     os.startfile('Arquivo.txt')
    #
    #     os.chdir(diretorio)

    def InicioJanela(self):
        pass
    def SelesaoCarro(self):
        pass


class Funcs_Pendentes(Funcs_os):
    def __init__(self):
        super().__init__()
        self.x = None
        self.os_janela = None
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
    def AtualizeLista_Pendentes(self):
        self.lista_c_clirPendentes.delete(*self.lista_c_clirPendentes.get_children())
        self.ConequitarBancoPendentes()
        lista_Carro = self.c.execute("""SELECT numero_pedido,cliente,telefone,placa,numero_cliente,retifica,
        M_O,total_peças,total_OS,data FROM dados_serviços ORDER BY data DESC;""")
        for i in lista_Carro:
            if i[9] != '00000000':
                self.lista_c_clirPendentes.insert("", tk.END,
                                                  values=(i[0], i[1], i[2], i[3], i[4], 'R$ ' + i[5].replace('.', ',')
                                                          , 'R$ ' + i[6].replace('.', ','),
                                                          'R$ ' + i[7].replace('.', ','),
                                                          'R$ ' + i[8].replace('.', ','), i[9]))
        self.DesconequitarBancoPendetes()
    def BuscarTelefonePendentes(self):
        self.telefone = self.entrada1.get()
        self.lista_c_clirPendentes.delete(*self.lista_c_clirPendentes.get_children())
        self.ConequitarBancoPendentes()
        self.c.execute("""SELECT numero_pedido,cliente,telefone,placa,numero_cliente,retifica,
        M_O,total_peças,total_OS,data FROM dados_serviços ORDER BY data ASC;""")
        DadosCarro = self.c.execute(f'SELECT numero_pedido,cliente,telefone,placa,numero_cliente,retifica,M_O,'
                                    f'total_peças,total_OS,data FROM dados_serviços WHERE telefone LIKE '
                                    f'"%{self.telefone.strip().replace(" ", "").replace("-", "")}%"'
                                    f'ORDER BY data DESC;')

        for i in DadosCarro:
            if i[9] != '00000000':
                self.lista_c_clirPendentes.insert("", tk.END,
                                                  values=(i[0], i[1], i[2], i[3], i[4], 'R$ ' + i[5].replace('.', ',')
                                                          , 'R$ ' + i[6].replace('.', ','),
                                                          'R$ ' + i[7].replace('.', ','),
                                                          'R$ ' + i[8].replace('.', ','), i[9]))
        self.DesconequitarBancoPendetes()
    def BuscarCodigoPendentes(self):
        self.codigo = self.entrada2.get()
        self.lista_c_clirPendentes.delete(*self.lista_c_clirPendentes.get_children())
        self.ConequitarBancoPendentes()
        self.c.execute("""SELECT numero_pedido,cliente,telefone,placa,numero_cliente,retifica,
        M_O,total_peças,total_OS,data FROM dados_serviços ORDER BY data ASC;""")
        DadosCarro = self.c.execute(f'SELECT numero_pedido,cliente,telefone,placa,numero_cliente,retifica,M_O,'
                                    f'total_peças,total_OS,data FROM dados_serviços WHERE numero_cliente LIKE '
                                    f'"%{self.codigo.strip().replace(" ", "").replace("-", "")}%"'
                                    f'ORDER BY data DESC;')

        for i in DadosCarro:
            if i[9] != '00000000':
                self.lista_c_clirPendentes.insert("", tk.END,
                                                  values=(i[0], i[1], i[2], i[3], i[4], 'R$ ' + i[5].replace('.', ',')
                                                          , 'R$ ' + i[6].replace('.', ','),
                                                          'R$ ' + i[7].replace('.', ','),
                                                          'R$ ' + i[8].replace('.', ','), i[9]))
        self.DesconequitarBancoPendetes()
    def BuscarPlacaPendetes(self):
        self.placa = self.entrada3.get()
        self.lista_c_clirPendentes.delete(*self.lista_c_clirPendentes.get_children())
        self.ConequitarBancoPendentes()
        self.c.execute("""SELECT numero_pedido,cliente,telefone,placa,numero_cliente,retifica,
        M_O,total_peças,total_OS,data FROM dados_serviços ORDER BY data ASC;""")
        DadosCarro = self.c.execute(f'SELECT numero_pedido,cliente,telefone,placa,numero_cliente,retifica,M_O,'
                                    f'total_peças,total_OS,data FROM dados_serviços WHERE placa LIKE '
                                    f'"%{self.placa.strip().upper().replace(" ", "").replace("-", "")}%"'
                                    f'ORDER BY data DESC;')

        for i in DadosCarro:
            if i[9] != '00000000':
                self.lista_c_clirPendentes.insert("", tk.END,
                                                  values=(i[0], i[1], i[2], i[3], i[4], 'R$ ' + i[5].replace('.', ',')
                                                          , 'R$ ' + i[6].replace('.', ','),
                                                          'R$ ' + i[7].replace('.', ','),
                                                          'R$ ' + i[8].replace('.', ','), i[9]))
        self.DesconequitarBancoPendetes()
    def AbrirPendentes(self,event):
        self.OsJanela()
        self.ConequitarBancoPendentes()
        self.lista_c_clirPendentes.selection()
        for n in self.lista_c_clirPendentes.selection():
            col1,col2,col3,col4,col5,col6,col7,col8,col9,col10= self.lista_c_clirPendentes.item(n, 'values')
            Dados = self.c.execute(f'SELECT numero_pedido,cliente,telefone,numero_cliente,placa,marca,modelo,ano,'
                                   f'motor,km,peças1,uni1,valor_peças1,peças2,uni2,valor_peças2,peças3,uni3,'
                                   f'valor_peças3,peças4,uni4,valor_peças4,peças5,uni5,valor_peças5,peças6,'
                                   f'uni6,valor_peças6,peças7,uni7,valor_peças7,peças8,uni8,valor_peças8,peças9,'
                                   f'uni9,valor_peças9,peças10,uni10,valor_peças10,peças11,uni11,valor_peças11,'
                                   f'peças12,uni12,valor_peças12,peças13,uni13,valor_peças13,peças14,uni14,'
                                   f'valor_peças14,peças15,uni15,valor_peças15,peças16,uni16,valor_peças16,'
                                   f'peças17,uni17,valor_peças17,peças18,uni18,valor_peças18,peças19,uni19,'
                                   f'valor_peças19,peças20,uni20,valor_peças20,retifica,M_O,total_peças,total_OS,'
                                   f'oid FROM dados_serviços WHERE numero_pedido = {col1}')
            for i in Dados:
                self.entrada_codigo.insert(tk.END,i[0])
                self.entraCarro.insert(tk.END,i[1])
                self.entra1Carro.insert(tk.END,i[2])
                self.entra2Carro.insert(tk.END,i[4])
                self.entra3Carro.insert(tk.END,i[5])
                self.entra4Carro.insert(tk.END,i[6])
                self.entra5Carro.insert(tk.END,i[7])
                self.entra6Carro.insert(tk.END,i[8])
                self.entra7Carro.insert(tk.END,i[9])
                self.entra8Carro.insert(tk.END,i[3])

                self.entrada_pesas.insert(tk.END,i[10])
                self.entrada_uni.insert(tk.END,i[11])
                self.entrada_v_uni.insert(tk.END,i[12])

                self.entrada_pesas1.insert(tk.END,i[13])
                self.entrada_uni1.insert(tk.END,i[14])
                self.entrada_v_uni1.insert(tk.END,i[15])

                self.entrada_pesas2.insert(tk.END,i[16])
                self.entrada_uni2.insert(tk.END,i[17])
                self.entrada_v_uni2.insert(tk.END,i[18])

                self.entrada_pesas3.insert(tk.END,i[19])
                self.entrada_uni3.insert(tk.END,i[20])
                self.entrada_v_uni3.insert(tk.END,i[21])

                self.entrada_pesas4.insert(tk.END,i[22])
                self.entrada_uni4.insert(tk.END,i[23])
                self.entrada_v_uni4.insert(tk.END,i[24])

                self.entrada_pesas5.insert(tk.END,i[25])
                self.entrada_uni5.insert(tk.END,i[26])
                self.entrada_v_uni5.insert(tk.END,i[27])

                self.entrada_pesas6.insert(tk.END,i[28])
                self.entrada_uni6.insert(tk.END,i[29])
                self.entrada_v_uni6.insert(tk.END,i[30])

                self.entrada_pesas7.insert(tk.END,i[31])
                self.entrada_uni7.insert(tk.END,i[32])
                self.entrada_v_uni7.insert(tk.END,i[33])

                self.entrada_pesas8.insert(tk.END,i[34])
                self.entrada_uni8.insert(tk.END,i[35])
                self.entrada_v_uni8.insert(tk.END,i[36])

                self.entrada_pesas9.insert(tk.END,i[37])
                self.entrada_uni9.insert(tk.END,i[38])
                self.entrada_v_uni9.insert(tk.END,i[39])

                self.entrada_pesas10.insert(tk.END,i[40])
                self.entrada_uni10.insert(tk.END,i[41])
                self.entrada_v_uni10.insert(tk.END,i[42])

                self.entrada_pesas11.insert(tk.END,i[43])
                self.entrada_uni11.insert(tk.END,i[44])
                self.entrada_v_uni11.insert(tk.END,i[45])

                self.entrada_pesas12.insert(tk.END,i[46])
                self.entrada_uni12.insert(tk.END,i[47])
                self.entrada_v_uni12.insert(tk.END,i[48])

                self.entrada_pesas13.insert(tk.END,i[49])
                self.entrada_uni13.insert(tk.END,i[50])
                self.entrada_v_uni13.insert(tk.END,i[51])

                self.entrada_pesas14.insert(tk.END,i[52])
                self.entrada_uni14.insert(tk.END,i[53])
                self.entrada_v_uni14.insert(tk.END,i[54])

                self.entrada_pesas15.insert(tk.END,i[55])
                self.entrada_uni15.insert(tk.END,i[56])
                self.entrada_v_uni15.insert(tk.END,i[57])

                self.entrada_pesas16.insert(tk.END,i[58])
                self.entrada_uni16.insert(tk.END,i[59])
                self.entrada_v_uni16.insert(tk.END,i[60])

                self.entrada_pesas17.insert(tk.END,i[61])
                self.entrada_uni17.insert(tk.END,i[62])
                self.entrada_v_uni17.insert(tk.END,i[63])

                self.entrada_pesas18.insert(tk.END,i[64])
                self.entrada_uni18.insert(tk.END,i[65])
                self.entrada_v_uni18.insert(tk.END,i[66])

                self.entrada_pesas19.insert(tk.END,i[67])
                self.entrada_uni19.insert(tk.END,i[68])
                self.entrada_v_uni19.insert(tk.END,i[69])

                self.Retifica.insert(tk.END,i[70])
                self.M_O.insert(tk.END,i[71])
                self.PesasTotal.insert(tk.END,i[72])
                self.TotalTotal.insert(tk.END,i[73])

        self.DesconequitarBancoPendetes()
        self.cr_janela.destroy()
        self.Somar()
    def CriarOS_Pendende(self):
        self.somar()
        self.Variavel_Os()
        if self.DadosOsCarro == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!ERRO NOME!!!')
            self.jMensagem.place(x=100, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o nome do cliente!')
            self.j2Mensagem.place(x=60, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.DataModificada()
            self.ConequitarBancoPendentes()
            self.c.execute("""INSERT INTO dados_serviços 
            (cliente,telefone,numero_cliente,placa,marca,modelo,ano,motor,km,peças1,uni1,valor_peças1,peças2,uni2,
            valor_peças2,peças3,uni3,valor_peças3,peças4,uni4,valor_peças4,peças5,uni5,valor_peças5,peças6,uni6,
            valor_peças6,peças7,uni7,valor_peças7,peças8,uni8,valor_peças8,peças9,uni9,valor_peças9,peças10,uni10,
            valor_peças10,peças11,uni11,valor_peças11,peças12,uni12,valor_peças12,peças13,uni13,valor_peças13,peças14,
            uni14,valor_peças14,peças15,uni15,valor_peças15,peças16,uni16,valor_peças16,peças17,uni17,valor_peças17,
            peças18,uni18,valor_peças18,peças19,uni19,valor_peças19,peças20,uni20,valor_peças20,retifica,M_O,total_peças,
            total_OS,data)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);
            """, (self.DadosOsCarro, self.DadosOsCarro1, self.DadosOsCarro8, self.DadosOsCarro2, self.DadosOsCarro3,
                  self.DadosOsCarro4, self.DadosOsCarro5, self.DadosOsCarro6, self.DadosOsCarro7, self.pasa, self.Upesa,
                  self.vUpesa, self.pasa1, self.Upesa1, self.vUpesa1, self.pasa2, self.Upesa2, self.vUpesa2, self.pasa3,
                  self.Upesa3, self.vUpesa3, self.pasa4, self.Upesa4, self.vUpesa4, self.pasa5, self.Upesa5,
                  self.vUpesa5, self.pasa6, self.Upesa6, self.vUpesa6, self.pasa7, self.Upesa7, self.vUpesa7,
                  self.pasa8, self.Upesa8, self.vUpesa8, self.pasa9, self.Upesa9, self.vUpesa9, self.pasa10,
                  self.Upesa10,
                  self.vUpesa10, self.pasa11, self.Upesa11, self.vUpesa11, self.pasa12, self.Upesa12, self.vUpesa12,
                  self.pasa13,
                  self.Upesa13, self.vUpesa13, self.pasa14, self.Upesa14, self.vUpesa14, self.pasa15, self.Upesa15,
                  self.vUpesa15,
                  self.pasa16, self.Upesa16, self.vUpesa16, self.pasa17, self.Upesa17, self.vUpesa17, self.pasa18,
                  self.Upesa18,
                  self.vUpesa18, self.pasa19, self.Upesa19, self.vUpesa19, self.retifica, self.mo, self.pesas_total,
                  self.totaltotal, self.data1))
            self.DesconequitarBancoPendetes()
            self.ConequitarBancoPendentes()
            self.c.execute(f"""DELETE FROM dados_serviços WHERE data = '00000000' """)
            self.c.execute("""INSERT INTO dados_serviços 
                    (cliente,telefone,numero_cliente,placa,marca,modelo,ano,motor,km,peças1,uni1,valor_peças1,peças2,uni2,
                    valor_peças2,peças3,uni3,valor_peças3,peças4,uni4,valor_peças4,peças5,uni5,valor_peças5,peças6,uni6,
                    valor_peças6,peças7,uni7,valor_peças7,peças8,uni8,valor_peças8,peças9,uni9,valor_peças9,peças10,uni10,
                    valor_peças10,peças11,uni11,valor_peças11,peças12,uni12,valor_peças12,peças13,uni13,valor_peças13,peças14,
                    uni14,valor_peças14,peças15,uni15,valor_peças15,peças16,uni16,valor_peças16,peças17,uni17,valor_peças17,
                    peças18,uni18,valor_peças18,peças19,uni19,valor_peças19,peças20,uni20,valor_peças20,retifica,M_O,total_peças,
                    total_OS,data)
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);
                    """, (
            " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ",
            " ", " ", " ", " ", "00000000"))
            self.DesconequitarBancoPendetes()
            self.LimparPesas()
            self.LimparOsCarro()
    def CriarOs_Pendente(self):
        self.DataModificada()
        self.ConequitarBancoPendentes()
        self.c.execute("""INSERT INTO dados_serviços 
        (cliente,telefone,numero_cliente,placa,marca,modelo,ano,motor,km,peças1,uni1,valor_peças1,peças2,uni2,
        valor_peças2,peças3,uni3,valor_peças3,peças4,uni4,valor_peças4,peças5,uni5,valor_peças5,peças6,uni6,
        valor_peças6,peças7,uni7,valor_peças7,peças8,uni8,valor_peças8,peças9,uni9,valor_peças9,peças10,uni10,
        valor_peças10,peças11,uni11,valor_peças11,peças12,uni12,valor_peças12,peças13,uni13,valor_peças13,peças14,
        uni14,valor_peças14,peças15,uni15,valor_peças15,peças16,uni16,valor_peças16,peças17,uni17,valor_peças17,
        peças18,uni18,valor_peças18,peças19,uni19,valor_peças19,peças20,uni20,valor_peças20,retifica,M_O,total_peças,
        total_OS,data)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
        ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);
        """, (self.DadosOsCarro, self.DadosOsCarro1, self.DadosOsCarro8, self.DadosOsCarro2, self.DadosOsCarro3,
              self.DadosOsCarro4, self.DadosOsCarro5, self.DadosOsCarro6, self.DadosOsCarro7, self.pasa, self.Upesa,
              self.vUpesa, self.pasa1, self.Upesa1, self.vUpesa1, self.pasa2, self.Upesa2, self.vUpesa2, self.pasa3,
              self.Upesa3, self.vUpesa3, self.pasa4, self.Upesa4, self.vUpesa4, self.pasa5, self.Upesa5,
              self.vUpesa5, self.pasa6, self.Upesa6, self.vUpesa6, self.pasa7, self.Upesa7, self.vUpesa7,
              self.pasa8, self.Upesa8, self.vUpesa8, self.pasa9, self.Upesa9, self.vUpesa9, self.pasa10,
              self.Upesa10,
              self.vUpesa10, self.pasa11, self.Upesa11, self.vUpesa11, self.pasa12, self.Upesa12, self.vUpesa12,
              self.pasa13,
              self.Upesa13, self.vUpesa13, self.pasa14, self.Upesa14, self.vUpesa14, self.pasa15, self.Upesa15,
              self.vUpesa15,
              self.pasa16, self.Upesa16, self.vUpesa16, self.pasa17, self.Upesa17, self.vUpesa17, self.pasa18,
              self.Upesa18,
              self.vUpesa18, self.pasa19, self.Upesa19, self.vUpesa19, self.retifica, self.mo, self.pesas_total,
              self.totaltotal, self.data1))
        self.DesconequitarBancoPendetes()
        self.ConequitarBancoPendentes()
        self.c.execute(f"""DELETE FROM dados_serviços WHERE data = '00000000' """)
        self.c.execute("""INSERT INTO dados_serviços 
                (cliente,telefone,numero_cliente,placa,marca,modelo,ano,motor,km,peças1,uni1,valor_peças1,peças2,uni2,
                valor_peças2,peças3,uni3,valor_peças3,peças4,uni4,valor_peças4,peças5,uni5,valor_peças5,peças6,uni6,
                valor_peças6,peças7,uni7,valor_peças7,peças8,uni8,valor_peças8,peças9,uni9,valor_peças9,peças10,uni10,
                valor_peças10,peças11,uni11,valor_peças11,peças12,uni12,valor_peças12,peças13,uni13,valor_peças13,peças14,
                uni14,valor_peças14,peças15,uni15,valor_peças15,peças16,uni16,valor_peças16,peças17,uni17,valor_peças17,
                peças18,uni18,valor_peças18,peças19,uni19,valor_peças19,peças20,uni20,valor_peças20,retifica,M_O,total_peças,
                total_OS,data)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);
                """, (
            " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ",
            " ", " ", " ", " ", "00000000"))
        self.DesconequitarBancoPendetes()
    def AbrirPorOS(self):
        self.os_janela.destroy()
        self.PendetesJanela()
    def Escolha_Modificar_Pendentes(self):
        if self.entrada_codigo.get() == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!NUMERO DA O.S NÃO INSIRIDO!!!')
            self.jMensagem.place(x=20, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o numero da O.S!')
            self.j2Mensagem.place(x=60, y=55)
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
            self.simbotam = tk.Button(self.aviso, text='SIM', font='Ariel', command=self.ModificarPendentes)
            self.simbotam.place(x=70, y=90, width=100, height=40)
            self.naobotam = tk.Button(self.aviso, text='NÃO', font='Ariel', command=self.aviso.destroy)
            self.naobotam.place(x=220, y=90, width=100, height=40)
    def ModificarPendentes(self):
        try:
            self.DataModificada()
            self.Somar()
            self.Variavel_Os()
            # self.ModificaNo_W()
            self.ConequitarBancoPendentes()
            self.c.execute(f"""UPDATE dados_serviços SET cliente = ?,telefone = ?,numero_cliente = ?,placa = ?,
            marca = ?,
            modelo = ?,ano = ?,motor = ?,km = ?,peças1 = ?,uni1 = ?,valor_peças1 = ?,peças2 = ?,uni2 = ?,
            valor_peças2 = ?,
            peças3 = ?,uni3 = ?,valor_peças3 = ?,peças4 = ?,uni4 = ?,valor_peças4 = ?,peças5 = ?,uni5 = ?,
            valor_peças5 = ?,
            peças6 = ?,uni6 = ?,valor_peças6 = ?,peças7 = ?,uni7 = ?,valor_peças7 = ?,peças8 = ?,uni8 = ?,
            valor_peças8 = ?,
            peças9 = ?,uni9 = ?,valor_peças9 = ?,peças10 = ?,uni10 = ?,valor_peças10 = ?,peças11 = ?,uni11 = ?,
            valor_peças11 = ?,peças12 = ?,uni12 = ?,valor_peças12 = ?,peças13 = ?,uni13 = ?,valor_peças13 = ?,
            peças14 = ?,
            uni14 = ?,valor_peças14 = ?,peças15 = ?,uni15 = ?,valor_peças15 = ?,peças16 = ?,uni16 = ?,valor_peças16 = ?,
            peças17 = ?,uni17 = ?,valor_peças17 = ?,peças18 = ?,uni18 = ?,valor_peças18 = ?,peças19 = ?,uni19 = ?,
            valor_peças19 = ?,peças20 = ?,uni20 = ?,valor_peças20 = ?,retifica = ?,M_O = ?,total_peças = ?,total_OS = ?,
            data = ? WHERE numero_pedido = ?""",
                           (self.DadosOsCarro, self.DadosOsCarro1, self.DadosOsCarro8, self.DadosOsCarro2,
                            self.DadosOsCarro3,
                            self.DadosOsCarro4, self.DadosOsCarro5, self.DadosOsCarro6, self.DadosOsCarro7, self.pasa,
                            self.Upesa,
                            self.vUpesa, self.pasa1, self.Upesa1, self.vUpesa1, self.pasa2, self.Upesa2, self.vUpesa2,
                            self.pasa3,
                            self.Upesa3, self.vUpesa3, self.pasa4, self.Upesa4, self.vUpesa4, self.pasa5, self.Upesa5,
                            self.vUpesa5, self.pasa6, self.Upesa6, self.vUpesa6, self.pasa7, self.Upesa7, self.vUpesa7,
                            self.pasa8, self.Upesa8, self.vUpesa8, self.pasa9, self.Upesa9, self.vUpesa9, self.pasa10,
                            self.Upesa10,
                            self.vUpesa10, self.pasa11, self.Upesa11, self.vUpesa11, self.pasa12, self.Upesa12,
                            self.vUpesa12, self.pasa13,
                            self.Upesa13, self.vUpesa13, self.pasa14, self.Upesa14, self.vUpesa14, self.pasa15,
                            self.Upesa15, self.vUpesa15,
                            self.pasa16, self.Upesa16, self.vUpesa16, self.pasa17, self.Upesa17, self.vUpesa17,
                            self.pasa18, self.Upesa18,
                            self.vUpesa18, self.pasa19, self.Upesa19, self.vUpesa19, self.retifica, self.mo,
                            self.pesas_total,
                            self.totaltotal, self.data1, self.codigo_os))
            self.DesconequitarBancoPendetes()
            # Finalizados
            self.ConequitarBancoFinalizados()
            self.x.execute(f"""UPDATE dados_finalizados SET cliente = ?,telefone = ?,numero_cliente = ?,placa = ?,marca = ?,
            modelo = ?,ano = ?,motor = ?,km = ?,peças1 = ?,uni1 = ?,valor_peças1 = ?,peças2 = ?,uni2 = ?,valor_peças2 = ?,
            peças3 = ?,uni3 = ?,valor_peças3 = ?,peças4 = ?,uni4 = ?,valor_peças4 = ?,peças5 = ?,uni5 = ?,valor_peças5 = ?,
            peças6 = ?,uni6 = ?,valor_peças6 = ?,peças7 = ?,uni7 = ?,valor_peças7 = ?,peças8 = ?,uni8 = ?,valor_peças8 = ?,
            peças9 = ?,uni9 = ?,valor_peças9 = ?,peças10 = ?,uni10 = ?,valor_peças10 = ?,peças11 = ?,uni11 = ?,
            valor_peças11 = ?,peças12 = ?,uni12 = ?,valor_peças12 = ?,peças13 = ?,uni13 = ?,valor_peças13 = ?,peças14 = ?,
            uni14 = ?,valor_peças14 = ?,peças15 = ?,uni15 = ?,valor_peças15 = ?,peças16 = ?,uni16 = ?,valor_peças16 = ?,
            peças17 = ?,uni17 = ?,valor_peças17 = ?,peças18 = ?,uni18 = ?,valor_peças18 = ?,peças19 = ?,uni19 = ?,
            valor_peças19 = ?,peças20 = ?,uni20 = ?,valor_peças20 = ?,retifica = ?,M_O = ?,total_peças = ?,total_OS = ?
             WHERE numero_pedido = ?""",
                           (self.DadosOsCarro, self.DadosOsCarro1, self.DadosOsCarro8, self.DadosOsCarro2,
                            self.DadosOsCarro3,
                            self.DadosOsCarro4, self.DadosOsCarro5, self.DadosOsCarro6, self.DadosOsCarro7, self.pasa,
                            self.Upesa,
                            self.vUpesa, self.pasa1, self.Upesa1, self.vUpesa1, self.pasa2, self.Upesa2, self.vUpesa2,
                            self.pasa3,
                            self.Upesa3, self.vUpesa3, self.pasa4, self.Upesa4, self.vUpesa4, self.pasa5, self.Upesa5,
                            self.vUpesa5, self.pasa6, self.Upesa6, self.vUpesa6, self.pasa7, self.Upesa7, self.vUpesa7,
                            self.pasa8, self.Upesa8, self.vUpesa8, self.pasa9, self.Upesa9, self.vUpesa9, self.pasa10,
                            self.Upesa10,
                            self.vUpesa10, self.pasa11, self.Upesa11, self.vUpesa11, self.pasa12, self.Upesa12,
                            self.vUpesa12, self.pasa13,
                            self.Upesa13, self.vUpesa13, self.pasa14, self.Upesa14, self.vUpesa14, self.pasa15,
                            self.Upesa15, self.vUpesa15,
                            self.pasa16, self.Upesa16, self.vUpesa16, self.pasa17, self.Upesa17, self.vUpesa17,
                            self.pasa18, self.Upesa18,
                            self.vUpesa18, self.pasa19, self.Upesa19, self.vUpesa19, self.retifica, self.mo,
                            self.pesas_total,
                            self.totaltotal, self.codigo_os))
            self.DesconequitarBancoFinalizados()
            self.aviso.destroy()
            self.LimparPesas()
            self.LimparOsCarro()

        except:
            self.Mensagenscaixa()
            self.cabesario_fo = ("Arial Black", "10")
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_fo, text='!!!ERRO!!!')
            self.jMensagem.place(x=150, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='ARQUIVO NÃO ENCONTRADO.')
            self.j2Mensagem.place(x=70, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        finally:
            os.chdir(diretorio)
    def Escolha_apagar_Pendentes(self):
        if self.entrada_codigo.get() == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!NUMERO DA O.S NÃO INSIRIDO!!!')
            self.jMensagem.place(x=20, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o numero da O.S!')
            self.j2Mensagem.place(x=60, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        else:
            self.cabesario_fo = ("Arial Black", "9")
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_fo, text='!VOCÊ REALMENTE'
                                                                               ' QUER APAGAR ESSA O.S!')
            self.jMensagem.place(x=20, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='Está ação não poderar ser desfeita!')
            self.j2Mensagem.place(x=70, y=50)
            self.simbotam = tk.Button(self.aviso, text='SIM', font='Ariel', command=self.DeletaPendentes)
            self.simbotam.place(x=70, y=90, width=100, height=40)
            self.naobotam = tk.Button(self.aviso, text='NÃO', font='Ariel', command=self.aviso.destroy)
            self.naobotam.place(x=220, y=90, width=100, height=40)
    def DeletaPendentes(self):
        try:
            self.Variavel_Os()
            self.ConequitarBancoPendentes()
            self.c.execute(f"""DELETE FROM dados_serviços WHERE numero_pedido = {self.codigo_os} """)
            self.DesconequitarBancoPendetes()
            self.ConequitarBancoFinalizados()
            self.x.execute(f"""DELETE FROM dados_finalizados WHERE numero_pedido = {self.codigo_os} """)
            self.DesconequitarBancoFinalizados()
            self.LimparOsCarro()
            self.LimparPesas()
            self.aviso.destroy()
        except sqlite3.OperationalError:
            self.Mensagenscaixa()
            self.cabesario_fo = ("Arial Black", "10")
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_fo, text='!!!ERRO!!!')
            self.jMensagem.place(x=150, y=10)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='ARQUIVO NÃO ENCONTRADO.')
            self.j2Mensagem.place(x=70, y=45)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        except:
            pass
        finally:
            os.chdir(diretorio)

    def OsJanela(self):
        pass
    def somar(self):
        pass
    def PendetesJanela(self):
        pass
    def ConequitarBancoFinalizados(self):
        pass
    def DesconequitarBancoFinalizados(self):
        pass


class Funcs_Finalizados(Funcs_Pendentes):
    def __init__(self):
        super().__init__()

        self.calendario1 = None
        self.Ent_calendario1 = None
        self.calendario = None
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
    def Variavel_Finalizar(self):
        self.ent_for = self.ent_Fin.get().replace(',','.')
        self.ent_for1 = self.ent_Fin1.get().replace(',','.')
        self.ent_for2 = self.ent_Fin2.get().replace(',','.')
        self.ent_for3 = self.ent_Fin3.get().upper()
        self.ent_for4 = self.ent_Fin4.get().replace(',','.')
        self.entra_criar6 = self.Ent6.get('1.0', tk.END)
    def ConequitarBancoFinalizados(self):
        self.pasta_bancos()
        self.conexao = sqlite3.connect('Banco_finalizados.db')
        self.x = self.conexao.cursor()
    def DesconequitarBancoFinalizados(self):
        self.conexao.commit()
        self.conexao.close()
        os.chdir(diretorio)
    def AtualizeLista_Finalizados(self):
        try:
            self.lista_c_clirFinalizados.delete(*self.lista_c_clirFinalizados.get_children())
            self.ConequitarBancoFinalizados()
            lista_Carro = self.x.execute("""SELECT numero_pedido,cliente,telefone,placa,numero_cliente,retifica,
            M_O,total_peças,total_OS,data FROM dados_finalizados ORDER BY data DESC;""")
            for i in lista_Carro:
                self.lista_c_clirFinalizados.insert("", tk.END,
                                                    values=(i[0], i[1], i[2], i[3], i[4], 'R$ ' + i[5].replace('.', ',')
                                                            , 'R$ ' + i[6].replace('.', ','),
                                                            'R$ ' + i[7].replace('.', ','),
                                                            'R$ ' + i[8].replace('.', ','), i[9]))
            self.DesconequitarBancoFinalizados()
        except:
            pass
    def BuscarTelefoneFinalizados(self):
        self.telefone = self.entrada1.get()
        self.lista_c_clirFinalizados.delete(*self.lista_c_clirFinalizados.get_children())
        self.ConequitarBancoFinalizados()
        self.x.execute("""SELECT numero_pedido,cliente,telefone,placa,numero_cliente,retifica,
        M_O,total_peças,total_OS,data FROM dados_finalizados ORDER BY data ASC;""")
        DadosCarro = self.x.execute(f'SELECT numero_pedido,cliente,telefone,placa,numero_cliente,retifica,M_O,'
                                    f'total_peças,total_OS,data FROM dados_finalizados WHERE telefone LIKE '
                                    f'"%{self.telefone.strip().replace(" ", "").replace("-", "")}%"'
                                    f'ORDER BY data DESC;')

        for i in DadosCarro:
            self.lista_c_clirFinalizados.insert("", tk.END,
                                                values=(i[0], i[1], i[2], i[3], i[4], 'R$ ' + i[5].replace('.', ',')
                                                        , 'R$ ' + i[6].replace('.', ','),
                                                        'R$ ' + i[7].replace('.', ','),
                                                        'R$ ' + i[8].replace('.', ','), i[9]))
        self.DesconequitarBancoFinalizados()
    def BuscarDataFinalizados(self):
        self.datapri = f'{self.dataprima[6:11]}-{self.dataprima[3:5]}-{self.dataprima[0:2]}'
        self.datapri1 = f'{self.dataprima1[6:11]}-{self.dataprima1[3:5]}-{self.dataprima1[0:2]}'
        self.lista_c_clirFinalizados.delete(*self.lista_c_clirFinalizados.get_children())
        self.ConequitarBancoFinalizados()
        self.x.execute("""SELECT numero_pedido,cliente,telefone,placa,numero_cliente,retifica,
        M_O,total_peças,total_OS,data FROM dados_finalizados ORDER BY data ASC;""")
        DadosCarro = self.x.execute(f'SELECT numero_pedido,cliente,telefone,placa,numero_cliente,retifica,M_O,'
                                    f'total_peças,total_OS,data FROM dados_finalizados WHERE data BETWEEN '
                                    f'"{self.datapri}" AND "{self.datapri1}"'
                                    f'ORDER BY data DESC;')

        for i in DadosCarro:
            self.lista_c_clirFinalizados.insert("", tk.END,
                                                values=(i[0], i[1], i[2], i[3], i[4], 'R$ ' + i[5].replace('.', ',')
                                                        , 'R$ ' + i[6].replace('.', ','),
                                                        'R$ ' + i[7].replace('.', ','),
                                                        'R$ ' + i[8].replace('.', ','), i[9]))
        self.DesconequitarBancoFinalizados()
    def BuscarCodigoFinalizados(self):
        self.codigo = self.entrada2.get()
        self.lista_c_clirFinalizados.delete(*self.lista_c_clirFinalizados.get_children())
        self.ConequitarBancoFinalizados()
        self.x.execute("""SELECT numero_pedido,cliente,telefone,placa,numero_cliente,retifica,
        M_O,total_peças,total_OS,data FROM dados_finalizados ORDER BY data ASC;""")
        DadosCarro = self.x.execute(f'SELECT numero_pedido,cliente,telefone,placa,numero_cliente,retifica,M_O,'
                                    f'total_peças,total_OS,data FROM dados_finalizados WHERE numero_cliente LIKE '
                                    f'"%{self.codigo.strip().replace(" ", "").replace("-", "")}%"'
                                    f'ORDER BY data DESC;')

        for i in DadosCarro:
            self.lista_c_clirFinalizados.insert("", tk.END,
                                                values=(i[0], i[1], i[2], i[3], i[4], 'R$ ' + i[5].replace('.', ',')
                                                        , 'R$ ' + i[6].replace('.', ','),
                                                        'R$ ' + i[7].replace('.', ','),
                                                        'R$ ' + i[8].replace('.', ','), i[9]))
        self.DesconequitarBancoFinalizados()
    def BuscarPlacaFinalizados(self):
        self.placa = self.entrada3.get()
        self.lista_c_clirFinalizados.delete(*self.lista_c_clirFinalizados.get_children())
        self.ConequitarBancoFinalizados()
        self.x.execute("""SELECT numero_pedido,cliente,telefone,placa,numero_cliente,retifica,
        M_O,total_peças,total_OS,data FROM dados_finalizados ORDER BY data ASC;""")
        DadosCarro = self.x.execute(f'SELECT numero_pedido,cliente,telefone,placa,numero_cliente,retifica,M_O,'
                                    f'total_peças,total_OS,data FROM dados_finalizados WHERE placa LIKE '
                                    f'"%{self.placa.strip().upper().replace(" ", "").replace("-", "")}%"'
                                    f'ORDER BY data DESC;')

        for i in DadosCarro:
            self.lista_c_clirFinalizados.insert("", tk.END,
                                                values=(i[0], i[1], i[2], i[3], i[4], 'R$ ' + i[5].replace('.', ',')
                                                        , 'R$ ' + i[6].replace('.', ','),
                                                        'R$ ' + i[7].replace('.', ','),
                                                        'R$ ' + i[8].replace('.', ','), i[9]))
        self.DesconequitarBancoFinalizados()
    def TrataFechamento(self):
        self.Variavel_Os()
        self.InicioJanela()

        self.cr_janela.geometry('300x520')
        self.Fontes()
        self.quadradoFinalizados = tk.Frame(self.cr_janela)
        self.quadradoFinalizados.place(x=5, y=5, width=290, height=40)
        self.quadradoFinalizados1 = tk.Frame(self.cr_janela)
        self.quadradoFinalizados1.place(x=5, y=50, width=290, height=165)
        self.quadradoFinalizados2 = tk.Frame(self.cr_janela)
        self.quadradoFinalizados2.place(x=5, y=220, width=290, height=160)
        self.quadradoFinalizados3 = tk.Frame(self.cr_janela)
        self.quadradoFinalizados3.place(x=5, y=385, width=290, height=130)

        self.Envio2 = IntVar()

        self.ComEnvio2 = tk.Checkbutton(self.cr_janela, text='Lembrar de fazer orçamento!', variable=self.Envio2,
                                        onvalue=1, offvalue=0)
        self.ComEnvio2.place(x=10, y=385)

        self.Ent6 = tk.Text(self.cr_janela, font=self.fonte_buton)
        self.Ent6.place(x=10, y=410, width=280, height=100)

        self.texto = tk.Label(self.cr_janela, text='FINALIZAR VENDA', font=self.cabesario_font)
        self.texto.place(x=60, y=10)

        self.texto = tk.Label(self.cr_janela, text='PAGO EM PEÇAS', font=self.fonte_titlo)
        self.texto.place(x=20, y=60)
        self.texto = tk.Label(self.cr_janela, text='R$', font=self.fonte_titlo)
        self.texto.place(x=10, y=80)
        self.ent_Fin = tk.Entry(self.cr_janela, font=self.fonte_buton)
        self.ent_Fin.place(x=30, y=80, width=170)

        self.texto = tk.Label(self.cr_janela, text='PAGO EM RETIFICA', font=self.fonte_titlo)
        self.texto.place(x=20, y=110)
        self.texto = tk.Label(self.cr_janela, text='R$', font=self.fonte_titlo)
        self.texto.place(x=10, y=130)
        self.ent_Fin1 = tk.Entry(self.cr_janela, font=self.fonte_buton)
        self.ent_Fin1.place(x=30, y=130, width=170)

        self.texto = tk.Label(self.cr_janela, text='PAGO EM OUTROS', font=self.fonte_titlo)
        self.texto.place(x=20, y=160)
        self.texto = tk.Label(self.cr_janela, text='R$', font=self.fonte_titlo)
        self.texto.place(x=10, y=180)
        self.ent_Fin2 = tk.Entry(self.cr_janela, font=self.fonte_buton)
        self.ent_Fin2.place(x=30, y=180, width=170)

        self.texto = tk.Label(self.cr_janela, text='PAGO DE QUE FORMA', font=self.fonte_titlo)
        self.texto.place(x=40, y=230)
        self.ent_Fin3 = tk.Entry(self.cr_janela, font=self.fonte_buton)
        self.ent_Fin3.place(x=30, y=250, width=170)

        self.texto = tk.Label(self.cr_janela, text='VALOR RECEBIDO', font=self.fonte_titlo)
        self.texto.place(x=20, y=280)
        self.texto = tk.Label(self.cr_janela, text='R$', font=self.fonte_titlo)
        self.texto.place(x=10, y=300)
        self.ent_Fin4 = tk.Entry(self.cr_janela, font=self.fonte_buton)
        self.ent_Fin4.place(x=30, y=300, width=170)

        self.fin = tk.Button(self.cr_janela, text="FINALIZAR", font=self.fonte_buton, bg="black",
                             foreground="white", command=self.CriarFinalizado)
        self.fin.place(x=190, y=330, width=100, height=40)

        self.criarfin = tk.Button(self.cr_janela, text="CANCELAR", font=self.fonte_buton, bg="black",
                                  foreground="white", command=self.cr_janela.destroy)
        self.criarfin.place(x=10, y=330, width=100, height=40)
    def JanelaFechamento(self):
        self.Variavel_Os()
        if self.DadosOsCarro8 == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!CARRO NÃO INSERIDO!!!')
            self.jMensagem.place(x=70, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir um carro para finalizar!')
            self.j2Mensagem.place(x=40, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif self.DadosOsCarro == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!ERRO NOME!!!')
            self.jMensagem.place(x=100, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o nome do cliente!')
            self.j2Mensagem.place(x=60, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif self.DadosOsCarro4 == '':
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!ERRO CARRO!!!')
            self.jMensagem.place(x=100, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o modelo do carro!')
            self.j2Mensagem.place(x=60, y=55)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
        elif self.entrada_codigo.get() == "":
            self.CriarOs_Pendente()
            sleep(2)
            self.ColocarNumeroPedido()
            self.TrataFechamento()
        else:
            self.TrataFechamento()
    def CriarFinalizado(self):
        try:
            if self.ent_Fin4.get() == '':
                self.Mensagenscaixa()
                self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!!!VALOR NÃO INSIRIDO!!!')
                self.jMensagem.place(x=70, y=15)
                self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir o valor pago!')
                self.j2Mensagem.place(x=70, y=55)
                self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
                self.jbotam.place(x=140, y=90, width=100, height=40)
            elif self.ent_Fin3.get() == '':
                self.Mensagenscaixa()
                self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font,
                                          text='FORMA DE PAGAMENTO NÃO INSIRIDO!')
                self.jMensagem.place(x=5, y=15)
                self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='É necessario inserir a forma de pagamento!')
                self.j2Mensagem.place(x=40, y=55)
                self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
                self.jbotam.place(x=140, y=90, width=100, height=40)
            else:
                self.somar()
                self.DataModificada()
                self.Variavel_Os()
                self.Variavel_Finalizar()
                self.valor_saidas = [self.ent_for, self.ent_for1, self.ent_for2]
                self.sumi = []
                self.ent_for_float3 = float(self.ent_for4)
                for s, w in enumerate(self.valor_saidas):
                    if w == '':
                        x = w.replace('', '0')
                        self.sumi.append(float(x))
                    else:
                        self.sumi.append(float(w))
                self.so = sum(self.sumi)
                self.paraobanco = []
                self.somas_rec_sai = (self.ent_for_float3 - self.so)
                for a, i in enumerate(self.valor_saidas):
                    if i == '':
                        x = i.replace('', '0')
                        self.paraobanco.append('{:.2f}'.format(float(x)))
                    else:
                        self.paraobanco.append('{:.2f}'.format(float(i)))
                self.so = sum(self.sumi)
                self.DadosForma = self.paraobanco[0]
                self.DadosForma1 = self.paraobanco[1]
                self.DadosForma2 = self.paraobanco[2]
                self.DadosForma3 = str('{:.2f}'.format(self.ent_for_float3))
                self.DadosForma4 = str('{:.2f}'.format(self.somas_rec_sai))
                self.ConequitarBancoPendentes()
                self.c.execute(f'SELECT *, oid FROM dados_serviços WHERE numero_pedido = {self.codigo_os}')
                self.ces = self.c.fetchall()
                for cc in self.ces:
                    self.ConequitarBancoFinalizados()
                    self.x.execute("""INSERT INTO dados_finalizados (numero_pedido,cliente,telefone,numero_cliente,placa,
                    marca,modelo,ano,motor,km,peças1,uni1,valor_peças1,peças2,uni2,
                    valor_peças2,peças3,uni3,valor_peças3,peças4,uni4,valor_peças4,peças5,uni5,valor_peças5,peças6,uni6,
                    valor_peças6,peças7,uni7,valor_peças7,peças8,uni8,valor_peças8,peças9,uni9,valor_peças9,peças10,uni10,
                    valor_peças10,peças11,uni11,valor_peças11,peças12,uni12,valor_peças12,peças13,uni13,valor_peças13,peças14,
                    uni14,valor_peças14,peças15,uni15,valor_peças15,peças16,uni16,valor_peças16,peças17,uni17,valor_peças17,
                    peças18,uni18,valor_peças18,peças19,uni19,valor_peças19,peças20,uni20,valor_peças20,retifica,M_O,
                    total_peças,total_OS,forma_paga,valor_recebido,gasto_pesas,gasto_retifica,gasto_outros,ganho,data)                  
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);
                    """, (
                        cc[0], cc[1], cc[2], cc[3], cc[4], cc[5], cc[6], cc[7], cc[8], cc[9], cc[10], cc[11], cc[12],
                        cc[13],
                        cc[14], cc[15],
                        cc[16], cc[17], cc[18], cc[19], cc[20], cc[21], cc[22], cc[23], cc[24], cc[25], cc[26], cc[27],
                        cc[28],
                        cc[29],
                        cc[30], cc[31], cc[32], cc[33], cc[34], cc[35], cc[36], cc[37], cc[38], cc[39], cc[40], cc[41],
                        cc[42],
                        cc[43],
                        cc[44], cc[45], cc[46], cc[47], cc[48], cc[49], cc[50], cc[51], cc[52], cc[53], cc[54], cc[55],
                        cc[56],
                        cc[57],
                        cc[58], cc[59], cc[60], cc[61], cc[62], cc[63], cc[64], cc[65], cc[66], cc[67], cc[68], cc[69],
                        cc[70],
                        cc[71],
                        cc[72], cc[73], self.ent_for3, self.DadosForma3, self.DadosForma, self.DadosForma1,
                        self.DadosForma2,
                        self.DadosForma4, self.data1))
                    self.DesconequitarBancoFinalizados()
                    self.ConequitarBancoPendentes()
                    self.c.execute(f"""DELETE FROM dados_serviços WHERE numero_pedido = {self.codigo_os} """)
                    self.DesconequitarBancoPendetes()
                    self.PerguntarAntesEnvios()
        except:
            self.Mensagenscaixa()
            self.jMensagem = tk.Label(self.aviso, font=self.cabesario_font, text='!ERRO NO NUMERO DA O.S!')
            self.jMensagem.place(x=60, y=15)
            self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='Você Pode estar tentando finalizar um pedido\n'
                                                                      'já finalizado, Verifique e tente de novo!')
            self.j2Mensagem.place(x=25, y=50)
            self.jbotam = tk.Button(self.aviso, text='OK', font='Ariel', command=self.aviso.destroy)
            self.jbotam.place(x=140, y=90, width=100, height=40)
            os.chdir(diretorio)
    def Colocardata(self):
        self.dataprima = self.calendario.get_date()
        self.Ent_calendario.delete(0,tk.END)
        self.Ent_calendario.insert(tk.END, self.dataprima)
        self.dataprima1 = self.calendario1.get_date()
        self.Ent_calendario1.delete(0,tk.END)
        self.Ent_calendario1.insert(tk.END, self.dataprima1)
        self.BuscarDataFinalizados()
    def AbrirFinalizados(self,event):
        self.OsJanela()
        self.ConequitarBancoFinalizados()
        self.lista_c_clirFinalizados.selection()
        for n in self.lista_c_clirFinalizados.selection():
            col1,col2,col3,col4,col5,col6,col7,col8,col9,col10= self.lista_c_clirFinalizados.item(n, 'values')
            Dados = self.x.execute(f'SELECT numero_pedido,cliente,telefone,numero_cliente,placa,marca,modelo,ano,'
                                   f'motor,km,peças1,uni1,valor_peças1,peças2,uni2,valor_peças2,peças3,uni3,'
                                   f'valor_peças3,peças4,uni4,valor_peças4,peças5,uni5,valor_peças5,peças6,'
                                   f'uni6,valor_peças6,peças7,uni7,valor_peças7,peças8,uni8,valor_peças8,peças9,'
                                   f'uni9,valor_peças9,peças10,uni10,valor_peças10,peças11,uni11,valor_peças11,'
                                   f'peças12,uni12,valor_peças12,peças13,uni13,valor_peças13,peças14,uni14,'
                                   f'valor_peças14,peças15,uni15,valor_peças15,peças16,uni16,valor_peças16,'
                                   f'peças17,uni17,valor_peças17,peças18,uni18,valor_peças18,peças19,uni19,'
                                   f'valor_peças19,peças20,uni20,valor_peças20,retifica,M_O,total_peças,total_OS,'
                                   f'oid FROM dados_finalizados WHERE numero_pedido = "{col1}"')
            for i in Dados:
                self.entrada_codigo.insert(tk.END,i[0])
                self.entraCarro.insert(tk.END,i[1])
                self.entra1Carro.insert(tk.END,i[2])
                self.entra2Carro.insert(tk.END,i[4])
                self.entra3Carro.insert(tk.END,i[5])
                self.entra4Carro.insert(tk.END,i[6])
                self.entra5Carro.insert(tk.END,i[7])
                self.entra6Carro.insert(tk.END,i[8])
                self.entra7Carro.insert(tk.END,i[9])
                self.entra8Carro.insert(tk.END,i[3])

                self.entrada_pesas.insert(tk.END,i[10])
                self.entrada_uni.insert(tk.END,i[11])
                self.entrada_v_uni.insert(tk.END,i[12])

                self.entrada_pesas1.insert(tk.END,i[13])
                self.entrada_uni1.insert(tk.END,i[14])
                self.entrada_v_uni1.insert(tk.END,i[15])

                self.entrada_pesas2.insert(tk.END,i[16])
                self.entrada_uni2.insert(tk.END,i[17])
                self.entrada_v_uni2.insert(tk.END,i[18])

                self.entrada_pesas3.insert(tk.END,i[19])
                self.entrada_uni3.insert(tk.END,i[20])
                self.entrada_v_uni3.insert(tk.END,i[21])

                self.entrada_pesas4.insert(tk.END,i[22])
                self.entrada_uni4.insert(tk.END,i[23])
                self.entrada_v_uni4.insert(tk.END,i[24])

                self.entrada_pesas5.insert(tk.END,i[25])
                self.entrada_uni5.insert(tk.END,i[26])
                self.entrada_v_uni5.insert(tk.END,i[27])

                self.entrada_pesas6.insert(tk.END,i[28])
                self.entrada_uni6.insert(tk.END,i[29])
                self.entrada_v_uni6.insert(tk.END,i[30])

                self.entrada_pesas7.insert(tk.END,i[31])
                self.entrada_uni7.insert(tk.END,i[32])
                self.entrada_v_uni7.insert(tk.END,i[33])

                self.entrada_pesas8.insert(tk.END,i[34])
                self.entrada_uni8.insert(tk.END,i[35])
                self.entrada_v_uni8.insert(tk.END,i[36])

                self.entrada_pesas9.insert(tk.END,i[37])
                self.entrada_uni9.insert(tk.END,i[38])
                self.entrada_v_uni9.insert(tk.END,i[39])

                self.entrada_pesas10.insert(tk.END,i[40])
                self.entrada_uni10.insert(tk.END,i[41])
                self.entrada_v_uni10.insert(tk.END,i[42])

                self.entrada_pesas11.insert(tk.END,i[43])
                self.entrada_uni11.insert(tk.END,i[44])
                self.entrada_v_uni11.insert(tk.END,i[45])

                self.entrada_pesas12.insert(tk.END,i[46])
                self.entrada_uni12.insert(tk.END,i[47])
                self.entrada_v_uni12.insert(tk.END,i[48])

                self.entrada_pesas13.insert(tk.END,i[49])
                self.entrada_uni13.insert(tk.END,i[50])
                self.entrada_v_uni13.insert(tk.END,i[51])

                self.entrada_pesas14.insert(tk.END,i[52])
                self.entrada_uni14.insert(tk.END,i[53])
                self.entrada_v_uni14.insert(tk.END,i[54])

                self.entrada_pesas15.insert(tk.END,i[55])
                self.entrada_uni15.insert(tk.END,i[56])
                self.entrada_v_uni15.insert(tk.END,i[57])

                self.entrada_pesas16.insert(tk.END,i[58])
                self.entrada_uni16.insert(tk.END,i[59])
                self.entrada_v_uni16.insert(tk.END,i[60])

                self.entrada_pesas17.insert(tk.END,i[61])
                self.entrada_uni17.insert(tk.END,i[62])
                self.entrada_v_uni17.insert(tk.END,i[63])

                self.entrada_pesas18.insert(tk.END,i[64])
                self.entrada_uni18.insert(tk.END,i[65])
                self.entrada_v_uni18.insert(tk.END,i[66])

                self.entrada_pesas19.insert(tk.END,i[67])
                self.entrada_uni19.insert(tk.END,i[68])
                self.entrada_v_uni19.insert(tk.END,i[69])

                self.Retifica.insert(tk.END,i[70])
                self.M_O.insert(tk.END,i[71])
                self.PesasTotal.insert(tk.END,i[72])
                self.TotalTotal.insert(tk.END,i[73])

        self.DesconequitarBancoFinalizados()
        self.cr_janela.destroy()
        self.Somar()
    def AbrirFinalizadosPorOS(self):
        self.os_janela.destroy()
        self.FinalizadosJanela()
    def ColocarNumeroPedido(self):
        self.entrada_codigo.delete(0, tk.END)
        self.DataModificada()
        self.ConequitarBancoPendentes()
        self.c.execute(f'SELECT numero_pedido oid FROM dados_serviços WHERE data < "{self.data1}"'
                       f' ORDER BY data DESC limit 1')
        self.tes = self.c.fetchall()
        self.entrada_codigo.insert(tk.END, self.tes)
        self.DesconequitarBancoPendetes()

    def TratarFinazerMensagens(self):
        self.AutoMengFin2()
        self.LimparPesas()
        self.LimparOsCarro()
        self.cr_janela.destroy()
        self.aviso.destroy()

    def PerguntarAntesEnvios(self):
        self.cabesario_fo = ("Arial Black", "9")
        self.Mensagenscaixa()
        self.jMensagem = tk.Label(self.aviso, font=self.cabesario_fo, text='CRIAR POS VENDA PARA ESSE SERVIÇO?')
        self.jMensagem.place(x=50, y=15)
        self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='Está ação ira criar mensagens automaticas para\nesse'
                                                                  ' cliente e apagar todas as outras mensagens!')
        self.j2Mensagem.place(x=20, y=45)
        self.simbotam = tk.Button(self.aviso, text='SIM', font='Ariel', command=self.AutoMengFin1)
        self.simbotam.place(x=70, y=90, width=100, height=40)
        self.naobotam = tk.Button(self.aviso, text='NÃO', font='Ariel', command=self.PerguntarAgradecimento)
        self.naobotam.place(x=220, y=90, width=100, height=40)
    def PerguntarAgradecimento(self):
        self.aviso.destroy()
        self.cabesario_fo = ("Arial Black", "9")
        self.Mensagenscaixa()
        self.jMensagem = tk.Label(self.aviso, font=self.cabesario_fo, text='ENVIAR MENSAGEM DE AGRADECIMENTO?')
        self.jMensagem.place(x=50, y=15)
        self.j2Mensagem = tk.Label(self.aviso, font='Ariel', text='Está ação abrir seu WhatsApp para agradecer\nao seu '
                                                                  'cliente!')
        self.j2Mensagem.place(x=30, y=45)
        self.simbotam = tk.Button(self.aviso, text='SIM', font='Ariel', command=self.AutoMengFin)
        self.simbotam.place(x=70, y=90, width=100, height=40)
        self.naobotam = tk.Button(self.aviso, text='NÃO', font='Ariel', command=self.TratarFinazerMensagens)
        self.naobotam.place(x=220, y=90, width=100, height=40)

    def AutoMengFin1(self):
        self.Variavel_Os()
        self.DataModificada()
        self.data = datetime.now()
        self.mais = timedelta(days=30)
        self.somasData = (self.data + self.mais)
        self.SomadaData = str(self.somasData)[0:11].strip()
        self.ConequitarBancoPosVenda()
        self.c.execute(f"""DELETE FROM pos_venda WHERE numero_cliente = '{self.DadosOsCarro8}'""")
        self.c.execute("""INSERT INTO pos_venda(nome,whats,numero_cliente,data_criada,data_executar,mensagem1,
                    mensagem2,mensagem3)VALUES(?,?,?,?,?,?,?,?);""",
                       (self.DadosOsCarro, self.DadosOsCarro1, self.DadosOsCarro8, self.dataP2, self.SomadaData
                        , f'Estamos entrando em contato a respeito do serviço efetuado no dia {self.dataP2}',
                        f'Gostaríamos de saber como está o funcionamento do seu '
                        f'{self.DadosOsCarro3} {self.DadosOsCarro4} ?',
                        'Qual quer duvida estamos a disposição!'))

        self.mais1 = timedelta(days=90)
        self.somasData1 = (self.data + self.mais1)
        self.SomadaData1 = str(self.somasData1)[0:11].strip()
        self.c.execute("""INSERT INTO pos_venda(nome,whats,numero_cliente,data_criada,data_executar,mensagem1,
                                                mensagem2,mensagem3)VALUES(?,?,?,?,?,?,?,?);""",
                       (self.DadosOsCarro, self.DadosOsCarro1, self.DadosOsCarro8, self.dataP2, self.SomadaData1
                        , f'Verificamos em nosso sistema que seu último serviço foi efetuado no dia {self.dataP2}',
                        f'Como está o desempenho seu, {self.DadosOsCarro3} {self.DadosOsCarro4}? '
                        f'Óleo, água, suspensão e motor tudo OK?',
                        'Qual quer duvida estamos a disposição!'))

        self.mais2 = timedelta(days=120)
        self.somasData2 = (self.data + self.mais2)
        self.SomadaData2 = str(self.somasData2)[0:11].strip()
        self.c.execute("""INSERT INTO pos_venda(nome,whats,numero_cliente,data_criada,data_executar,mensagem1,
                                                mensagem2,mensagem3)VALUES(?,?,?,?,?,?,?,?);""",
                       (self.DadosOsCarro, self.DadosOsCarro1, self.DadosOsCarro8, self.dataP2, self.SomadaData2
                        , f'Verificamos em nosso sistema que seu último serviço foi efetuado no dia {self.dataP2}',
                        f'Como está o desempenho seu, {self.DadosOsCarro3} {self.DadosOsCarro4}? '
                        f'Óleo, água, suspensão e motor tudo OK?',
                        'Qual quer duvida estamos a disposição!'))

        self.mais3 = timedelta(days=150)
        self.somasData1 = (self.data + self.mais3)
        self.SomadaData1 = str(self.somasData1)[0:11].strip()
        self.c.execute("""INSERT INTO pos_venda(nome,whats,numero_cliente,data_criada,data_executar,mensagem1,
                                                mensagem2,mensagem3)VALUES(?,?,?,?,?,?,?,?);""",
                       (self.DadosOsCarro, self.DadosOsCarro1, self.DadosOsCarro8, self.dataP2, self.SomadaData1
                        , f'Verificamos em nosso sistema que seu último serviço foi efetuado no dia {self.dataP2}',
                        f'Como está o desempenho seu, {self.DadosOsCarro3} {self.DadosOsCarro4}? '
                        f'Óleo, água, suspensão e motor tudo OK?',
                        'Qual quer duvida estamos a disposição!'))

        self.mais4 = timedelta(days=180)
        self.somasData1 = (self.data + self.mais4)
        self.SomadaData1 = str(self.somasData1)[0:11].strip()
        self.c.execute("""INSERT INTO pos_venda(nome,whats,numero_cliente,data_criada,data_executar,mensagem1,
                                                mensagem2,mensagem3)VALUES(?,?,?,?,?,?,?,?);""",
                       (self.DadosOsCarro, self.DadosOsCarro1, self.DadosOsCarro8, self.dataP2, self.SomadaData1
                        , f'Verificamos em nosso sistema que seu último serviço foi efetuado no dia {self.dataP2}',
                        f'Como está o desempenho seu, {self.DadosOsCarro3} {self.DadosOsCarro4}? '
                        f'Óleo, água, suspensão e motor tudo OK?',
                        'Qual quer duvida estamos a disposição!'))

        self.mais5 = timedelta(days=210)
        self.somasData1 = (self.data + self.mais5)
        self.SomadaData1 = str(self.somasData1)[0:11].strip()
        self.c.execute("""INSERT INTO pos_venda(nome,whats,numero_cliente,data_criada,data_executar,mensagem1,
                                                mensagem2,mensagem3)VALUES(?,?,?,?,?,?,?,?);""",
                       (self.DadosOsCarro, self.DadosOsCarro1, self.DadosOsCarro8, self.dataP2, self.SomadaData1
                        , f'Verificamos em nosso sistema que seu último serviço foi efetuado no dia {self.dataP2}',
                        f'Como está o desempenho seu, {self.DadosOsCarro3} {self.DadosOsCarro4}? '
                        f'Óleo, água, suspensão e motor tudo OK?',
                        'Qual quer duvida estamos a disposição!'))

        self.mais6 = timedelta(days=240)
        self.somasData1 = (self.data + self.mais6)
        self.SomadaData1 = str(self.somasData1)[0:11].strip()
        self.c.execute("""INSERT INTO pos_venda(nome,whats,numero_cliente,data_criada,data_executar,mensagem1,
                                                mensagem2,mensagem3)VALUES(?,?,?,?,?,?,?,?);""",
                       (self.DadosOsCarro, self.DadosOsCarro1, self.DadosOsCarro8, self.dataP2, self.SomadaData1
                        , f'Verificamos em nosso sistema que seu último serviço foi efetuado no dia {self.dataP2}',
                        f'Como está o desempenho seu, {self.DadosOsCarro3} {self.DadosOsCarro4}? '
                        f'Óleo, água, suspensão e motor tudo OK?',
                        'Qual quer duvida estamos a disposição!'))

        self.mais7 = timedelta(days=270)
        self.somasData1 = (self.data + self.mais7)
        self.SomadaData1 = str(self.somasData1)[0:11].strip()
        self.c.execute("""INSERT INTO pos_venda(nome,whats,numero_cliente,data_criada,data_executar,mensagem1,
                                                mensagem2,mensagem3)VALUES(?,?,?,?,?,?,?,?);""",
                       (self.DadosOsCarro, self.DadosOsCarro1, self.DadosOsCarro8, self.dataP2, self.SomadaData1
                        , f'Verificamos em nosso sistema que seu último serviço foi efetuado no dia {self.dataP2}',
                        f'Como está o desempenho seu, {self.DadosOsCarro3} {self.DadosOsCarro4}? '
                        f'Óleo, água, suspensão e motor tudo OK?',
                        'Qual quer duvida estamos a disposição!'))

        self.mais8 = timedelta(days=300)
        self.somasData1 = (self.data + self.mais8)
        self.SomadaData1 = str(self.somasData1)[0:11].strip()
        self.c.execute("""INSERT INTO pos_venda(nome,whats,numero_cliente,data_criada,data_executar,mensagem1,
                                                mensagem2,mensagem3)VALUES(?,?,?,?,?,?,?,?);""",
                       (self.DadosOsCarro, self.DadosOsCarro1, self.DadosOsCarro8, self.dataP2, self.SomadaData1
                        , f'Verificamos em nosso sistema que seu último serviço foi efetuado no dia {self.dataP2}',
                        f'Como está o desempenho seu, {self.DadosOsCarro3} {self.DadosOsCarro4}? '
                        f'Óleo, água, suspensão e motor tudo OK?',
                        'Qual quer duvida estamos a disposição!'))

        self.mais9 = timedelta(days=330)
        self.somasData1 = (self.data + self.mais9)
        self.SomadaData1 = str(self.somasData1)[0:11].strip()
        self.c.execute("""INSERT INTO pos_venda(nome,whats,numero_cliente,data_criada,data_executar,mensagem1,
                                                mensagem2,mensagem3)VALUES(?,?,?,?,?,?,?,?);""",
                       (self.DadosOsCarro, self.DadosOsCarro1, self.DadosOsCarro8, self.dataP2, self.SomadaData1
                        , f'Verificamos em nosso sistema que seu último serviço foi efetuado no dia {self.dataP2}',
                        f'Como está o desempenho seu, {self.DadosOsCarro3} {self.DadosOsCarro4}? '
                        f'Óleo, água, suspensão e motor tudo OK?',
                        'Qual quer duvida estamos a disposição!'))

        self.mais10 = timedelta(days=360)
        self.somasData1 = (self.data + self.mais10)
        self.SomadaData1 = str(self.somasData1)[0:11].strip()
        self.c.execute("""INSERT INTO pos_venda(nome,whats,numero_cliente,data_criada,data_executar,mensagem1,
                                                mensagem2,mensagem3)VALUES(?,?,?,?,?,?,?,?);""",
                       (self.DadosOsCarro, self.DadosOsCarro1, self.DadosOsCarro8, self.dataP2, self.SomadaData1
                        , f'Tudo certo?',
                        f'Notamos que você é nosso cliente a mais de uma ano e anda meio sumido.'
                        f' Gostaríamos de te manter mais próximo!Então, estamos lhe oferecendo uma troca de óleo'
                        f' inteiramente grátis, porque para nós você é muito importante.',
                        'Com carinho Maicá Manutenção automotiva!'))

        self.DesconequitarBancoPosVenda()
        self.aviso.destroy()
        self.PerguntarAgradecimento()

    def AutoMengFin(self):
        self.Variavel_Os()
        self.DataModificada()
        mes = f'Olá {self.DadosOsCarro}!!!'
        mes1 = f'                                                           Muito Obrigado Pela confiança!!!'
        mes2 = f'                                                         Se puder nos avaliar no google!!!'
        mes3 = f'                                                       https://g.page/r/CXfHde-C-cL6EB0/review'
        texto = f'{mes}\n{mes1}\n{mes2}\n{mes3}'
        link = f"https://wa.me/55{self.DadosOsCarro1}?text={texto}"
        webbrowser.open(link)
        self.AutoMengFin2()
        self.LimparPesas()
        self.LimparOsCarro()
        self.cr_janela.destroy()
        self.aviso.destroy()

    def AutoMengFin2(self):
        self.Variavel_Os()
        self.Variavel_Finalizar()
        self.DataModificada()
        self.envio2 = self.Envio2.get()
        if self.envio2 == 1:
            self.data = datetime.now()
            self.mais = timedelta(days=1)
            self.somasData = (self.data + self.mais)
            self.SomadaData = str(self.somasData)[0:11].strip()
            self.ConequitarBancoPosVenda()
            self.c.execute("""INSERT INTO pos_venda(nome,whats,numero_cliente,data_criada,data_executar,mensagem1,
                        mensagem2,mensagem3)VALUES(?,?,?,?,?,?,?,?);""",
                           ('Lucas','51994008112', '0', self.dataP2,self.SomadaData
                            , f'Lucas Não esquece de criar o orçamento.',
                            f'Para O {self.DadosOsCarro} do telefone {self.DadosOsCarro1} Do carro  {self.DadosOsCarro4}',
                            f'{self.entra_criar6}'))
            self.DesconequitarBancoPosVenda()

    def Fontes(self):
        pass
    def FinalizadosJanela(self):
        pass

