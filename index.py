from tkinter import *
from tkinter import filedialog
from util.download import downloadN
from util.rename import nameNotePF, nameNotePJ

PATHNOTEDIR = r"C:\Users\Karol\Desktop\excel-python\note"

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
                                            filetypes=[("Excel files", ".TXT .txt")])
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

        #INSERIR ARQUIVO
        with open(pathExcelKIT) as f:
            content = f.readlines()
        content = [x.strip('\n') for x in content]
            
        import os
        dir = r'C:\Users\Karol\Desktop\excel-python\note'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

        pathNotas = r'C:\Users\Karol\Desktop\excel-python\note\PF.txt'
        lines_cod = "----------------------------------------------------------------------------------------------------------------------------------------------------------------"

        listaGeral = []
        for line in content:
            listaGeral.append(line)
            listaGeral = filter(None, listaGeral)
            serv_tit = "Servicos"
            demo_tit = "Demonstrativo"
            clie_tit = "Cliente"
            pont_tit = "--------"
            codi_tit = "Codigo"
            sald_cod = "Saldo por Código"
            listaGeral = [item for item in listaGeral if serv_tit not in item]
            listaGeral = [item for item in listaGeral if demo_tit not in item]
            listaGeral = [item for item in listaGeral if clie_tit not in item]
            listaGeral = [item for item in listaGeral if pont_tit not in item]
            listaGeral = [item for item in listaGeral if codi_tit not in item]
            listaGeral = [item for item in listaGeral if sald_cod not in item]  

        with open(pathNotas, 'w', encoding="utf=8") as f:
            cabecalho = list(range(0, 6))
            for i in cabecalho:
                #print(content[i])
                with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(content[i] + '\n')      

        with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write("================================================================================================================================================================\n")
            f.write("                                                                            PEIXES                                                              \n")
            f.write("================================================================================================================================================================\n")

        listbac = []
        for line in content:
            bacalhau = "LBAMS-PT"
            if bacalhau in line:
                if line[9] != "B":
                    listbac.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listbac):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listbac]

        listsemPele = []
        for line in content:
            camarao = "CAMMC-AR"
            semPele = "CAMARÃO S/PELE"
            if (camarao and semPele) in line:
                if line[9] != "B":
                    listsemPele.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listsemPele):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listsemPele]

        listcomRabo = []
        for line in content:
            camarao = "CAMMC-AR"
            comRabo = "CAMARÃO C/RABO"
            if (camarao and comRabo) in line:
                if line[9] != "B":
                    listcomRabo.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcomRabo):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcomRabo]

        listcamMRbr = []
        for line in content:
            camMRbr = "CAMMR-BR"
            if camMRbr in line:
                if line[9] != "B":
                    listcamMRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcamMRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcamMRbr]

        listcamPNar = []
        for line in content:
            camPNar = "CAMPN-AR"
            if camPNar in line:
                if line[9] != "B":
                    listcamPNar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcamPNar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcamPNar]

        listfilePanga = []
        for line in content:
            filePanga = "FILE DE PANGA"
            if filePanga in line:
                if line[9] != "B":
                    listfilePanga.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfilePanga):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfilePanga]

        listfileSalmao = []
        for line in content:
            fileSalmao = "FILE DE SALMAO"
            if fileSalmao in line:
                if line[9] != "B":
                    listfileSalmao.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfileSalmao):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfileSalmao]


        listfileLing = []
        for line in content:
            fileLing = "FLIFE-BR"
            if fileLing in line:
                if line[9] != "B":
                    listfileLing.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfileLing):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfileLing]

        listpolvo = []
        for line in content:
            polvo = "POLVO"
            if polvo in line:
                if line[9] != "B":
                    listpolvo.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpolvo):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpolvo]

        listvieira = []
        for line in content:
            vieira = "VIEPN-PR"
            if vieira in line:
                if line[9] != "B":
                    listvieira.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listvieira):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listvieira]


        with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write("================================================================================================================================================================\n")
            f.write("                                                                          NÃO VENDEMOS                                                          \n")
            f.write("================================================================================================================================================================\n")

        listb= []
        for line in content:
            listb.append(line)
        listbprod = []
        for bproduct in listb:
            try:
                if bproduct[9] == "B":
                    listbprod.append(bproduct)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(bproduct + '\n')
            except:
                None
            pass
        listaGeral = [ele for ele in listaGeral if ele not in listbprod]

        with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write("================================================================================================================================================================\n")
            f.write("                                                                            CARNES                                                          \n")
            f.write("================================================================================================================================================================\n")

        listpicBBar = []
        for line in content:
            picBBar = "PICBB-AR"
            if picBBar in line:
                if line[9] != "B":
                    listpicBBar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicBBar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicBBar]

        listpicCJar = []
        for line in content:
            picCJar = "PICCJ-AR"
            if picCJar in line:
                if line[9] != "B":
                    listpicCJar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicCJar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicCJar]

        listpicCPuy = []
        for line in content:
            picCPuy = "PICCP-UY"
            if picCPuy in line:
                if line[9] != "B":
                    listpicCPuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicCPuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicCPuy]

        listpicFBar = []
        for line in content:
            picFBar = "PICFB-AR"
            if picFBar in line:
                if line[9] != "B":
                    listpicFBar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicFBar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicFBar]

        listpicFCpy = []
        for line in content:
            picFCpy = "PICFC-PY"
            if picFCpy in line:
                if line[9] != "B":
                    listpicFCpy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicFCpy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicFCpy]

        listpicFGar = []
        for line in content:
            picFGar = "PICFG-AR"
            if picFGar in line:
                if line[9] != "B":
                    listpicFGar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicFGar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicFGar]

        listpicGRpy = []
        for line in content:
            picGRpy = "PICGR-PY"
            if picGRpy in line:
                if line[9] != "B":
                    listpicGRpy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicGRpy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicGRpy]

        listpicLMuy = []
        for line in content:
            picLMuy = "PICLM-UY"
            if picLMuy in line:
                if line[9] != "B":
                    listpicLMuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicLMuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicLMuy]

        listpicNGbr = []
        for line in content:
            picNGbr = "PICNG-BR"
            if picNGbr in line:
                if line[9] != "B":
                    listpicNGbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicNGbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicNGbr]

        listpicPDuy = []
        for line in content:
            picPDuy = "PICPD-UY"
            if picPDuy in line:
                if line[9] != "B":
                    listpicPDuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicPDuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicPDuy]

        listpicPIarC = []
        for line in content:
            picPIarC = "PICPI-AR-01C"
            if picPIarC in line:
                if line[9] != "B":
                    listpicPIarC.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicPIarC):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicPIarC]

        listpicPIarR = []
        for line in content:
            picPIarR = "PICPI-AR-01R"
            if picPIarR in line:
                if line[9] != "B":
                    listpicPIarR.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicPIarR):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicPIarR]

        listpicSOuy = []
        for line in content:
            picSOuy = "PICSO-UY"
            if picSOuy in line:
                if line[9] != "B":
                    listpicSOuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicSOuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicSOuy]

        listpicZMbr = []
        for line in content:
            picZMbr = "PICZM-BR"
            if picZMbr in line:
                if line[9] != "B":
                    listpicZMbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicZMbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicZMbr]

        #FILE DE COSTELA

        listfcCCRbr = []
        for line in content:
            fcCCRbr = "FCCCR-BR"
            if fcCCRbr in line:
                if line[9] != "B":
                    listfcCCRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcCCRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcCCRbr]

        listfcCFRbr = []
        for line in content:
            fcCFRbr = "FCCFR-BR"
            if fcCFRbr in line:
                if line[9] != "B":
                    listfcCFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcCFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcCFRbr]

        listfcCBSbr = []
        for line in content:
            fcCBSbr = "FCCBS-BR"
            if fcCBSbr in line:
                if line[9] != "B":
                    listfcCBSbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcCBSbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcCBSbr]

        listfcOBBar = []
        for line in content:
            fcOBBar = "FCOBB-AR"
            if fcOBBar in line:
                if line[9] != "B":
                    listfcOBBar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcOBBar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcOBBar]

        listfcOCPuy = []
        for line in content:
            fcOCPuy = "FCOCP-UY"
            if fcOCPuy in line:
                if line[9] != "B":
                    listfcOCPuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcOCPuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcOCPuy]

        listfcOIFuy = []
        for line in content:
            fcOIFuy = "FCOIF-UY"
            if fcOIFuy in line:
                if line[9] != "B":
                    listfcOIFuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcOIFuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcOIFuy]

        listfcOLMuy = []
        for line in content:
            fcOLMuy = "FCOLM-UY"
            if fcOLMuy in line:
                if line[9] != "B":
                    listfcOLMuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcOLMuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcOLMuy]

        listfcOOPar = []
        for line in content:
            fcOOPar = "FCOOP-AR"
            if fcOOPar in line:
                if line[9] != "B":
                    listfcOOPar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcOOPar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcOOPar]

        listfcOPDuy = []
        for line in content:
            fcOPDuy = "FCOPD-UY"
            if fcOPDuy in line:
                if line[9] != "B":
                    listfcOPDuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcOPDuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcOPDuy]

        listfcOPIar = []
        for line in content:
            fcOPIar = "FCOPI-AR"
            if fcOPIar in line:
                if line[9] != "B":
                    listfcOPIar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcOPIar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcOPIar]

        listfcOSOuy = []
        for line in content:
            fcOSOuy = "FCOSO-UY"
            if fcOSOuy in line:
                if line[9] != "B":
                    listfcOSOuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcOSOuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcOSOuy]

        listcfIBBar = []
        for line in content:
            cfIBBar = "CFIBB-AR"
            if cfIBBar in line:
                if line[9] != "B":
                    listcfIBBar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfIBBar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfIBBar]

        listcfiBSbr = []
        for line in content:
            cfiBSbr = "CFIBS-BR"
            if cfiBSbr in line:
                if line[9] != "B":
                    listcfiBSbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiBSbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiBSbr]

        listcfiCPuy = []
        for line in content:
            cfiCPuy = "CFICP-UY"
            if cfiCPuy in line:
                if line[9] != "B":
                    listcfiCPuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiCPuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiCPuy]

        listcfiFRbr = []
        for line in content:
            cfiFRbr = "CFIFR-BR"
            if cfiFRbr in line:
                if line[9] != "B":
                    listcfiFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiFRbr]

        listcfiGRpy = []
        for line in content:
            cfiGRpy = "CFIGR-PY"
            if cfiGRpy in line:
                if line[9] != "B":
                    listcfiGRpy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiGRpy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiGRpy]

        listcfiIFuy = []
        for line in content:
            cfiIFuy = "CFIIF-UY"
            if cfiIFuy in line:
                if line[9] != "B":
                    listcfiIFuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiIFuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiIFuy]

        listcfiLMuy = []
        for line in content:
            cfiLMuy = "CFILM-UY"
            if cfiLMuy in line:
                if line[9] != "B":
                    listcfiLMuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiLMuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiLMuy]

        listcfiOPar = []
        for line in content:
            cfiOPar = "CFIOP-AR"
            if cfiOPar in line:
                if line[9] != "B":
                    listcfiOPar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiOPar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiOPar]

        listcfiPDuy = []
        for line in content:
            cfiPDuy = "CFIPD-UY"
            if cfiPDuy in line:
                if line[9] != "B":
                    listcfiPDuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiPDuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiPDuy]

        listcfiPIar = []
        for line in content:
            cfiPIar = "CFIPI-AR"
            if cfiPIar in line:
                if line[9] != "B":
                    listcfiPIar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiPIar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiPIar]

        listcfiSOuy = []
        for line in content:
            cfiSOuy = "CFISO-UY"
            if cfiSOuy in line:
                if line[9] != "B":
                    listcfiSOuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiSOuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiSOuy]



        listaccCRbr = []
        for line in content:
            accCRbr = "ACCCR-BR"
            if accCRbr in line:
                if line[9] != "B":
                    listaccCRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listaccCRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listaccCRbr]

        listaccFRbr = []
        for line in content:
            accFRbr = "ACCFR-BR"
            if accFRbr in line:
                if line[9] != "B":
                    listaccFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listaccFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listaccFRbr]

        listaccFUbr= []
        for line in content:
            accFUbr= "ACCFU-BR"
            if accFUbr in line:
                if line[9] != "B":
                    listaccFUbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listaccFUbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listaccFUbr]

        listalcFCpy= []
        for line in content:
            alcFCpy= "ALCFC-PY"
            if alcFCpy in line:
                if line[9] != "B":
                    listalcFCpy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listalcFCpy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listalcFCpy]

        listatiBSbr= []
        for line in content:
            atiBSbr= "ATIBS-BR"
            if atiBSbr in line:
                if line[9] != "B":
                    listatiBSbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listatiBSbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listatiBSbr]

        listatiCRbr= []
        for line in content:
            atiCRbr= "ATICR-BR"
            if atiCRbr in line:
                if line[9] != "B":
                    listatiCRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listatiCRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listatiCRbr]

        listatiFRbr= []
        for line in content:
            atiFRbr= "ATIFR-BR"
            if atiFRbr in line:
                if line[9] != "B":
                    listatiFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listatiFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listatiFRbr]

        listatiPDuy= []
        for line in content:
            atiPDuy= "ATIPD-UY"
            if atiPDuy in line:
                if line[9] != "B":
                    listatiPDuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listatiPDuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listatiPDuy]

        listbar19br= []
        for line in content:
            bar19br= "BAR19-BR"
            if bar19br in line:
                if line[9] != "B":
                    listbar19br.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listbar19br):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listbar19br]

        listbbmFRbr= []
        for line in content:
            bbmFRbr= "BBMFR-BR"
            if bbmFRbr in line:
                if line[9] != "B":
                    listbbmFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listbbmFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listbbmFRbr]

        listcarDCuy= []
        for line in content:
            carDCuy= "CARDC-UY"
            if carDCuy in line:
                if line[9] != "B":
                    listcarDCuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcarDCuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcarDCuy]

        listcfrGTar= []
        for line in content:
            cfrGTar= "CFRGT-AR"
            if cfrGTar in line:
                if line[9] != "B":
                    listcfrGTar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfrGTar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfrGTar]

        listcfrPOar= []
        for line in content:
            cfrPOar= "CFRPO-AR"
            if cfrPOar in line:
                if line[9] != "B":
                    listcfrPOar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfrPOar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfrPOar]

        listcosFRbr= []
        for line in content:
            cosFRbr= "COSFR-BR"
            if cosFRbr in line:
                if line[9] != "B":
                    listcosFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcosFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcosFRbr]

        listcosGAbr= []
        for line in content:
            cosGAbr= "COSGA-BR"
            if cosGAbr in line:
                if line[9] != "B":
                    listcosGAbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcosGAbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcosGAbr]

        listcosPDuy= []
        for line in content:
            cosPDuy= "COSPD-UY"
            if cosPDuy in line:
                if line[9] != "B":
                    listcosPDuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcosPDuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcosPDuy]

        listcosSWbr= []
        for line in content:
            cosSWbr= "COSSW-BR"
            if cosSWbr in line:
                if line[9] != "B":
                    listcosSWbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcosSWbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcosSWbr]

        listcotGAbr= []
        for line in content:
            cotGAbr= "COTGA-BR"
            if cotGAbr in line:
                if line[9] != "B":
                    listcotGAbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcotGAbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcotGAbr]

        listfliFEbr= []
        for line in content:
            fliFEbr= "FLIFE-BR"
            if fliFEbr in line:
                if line[9] != "B":
                    listfliFEbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfliFEbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfliFEbr]

        listfmiBCbr= []
        for line in content:
            fmiBCbr= "FMIBC-BR"
            if fmiBCbr in line:
                if line[9] != "B":
                    listfmiBCbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfmiBCbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfmiBCbr]

        listfrCFCuy= []
        for line in content:
            frCFCuy= "FRCFC-UY"
            if frCFCuy in line:
                if line[9] != "B":
                    listfrCFCuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfrCFCuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfrCFCuy]

        listfrDCRbr= []
        for line in content:
            frDCRbr= "FRDCR-BR"
            if frDCRbr in line:
                if line[9] != "B":
                    listfrDCRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfrDCRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfrDCRbr]

        listfrSCPuy= []
        for line in content:
            frSCPuy= "FRSCP-UY"
            if frSCPuy in line:
                if line[9] != "B":
                    listfrSCPuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfrSCPuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfrSCPuy]

        listfrSFRbr= []
        for line in content:
            frSFRbr= "FRSFR-BR"
            if frSFRbr in line:
                if line[9] != "B":
                    listfrSFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfrSFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfrSFRbr]

        listfrSIFuy= []
        for line in content:
            frSIFuy= "FRSIF-UY"
            if frSIFuy in line:
                if line[9] != "B":
                    listfrSIFuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfrSIFuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfrSIFuy]

        listfrSLMuy= []
        for line in content:
            frSLMuy= "FRSLM-UY"
            if frSLMuy in line:
                if line[9] != "B":
                    listfrSLMuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfrSLMuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfrSLMuy]

        listfrSPDuy= []
        for line in content:
            frSPDuy= "FRSPD-UY"
            if frSPDuy in line:
                if line[9] != "B":
                    listfrSPDuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfrSPDuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfrSPDuy]

        listfrSSOuy= []
        for line in content:
            frSSOuy= "FRSSO-UY"
            if frSSOuy in line:
                if line[9] != "B":
                    listfrSSOuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfrSSOuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfrSSOuy]

        listicfFRbr= []
        for line in content:
            icfFRbr= "ICFFR-BR"
            if icfFRbr in line:
                if line[9] != "B":
                    listicfFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listicfFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listicfFRbr]

        listintBCbr= []
        for line in content:
            intBCbr= "INTBC-BR"
            if intBCbr in line:
                if line[9] != "B":
                    listintBCbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listintBCbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listintBCbr]

        listlinSBuy= []
        for line in content:
            linSBuy= "LINSB-UY"
            if linSBuy in line:
                if line[9] != "B":
                    listlinSBuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listlinSBuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listlinSBuy]

        listmacBBar= []
        for line in content:
            macBBar= "MACBB-AR"
            if macBBar in line:
                if line[9] != "B":
                    listmacBBar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmacBBar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmacBBar]

        listmalBBar= []
        for line in content:
            malBBar= "MALBB-AR"
            if malBBar in line:
                if line[9] != "B":
                    listmalBBar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmalBBar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmalBBar]

        listmalCPuy= []
        for line in content:
            malCPuy= "MALCP-UY"
            if malCPuy in line:
                if line[9] != "B":
                    listmalCPuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmalCPuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmalCPuy]

        listmalFCpy= []
        for line in content:
            malFCpy= "MALFC-PY"
            if malFCpy in line:
                if line[9] != "B":
                    listmalFCpy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmalFCpy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmalFCpy]

        listmalGRpy= []
        for line in content:
            malGRpy= "MALGR-PY"
            if malGRpy in line:
                if line[9] != "B":
                    listmalGRpy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmalGRpy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmalGRpy]

        listmalIFuy= []
        for line in content:
            malIFuy= "MALIF-UY"
            if malIFuy in line:
                if line[9] != "B":
                    listmalIFuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmalIFuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmalIFuy]

        listmalPIar= []
        for line in content:
            malPIar= "MALPI-AR"
            if malPIar in line:
                if line[9] != "B":
                    listmalPIar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmalPIar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmalPIar]

        listmalSOuy= []
        for line in content:
            malSOuy= "MALSO-UY"
            if malSOuy in line:
                if line[9] != "B":
                    listmalSOuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmalSOuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmalSOuy]

        listmamBSbr= []
        for line in content:
            mamBSbr= "MAMBS-BR"
            if mamBSbr in line:
                if line[9] != "B":
                    listmamBSbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmamBSbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmamBSbr]

        listmamFCpy= []
        for line in content:
            mamFCpy= "MAMFC-PY"
            if mamFCpy in line:
                if line[9] != "B":
                    listmamFCpy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmamFCpy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmamFCpy]

        listmamLMuy= []
        for line in content:
            mamLMuy= "MAMLM-UY"
            if mamLMuy in line:
                if line[9] != "B":
                    listmamLMuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmamLMuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmamLMuy]

        listmamPIar= []
        for line in content:
            mamPIar= "MAMPI-AR"
            if mamPIar in line:
                if line[9] != "B":
                    listmamPIar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmamPIar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmamPIar]

        listmamSOuy= []
        for line in content:
            mamSOuy= "MAMSO-UY"
            if mamSOuy in line:
                if line[9] != "B":
                    listmamSOuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmamSOuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmamSOuy]

        listpltDCuy= []
        for line in content:
            pltDCuy= "PLTDC-UY"
            if pltDCuy in line:
                if line[9] != "B":
                    listpltDCuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpltDCuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpltDCuy]

        listraqBBar= []
        for line in content:
            raqBBar= "RAQBB-AR"
            if raqBBar in line:
                if line[9] != "B":
                    listraqBBar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listraqBBar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listraqBBar]

        listtbExc= []
        for line in content:
            tbExc= "T BONE"
            if tbExc in line:
                if line[9] != "B":
                    listtbExc.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listtbExc):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listtbExc]

        listtboCRbr= []
        for line in content:
            tboCRbr= "TBOCR-BR"
            if tboCRbr in line:
                if line[9] != "B":
                    listtboCRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listtboCRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listtboCRbr]

        listtboFRbr= []
        for line in content:
            tboFRbr= "TBOFR-BR"
            if tboFRbr in line:
                if line[9] != "B":
                    listtboFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listtboFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listtboFRbr]

        listtboOPar= []
        for line in content:
            tboOPar= "TBOOP-AR"
            if tboOPar in line:
                if line[9] != "B":
                    listtboOPar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listtboOPar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listtboOPar]

        with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write("================================================================================================================================================================\n")
            f.write("                                                                            OUTROS                                                          \n")
            f.write("================================================================================================================================================================\n")

        listcaixa= []
        for line in content:
            caixa= "SUD-800"
            if caixa in line:
                if line[9] != "B":
                    listcaixa.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcaixa):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcaixa]

        if len(listaGeral) != 0:
            print("Produto não adicionado no programa:")
            with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write("================================================================================================================================================================\n")
                f.write("                                                                         FALTA ADICIONAR                                                          \n")
                f.write("================================================================================================================================================================\n")
            for l in listaGeral:
                with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(l + '\n')
                print(l)
        else:
            print("Todos os códigos foram inseridos")

        

    def exportPJ(self):
        pathExcelKIT = self.nome["text"]
        #INSERIR ARQUIVO
        with open(pathExcelKIT) as f:
            content = f.readlines()
        content = [x.strip('\n') for x in content]
            
        import os
        dir = r'C:\Users\Karol\Desktop\excel-python\note'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

        pathNotas = r'C:\Users\Karol\Desktop\excel-python\note\PJ.txt'
        lines_cod = "----------------------------------------------------------------------------------------------------------------------------------------------------------------"

        listaGeral = []
        for line in content:
            listaGeral.append(line)
            listaGeral = filter(None, listaGeral)
            serv_tit = "Servicos"
            demo_tit = "Demonstrativo"
            clie_tit = "Cliente"
            pont_tit = "--------"
            codi_tit = "Codigo"
            sald_cod = "Saldo por Código"
            listaGeral = [item for item in listaGeral if serv_tit not in item]
            listaGeral = [item for item in listaGeral if demo_tit not in item]
            listaGeral = [item for item in listaGeral if clie_tit not in item]
            listaGeral = [item for item in listaGeral if pont_tit not in item]
            listaGeral = [item for item in listaGeral if codi_tit not in item]
            listaGeral = [item for item in listaGeral if sald_cod not in item]  

        with open(pathNotas, 'w', encoding="utf=8") as f:
            cabecalho = list(range(0, 6))
            for i in cabecalho:
                #print(content[i])
                with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(content[i] + '\n')      

        with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write("================================================================================================================================================================\n")
            f.write("                                                                            PEIXES                                                              \n")
            f.write("================================================================================================================================================================\n")

        listbac = []
        for line in content:
            bacalhau = "LBAMS-PT"
            if bacalhau in line:
                if line[9] != "B":
                    listbac.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listbac):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listbac]

        listsemPele = []
        for line in content:
            camarao = "CAMMC-AR"
            semPele = "CAMARÃO S/PELE"
            if (camarao and semPele) in line:
                if line[9] != "B":
                    listsemPele.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listsemPele):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listsemPele]

        listcomRabo = []
        for line in content:
            camarao = "CAMMC-AR"
            comRabo = "CAMARÃO C/RABO"
            if (camarao and comRabo) in line:
                if line[9] != "B":
                    listcomRabo.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcomRabo):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcomRabo]

        listcamMRbr = []
        for line in content:
            camMRbr = "CAMMR-BR"
            if camMRbr in line:
                if line[9] != "B":
                    listcamMRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcamMRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcamMRbr]

        listcamPNar = []
        for line in content:
            camPNar = "CAMPN-AR"
            if camPNar in line:
                if line[9] != "B":
                    listcamPNar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcamPNar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcamPNar]

        listfilePanga = []
        for line in content:
            filePanga = "FILE DE PANGA"
            if filePanga in line:
                if line[9] != "B":
                    listfilePanga.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfilePanga):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfilePanga]

        listfileSalmao = []
        for line in content:
            fileSalmao = "FILE DE SALMAO"
            if fileSalmao in line:
                if line[9] != "B":
                    listfileSalmao.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfileSalmao):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfileSalmao]


        listfileLing = []
        for line in content:
            fileLing = "FLIFE-BR"
            if fileLing in line:
                if line[9] != "B":
                    listfileLing.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfileLing):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfileLing]

        listpolvo = []
        for line in content:
            polvo = "POLVO"
            if polvo in line:
                if line[9] != "B":
                    listpolvo.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpolvo):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpolvo]

        listvieira = []
        for line in content:
            vieira = "VIEPN-PR"
            if vieira in line:
                if line[9] != "B":
                    listvieira.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listvieira):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listvieira]


        with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write("================================================================================================================================================================\n")
            f.write("                                                                          NÃO VENDEMOS                                                          \n")
            f.write("================================================================================================================================================================\n")

        listb= []
        for line in content:
            listb.append(line)
        listbprod = []
        for bproduct in listb:
            try:
                if bproduct[9] == "B":
                    listbprod.append(bproduct)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(bproduct + '\n')
            except:
                None
            pass
        listaGeral = [ele for ele in listaGeral if ele not in listbprod]

        with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write("================================================================================================================================================================\n")
            f.write("                                                                            CARNES                                                          \n")
            f.write("================================================================================================================================================================\n")

        listpicBBar = []
        for line in content:
            picBBar = "PICBB-AR"
            if picBBar in line:
                if line[9] != "B":
                    listpicBBar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicBBar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicBBar]

        listpicCJar = []
        for line in content:
            picCJar = "PICCJ-AR"
            if picCJar in line:
                if line[9] != "B":
                    listpicCJar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicCJar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicCJar]

        listpicCPuy = []
        for line in content:
            picCPuy = "PICCP-UY"
            if picCPuy in line:
                if line[9] != "B":
                    listpicCPuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicCPuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicCPuy]

        listpicFBar = []
        for line in content:
            picFBar = "PICFB-AR"
            if picFBar in line:
                if line[9] != "B":
                    listpicFBar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicFBar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicFBar]

        listpicFCpy = []
        for line in content:
            picFCpy = "PICFC-PY"
            if picFCpy in line:
                if line[9] != "B":
                    listpicFCpy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicFCpy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicFCpy]

        listpicFGar = []
        for line in content:
            picFGar = "PICFG-AR"
            if picFGar in line:
                if line[9] != "B":
                    listpicFGar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicFGar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicFGar]

        listpicGRpy = []
        for line in content:
            picGRpy = "PICGR-PY"
            if picGRpy in line:
                if line[9] != "B":
                    listpicGRpy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicGRpy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicGRpy]

        listpicLMuy = []
        for line in content:
            picLMuy = "PICLM-UY"
            if picLMuy in line:
                if line[9] != "B":
                    listpicLMuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicLMuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicLMuy]

        listpicNGbr = []
        for line in content:
            picNGbr = "PICNG-BR"
            if picNGbr in line:
                if line[9] != "B":
                    listpicNGbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicNGbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicNGbr]

        listpicPDuy = []
        for line in content:
            picPDuy = "PICPD-UY"
            if picPDuy in line:
                if line[9] != "B":
                    listpicPDuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicPDuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicPDuy]

        listpicPIarC = []
        for line in content:
            picPIarC = "PICPI-AR-01C"
            if picPIarC in line:
                if line[9] != "B":
                    listpicPIarC.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicPIarC):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicPIarC]

        listpicPIarR = []
        for line in content:
            picPIarR = "PICPI-AR-01R"
            if picPIarR in line:
                if line[9] != "B":
                    listpicPIarR.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicPIarR):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicPIarR]

        listpicSOuy = []
        for line in content:
            picSOuy = "PICSO-UY"
            if picSOuy in line:
                if line[9] != "B":
                    listpicSOuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicSOuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicSOuy]

        listpicZMbr = []
        for line in content:
            picZMbr = "PICZM-BR"
            if picZMbr in line:
                if line[9] != "B":
                    listpicZMbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpicZMbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpicZMbr]

        #FILE DE COSTELA

        listfcCCRbr = []
        for line in content:
            fcCCRbr = "FCCCR-BR"
            if fcCCRbr in line:
                if line[9] != "B":
                    listfcCCRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcCCRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcCCRbr]

        listfcCFRbr = []
        for line in content:
            fcCFRbr = "FCCFR-BR"
            if fcCFRbr in line:
                if line[9] != "B":
                    listfcCFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcCFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcCFRbr]

        listfcCBSbr = []
        for line in content:
            fcCBSbr = "FCCBS-BR"
            if fcCBSbr in line:
                if line[9] != "B":
                    listfcCBSbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcCBSbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcCBSbr]

        listfcOBBar = []
        for line in content:
            fcOBBar = "FCOBB-AR"
            if fcOBBar in line:
                if line[9] != "B":
                    listfcOBBar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcOBBar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcOBBar]

        listfcOCPuy = []
        for line in content:
            fcOCPuy = "FCOCP-UY"
            if fcOCPuy in line:
                if line[9] != "B":
                    listfcOCPuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcOCPuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcOCPuy]

        listfcOIFuy = []
        for line in content:
            fcOIFuy = "FCOIF-UY"
            if fcOIFuy in line:
                if line[9] != "B":
                    listfcOIFuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcOIFuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcOIFuy]

        listfcOLMuy = []
        for line in content:
            fcOLMuy = "FCOLM-UY"
            if fcOLMuy in line:
                if line[9] != "B":
                    listfcOLMuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcOLMuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcOLMuy]

        listfcOOPar = []
        for line in content:
            fcOOPar = "FCOOP-AR"
            if fcOOPar in line:
                if line[9] != "B":
                    listfcOOPar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcOOPar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcOOPar]

        listfcOPDuy = []
        for line in content:
            fcOPDuy = "FCOPD-UY"
            if fcOPDuy in line:
                if line[9] != "B":
                    listfcOPDuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcOPDuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcOPDuy]

        listfcOPIar = []
        for line in content:
            fcOPIar = "FCOPI-AR"
            if fcOPIar in line:
                if line[9] != "B":
                    listfcOPIar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcOPIar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcOPIar]

        listfcOSOuy = []
        for line in content:
            fcOSOuy = "FCOSO-UY"
            if fcOSOuy in line:
                if line[9] != "B":
                    listfcOSOuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfcOSOuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfcOSOuy]

        listcfIBBar = []
        for line in content:
            cfIBBar = "CFIBB-AR"
            if cfIBBar in line:
                if line[9] != "B":
                    listcfIBBar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfIBBar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfIBBar]

        listcfiBSbr = []
        for line in content:
            cfiBSbr = "CFIBS-BR"
            if cfiBSbr in line:
                if line[9] != "B":
                    listcfiBSbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiBSbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiBSbr]

        listcfiCPuy = []
        for line in content:
            cfiCPuy = "CFICP-UY"
            if cfiCPuy in line:
                if line[9] != "B":
                    listcfiCPuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiCPuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiCPuy]

        listcfiFRbr = []
        for line in content:
            cfiFRbr = "CFIFR-BR"
            if cfiFRbr in line:
                if line[9] != "B":
                    listcfiFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiFRbr]

        listcfiGRpy = []
        for line in content:
            cfiGRpy = "CFIGR-PY"
            if cfiGRpy in line:
                if line[9] != "B":
                    listcfiGRpy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiGRpy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiGRpy]

        listcfiIFuy = []
        for line in content:
            cfiIFuy = "CFIIF-UY"
            if cfiIFuy in line:
                if line[9] != "B":
                    listcfiIFuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiIFuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiIFuy]

        listcfiLMuy = []
        for line in content:
            cfiLMuy = "CFILM-UY"
            if cfiLMuy in line:
                if line[9] != "B":
                    listcfiLMuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiLMuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiLMuy]

        listcfiOPar = []
        for line in content:
            cfiOPar = "CFIOP-AR"
            if cfiOPar in line:
                if line[9] != "B":
                    listcfiOPar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiOPar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiOPar]

        listcfiPDuy = []
        for line in content:
            cfiPDuy = "CFIPD-UY"
            if cfiPDuy in line:
                if line[9] != "B":
                    listcfiPDuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiPDuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiPDuy]

        listcfiPIar = []
        for line in content:
            cfiPIar = "CFIPI-AR"
            if cfiPIar in line:
                if line[9] != "B":
                    listcfiPIar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiPIar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiPIar]

        listcfiSOuy = []
        for line in content:
            cfiSOuy = "CFISO-UY"
            if cfiSOuy in line:
                if line[9] != "B":
                    listcfiSOuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfiSOuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfiSOuy]



        listaccCRbr = []
        for line in content:
            accCRbr = "ACCCR-BR"
            if accCRbr in line:
                if line[9] != "B":
                    listaccCRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listaccCRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listaccCRbr]

        listaccFRbr = []
        for line in content:
            accFRbr = "ACCFR-BR"
            if accFRbr in line:
                if line[9] != "B":
                    listaccFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listaccFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listaccFRbr]

        listaccFUbr= []
        for line in content:
            accFUbr= "ACCFU-BR"
            if accFUbr in line:
                if line[9] != "B":
                    listaccFUbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listaccFUbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listaccFUbr]

        listalcFCpy= []
        for line in content:
            alcFCpy= "ALCFC-PY"
            if alcFCpy in line:
                if line[9] != "B":
                    listalcFCpy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listalcFCpy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listalcFCpy]

        listatiBSbr= []
        for line in content:
            atiBSbr= "ATIBS-BR"
            if atiBSbr in line:
                if line[9] != "B":
                    listatiBSbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listatiBSbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listatiBSbr]

        listatiCRbr= []
        for line in content:
            atiCRbr= "ATICR-BR"
            if atiCRbr in line:
                if line[9] != "B":
                    listatiCRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listatiCRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listatiCRbr]

        listatiFRbr= []
        for line in content:
            atiFRbr= "ATIFR-BR"
            if atiFRbr in line:
                if line[9] != "B":
                    listatiFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listatiFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listatiFRbr]

        listatiPDuy= []
        for line in content:
            atiPDuy= "ATIPD-UY"
            if atiPDuy in line:
                if line[9] != "B":
                    listatiPDuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listatiPDuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listatiPDuy]

        listbar19br= []
        for line in content:
            bar19br= "BAR19-BR"
            if bar19br in line:
                if line[9] != "B":
                    listbar19br.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listbar19br):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listbar19br]

        listbbmFRbr= []
        for line in content:
            bbmFRbr= "BBMFR-BR"
            if bbmFRbr in line:
                if line[9] != "B":
                    listbbmFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listbbmFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listbbmFRbr]

        listcarDCuy= []
        for line in content:
            carDCuy= "CARDC-UY"
            if carDCuy in line:
                if line[9] != "B":
                    listcarDCuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcarDCuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcarDCuy]

        listcfrGTar= []
        for line in content:
            cfrGTar= "CFRGT-AR"
            if cfrGTar in line:
                if line[9] != "B":
                    listcfrGTar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfrGTar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfrGTar]

        listcfrPOar= []
        for line in content:
            cfrPOar= "CFRPO-AR"
            if cfrPOar in line:
                if line[9] != "B":
                    listcfrPOar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcfrPOar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcfrPOar]

        listcosFRbr= []
        for line in content:
            cosFRbr= "COSFR-BR"
            if cosFRbr in line:
                if line[9] != "B":
                    listcosFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcosFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcosFRbr]

        listcosGAbr= []
        for line in content:
            cosGAbr= "COSGA-BR"
            if cosGAbr in line:
                if line[9] != "B":
                    listcosGAbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcosGAbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcosGAbr]

        listcosPDuy= []
        for line in content:
            cosPDuy= "COSPD-UY"
            if cosPDuy in line:
                if line[9] != "B":
                    listcosPDuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcosPDuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcosPDuy]

        listcosSWbr= []
        for line in content:
            cosSWbr= "COSSW-BR"
            if cosSWbr in line:
                if line[9] != "B":
                    listcosSWbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcosSWbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcosSWbr]

        listcotGAbr= []
        for line in content:
            cotGAbr= "COTGA-BR"
            if cotGAbr in line:
                if line[9] != "B":
                    listcotGAbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcotGAbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcotGAbr]

        listfliFEbr= []
        for line in content:
            fliFEbr= "FLIFE-BR"
            if fliFEbr in line:
                if line[9] != "B":
                    listfliFEbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfliFEbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfliFEbr]

        listfmiBCbr= []
        for line in content:
            fmiBCbr= "FMIBC-BR"
            if fmiBCbr in line:
                if line[9] != "B":
                    listfmiBCbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfmiBCbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfmiBCbr]

        listfrCFCuy= []
        for line in content:
            frCFCuy= "FRCFC-UY"
            if frCFCuy in line:
                if line[9] != "B":
                    listfrCFCuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfrCFCuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfrCFCuy]

        listfrDCRbr= []
        for line in content:
            frDCRbr= "FRDCR-BR"
            if frDCRbr in line:
                if line[9] != "B":
                    listfrDCRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfrDCRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfrDCRbr]

        listfrSCPuy= []
        for line in content:
            frSCPuy= "FRSCP-UY"
            if frSCPuy in line:
                if line[9] != "B":
                    listfrSCPuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfrSCPuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfrSCPuy]

        listfrSFRbr= []
        for line in content:
            frSFRbr= "FRSFR-BR"
            if frSFRbr in line:
                if line[9] != "B":
                    listfrSFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfrSFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfrSFRbr]

        listfrSIFuy= []
        for line in content:
            frSIFuy= "FRSIF-UY"
            if frSIFuy in line:
                if line[9] != "B":
                    listfrSIFuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfrSIFuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfrSIFuy]

        listfrSLMuy= []
        for line in content:
            frSLMuy= "FRSLM-UY"
            if frSLMuy in line:
                if line[9] != "B":
                    listfrSLMuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfrSLMuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfrSLMuy]

        listfrSPDuy= []
        for line in content:
            frSPDuy= "FRSPD-UY"
            if frSPDuy in line:
                if line[9] != "B":
                    listfrSPDuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfrSPDuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfrSPDuy]

        listfrSSOuy= []
        for line in content:
            frSSOuy= "FRSSO-UY"
            if frSSOuy in line:
                if line[9] != "B":
                    listfrSSOuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listfrSSOuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listfrSSOuy]

        listicfFRbr= []
        for line in content:
            icfFRbr= "ICFFR-BR"
            if icfFRbr in line:
                if line[9] != "B":
                    listicfFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listicfFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listicfFRbr]

        listintBCbr= []
        for line in content:
            intBCbr= "INTBC-BR"
            if intBCbr in line:
                if line[9] != "B":
                    listintBCbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listintBCbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listintBCbr]

        listlinSBuy= []
        for line in content:
            linSBuy= "LINSB-UY"
            if linSBuy in line:
                if line[9] != "B":
                    listlinSBuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listlinSBuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listlinSBuy]

        listmacBBar= []
        for line in content:
            macBBar= "MACBB-AR"
            if macBBar in line:
                if line[9] != "B":
                    listmacBBar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmacBBar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmacBBar]

        listmalBBar= []
        for line in content:
            malBBar= "MALBB-AR"
            if malBBar in line:
                if line[9] != "B":
                    listmalBBar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmalBBar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmalBBar]

        listmalCPuy= []
        for line in content:
            malCPuy= "MALCP-UY"
            if malCPuy in line:
                if line[9] != "B":
                    listmalCPuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmalCPuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmalCPuy]

        listmalFCpy= []
        for line in content:
            malFCpy= "MALFC-PY"
            if malFCpy in line:
                if line[9] != "B":
                    listmalFCpy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmalFCpy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmalFCpy]

        listmalGRpy= []
        for line in content:
            malGRpy= "MALGR-PY"
            if malGRpy in line:
                if line[9] != "B":
                    listmalGRpy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmalGRpy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmalGRpy]

        listmalIFuy= []
        for line in content:
            malIFuy= "MALIF-UY"
            if malIFuy in line:
                if line[9] != "B":
                    listmalIFuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmalIFuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmalIFuy]

        listmalPIar= []
        for line in content:
            malPIar= "MALPI-AR"
            if malPIar in line:
                if line[9] != "B":
                    listmalPIar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmalPIar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmalPIar]

        listmalSOuy= []
        for line in content:
            malSOuy= "MALSO-UY"
            if malSOuy in line:
                if line[9] != "B":
                    listmalSOuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmalSOuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmalSOuy]

        listmamBSbr= []
        for line in content:
            mamBSbr= "MAMBS-BR"
            if mamBSbr in line:
                if line[9] != "B":
                    listmamBSbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmamBSbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmamBSbr]

        listmamFCpy= []
        for line in content:
            mamFCpy= "MAMFC-PY"
            if mamFCpy in line:
                if line[9] != "B":
                    listmamFCpy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmamFCpy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmamFCpy]

        listmamLMuy= []
        for line in content:
            mamLMuy= "MAMLM-UY"
            if mamLMuy in line:
                if line[9] != "B":
                    listmamLMuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmamLMuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmamLMuy]

        listmamPIar= []
        for line in content:
            mamPIar= "MAMPI-AR"
            if mamPIar in line:
                if line[9] != "B":
                    listmamPIar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmamPIar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmamPIar]

        listmamSOuy= []
        for line in content:
            mamSOuy= "MAMSO-UY"
            if mamSOuy in line:
                if line[9] != "B":
                    listmamSOuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listmamSOuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listmamSOuy]

        listpltDCuy= []
        for line in content:
            pltDCuy= "PLTDC-UY"
            if pltDCuy in line:
                if line[9] != "B":
                    listpltDCuy.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listpltDCuy):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listpltDCuy]

        listraqBBar= []
        for line in content:
            raqBBar= "RAQBB-AR"
            if raqBBar in line:
                if line[9] != "B":
                    listraqBBar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listraqBBar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listraqBBar]

        listtbExc= []
        for line in content:
            tbExc= "T BONE"
            if tbExc in line:
                if line[9] != "B":
                    listtbExc.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listtbExc):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listtbExc]

        listtboCRbr= []
        for line in content:
            tboCRbr= "TBOCR-BR"
            if tboCRbr in line:
                if line[9] != "B":
                    listtboCRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listtboCRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listtboCRbr]

        listtboFRbr= []
        for line in content:
            tboFRbr= "TBOFR-BR"
            if tboFRbr in line:
                if line[9] != "B":
                    listtboFRbr.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listtboFRbr):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listtboFRbr]

        listtboOPar= []
        for line in content:
            tboOPar= "TBOOP-AR"
            if tboOPar in line:
                if line[9] != "B":
                    listtboOPar.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listtboOPar):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listtboOPar]

        with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write("================================================================================================================================================================\n")
            f.write("                                                                            OUTROS                                                          \n")
            f.write("================================================================================================================================================================\n")

        listcaixa= []
        for line in content:
            caixa= "SUD-800"
            if caixa in line:
                if line[9] != "B":
                    listcaixa.append(line)
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(line + '\n')
                    #print(line)
        if len(listcaixa):
            with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(lines_cod + '\n')
        else:
            None
        listaGeral = [ele for ele in listaGeral if ele not in listcaixa]

        if len(listaGeral) != 0:
            print("Produto não adicionado no programa:")
            with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write("================================================================================================================================================================\n")
                f.write("                                                                         FALTA ADICIONAR                                                          \n")
                f.write("================================================================================================================================================================\n")
            for l in listaGeral:
                with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(l + '\n')
                print(l)
        else:
            print("Todos os códigos foram inseridos")

    

root = Tk()
Application(root)
# Set window title
root.title('SUDAMBEEF')
  
# Set window size

root.mainloop()