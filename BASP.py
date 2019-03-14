import os

while True:
    
    print('██████╗  █████╗ ███████╗██████╗ ')
    print('██╔══██╗██╔══██╗██╔════╝██╔══██╗')
    print('██████╔╝███████║███████╗██████╔╝')
    print('██╔══██╗██╔══██║╚════██║██╔═══╝ ')
    print('██████╔╝██║  ██║███████║██║     ')
    print('╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ')
    print('')
    print(' =========================== ')
    print(' | Base Aérea de São Paulo |  ')
    print(' =========================== ')

    print("\n")
    Horário = input("Horário: \n")
    Saram = input("Saram: \n")
    NG = input("Nome: \n")
    Placa = input("Placa: \n")
    Modelo = input("Modelo: \n")
    c = 0
    arquivo = open('G3_TESTE.txt','a')
    arquivo.write(Horário + "  | " + Saram + "  | " + NG + "  | " + Placa + "  | " + Modelo + "\n")
    while c < 1:
        print(NG, "Identificado com sucesso ! ")
        c += 1
        arquivo.close()
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
