from Calculadora_de_Unidades_de_armazenamento import converterStringParaFloat, bitParaByte, byteParaBit, BytesParaKbyte, kbyteParBytes, KbyteParaMbyte, MBparaKB, MBparaGB, GBparaMB, GBparaTB, TBparaGB, TBparaPB, PBparaTB 

print("-Escreva 1 para converter Bit(b) para Byte(B) \n-Escreva 2 para converter Byte(B) para Bit(b) \n-Escreva 3 para converter Byte(B) para KiloByte(KB) \n-Escreva 4 para converter Kilobyte(KB) para Byte(B) \n-Escreva 5 para converter Kilobyte(KB) para MegaByte(MB) \n-Escreva 6 para converter Megabyte(MB) para Kilobyte(KB) \n-Escreva 7 para converter Megabyte(MB) para GigaByte(GB) \n-Escreva 8 para converter Gigabyte(GB) para Megabyte(MB) \n-Escreva 9 para converter Gigabyte(GB) para Terabyte(TB) \n-Escreva 10 para converter Terabyte(TB) para Gigabyte(GB) \n-Escreva 11 para converter Terabyte(TB) para Petabyte(PB) \n-Escreva 12 Para converter Petabyte(PB) para Terabyte(TB)")
funcEscolha = input()
if(funcEscolha == '1'):
    print('Insira o valor a ser convertido (Bit para Byte)')
    entradaDotecladoValoraSerConvertido = converterStringParaFloat(input())
    valorConvertido = bitParaByte (entradaDotecladoValoraSerConvertido)
    print(valorConvertido)

elif(funcEscolha == '2'):
    print('Insira o valor a ser convertido (Byte para Bit)')
    entradaDotecladoValoraSerConvertido = converterStringParaFloat(input())
    valorConvertido = byteParaBit (entradaDotecladoValoraSerConvertido)
    print(valorConvertido)

elif(funcEscolha == '3'):
    print('Insira o valor a ser convertido (Byte para Kilobyte)')
    entradaDotecladoValoraSerConvertido = converterStringParaFloat(input())
    valorConvertido = BytesParaKbyte (entradaDotecladoValoraSerConvertido)
    print(valorConvertido)

elif(funcEscolha == '4'):
    print('Insira o valor a ser convertido (Kilobyte para Byte)')
    entradaDotecladoValoraSerConvertido = converterStringParaFloat(input())
    valorConvertido = kbyteParBytes(entradaDotecladoValoraSerConvertido)
    print(valorConvertido)

elif(funcEscolha == '5'):
    print('Insira o valor a ser convertido (Kilobyte para Megabyte)')
    entradaDotecladoValoraSerConvertido = converterStringParaFloat(input())
    valorConvertido = KbyteParaMbyte (entradaDotecladoValoraSerConvertido)
    print(valorConvertido)

elif(funcEscolha == '6'):
    print('Insira o valor a ser convertido (Megabyte para Kilobyte)')
    entradaDotecladoValoraSerConvertido = converterStringParaFloat(input())
    valorConvertido = MBparaKB (entradaDotecladoValoraSerConvertido)
    print(valorConvertido)

elif(funcEscolha == '7'):
    print('Insira o valor a ser convertido (Megabyte para Gigabyte)')
    entradaDotecladoValoraSerConvertido = converterStringParaFloat(input())
    valorConvertido = MBparaGB (entradaDotecladoValoraSerConvertido)
    print(valorConvertido)

elif(funcEscolha == '8'):
    print('Insira o valor a ser convertido (Gigabyte para Megabyte)')
    entradaDotecladoValoraSerConvertido = converterStringParaFloat(input())
    valorConvertido = GBparaMB(entradaDotecladoValoraSerConvertido)
    print(valorConvertido)

elif(funcEscolha == '9'):
    print('Insira o valor a ser convertido (Gigabyte para Terabyte)')
    entradaDotecladoValoraSerConvertido = converterStringParaFloat(input())
    valorConvertido = GBparaTB (entradaDotecladoValoraSerConvertido)
    print(valorConvertido)

elif(funcEscolha == '10'):
    print('Insira o valor a ser convertido (Terabyte para Gigabyte)')
    entradaDotecladoValoraSerConvertido = converterStringParaFloat(input())
    valorConvertido = TBparaGB (entradaDotecladoValoraSerConvertido)
    print(valorConvertido)

elif(funcEscolha == '11'):
    print('Insira o valor a ser convertido (Terabyte para Petabyte)')
    entradaDotecladoValoraSerConvertido = converterStringParaFloat(input())
    valorConvertido = TBparaPB (entradaDotecladoValoraSerConvertido)
    print(valorConvertido)

elif(funcEscolha == '12'):
    print('Insira o valor a ser convertido (Petabyte para Terabyte)')
    entradaDotecladoValoraSerConvertido = converterStringParaFloat(input())
    valorConvertido = PBparaTB (entradaDotecladoValoraSerConvertido)
    print(valorConvertido)

