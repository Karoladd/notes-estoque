from tkinter import *
from tkinter import filedialog
from util.download import downloadN
from util.rename import nameNotePF, nameNotePJ

PATHNOTEDIR = r"C:\Users\Karol\Desktop\excel-python\test\note"

class Application:

    def __init__(self, master):
        self.master = master
        self.master.geometry("700x550")
        root.config(background = "white")
        self.menu()

    def kit(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(self.master)
        self.primeiroContainer["pady"] = 30
        self.primeiroContainer["bg"] = "white"
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(self.master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer["bg"] = "white"
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(self.master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["bg"] = "white"
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(self.master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer["bg"] = "white"
        self.quartoContainer.pack()

        self.quintoContainer = Frame(self.master)
        self.quintoContainer["pady"] = 10
        self.quintoContainer["bg"] = "white"
        self.quintoContainer.pack()

        self.sextoContainer = Frame(self.master)
        self.sextoContainer["pady"] = 10
        self.sextoContainer["bg"] = "white"
        self.sextoContainer.pack()

        self.setimoContainer = Frame(self.master)
        self.setimoContainer["pady"] = 10
        self.setimoContainer["bg"] = "white"
        self.setimoContainer.pack()

        self.oitavoContainer = Frame(self.master)
        self.oitavoContainer["pady"] = 10
        self.oitavoContainer["bg"] = "white"
        self.oitavoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="ANÁLISE DO ESTOQUE - KIT")
        self.titulo["font"] = ("Arial", "14", "bold")
        self.titulo["bg"] = "white"
        self.titulo.pack()

        self.nome = Label(self.segundoContainer,width = 100,fg = "#003366")
        self.nome["width"] = 60
        self.nome["font"] = ("Arial", "10", "bold")
        self.nome["bg"] = "white"
        self.nome["font"] = self.fontePadrao
        self.nome.pack()

        self.nomeLabel = Button(self.terceiroContainer,text="Escolha o arquivo: KIT", font=self.fontePadrao)
        self.nomeLabel["command"] = self.browseFiles
        self.nomeLabel["width"] = 40
        self.nomeLabel["height"] = 2
        self.nomeLabel["bg"] = "#003366"
        self.nomeLabel["fg"] = "white"
        self.nomeLabel["font"] = ("Arial", "14", "bold")
        self.nomeLabel.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "AUTOMATIZAÇÃO - clique 2x"
        self.autenticar["width"] = 40
        self.autenticar["height"] = 2
        self.autenticar["bg"] = "#003366"
        self.autenticar["fg"] = "white"
        self.autenticar["font"] = ("Arial", "14", "bold")
        self.autenticar["command"] = self.automPF
        self.autenticar.pack()

        self.aguarde = Label(self.sextoContainer,text="", font=self.fontePadrao, width=30)
        self.aguarde["bg"] = "white"
        self.aguarde["font"] = ("Arial", "14", "bold")
        self.aguarde.pack(side=LEFT)

        self.downloadNote = Button(self.quintoContainer,text="DOWNLOAD - KIT", font=self.fontePadrao)
        self.downloadNote["command"] = self.downloadPF
        self.downloadNote["width"] = 40
        self.downloadNote["height"] = 2
        self.downloadNote["font"] = ("Arial", "14", "bold")
        self.downloadNote["bg"] = "#003366"
        self.downloadNote["fg"] = "white"
        self.downloadNote.pack(side=LEFT)

        self.voltar = Button(self.setimoContainer,text="VOLTAR", font=self.fontePadrao)
        self.voltar["command"] = self.menu
        self.voltar["width"] = 10
        self.voltar["height"] = 1
        self.voltar["bg"] = "#000"
        self.voltar["fg"] = "white"
        self.voltar.pack(side=LEFT)
        

    def menu(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(self.master)
        self.primeiroContainer["pady"] = 30
        self.primeiroContainer["bg"] = "white"
        self.primeiroContainer.pack()

        self.terceiroContainer = Frame(self.master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["bg"] = "white"
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(self.master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer["bg"] = "white"
        self.quartoContainer.pack()

        self.quintoContainer = Frame(self.master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer["bg"] = "white"
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="MENU")
        self.titulo["font"] = ("Arial", "40", "bold")
        self.titulo["bg"] = "white"
        self.titulo.pack()

        self.nomeLabel = Button(self.terceiroContainer,text="KIT", font=self.fontePadrao)
        self.nomeLabel["width"] = 40
        self.nomeLabel["height"] = 5
        self.nomeLabel["bg"] = "#003366"
        self.nomeLabel["fg"] = "white"
        self.nomeLabel["font"] = ("Arial", "14", "bold")
        self.nomeLabel["command"] = self.kit
        self.nomeLabel.pack()

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "CAIXA"
        self.autenticar["width"] = 40
        self.autenticar["height"] = 5
        self.autenticar["bg"] = "#003366"
        self.autenticar["fg"] = "white"
        self.autenticar["font"] = ("Arial", "14", "bold")
        self.autenticar["command"] = self.caixa
        self.autenticar.pack()

    def caixa(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(self.master)
        self.primeiroContainer["bg"] = "white"
        self.primeiroContainer["pady"] = 30
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(self.master)
        self.segundoContainer["bg"] = "white"
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(self.master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["bg"] = "white"
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(self.master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer["bg"] = "white"
        self.quartoContainer.pack()

        self.quintoContainer = Frame(self.master)
        self.quintoContainer["pady"] = 10
        self.quintoContainer["bg"] = "white"
        self.quintoContainer.pack()

        self.sextoContainer = Frame(self.master)
        self.sextoContainer["pady"] = 10
        self.sextoContainer["bg"] = "white"
        self.sextoContainer.pack()

        self.setimoContainer = Frame(self.master)
        self.setimoContainer["pady"] = 10
        self.setimoContainer["bg"] = "white"
        self.setimoContainer.pack()

        self.oitavoContainer = Frame(self.master)
        self.oitavoContainer["pady"] = 10
        self.oitavoContainer["bg"] = "white"
        self.oitavoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="ANÁLISE DO ESTOQUE - CAIXA")
        self.titulo["font"] = ("Arial", "14", "bold")
        self.titulo["bg"] = "white"
        self.titulo.pack()

        self.nome = Label(self.segundoContainer,width = 100,fg = "#003366")
        self.nome["width"] = 60
        self.nome["font"] = ("Arial", "10", "bold")
        self.nome["bg"] = "white"
        self.nome["font"] = self.fontePadrao
        self.nome.pack()

        self.nomeLabel = Button(self.terceiroContainer,text="Escolha o arquivo: CAIXA", font=self.fontePadrao)
        self.nomeLabel["width"] = 40
        self.nomeLabel["height"] = 2
        self.nomeLabel["bg"] = "#003366"
        self.nomeLabel["fg"] = "white"
        self.nomeLabel["font"] = ("Arial", "14", "bold")
        self.nomeLabel.pack(side=LEFT)
        self.nomeLabel["command"] = self.browseFiles

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "AUTOMATIZAÇÃO - clique 2x"
        self.autenticar["width"] = 40
        self.autenticar["height"] = 2
        self.autenticar["bg"] = "#003366"
        self.autenticar["fg"] = "white"
        self.autenticar["font"] = ("Arial", "14", "bold")
        self.autenticar["command"] = self.automPJ
        self.autenticar.pack()

        self.aguarde = Label(self.sextoContainer,text="", font=self.fontePadrao, width=30)
        self.aguarde["bg"] = "white"
        self.aguarde["font"] = ("Arial", "14", "bold")
        self.aguarde.pack(side=LEFT)

        self.downloadNote = Button(self.quintoContainer,text="DOWNLOAD - CAIXA", font=self.fontePadrao)
        self.downloadNote["command"] = self.downloadPJ
        self.downloadNote["width"] = 40
        self.downloadNote["height"] = 2
        self.downloadNote["font"] = ("Arial", "14", "bold")
        self.downloadNote["bg"] = "#003366"
        self.downloadNote["fg"] = "white"
        self.downloadNote.pack(side=LEFT)


        self.voltar = Button(self.setimoContainer,text="VOLTAR", font=self.fontePadrao)
        self.voltar["command"] = self.menu
        self.voltar["width"] = 10
        self.voltar["height"] = 1
        self.voltar["bg"] = "#000"
        self.voltar["fg"] = "white"
        self.voltar.pack(side=LEFT)

    def downloadPF(self):

        self.aguarde.config(bg='red')
        self.aguarde.after(0000, lambda: self.aguarde.config(text='Aguarde...'))
        import os

        path = PATHNOTEDIR
        
        # Getting the list of directories
        dir = os.listdir(path)
        
        # Checking if the list is empty or not
        if len(dir) == 0:
            self.aguarde.after(1000, lambda: self.aguarde.config(bg="orange",text='Coloque para automatizar!'))
        else:
            self.aguarde.after(3000, lambda: self.aguarde.config(bg="green",text='Finalizado!')) # after 1000ms

        nome = "PF"
        nameNotePF(nome)
        downloadN()

    def downloadPJ(self):

        self.aguarde.config(bg='red')
        self.aguarde.after(0000, lambda: self.aguarde.config(text='Aguarde...'))
        import os

        path = PATHNOTEDIR
        
        # Getting the list of directories
        dir = os.listdir(path)
        
        # Checking if the list is empty or not
        if len(dir) == 0:
            self.aguarde.after(1000, lambda: self.aguarde.config(bg="orange",text='Coloque para automatizar!'))
        else:
            self.aguarde.after(3000, lambda: self.aguarde.config(bg="green",text='Finalizado!')) # after 1000ms

        nome = "PJ"
        nameNotePJ(nome)
        downloadN()

    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Selecionar arquivo",
                                            filetypes=[("Excel files", ".xlsx .xls")])
        # Change label contents
        self.nome.configure(text=filename)

    def automPF(self):
        if (self.nome["text"] == ""):
            self.aguarde.after(0000, lambda: self.aguarde.config(bg="orange",text='Insira o arquivo!'))
        else:
            self.autenticar["command"] = self.exportPF
            self.aguarde.after(2000, lambda: self.aguarde.config(bg="green",text='Automatiçao finalizada!'))

    def automPJ(self):
        if (self.nome["text"] == ""):
            self.aguarde.after(0000, lambda: self.aguarde.config(bg="orange",text='Insira o arquivo!'))
        else:
            self.autenticar["command"] = self.exportPJ
            self.aguarde.after(2000, lambda: self.aguarde.config(bg="green",text='Automatiçao finalizada!'))

    def exportPF(self):
        pathExcelKIT = self.nome["text"]

        import pandas as pd

        ignore = list(range(0, 5))
        ignore.append(6)
        #xls/SAL2223.xlsx
        df = pd.read_excel(pathExcelKIT, sheet_name = "Plan1", skiprows = ignore)
        bremove = df.loc[df['Lote'].str.contains('B', na=False)]
        df.drop(bremove.index, inplace = True)
        nan = df.loc[df['Lote'].isna()]
        df.drop(nan.index, inplace = True)

        # PEIXES
        bacalhau = df.loc[df['Codigo'].str.contains('LBAMS-PT', na=False)]
        camarao = df.loc[df['Codigo'].str.contains('CAM', na=False)]
        fileSalm = df.loc[df['Produto'].str.contains('SALMAO', na=False)]
        fileLing = df.loc[df['Codigo'].str.contains('FLIFE-BR', na=False)]
        polvo = df.loc[df['Produto'].str.contains('POLVO', na=False)]
        vieira = df.loc[df['Codigo'].str.contains('VIEPN-PR', na=False)]

        peixes = pd.concat([bacalhau, camarao, fileSalm, fileLing, polvo, vieira], ignore_index = True)
        #print(peixes)

        #Variações

        camMCar_sp = df.loc[df['Codigo'].str.contains('CAMMC-AR', na=False)& df['Produto'].str.contains('CAMARÃO S/PELE')]
        camMCar_cr = df.loc[df['Codigo'].str.contains('CAMMC-AR', na=False)& df['Produto'].str.contains('CAMARÃO C/RABO')]
        camMRbr = df.loc[df['Codigo'].str.contains('CAMMR-BR', na=False)]
        camPNar = df.loc[df['Codigo'].str.contains('CAMPN-AR', na=False)]

        df.drop(bacalhau.index, inplace = True)
        df.drop(camMCar_sp.index, inplace = True)
        df.drop(camMCar_cr.index, inplace = True)
        df.drop(camMRbr.index, inplace = True)
        df.drop(camPNar.index, inplace = True)
        df.drop(fileSalm.index, inplace = True)
        df.drop(polvo.index, inplace = True)
        df.drop(vieira.index, inplace = True)

        #CARNES
        picanha = df.loc[df['Codigo'].str.contains('PIC', na=False)]
        fileCostela = df.loc[(df['Produto'].str.contains('COSTELA', na=False)) & df['Codigo'].str.contains('FC')]
        contFile = df.loc[(df['Produto'].str.contains('CONTRA FILE', na=False)) & df['Codigo'].str.contains('CFI')]

        carnesTop = pd.concat([picanha, fileCostela, contFile], ignore_index = True)

        #print(carnesTop)

        #Variações

        picBBar = df.loc[df['Codigo'].str.contains('PICBB-AR', na=False)]
        picCJar = df.loc[df['Codigo'].str.contains('PICCJ-AR', na=False)]
        picCPuy = df.loc[df['Codigo'].str.contains('PICCP-UY', na=False)]
        picFBar = df.loc[df['Codigo'].str.contains('PICFB-AR', na=False)]
        picFCpy = df.loc[df['Codigo'].str.contains('PICFC-PY', na=False)]
        picFGar = df.loc[df['Codigo'].str.contains('PICFG-AR', na=False)]
        picGRpy = df.loc[df['Codigo'].str.contains('PICGR-PY', na=False)]
        picLMuy = df.loc[df['Codigo'].str.contains('PICLM-UY', na=False)]
        picNGbr = df.loc[df['Codigo'].str.contains('PICNG-BR', na=False)]
        picPDuy = df.loc[df['Codigo'].str.contains('PICPD-UY', na=False)]
        picPIarC = df.loc[df['Codigo'].str.contains('PICPI-AR-01C', na=False)]
        picPIarR = df.loc[df['Codigo'].str.contains('PICPI-AR-01R', na=False)]
        picSOuy = df.loc[df['Codigo'].str.contains('PICSO-UY', na=False)]
        picZMbr = df.loc[df['Codigo'].str.contains('PICZM-BR', na=False)]

        df.drop(picBBar.index, inplace = True)
        df.drop(picCJar.index, inplace = True)
        df.drop(picCPuy.index, inplace = True)
        df.drop(picFBar.index, inplace = True)
        df.drop(picFCpy.index, inplace = True)
        df.drop(picFGar.index, inplace = True)
        df.drop(picGRpy.index, inplace = True)
        df.drop(picLMuy.index, inplace = True)
        df.drop(picNGbr.index, inplace = True)
        df.drop(picPDuy.index, inplace = True)
        df.drop(picPIarC.index, inplace = True)
        df.drop(picPIarR.index, inplace = True)
        df.drop(picSOuy.index, inplace = True)
        df.drop(picZMbr.index, inplace = True)


        fcCCRbr = df.loc[df['Codigo'].str.contains('FCCCR-BR', na=False)]
        fcCFRbr = df.loc[df['Codigo'].str.contains('FCCFR-BR', na=False)] 
        fcCNSbr = df.loc[df['Codigo'].str.contains('FCCBS-BR', na=False)]
        fcOBBar = df.loc[df['Codigo'].str.contains('FCOBB-AR', na=False)]
        fcOCPuy = df.loc[df['Codigo'].str.contains('FCOCP-UY', na=False)]
        fcOIFuy = df.loc[df['Codigo'].str.contains('FCOIF-UY', na=False)]
        fcOLMuy = df.loc[df['Codigo'].str.contains('FCOLM-UY', na=False)] 
        fcOOPar = df.loc[df['Codigo'].str.contains('FCOOP-AR', na=False)]
        fcOPDuy = df.loc[df['Codigo'].str.contains('FCOPD-UY', na=False)]
        fcOPIar = df.loc[df['Codigo'].str.contains('FCOPI-AR', na=False)]
        fcOSOuy = df.loc[df['Codigo'].str.contains('FCOSO-UY', na=False)] 

        df.drop(fcCCRbr.index, inplace = True)
        df.drop(fcCFRbr.index, inplace = True)
        df.drop(fcCNSbr.index, inplace = True)
        df.drop(fcOBBar.index, inplace = True)
        df.drop(fcOCPuy.index, inplace = True)
        df.drop(fcOIFuy.index, inplace = True)
        df.drop(fcOLMuy.index, inplace = True)
        df.drop(fcOOPar.index, inplace = True)
        df.drop(fcOPDuy.index, inplace = True)
        df.drop(fcOPIar.index, inplace = True)
        df.drop(fcOSOuy.index, inplace = True)

        cfIBBar = df.loc[df['Codigo'].str.contains('CFIBB-AR', na=False)] 
        cfiBSbr = df.loc[df['Codigo'].str.contains('CFIBS-BR', na=False)] 
        cfiCPuy = df.loc[df['Codigo'].str.contains('CFICP-UY', na=False)]
        cfiFRbr = df.loc[df['Codigo'].str.contains('CFIFR-BR', na=False)]
        cfiGRpy = df.loc[df['Codigo'].str.contains('CFIGR-PY', na=False)]
        cfiIFuy = df.loc[df['Codigo'].str.contains('CFIIF-UY', na=False)]
        cfiLMuy = df.loc[df['Codigo'].str.contains('CFILM-UY', na=False)]
        cfiOPar = df.loc[df['Codigo'].str.contains('CFIOP-AR', na=False)]
        cfiPDuy = df.loc[df['Codigo'].str.contains('CFIPD-UY', na=False)]
        cfiPIar = df.loc[df['Codigo'].str.contains('CFIPI-AR', na=False)]
        cfiSOuy = df.loc[df['Codigo'].str.contains('CFISO-UY', na=False)]

        df.drop(cfIBBar.index, inplace = True)
        df.drop(cfiBSbr.index, inplace = True)
        df.drop(cfiCPuy.index, inplace = True)
        df.drop(cfiFRbr.index, inplace = True)
        df.drop(cfiGRpy.index, inplace = True)
        df.drop(cfiIFuy.index, inplace = True)
        df.drop(cfiLMuy.index, inplace = True)
        df.drop(cfiOPar.index, inplace = True)
        df.drop(cfiPDuy.index, inplace = True)
        df.drop(cfiPIar.index, inplace = True)
        df.drop(cfiSOuy.index, inplace = True)


        accCRbr = df.loc[df['Codigo'].str.contains('ACCCR-BR', na=False)]
        accFRbr = df.loc[df['Codigo'].str.contains('ACCFR-BR', na=False)]
        accFUbr = df.loc[df['Codigo'].str.contains('ACCFU-BR', na=False)]
        df.drop(accCRbr.index, inplace = True)
        df.drop(accFRbr.index, inplace = True)
        df.drop(accFUbr.index, inplace = True)

        alcFCpy = df.loc[df['Codigo'].str.contains('ALCFC-PY', na=False)]
        df.drop(alcFCpy.index, inplace = True)

        atiBSbr = df.loc[df['Codigo'].str.contains('ATIBS-BR', na=False)]
        atiCRbr = df.loc[df['Codigo'].str.contains('ATICR-BR', na=False)]
        atiFRbr = df.loc[df['Codigo'].str.contains('ATIFR-BR', na=False)]
        atiPDuy = df.loc[df['Codigo'].str.contains('ATIPD-UY', na=False)]
        df.drop(atiBSbr.index, inplace = True)
        df.drop(atiCRbr.index, inplace = True)
        df.drop(atiFRbr.index, inplace = True)
        df.drop(atiPDuy.index, inplace = True)

        bar19br = df.loc[df['Codigo'].str.contains('BAR19-BR', na=False)]
        bbmFRbr = df.loc[df['Codigo'].str.contains('BBMFR-BR', na=False)]
        df.drop(bar19br.index, inplace = True)
        df.drop(bbmFRbr.index, inplace = True)

        carDCuy = df.loc[df['Codigo'].str.contains('CARDC-UY', na=False)]
        df.drop(carDCuy.index, inplace = True)

        cfrGTar = df.loc[df['Codigo'].str.contains('CFRGT-AR', na=False)]
        cfrPOar = df.loc[df['Codigo'].str.contains('CFRPO-AR', na=False)]
        df.drop(cfrGTar.index, inplace = True)
        df.drop(cfrPOar.index, inplace = True)

        cosFRbr = df.loc[df['Codigo'].str.contains('COSFR-BR', na=False)]
        cosGAbr = df.loc[df['Codigo'].str.contains('COSGA-BR', na=False)]
        cosPDuy = df.loc[df['Codigo'].str.contains('COSPD-UY', na=False)]
        cosSWbr = df.loc[df['Codigo'].str.contains('COSSW-BR', na=False)]
        cotGAbr = df.loc[df['Codigo'].str.contains('COTGA-BR', na=False)]

        df.drop(cosFRbr.index, inplace = True)
        df.drop(cosGAbr.index, inplace = True)
        df.drop(cosPDuy.index, inplace = True)
        df.drop(cosSWbr.index, inplace = True)
        df.drop(cotGAbr.index, inplace = True)

        fliFEbr = df.loc[df['Codigo'].str.contains('FLIFE-BR', na=False)]
        df.drop(fliFEbr.index, inplace = True)

        fmiBCbr = df.loc[df['Codigo'].str.contains('FMIBC-BR', na=False)]
        df.drop(fmiBCbr.index, inplace = True)

        frCFCuy = df.loc[df['Codigo'].str.contains('FRCFC-UY', na=False)]
        frDCRbr = df.loc[df['Codigo'].str.contains('FRDCR-BR', na=False)]
        frSCPuy = df.loc[df['Codigo'].str.contains('FRSCP-UY', na=False)]
        frSFRbr = df.loc[df['Codigo'].str.contains('FRSFR-BR', na=False)]
        frSIFuy = df.loc[df['Codigo'].str.contains('FRSIF-UY', na=False)]
        frSLMuy = df.loc[df['Codigo'].str.contains('FRSLM-UY', na=False)]
        frSPDuy = df.loc[df['Codigo'].str.contains('FRSPD-UY', na=False)]
        frSSOuy = df.loc[df['Codigo'].str.contains('FRSSO-UY', na=False)]

        df.drop(frCFCuy.index, inplace = True)
        df.drop(frDCRbr.index, inplace = True)
        df.drop(frSCPuy.index, inplace = True)
        df.drop(frSFRbr.index, inplace = True)
        df.drop(frSIFuy.index, inplace = True)
        df.drop(frSLMuy.index, inplace = True)
        df.drop(frSPDuy.index, inplace = True)
        df.drop(frSSOuy.index, inplace = True)

        icfFRbr = df.loc[df['Codigo'].str.contains('ICFFR-BR', na=False)]
        df.drop(icfFRbr.index, inplace = True)

        intBCbr = df.loc[df['Codigo'].str.contains('INTBC-BR', na=False)] 
        df.drop(intBCbr.index, inplace = True)

        linSBuy = df.loc[df['Codigo'].str.contains('LINSB-UY', na=False)]
        df.drop(linSBuy.index, inplace = True)

        macBBar = df.loc[df['Codigo'].str.contains('MACBB-AR', na=False)]
        malBBar = df.loc[df['Codigo'].str.contains('MALBB-AR', na=False)]
        malCPuy = df.loc[df['Codigo'].str.contains('MALCP-UY', na=False)]
        malFCpy = df.loc[df['Codigo'].str.contains('MALFC-PY', na=False)]
        malGRpy = df.loc[df['Codigo'].str.contains('MALGR-PY', na=False)]
        malIFuy = df.loc[df['Codigo'].str.contains('MALIF-UY', na=False)]
        malPIar = df.loc[df['Codigo'].str.contains('MALPI-AR', na=False)]
        malSOuy = df.loc[df['Codigo'].str.contains('MALSO-UY', na=False)]

        df.drop(macBBar.index, inplace = True)
        df.drop(malBBar.index, inplace = True)
        df.drop(malCPuy.index, inplace = True)
        df.drop(malFCpy.index, inplace = True)
        df.drop(malGRpy.index, inplace = True)
        df.drop(malIFuy.index, inplace = True)
        df.drop(malPIar.index, inplace = True)
        df.drop(malSOuy.index, inplace = True)

        mamBSbr = df.loc[df['Codigo'].str.contains('MAMBS-BR', na=False)]
        mamFCpy = df.loc[df['Codigo'].str.contains('MAMFC-PY', na=False)]
        mamLMuy = df.loc[df['Codigo'].str.contains('MAMLM-UY', na=False)]
        mamPIar = df.loc[df['Codigo'].str.contains('MAMPI-AR', na=False)]
        mamSOuy = df.loc[df['Codigo'].str.contains('MAMSO-UY', na=False)]

        df.drop(mamBSbr.index, inplace = True)
        df.drop(mamFCpy.index, inplace = True)
        df.drop(mamLMuy.index, inplace = True)
        df.drop(mamPIar.index, inplace = True)
        df.drop(mamSOuy.index, inplace = True)

        pltDCuy = df.loc[df['Codigo'].str.contains('PLTDC-UY', na=False)]
        df.drop(pltDCuy.index, inplace = True)

        raqBBar = df.loc[df['Codigo'].str.contains('RAQBB-AR', na=False)]
        df.drop(raqBBar.index, inplace = True)

        tbExc = df.loc[df['Produto'].str.contains('T BONE', na=False)]
        tboCRbr = df.loc[df['Codigo'].str.contains('TBOCR-BR', na=False)]
        tboFRbr = df.loc[df['Codigo'].str.contains('TBOFR-BR', na=False)] 
        tboOPar = df.loc[df['Codigo'].str.contains('TBOOP-AR', na=False)] 

        df.drop(tbExc.index, inplace = True)
        df.drop(tboCRbr.index, inplace = True)
        df.drop(tboFRbr.index, inplace = True)
        df.drop(tboOPar.index, inplace = True)

        dTbone = pd.concat([tbExc, tboCRbr, tboFRbr, tboOPar], ignore_index = True)

        caixa = df.loc[df['Codigo'].str.contains('SUD-800', na=False)]
        df.drop(caixa.index, inplace = True)

        #PRODUTO NÃO CADASTRADO
        if not df.empty:
            print(df)


        dTotal = pd.concat([peixes, bremove, carnesTop, df, dTbone, caixa], ignore_index = True)
        #print(dTotal)

        try:
            dadosGeral = pd.DataFrame(data=dTotal)
            #print(dadosGeral)
        except (NameError):
            print('Por favor, atualize o programa novamente...')
        pass

        writer = pd.ExcelWriter(r'C:\Users\Karol\Desktop\excel-python\test\excel\SaldoProdPF.xlsx')
        dadosGeral.to_excel(writer, sheet_name='Geral', index=False)
        writer.save()
        '''
        'r' -> Usado para ler
        'w' -> Usado para escrever
        'r+' -> Ler e escrever
        'a' -> acrescentar algo
        '''

        dftitulo = pd.read_excel(pathExcelKIT, sheet_name = "Plan1")
        titulo = list(range(0, 4))
        titnote = dftitulo.iloc[titulo]
        colunas = dftitulo.iloc[[4]]
        dftitulo = pd.read_excel(pathExcelKIT, sheet_name = "Plan1", skiprows = ignore)
        rodape = dftitulo.loc[dftitulo['Lote'].isna()]

        import os
        dir = r'C:\Users\Karol\Desktop\excel-python\test\note'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

        titnote.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='w')
        with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
            f.write("======================================================================================================================================================================================\n")
        colunas.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')
        with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
            f.write("======================================================================================================================================================================================\n")
            f.write("                                                                                      PEIXES                                                                                          \n")
            f.write("======================================================================================================================================================================================\n")
        if not bacalhau.empty:
            bacalhau.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')

        if not camMCar_sp.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            camMCar_sp.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')
        if not camMCar_cr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            camMCar_cr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')
        if not camMRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            camMRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')
        if not camPNar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            camPNar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')
        if not fileSalm.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fileSalm.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')
        if not fileLing.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fileLing.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')

        if not polvo.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            polvo.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')
        if not vieira.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            polvo.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')
        with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a', encoding="utf=8") as f:
            f.write("======================================================================================================================================================================================\n")
            f.write("                                                                                   NÃO VENDEMOS                                                                                       \n")
            f.write("======================================================================================================================================================================================\n")
        if not bremove.empty:
            bremove.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')
        else:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a', encoding="utf=8") as f:
                f.write("                                                                         Nenhum produto foi encontrado                                                                              \n")
        with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a', encoding="utf=8") as f:
            f.write("======================================================================================================================================================================================\n")
            f.write("                                                                                      CARNES                                                                                          \n")
            f.write("======================================================================================================================================================================================\n")
        if not picBBar.empty:
            picBBar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')
        if not picCJar.empty:
            if picBBar.empty:
                picCJar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
            else:
                with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                    f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                picCJar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not picCPuy.empty:
            if picCJar.empty:
                picCPuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')
            else: 
                with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                    f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                picCPuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not picFBar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picFBar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not picFCpy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picFCpy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not picFGar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picFGar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not picGRpy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picGRpy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not picLMuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picLMuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not picNGbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picNGbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not picPDuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picPDuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not picPIarC.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picPIarC.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not picPIarR.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picPIarR.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not picSOuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picSOuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not picZMbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picZMbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 




        if not fcCCRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcCCRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcCFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcCFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcCNSbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcCNSbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcOBBar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcOBBar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcOCPuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcOCPuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcOIFuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcOIFuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcOLMuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcOLMuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcOOPar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcOOPar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcOPDuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcOPDuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcOPIar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcOPIar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcOSOuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcOSOuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a') 




        if not cfIBBar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfIBBar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiBSbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiBSbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiCPuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiCPuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiGRpy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiGRpy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiIFuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiIFuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')
        if not cfiLMuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiLMuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiOPar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiOPar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiPDuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiPDuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiPIar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiPIar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiSOuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiSOuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    




        if not accCRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            accCRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not accFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            accFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not accFUbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            accFUbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not alcFCpy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            alcFCpy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    

        if not atiBSbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            atiBSbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not atiCRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            atiCRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not atiFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            atiFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not atiPDuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            atiPDuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    

        if not bar19br.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            bar19br.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not bbmFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            bbmFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    


        if not carDCuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            carDCuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    

        if not cfrGTar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfrGTar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfrPOar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfrPOar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    

        if not cosFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cosFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not cosGAbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cosGAbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not cosPDuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cosPDuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not cosSWbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cosSWbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not cotGAbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cotGAbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    

        if not fliFEbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fliFEbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    

        if not fmiBCbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fmiBCbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    

        if not frCFCuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            frCFCuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not frDCRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            frDCRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not frSCPuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            frSCPuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not frSFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            frSFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not frSIFuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            frSIFuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not frSLMuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            frSLMuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not frSPDuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            frSPDuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not frSSOuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            frSSOuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not icfFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            icfFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not intBCbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            intBCbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    

        if not linSBuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            linSBuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    

        if not macBBar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            macBBar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not malBBar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            malBBar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not malCPuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            malCPuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not malFCpy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            malFCpy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not malGRpy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            malGRpy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not malIFuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            malIFuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not malPIar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            malPIar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not malSOuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            malSOuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not mamBSbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            mamBSbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not mamFCpy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            mamFCpy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    

        if not mamLMuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            mamLMuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not mamPIar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            mamPIar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    

        if not mamSOuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            mamSOuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not pltDCuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            pltDCuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    

        if not raqBBar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            raqBBar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    

        if not tbExc.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            tbExc.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not tboCRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            tboCRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')
        if not tboFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            tboFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')
        if not tboOPar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            tboOPar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')


        #df.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')

        with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a', encoding="utf=8") as f:
            f.write("======================================================================================================================================================================================\n")
            f.write("                                                                                      OUTROS                                                                                          \n")
            f.write("======================================================================================================================================================================================\n")
        if not caixa.empty:
            caixa.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')
        else:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a', encoding="utf=8") as f:
                f.write("                                                                         Nenhum produto foi encontrado                                                                              \n")
        with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a', encoding="utf=8") as f:
            f.write("======================================================================================================================================================================================\n")
        with open('C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', 'a', encoding="utf=8") as f:
            f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            f.write("                                                   Obs.: (*) - sem NF de Armazenagem         (B) - Bloqueado         (v) - Peso Variavel                                              \n")
        #dadosGeral.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')

        """ with open('C:/Users/Karol/Desktop/excel-python/PF.txt', 'w') as f:
            for line in dTotal:
                dTotal.write(str(line)+'\n') """

    def exportPJ(self):

        import pandas as pd
        ignore = list(range(0, 5))
        ignore.append(6)
        #'xls/SAL1146.xls'
        pathExcelCaixa = self.nome["text"] 
        df = pd.read_excel(pathExcelCaixa, sheet_name = "Plan1", skiprows = ignore)

        bremove = df.loc[df['Lote'].str.contains('B', na=False)]
        df.drop(bremove.index, inplace = True)
        nan = df.loc[df['Lote'].isna()]
        df.drop(nan.index, inplace = True)

        # PEIXES
        bacalhau = df.loc[df['Codigo'].str.contains('LBAMS-PT', na=False)]
        camarao = df.loc[df['Codigo'].str.contains('CAM', na=False)]
        fileSalm = df.loc[df['Produto'].str.contains('SALMAO', na=False)]
        fileLing = df.loc[df['Codigo'].str.contains('FLIFE-BR', na=False)]
        polvo = df.loc[df['Produto'].str.contains('POLVO', na=False)]
        vieira = df.loc[df['Codigo'].str.contains('VIEPN-PR', na=False)]

        peixes = pd.concat([bacalhau, camarao, fileSalm, fileLing, polvo, vieira], ignore_index = True)
        #print(peixes)

        #Variações

        camMCar_sp = df.loc[df['Codigo'].str.contains('CAMMC-AR', na=False)& df['Produto'].str.contains('CAMARÃO S/PELE')]
        camMCar_cr = df.loc[df['Codigo'].str.contains('CAMMC-AR', na=False)& df['Produto'].str.contains('CAMARÃO C/RABO')]
        camMRbr = df.loc[df['Codigo'].str.contains('CAMMR-BR', na=False)]
        camPNar = df.loc[df['Codigo'].str.contains('CAMPN-AR', na=False)]

        df.drop(bacalhau.index, inplace = True)
        df.drop(camMCar_sp.index, inplace = True)
        df.drop(camMCar_cr.index, inplace = True)
        df.drop(camMRbr.index, inplace = True)
        df.drop(camPNar.index, inplace = True)
        df.drop(fileSalm.index, inplace = True)
        df.drop(polvo.index, inplace = True)
        df.drop(vieira.index, inplace = True)

        #CARNES
        picanha = df.loc[df['Codigo'].str.contains('PIC', na=False)]
        fileCostela = df.loc[(df['Produto'].str.contains('COSTELA', na=False)) & df['Codigo'].str.contains('FC')]
        contFile = df.loc[(df['Produto'].str.contains('CONTRA FILE', na=False)) & df['Codigo'].str.contains('CFI')]

        carnesTop = pd.concat([picanha, fileCostela, contFile], ignore_index = True)

        #print(carnesTop)

        #Variações

        picBBar = df.loc[df['Codigo'].str.contains('PICBB-AR', na=False)]
        picCJar = df.loc[df['Codigo'].str.contains('PICCJ-AR', na=False)]
        picCPuy = df.loc[df['Codigo'].str.contains('PICCP-UY', na=False)]
        picFBar = df.loc[df['Codigo'].str.contains('PICFB-AR', na=False)]
        picFCpy = df.loc[df['Codigo'].str.contains('PICFC-PY', na=False)]
        picFGar = df.loc[df['Codigo'].str.contains('PICFG-AR', na=False)]
        picGRpy = df.loc[df['Codigo'].str.contains('PICGR-PY', na=False)]
        picLMuy = df.loc[df['Codigo'].str.contains('PICLM-UY', na=False)]
        picNGbr = df.loc[df['Codigo'].str.contains('PICNG-BR', na=False)]
        picPDuy = df.loc[df['Codigo'].str.contains('PICPD-UY', na=False)]
        picPIarC = df.loc[df['Codigo'].str.contains('PICPI-AR-01C', na=False)]
        picPIarR = df.loc[df['Codigo'].str.contains('PICPI-AR-01R', na=False)]
        picSOuy = df.loc[df['Codigo'].str.contains('PICSO-UY', na=False)]
        picZMbr = df.loc[df['Codigo'].str.contains('PICZM-BR', na=False)]

        df.drop(picBBar.index, inplace = True)
        df.drop(picCJar.index, inplace = True)
        df.drop(picCPuy.index, inplace = True)
        df.drop(picFBar.index, inplace = True)
        df.drop(picFCpy.index, inplace = True)
        df.drop(picFGar.index, inplace = True)
        df.drop(picGRpy.index, inplace = True)
        df.drop(picLMuy.index, inplace = True)
        df.drop(picNGbr.index, inplace = True)
        df.drop(picPDuy.index, inplace = True)
        df.drop(picPIarC.index, inplace = True)
        df.drop(picPIarR.index, inplace = True)
        df.drop(picSOuy.index, inplace = True)
        df.drop(picZMbr.index, inplace = True)


        fcCCRbr = df.loc[df['Codigo'].str.contains('FCCCR-BR', na=False)]
        fcCFRbr = df.loc[df['Codigo'].str.contains('FCCFR-BR', na=False)] 
        fcCNSbr = df.loc[df['Codigo'].str.contains('FCCBS-BR', na=False)]
        fcOBBar = df.loc[df['Codigo'].str.contains('FCOBB-AR', na=False)]
        fcOCPuy = df.loc[df['Codigo'].str.contains('FCOCP-UY', na=False)]
        fcOIFuy = df.loc[df['Codigo'].str.contains('FCOIF-UY', na=False)]
        fcOLMuy = df.loc[df['Codigo'].str.contains('FCOLM-UY', na=False)] 
        fcOOPar = df.loc[df['Codigo'].str.contains('FCOOP-AR', na=False)]
        fcOPDuy = df.loc[df['Codigo'].str.contains('FCOPD-UY', na=False)]
        fcOPIar = df.loc[df['Codigo'].str.contains('FCOPI-AR', na=False)]
        fcOSOuy = df.loc[df['Codigo'].str.contains('FCOSO-UY', na=False)] 

        df.drop(fcCCRbr.index, inplace = True)
        df.drop(fcCFRbr.index, inplace = True)
        df.drop(fcCNSbr.index, inplace = True)
        df.drop(fcOBBar.index, inplace = True)
        df.drop(fcOCPuy.index, inplace = True)
        df.drop(fcOIFuy.index, inplace = True)
        df.drop(fcOLMuy.index, inplace = True)
        df.drop(fcOOPar.index, inplace = True)
        df.drop(fcOPDuy.index, inplace = True)
        df.drop(fcOPIar.index, inplace = True)
        df.drop(fcOSOuy.index, inplace = True)

        cfIBBar = df.loc[df['Codigo'].str.contains('CFIBB-AR', na=False)] 
        cfiBSbr = df.loc[df['Codigo'].str.contains('CFIBS-BR', na=False)] 
        cfiCPuy = df.loc[df['Codigo'].str.contains('CFICP-UY', na=False)]
        cfiFRbr = df.loc[df['Codigo'].str.contains('CFIFR-BR', na=False)]
        cfiGRpy = df.loc[df['Codigo'].str.contains('CFIGR-PY', na=False)]
        cfiIFuy = df.loc[df['Codigo'].str.contains('CFIIF-UY', na=False)]
        cfiLMuy = df.loc[df['Codigo'].str.contains('CFILM-UY', na=False)]
        cfiOPar = df.loc[df['Codigo'].str.contains('CFIOP-AR', na=False)]
        cfiPDuy = df.loc[df['Codigo'].str.contains('CFIPD-UY', na=False)]
        cfiPIar = df.loc[df['Codigo'].str.contains('CFIPI-AR', na=False)]
        cfiSOuy = df.loc[df['Codigo'].str.contains('CFISO-UY', na=False)]

        df.drop(cfIBBar.index, inplace = True)
        df.drop(cfiBSbr.index, inplace = True)
        df.drop(cfiCPuy.index, inplace = True)
        df.drop(cfiFRbr.index, inplace = True)
        df.drop(cfiGRpy.index, inplace = True)
        df.drop(cfiIFuy.index, inplace = True)
        df.drop(cfiLMuy.index, inplace = True)
        df.drop(cfiOPar.index, inplace = True)
        df.drop(cfiPDuy.index, inplace = True)
        df.drop(cfiPIar.index, inplace = True)
        df.drop(cfiSOuy.index, inplace = True)


        accCRbr = df.loc[df['Codigo'].str.contains('ACCCR-BR', na=False)]
        accFRbr = df.loc[df['Codigo'].str.contains('ACCFR-BR', na=False)]
        accFUbr = df.loc[df['Codigo'].str.contains('ACCFU-BR', na=False)]
        df.drop(accCRbr.index, inplace = True)
        df.drop(accFRbr.index, inplace = True)
        df.drop(accFUbr.index, inplace = True)

        alcFCpy = df.loc[df['Codigo'].str.contains('ALCFC-PY', na=False)]
        df.drop(alcFCpy.index, inplace = True)

        atiBSbr = df.loc[df['Codigo'].str.contains('ATIBS-BR', na=False)]
        atiCRbr = df.loc[df['Codigo'].str.contains('ATICR-BR', na=False)]
        atiFRbr = df.loc[df['Codigo'].str.contains('ATIFR-BR', na=False)]
        atiPDuy = df.loc[df['Codigo'].str.contains('ATIPD-UY', na=False)]
        df.drop(atiBSbr.index, inplace = True)
        df.drop(atiCRbr.index, inplace = True)
        df.drop(atiFRbr.index, inplace = True)
        df.drop(atiPDuy.index, inplace = True)

        bar19br = df.loc[df['Codigo'].str.contains('BAR19-BR', na=False)]
        bbmFRbr = df.loc[df['Codigo'].str.contains('BBMFR-BR', na=False)]
        df.drop(bar19br.index, inplace = True)
        df.drop(bbmFRbr.index, inplace = True)

        carDCuy = df.loc[df['Codigo'].str.contains('CARDC-UY', na=False)]
        df.drop(carDCuy.index, inplace = True)

        cfrGTar = df.loc[df['Codigo'].str.contains('CFRGT-AR', na=False)]
        cfrPOar = df.loc[df['Codigo'].str.contains('CFRPO-AR', na=False)]
        df.drop(cfrGTar.index, inplace = True)
        df.drop(cfrPOar.index, inplace = True)

        cosFRbr = df.loc[df['Codigo'].str.contains('COSFR-BR', na=False)]
        cosGAbr = df.loc[df['Codigo'].str.contains('COSGA-BR', na=False)]
        cosPDuy = df.loc[df['Codigo'].str.contains('COSPD-UY', na=False)]
        cosSWbr = df.loc[df['Codigo'].str.contains('COSSW-BR', na=False)]
        cotGAbr = df.loc[df['Codigo'].str.contains('COTGA-BR', na=False)]

        df.drop(cosFRbr.index, inplace = True)
        df.drop(cosGAbr.index, inplace = True)
        df.drop(cosPDuy.index, inplace = True)
        df.drop(cosSWbr.index, inplace = True)
        df.drop(cotGAbr.index, inplace = True)

        fliFEbr = df.loc[df['Codigo'].str.contains('FLIFE-BR', na=False)]
        df.drop(fliFEbr.index, inplace = True)

        fmiBCbr = df.loc[df['Codigo'].str.contains('FMIBC-BR', na=False)]
        df.drop(fmiBCbr.index, inplace = True)

        frCFCuy = df.loc[df['Codigo'].str.contains('FRCFC-UY', na=False)]
        frDCRbr = df.loc[df['Codigo'].str.contains('FRDCR-BR', na=False)]
        frSCPuy = df.loc[df['Codigo'].str.contains('FRSCP-UY', na=False)]
        frSFRbr = df.loc[df['Codigo'].str.contains('FRSFR-BR', na=False)]
        frSIFuy = df.loc[df['Codigo'].str.contains('FRSIF-UY', na=False)]
        frSLMuy = df.loc[df['Codigo'].str.contains('FRSLM-UY', na=False)]
        frSPDuy = df.loc[df['Codigo'].str.contains('FRSPD-UY', na=False)]
        frSSOuy = df.loc[df['Codigo'].str.contains('FRSSO-UY', na=False)]

        df.drop(frCFCuy.index, inplace = True)
        df.drop(frDCRbr.index, inplace = True)
        df.drop(frSCPuy.index, inplace = True)
        df.drop(frSFRbr.index, inplace = True)
        df.drop(frSIFuy.index, inplace = True)
        df.drop(frSLMuy.index, inplace = True)
        df.drop(frSPDuy.index, inplace = True)
        df.drop(frSSOuy.index, inplace = True)

        icfFRbr = df.loc[df['Codigo'].str.contains('ICFFR-BR', na=False)]
        df.drop(icfFRbr.index, inplace = True)

        intBCbr = df.loc[df['Codigo'].str.contains('INTBC-BR', na=False)] 
        df.drop(intBCbr.index, inplace = True)

        linSBuy = df.loc[df['Codigo'].str.contains('LINSB-UY', na=False)]
        df.drop(linSBuy.index, inplace = True)

        macBBar = df.loc[df['Codigo'].str.contains('MACBB-AR', na=False)]
        malBBar = df.loc[df['Codigo'].str.contains('MALBB-AR', na=False)]
        malCPuy = df.loc[df['Codigo'].str.contains('MALCP-UY', na=False)]
        malFCpy = df.loc[df['Codigo'].str.contains('MALFC-PY', na=False)]
        malGRpy = df.loc[df['Codigo'].str.contains('MALGR-PY', na=False)]
        malIFuy = df.loc[df['Codigo'].str.contains('MALIF-UY', na=False)]
        malPIar = df.loc[df['Codigo'].str.contains('MALPI-AR', na=False)]
        malSOuy = df.loc[df['Codigo'].str.contains('MALSO-UY', na=False)]

        df.drop(macBBar.index, inplace = True)
        df.drop(malBBar.index, inplace = True)
        df.drop(malCPuy.index, inplace = True)
        df.drop(malFCpy.index, inplace = True)
        df.drop(malGRpy.index, inplace = True)
        df.drop(malIFuy.index, inplace = True)
        df.drop(malPIar.index, inplace = True)
        df.drop(malSOuy.index, inplace = True)

        mamBSbr = df.loc[df['Codigo'].str.contains('MAMBS-BR', na=False)]
        mamFCpy = df.loc[df['Codigo'].str.contains('MAMFC-PY', na=False)]
        mamLMuy = df.loc[df['Codigo'].str.contains('MAMLM-UY', na=False)]
        mamPIar = df.loc[df['Codigo'].str.contains('MAMPI-AR', na=False)]
        mamSOuy = df.loc[df['Codigo'].str.contains('MAMSO-UY', na=False)]

        df.drop(mamBSbr.index, inplace = True)
        df.drop(mamFCpy.index, inplace = True)
        df.drop(mamLMuy.index, inplace = True)
        df.drop(mamPIar.index, inplace = True)
        df.drop(mamSOuy.index, inplace = True)

        pltDCuy = df.loc[df['Codigo'].str.contains('PLTDC-UY', na=False)]
        df.drop(pltDCuy.index, inplace = True)

        raqBBar = df.loc[df['Codigo'].str.contains('RAQBB-AR', na=False)]
        df.drop(raqBBar.index, inplace = True)

        tbExc = df.loc[df['Produto'].str.contains('T BONE', na=False)]
        tboCRbr = df.loc[df['Codigo'].str.contains('TBOCR-BR', na=False)]
        tboFRbr = df.loc[df['Codigo'].str.contains('TBOFR-BR', na=False)] 
        tboOPar = df.loc[df['Codigo'].str.contains('TBOOP-AR', na=False)] 

        df.drop(tbExc.index, inplace = True)
        df.drop(tboCRbr.index, inplace = True)
        df.drop(tboFRbr.index, inplace = True)
        df.drop(tboOPar.index, inplace = True)

        dTbone = pd.concat([tbExc, tboCRbr, tboFRbr, tboOPar], ignore_index = True)

        caixa = df.loc[df['Codigo'].str.contains('SUD-800', na=False)]
        df.drop(caixa.index, inplace = True)

        #PRODUTO NÃO CADASTRADO
        if not df.empty:
            print(df)

        dTotal = pd.concat([peixes, bremove, carnesTop, df, dTbone, caixa], ignore_index = True)
        #print(dTotal)

        try:
            dadosGeral = pd.DataFrame(data=dTotal)
            #print(dadosGeral)
        except (NameError):
            print('Por favor, atualize o programa novamente...')
        pass

        writer = pd.ExcelWriter(r'C:\Users\Karol\Desktop\excel-python\excel\SaldoProdPJ.xlsx')
        dadosGeral.to_excel(writer, sheet_name='Geral', index=False)
        writer.save()
        '''
        'r' -> Usado para ler
        'w' -> Usado para escrever
        'r+' -> Ler e escrever
        'a' -> acrescentar algo
        '''
        import os
        dir = r'C:\Users\Karol\Desktop\excel-python\note'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

        dftitulo = pd.read_excel(pathExcelCaixa, sheet_name = "Plan1")
        titulo = list(range(0, 4))
        titnote = dftitulo.iloc[titulo]
        colunas = dftitulo.iloc[[4]]
        dftitulo = pd.read_excel(pathExcelCaixa, sheet_name = "Plan1", skiprows = ignore)
        rodape = dftitulo.loc[dftitulo['Lote'].isna()]


        titnote.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='w')
        with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
            f.write("======================================================================================================================================================================================\n")
        colunas.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
        with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
            f.write("======================================================================================================================================================================================\n")
            f.write("                                                                                      PEIXES                                                                                          \n")
            f.write("======================================================================================================================================================================================\n")
        if not bacalhau.empty:
            bacalhau.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')

        if not camMCar_sp.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            camMCar_sp.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
        if not camMCar_cr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            camMCar_cr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')

        if not camMRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            camMRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
        if not camPNar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            camPNar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
        if not fileSalm.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fileSalm.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
        if not fileLing.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fileLing.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')

        if not polvo.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            polvo.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
        if not vieira.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            vieira.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
        with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a', encoding="utf=8") as f:
            f.write("======================================================================================================================================================================================\n")
            f.write("                                                                                   NÃO VENDEMOS                                                                                       \n")
            f.write("======================================================================================================================================================================================\n")
        if not bremove.empty:
            bremove.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
        with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a', encoding="utf=8") as f:
            f.write("======================================================================================================================================================================================\n")
            f.write("                                                                                      CARNES                                                                                          \n")
            f.write("======================================================================================================================================================================================\n")
        if not picBBar.empty:
            picBBar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
        if not picCJar.empty:
            if picBBar.empty:
                picCJar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
            else:
                with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                    f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                picCJar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not picCPuy.empty:
            if picCJar.empty:
                picCPuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
            else: 
                with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                    f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                picCPuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not picFBar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picFBar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not picFCpy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picFCpy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not picFGar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picFGar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not picGRpy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picGRpy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not picLMuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picLMuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not picNGbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picNGbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not picPDuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picPDuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not picPIarC.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picPIarC.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not picPIarR.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picPIarR.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not picSOuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picSOuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not picZMbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            picZMbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 





        if not fcCCRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcCCRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcCFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcCFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcCNSbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcCNSbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcOBBar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcOBBar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcOCPuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcOCPuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcOIFuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcOIFuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcOLMuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcOLMuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcOOPar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcOOPar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcOPDuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcOPDuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcOPIar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcOPIar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
        if not fcOSOuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fcOSOuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 


        if not cfIBBar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfIBBar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiBSbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiBSbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiCPuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiCPuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiGRpy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiGRpy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiIFuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiIFuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
        if not cfiLMuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiLMuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiOPar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiOPar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiPDuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiPDuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiPIar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiPIar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfiSOuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfiSOuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    



        if not accCRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            accCRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not accFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            accFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not accFUbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            accFUbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not alcFCpy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            alcFCpy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    

        if not atiBSbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            atiBSbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not atiCRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            atiCRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not atiFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            atiFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    

        if not atiPDuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            atiPDuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    

        if not bar19br.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            bar19br.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    
        if not bbmFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            bbmFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PF.txt', header=None, index=None, sep='\t', mode='a')    


        if not carDCuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            carDCuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    

        if not cfrGTar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfrGTar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not cfrPOar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cfrPOar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    

        if not cosFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cosFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not cosGAbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cosGAbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not cosPDuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cosPDuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not cosSWbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cosSWbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not cotGAbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            cotGAbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    

        if not fliFEbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fliFEbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    

        if not fmiBCbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            fmiBCbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    

        if not frCFCuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            frCFCuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not frDCRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            frDCRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not frSCPuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            frSCPuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not frSFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            frSFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not frSIFuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            frSIFuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not frSLMuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            frSLMuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not frSPDuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            frSPDuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not frSSOuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            frSSOuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not icfFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            icfFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not intBCbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            intBCbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')   
        if not linSBuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            linSBuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    

        if not macBBar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            macBBar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not malBBar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            malBBar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not malCPuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            malCPuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not malFCpy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            malFCpy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not malGRpy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            malGRpy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not malIFuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            malIFuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not malPIar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            malPIar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not malSOuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            malSOuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not mamBSbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            mamBSbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not mamFCpy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            mamFCpy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    

        if not mamLMuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            mamLMuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not mamPIar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            mamPIar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    

        if not mamSOuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            mamSOuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not pltDCuy.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            pltDCuy.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    

        if not raqBBar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            raqBBar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    

        if not tbExc.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            tbExc.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not tboCRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            tboCRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not tboFRbr.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            tboFRbr.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    
        if not tboOPar.empty:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a') as f:
                f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            tboOPar.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    



        #df.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')

        with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a', encoding="utf=8") as f:
            f.write("======================================================================================================================================================================================\n")
            f.write("                                                                                      OUTROS                                                                                          \n")
            f.write("======================================================================================================================================================================================\n")
        if not caixa.empty:
            caixa.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
        else:
            with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a', encoding="utf=8") as f:
                f.write("                                                                         Nenhum produto foi encontrado                                                                              \n")
        with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a', encoding="utf=8") as f:
            f.write("======================================================================================================================================================================================\n")
        with open('C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', 'a', encoding="utf=8") as f:
            f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            f.write("                                                   Obs.: (*) - sem NF de Armazenagem         (B) - Bloqueado         (v) - Peso Variavel                                              \n")

        #dadosGeral.to_csv(r'C:/Users/Karol/Desktop/excel-python/test/note/PJ.txt', header=None, index=None, sep='\t', mode='a')

        """ with open('C:/Users/Karol/Desktop/excel=python/PJ.txt', 'w') as f:
            for line in dTotal:
                dTotal.write(str(line)+'\n') """

root = Tk()
Application(root)
# Set window title
root.title('SUDAMBEEF')
  
# Set window size

root.mainloop()