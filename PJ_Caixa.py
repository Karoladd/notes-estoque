import pandas as pd

ignore = list(range(0, 5))
ignore.append(6)
df = pd.read_excel('data/SAL1146.xls', sheet_name = "Plan1", skiprows = ignore)
bremove = df.loc[df['Lote'].str.contains('B', na=False)]
df.drop(bremove.index, inplace = True)
nan = df.loc[df['Lote'].isna()]
df.drop(nan.index, inplace = True)

# PEIXES
bacalhau = df.loc[df['Codigo'].str.contains('LBAMS-PT', na=False)]
camarao = df.loc[df['Codigo'].str.contains('CAM', na=False)]
fileSalm = df.loc[df['Produto'].str.contains('SALMAO', na=False)]
polvo = df.loc[df['Produto'].str.contains('POLVO', na=False)]
vieira = df.loc[df['Codigo'].str.contains('VIEPN', na=False)]

peixes = pd.concat([bacalhau, camarao, fileSalm, polvo, vieira], ignore_index = True)
print(peixes)

df.drop(bacalhau.index, inplace = True)
df.drop(camarao.index, inplace = True)
df.drop(fileSalm.index, inplace = True)
df.drop(polvo.index, inplace = True)
df.drop(vieira.index, inplace = True)

# NÃO VENDEMOS
print(bremove)

#CARNES
picanha = df.loc[df['Codigo'].str.contains('PIC', na=False)]
fileCostela = df.loc[(df['Produto'].str.contains('COSTELA', na=False)) & df['Codigo'].str.contains('FC')]
contFile = df.loc[(df['Produto'].str.contains('CONTRA FILE', na=False)) & df['Codigo'].str.contains('CFI')]

carnesTop = pd.concat([picanha, fileCostela, contFile], ignore_index = True)
print(carnesTop)

df.drop(picanha.index, inplace = True)
df.drop(fileCostela.index, inplace = True)
df.drop(contFile.index, inplace = True)

caixa = df.loc[df['Codigo'].str.contains('SUD-800', na=False)]
df.drop(caixa.index, inplace = True)


dTotal = pd.concat([peixes, bremove, carnesTop, df, caixa], ignore_index = True)
print(dTotal)

try:
    dadosGeral = pd.DataFrame(data=dTotal)
    print(dadosGeral)
except (NameError):
    print('Por favor, atualize o programa novamente...')
pass

writer = pd.ExcelWriter('excel/SaldoProdPJ.xlsx')
dadosGeral.to_excel(writer, sheet_name='Geral', index=False)
writer.save()
'''
'r' -> Usado para ler
'w' -> Usado para escrever
'r+' -> Ler e escrever
'a' -> acrescentar algo
'''

dftitulo = pd.read_excel('data/SAL1146.xls', sheet_name = "Plan1")
titulo = list(range(0, 4))
titnote = dftitulo.iloc[titulo]
colunas = dftitulo.iloc[[4]]
dftitulo = pd.read_excel('data/SAL1146.xls', sheet_name = "Plan1", skiprows = ignore)
rodape = dftitulo.loc[dftitulo['Lote'].isna()]


titnote.to_csv(r'C:/Users/Karol/Desktop/excel-python/note/PJ.txt', header=None, index=None, sep='\t', mode='w')
with open('C:/Users/Karol/Desktop/excel-python/note/PJ.txt', 'a') as f:
    f.write("======================================================================================================================================================================================\n")
colunas.to_csv(r'C:/Users/Karol/Desktop/excel-python/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
with open('C:/Users/Karol/Desktop/excel-python/note/PJ.txt', 'a') as f:
    f.write("======================================================================================================================================================================================\n")
    f.write("                                                                                      PEIXES                                                                                          \n")
    f.write("======================================================================================================================================================================================\n")
if not bacalhau.empty:
    bacalhau.to_csv(r'C:/Users/Karol/Desktop/excel-python/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
if not camarao.empty:
    with open('C:/Users/Karol/Desktop/excel-python/note/PJ.txt', 'a') as f:
        f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    camarao.to_csv(r'C:/Users/Karol/Desktop/excel-python/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
if not polvo.empty:
    with open('C:/Users/Karol/Desktop/excel-python/note/PJ.txt', 'a') as f:
        f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    polvo.to_csv(r'C:/Users/Karol/Desktop/excel-python/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
if not vieira.empty:
    with open('C:/Users/Karol/Desktop/excel-python/note/PJ.txt', 'a') as f:
        f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    vieira.to_csv(r'C:/Users/Karol/Desktop/excel-python/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
with open('C:/Users/Karol/Desktop/excel-python/note/PJ.txt', 'a', encoding="utf=8") as f:
    f.write("======================================================================================================================================================================================\n")
    f.write("                                                                                   NÃO VENDEMOS                                                                                       \n")
    f.write("======================================================================================================================================================================================\n")
if not bremove.empty:
    bremove.to_csv(r'C:/Users/Karol/Desktop/excel-python/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
with open('C:/Users/Karol/Desktop/excel-python/note/PJ.txt', 'a', encoding="utf=8") as f:
    f.write("======================================================================================================================================================================================\n")
    f.write("                                                                                      CARNES                                                                                          \n")
    f.write("======================================================================================================================================================================================\n")
if not picanha.empty:
    picanha.to_csv(r'C:/Users/Karol/Desktop/excel-python/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
if not fileCostela.empty:
    with open('C:/Users/Karol/Desktop/excel-python/note/PJ.txt', 'a') as f:
        f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    fileCostela.to_csv(r'C:/Users/Karol/Desktop/excel-python/note/PJ.txt', header=None, index=None, sep='\t', mode='a') 
if not contFile.empty:
    with open('C:/Users/Karol/Desktop/excel-python/note/PJ.txt', 'a') as f:
        f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    contFile.to_csv(r'C:/Users/Karol/Desktop/excel-python/note/PJ.txt', header=None, index=None, sep='\t', mode='a')    

df.to_csv(r'C:/Users/Karol/Desktop/excel-python/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
with open('C:/Users/Karol/Desktop/excel-python/note/PJ.txt', 'a', encoding="utf=8") as f:
    f.write("======================================================================================================================================================================================\n")
    f.write("                                                                                      OUTROS                                                                                          \n")
    f.write("======================================================================================================================================================================================\n")
if not caixa.empty:
    caixa.to_csv(r'C:/Users/Karol/Desktop/excel-python/note/PJ.txt', header=None, index=None, sep='\t', mode='a')
else:
    with open('C:/Users/Karol/Desktop/excel-python/note/PJ.txt', 'a', encoding="utf=8") as f:
        f.write("                                                                         Nenhum produto foi encontrado                                                                              \n")
with open('C:/Users/Karol/Desktop/excel-python/note/PJ.txt', 'a', encoding="utf=8") as f:
    f.write("======================================================================================================================================================================================\n")
    f.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
rodape.to_csv(r'C:/Users/Karol/Desktop/excel-python/note/PJ.txt', header=None, index=None, sep='\t', mode='a')

#dadosGeral.to_csv(r'C:/Users/Karol/Desktop/excel-python/note/PJ.txt', header=None, index=None, sep='\t', mode='a')

""" with open('C:/Users/Karol/Desktop/excel=python/PJ.txt', 'w') as f:
    for line in dTotal:
        dTotal.write(str(line)+'\n') """