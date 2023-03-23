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

