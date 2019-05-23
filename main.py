# coding: utf-8
import boot


def main():
    print('''
        ############################
        # BEM VINDO AO SERENISSIMA #
        ############################

        Escolha uma opção
        1- Pesquisar em sites do governo
        2- Pesquisar site especifico (ex: site.gov.br)
        3- Pesquisar documentos (ex: pdf, img, etc.)
        0- Cancelar
        ''')

    option = input(">> ")

    if option == '1':
        for result in boot.searchAll():
            print(result)
        
    elif option == '2':
        for result in boot.getSite():
                print(result)
        
    elif option == '3':
        for result in boot.getDocuments():
                print(result)
        
    elif option == '0':
        print('Até mais!')
    else:
        print('Opção inválida')
        main()


if __name__ == "__main__":
    main()