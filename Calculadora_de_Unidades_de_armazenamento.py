CONSTANTE_CONVERSÃO_PRINCIPAL = 1024

def converterStringParaFloat(value):
    print('valor convertido de str para float')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para bytes')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

def BytesParaKbyte(valorASerConvertido):
    print('Valor convertido de byte para kbyte')
    BytesParaKbyte = valorASerConvertido / (CONSTANTE_CONVERSÃO_PRINCIPAL)
    return BytesParaKbyte

def kbyteParBytes(valorASerConvertido):
    print('Valor convertido de Kbyte para bytes')
    kbyteParaBytes = valorASerConvertido * (CONSTANTE_CONVERSÃO_PRINCIPAL)
    return kbyteParaBytes

def KbyteParaMbyte(valorASerConvertido):
    print('Valor convertido de Kbytes para Mbytes1')
    KbyteParaMbyte = valorASerConvertido / (CONSTANTE_CONVERSÃO_PRINCIPAL)
    return KbyteParaMbyte

def MBparaKB(valorASerConvertido):
    print('Valor convertido de Mbytes para Kbytes')
    MBparaKB = valorASerConvertido * (CONSTANTE_CONVERSÃO_PRINCIPAL)
    return MBparaKB

def MBparaGB(valorASerConvertido):
    print('Valor convertido de MBytes para GBytes')
    MBparaGB= valorASerConvertido / (CONSTANTE_CONVERSÃO_PRINCIPAL)
    return MBparaGB

def GBparaMB(valorASerConvertido):
    print('Valor convertido de GBytes para MBytes')
    GBparaMB = valorASerConvertido * (CONSTANTE_CONVERSÃO_PRINCIPAL)
    return GBparaMB

def GBparaTB(valorASerConvertido):
    print('Valor convertido de Gbytes para Tbytes')
    GBparaTB= valorASerConvertido / (CONSTANTE_CONVERSÃO_PRINCIPAL)
    return GBparaTB

def TBparaGB(valorASerConvertido):
    print('Valor convertido de Tbytes para Gbytes')
    TBparaGB = valorASerConvertido * (CONSTANTE_CONVERSÃO_PRINCIPAL)
    return TBparaGB

def TBparaPB(valorASerConvertido):
    print('Valor convertido de TBytes para Pbytes')
    TBparaPB= valorASerConvertido / (CONSTANTE_CONVERSÃO_PRINCIPAL)
    return TBparaPB

def PBparaTB(valorASerConvertido):
    print('Valor convertido de Pbytes para TBytes')
    PBparaTB = valorASerConvertido * (CONSTANTE_CONVERSÃO_PRINCIPAL)
    return PBparaTB


print('Insira o valor a ser convertido de bytes para bit')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat (input())
valorConvertido = byteParaBit (entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de bit para Bytes')
entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
valorConvertido = bitParaByte (entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de Bytes para Kbytes')
entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
valorConvertido = BytesParaKbyte (entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de Kbytes para Bytes')
entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
valorConvertido = kbyteParBytes(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de Kbytes para Mbytes')
entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
valorConvertido = KbyteParaMbyte (entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de Mbytes para Kbytes')
entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
valorConvertido = MBparaKB (entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de Gigabytes para MBytes')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = GBparaMB (entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de MBytes para Gbytes')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = MBparaGB (entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de TBytes para Gbytes')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = TBparaGB (entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de Gbytes para TBytes')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = GBparaTB (entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de PBytes para Tbytes')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = PBparaTB (entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de Tbytes para Pbytes')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = TBparaPB (entradaDoTecladoValorASerConvertido)
print(valorConvertido)
