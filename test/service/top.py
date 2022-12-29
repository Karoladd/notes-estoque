#INSERIR ARQUIVO
with open(r'C:\Users\Karol\Desktop\excel-python\test\ex-Caixa\SAL1146.TXT') as f:
    content = f.readlines()
content = [x.strip('\n') for x in content]
    
import os
dir = r'C:\Users\Karol\Desktop\excel-python\note'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

pathNotas = r'C:\Users\Karol\Desktop\excel-python\note\PJ.txt'
lines_cod = "----------------------------------------------------------------------------------------------------------------------------------------------------------------"

listaGeral = []
vazioMarca = "                   "
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
    cabecalho = list(range(0, 3))
    for i in cabecalho:
        #print(content[i])
        with open(pathNotas, 'a', encoding="utf=8") as f:
          f.write(content[i]+"\n")
    
with open(pathNotas, 'a', encoding="utf=8") as f:
    f.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    f.write("Marca              Lote       Codigo          *----------- P  o d u t o ---------*  Un     Qtd   Peso Liq.  Peso Buto  Fbi. Vlidde Cm     NFE       Entd  Plt. \n")
    f.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    
with open(pathNotas, 'a', encoding="utf=8") as f:
    f.write("================================================================================================================================================================\n")
    f.write("                                                                            PEIXES                                                              \n")
    f.write("================================================================================================================================================================\n")

def Produto1(var, cod):
    global listaGeral 
    listaProduto = []
    for line in content:
        var = cod
        if var in line:
            if line[9] != "B":
                listaProduto.append(line)
                if "#" in line:
                    marca = "#"+ (line.split("#",1)[1])
                    top = line.replace(marca,"")
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(marca + "   " + top + '\n')
                else:
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(vazioMarca + line+ '\n')           
                #print(line)
    if len(listaProduto):
        with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(lines_cod + '\n')
    else:
        None
    listaGeral = [ele for ele in listaGeral if ele not in listaProduto]

def Produto2(var, cod1, cod2):
    global listaGeral 
    listaProduto = []
    for line in content:
        var = cod1
        var2 = cod2
        if (var and var2) in line:
            if line[9] != "B":
                listaProduto.append(line)
                if "#" in line:
                    marca = "#"+ (line.split("#",1)[1])
                    top = line.replace(marca,"")
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(marca + "   " + top + '\n')
                else:
                    with open(pathNotas, 'a', encoding="utf=8") as f:
                        f.write(vazioMarca + line+ '\n')           
                #print(line)
    if len(listaProduto):
        with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(lines_cod + '\n')
    else:
        None
    listaGeral = [ele for ele in listaGeral if ele not in listaProduto]

Produto1("bacalhau","LBAMS-PT")
Produto2("camsempele","CAMMC-AR", "CAMARÃO S/PELE")
Produto2("camcomrabo", "CAMMC-AR", "CAMARÃO C/RABO")
Produto1("camMRbr","CAMMR-BR")
Produto1("camPNar","CAMPN-AR")
Produto1("filePanga","FILE DE PANGA")
Produto1("fileSalmao","FILE DE SALMAO")
print(listaGeral)



