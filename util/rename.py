def nameNotePF(nome):
    from datetime import  date
    data = date.today()
    sdata = str(data)
    separa = sdata.split("-")
    dia = separa[2]
    mes = separa[1]
    ano = separa[0]

    dia_comp = (dia+"."+mes+"."+ano+nome)

    import os

    text = dia_comp+".txt"

    # Absolute path of a file
    old_name = "C:/Users/Karol/Desktop/excel-python/note/PF.txt"
    new_name = 'C:/Users/Karol/Desktop/excel-python/note/' + text

    # Renaming the file
    dayname = os.rename(old_name, new_name)

    return dayname

def nameNotePJ(nome):
    from datetime import  date
    data = date.today()
    sdata = str(data)
    separa = sdata.split("-")
    dia = separa[2]
    mes = separa[1]
    ano = separa[0]

    dia_comp = (dia+"."+mes+"."+ano+nome)

    import os

    text = dia_comp+".txt"

    # Absolute path of a file
    old_name = "C:/Users/Karol/Desktop/excel-python/note/PJ.txt"
    new_name = 'C:/Users/Karol/Desktop/excel-python/note/' + text

    # Renaming the file
    dayname = os.rename(old_name, new_name)

    return dayname