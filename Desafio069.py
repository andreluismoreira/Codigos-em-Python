print('*'*20)
print('Cadastro de Pessoas')
print('*'*20)
maior18 = men = m20 = 0
while True:
    i = int(input('Idade: '))
    s = ' '
    while s not in 'FM':
        s = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if i >= 18:
        maior18 += 1
    if s == 'M':
        men += 1
    if s == 'F' and i < 20:
        m20 += 1
    rsp = ' '
    while rsp not in 'SN':
        rsp = str(input('Quer continuar [S/N] ?: ')).upper().strip()[0]
    if rsp == 'N':
            break
print(f"""Os dados foram adicionados, sendo:
          {maior18} total de pessoas maiores de 18 anos
          {men} homens cadastrados
          {m20} mulheres menores de 18 anos""")



