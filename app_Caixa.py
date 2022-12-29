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
    f.write("Marca              Lote       Codigo          *--------- P r o d u t o ----------*  Un     Qtd   Peso Liq.  Peso Buto  Fbi. Vlidde Cm     NFE       Entd  Plt. \n")
    f.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listbac):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listbac]

listcamarao = []
for line in content:
    camarao = "CAMAR"
    if camarao in line:
        if line[9] != "B":
            listcamarao.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listcamarao):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listcamarao]

listfilePanga = []
for line in content:
    filePanga = "FILE DE PANGA"
    if filePanga in line:
        if line[9] != "B":
            listfilePanga.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in bproduct:
                marca = "#"+ (bproduct.split("#",1)[1])
                top = bproduct.replace(marca,"")
                with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + bproduct+ '\n')           
            #print(line)

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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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
    fcCCRbr = "FILE COSTELA"
    fcdfc = "FILE DE COSTELA"
    if (fcCCRbr) in line:
        if line[9] != "B":
            listfcCCRbr.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')    
    if (fcdfc) in line:
        if line[9] != "B":
            listfcCCRbr.append(line)
            if "#" in line:
                marca = "#"+ (line.split("#",1)[1])
                top = line.replace(marca,"")
                with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(marca + "   " + top + '\n')
            else:
                with open(pathNotas, 'a', encoding="utf=8") as f:
                    f.write(vazioMarca + line+ '\n') 
                #print(line)
if len(listfcCCRbr):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listfcCCRbr]

listcfIBBar = []
for line in content:
    cfIBBar = "CONTRA FILE"
    cf = "CFI"
    if (cfIBBar and cf) in line:
        if line[9] != "B":
            listcfIBBar.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listcfIBBar):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listcfIBBar]

listaccCRbr = []
listacbovosso = []
for line in content:
    accCRbr = "ACEM C/OSSO"
    acbovosso = "ACEM BOV. C/ OSSO"
    if accCRbr in line:
        if line[9] != "B":
            listaccCRbr.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
    if acbovosso in line:
        if line[9] != "B":
            listacbovosso.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n') 
if len(listaccCRbr):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listaccCRbr]
listaGeral = [ele for ele in listaGeral if ele not in listacbovosso]

listalcFCpy = []
for line in content:
    alcFCpy = "ALCATRA"
    alc = "ALCFC"
    if (alcFCpy and alc) in line:
        if line[9] != "B":
            listalcFCpy.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listalcFCpy):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listalcFCpy]

listatiBSbr = []
for line in content:
    atiBSbr = "ASSADO DE TIRA"
    if atiBSbr in line:
        if line[9] != "B":
            listatiBSbr.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listatiBSbr):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listatiBSbr]

listbar19br = []
for line in content:
    bar19br = "BARRIGA"
    if bar19br in line:
        if line[9] != "B":
            listbar19br.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listbar19br):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listbar19br]

listbbmFRbr = []
for line in content:
    bbmFRbr = "BOMBOM DA ALCATRA"
    if bbmFRbr in line:
        if line[9] != "B":
            listbbmFRbr.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listbbmFRbr):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listbbmFRbr]

listcarDCuy = []
for line in content:
    carDCuy = "CARRE FRANCES"
    if carDCuy in line:
        if line[9] != "B":
            listcarDCuy.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listcarDCuy):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listcarDCuy]

listcfrGTar = []
listcorac = []
for line in content:
    cfrGTar = "CORAÇAO DE FRANGO"
    corac = "CORACAO DE FRANGO"
    if cfrGTar in line:
        if line[9] != "B":
            listcfrGTar.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
    if corac in line:
        if line[9] != "B":
            listcfrGTar.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')
if len(listcfrGTar):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listcfrGTar]

listcosFRbr = []
listcosDiant = []
listcosTras = []
for line in content:
    cosFRbr = "COSTELA BOV JANELA"
    cosDiant = "COSTELA BOV DIANTEIRO"
    cosTras = "COSTELA BOV. TRASEIRO"
    if cosFRbr in line:
        if line[9] != "B":
            listcosFRbr.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
    if cosDiant in line:
        if line[9] != "B":
            listcosFRbr.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
    if cosTras in line:
        if line[9] != "B":
            listcosFRbr.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listcosFRbr):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listcosFRbr]



listcupFCpy = []
for line in content:
    cupFCpy = "CUPFC-PY"
    if cupFCpy in line:
        if line[9] != "B":
            listcupFCpy.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listcupFCpy):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listcupFCpy]


