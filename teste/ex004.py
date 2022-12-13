idade  =  int(input("\n qual a  sua idade: "))
peso =  int(input('\n digite seu peso: '))
horas = int(input('\n me fale quantas horas você dormiu: '))
if idade >= 16 and peso >= 50 and horas >= 6:
    print('você pode tirar sangue : ')
elif idade <= 16 and peso <= 50 and horas <= 6:
    print('você não pode  tirarsangue: ')