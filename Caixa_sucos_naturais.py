print('','Sucos Naturais (500 ml)',sep='-->')
print('Escolha entre 4 sabores de suco:')
s1 = 'Goiaba'
s2 = 'Morango'
s3 = 'Abacaxi'
s4 = 'Manga'
print(' 1 - Goiaba ') # R$ 12.00
print(' 2 - Morango ') # R$ 14.00
print(' 3 - Abacaxi ') # R$ 12.00
print(' 4 - Manga ') # R$ 12.00
sbr = (int(input('Selecione o numero correpondente ao sabor esccolhido:')))
qtd = (int(input('Selecione a quantidade:')))

if qtd <= 0:
    print('Quantidade inválida!')

else:
    if sbr == 1 :
        pagar = qtd * 12.00
        print (f'O sabor escolhido foi: {s1} ')
        print (f'A quantidade escolhida foi: {qtd}')
        print (f'Total a pagar baseado nas suas escolhas: R$ {pagar:.2f}')
    else :
        if sbr == 2 :
            pagar = qtd * 14.00
            print(f'O sabor escolhido foi: {s2} ')
            print(f'A quantidade escolhida foi: {qtd}')
            print (f'Total a pagar baseado nas suas escolhas: R$ {pagar:.2f}')
        else :
            if sbr == 3 :
                pagar = qtd * 12.00
                print(f'O sabor escolhido foi: {s3} ')
                print(f'A quantidade escolhida foi: {qtd}')
                print (f'Total a pagar baseado nas suas escolhas: R$ {pagar:.2f}')
            else:
                if sbr == 4 :
                    pagar = qtd * 12.00
                    print(f'O sabor escolhido foi: {s4} ')
                    print(f'A quantidade escolhida foi: {qtd}')
                    print (f'Total a pagar baseado nas suas escolhas: R$ {pagar:.2f}')
                else :
                 print('Informação inexistente!')

# Utilizando a condicional de múltipla escolha (elif):

print('','Sucos Naturais (500 ml)',sep='-->')
print('Escolha entre 4 sabores de suco:')
s1 = 'Goiaba'
s2 = 'Morango'
s3 = 'Abacaxi'
s4 = 'Manga'
print(' 1 - Goiaba ') # R$ 12.00
print(' 2 - Morango ') # R$ 14.00
print(' 3 - Abacaxi ') # R$ 12.00
print(' 4 - Manga ') # R$ 12.00
sbr = (int(input('Selecione o numero correpondente ao sabor esccolhido:')))
qtd = (int(input('Selecione a quantidade:')))

if qtd <= 0:
    print('Quantidade inválida')
    
elif sbr == 1 :
    pagar = qtd * 12.00
    print (f'O sabor escolhido foi: {s1} ')
    print (f'A quantidade escolhida foi: {qtd}')
    print (f'Total a pagar baseado nas suas escolhas: R$ {pagar:.2f}')
elif sbr == 2 :
    pagar = qtd * 14.00
    print(f'O sabor escolhido foi: {s2} ')
    print(f'A quantidade escolhida foi: {qtd}')
    print (f'Total a pagar baseado nas suas escolhas: R$ {pagar:.2f}')
elif sbr == 3 :
    pagar = qtd * 12.00
    print(f'O sabor escolhido foi: {s3} ')
    print(f'A quantidade escolhida foi: {qtd}')
    print (f'Total a pagar baseado nas suas escolhas: R$ {pagar:.2f}')
elif sbr == 4 :
    pagar = qtd * 12.00
    print(f'O sabor escolhido foi: {s4} ')
    print(f'A quantidade escolhida foi: {qtd}')
    print (f'Total a pagar baseado nas suas escolhas: R$ {pagar:.2f}')
else :
    print('Informação inexistente!')