listfliFEbr = []
for line in content:
    fliFEbr = "FILE DE LINGUADO"
    if fliFEbr in line:
        if line[9] != "B":
            listfliFEbr.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listfliFEbr):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listfliFEbr]

listfmiBCbr = []
for line in content:
    fmiBCbr = "FILE MIGNON BOV"
    if fmiBCbr in line:
        if line[9] != "B":
            listfmiBCbr.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listfmiBCbr):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listfmiBCbr]

listfrCFCuy = []
for line in content:
    frCFCuy = "FRALDA"
    if frCFCuy in line:
        if line[9] != "B":
            listfrCFCuy.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listfrCFCuy):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listfrCFCuy]

listicfFRbr = []
for line in content:
    icfFRbr = "ISCA DE CONTRA FILE"
    if icfFRbr in line:
        if line[9] != "B":
            listicfFRbr.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listicfFRbr):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listicfFRbr]

listintBCbr = []
for line in content:
    intBCbr = "INTBC-BR"
    if intBCbr in line:
        if line[9] != "B":
            listintBCbr.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listintBCbr):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listintBCbr]

listlinSBuy = []
for line in content:
    linSBuy = "LINGUICA"
    if linSBuy in line:
        if line[9] != "B":
            listlinSBuy.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listlinSBuy):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listlinSBuy]

listmacBBar = []
for line in content:
    macBBar = "MIOLO DE ACEM"
    if macBBar in line:
        if line[9] != "B":
            listmacBBar.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listmacBBar):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listmacBBar]

listmalBBar = []
for line in content:
    malBBar = "MIOLO DE ALCATRA"
    mioloAlcatra = "MIOLO ALCATRA"
    if malBBar in line:
        if line[9] != "B":
            listmalBBar.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
    if mioloAlcatra in line:
        if line[9] != "B":
            listmalBBar.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')     
if len(listmalBBar):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listmalBBar]

listmamBSbr = []
for line in content:
    mamBSbr = "MAMINHA BOV"
    if mamBSbr in line:
        if line[9] != "B":
            listmamBSbr.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listmamBSbr):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listmamBSbr]

listpltDCuy = []
for line in content:
    pltDCuy = "PALETA"
    if pltDCuy in line:
        if line[9] != "B":
            listpltDCuy.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listpltDCuy):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listpltDCuy]

listraqBBar = []
for line in content:
    raqBBar = "RAQUETE BOVINO"
    if raqBBar in line:
        if line[9] != "B":
            listraqBBar.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listraqBBar):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listraqBBar]

listtbExc = []
for line in content:
    tbExc = "T BONE"
    tibone = "TIBONE"
    if tbExc in line:
        if line[9] != "B":
            listtbExc.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
    if tibone in line:
        if line[9] != "B":
            listtbExc.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
            #print(line)
if len(listtbExc):
    with open(pathNotas, 'a', encoding="utf=8") as f:
            f.write(lines_cod + '\n')
else:
    None
listaGeral = [ele for ele in listaGeral if ele not in listtbExc]


with open(pathNotas, 'a', encoding="utf=8") as f:
    f.write("================================================================================================================================================================\n")
    f.write("                                                                            OUTROS                                                          \n")
    f.write("================================================================================================================================================================\n")

listcaixa = []
for line in content:
    caixa = "SUD-800"
    if caixa in line:
        if line[9] != "B":
            listcaixa.append(line)
            if "#" in line:
              marca = "#"+ (line.split("#",1)[1])
              top = line.replace(marca,"")
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(marca + "   " + top + '\n')
            else:
              with open(pathNotas, 'a', encoding="utf=8") as f:
                f.write(vazioMarca + line+ '\n')           
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



#EXEMPLO DE DUAS CONDIÇÕES

#listcomRabo = []
#for line in content:
#    camarao = "CAMMC-AR"
#    comRabo = "CAMARÃO C/RABO"
#    if (camarao and comRabo) in line:
#        if line[9] != "B":
#            listcomRabo.append(line)
#            if "#" in line:
#              marca = "#"+ (line.split("#",1)[1])
#              top = line.replace(marca,"")
#              with open(pathNotas, 'a', encoding="utf=8") as f:
#                f.write(marca + "   " + top + '\n')
#            else:
#              with open(pathNotas, 'a', encoding="utf=8") as f:
#                f.write(vazioMarca + line+ '\n')           
#            #print(line)
#if len(listcomRabo):
#    with open(pathNotas, 'a', encoding="utf=8") as f:
#            f.write(lines_cod + '\n')
#else:
#    None
#listaGeral = [ele for ele in listaGeral if ele not in listcomRabo]
    