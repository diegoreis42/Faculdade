class Veiculo():
    def __init__(self, marca: str, cor: str, motorLigado: bool = False):
        self.__marca = marca
        self.__cor = cor
        self.__motorLigado = motorLigado

    def ligaMotor(self):
        if self.__motorLigado == True:
            print('O motor ja esta ligado!\n')
        else:
            self.__motorLigado = True
            print('O motor foi ligado\n')

    def desligaMotor(self):
        if self.__motorLigado == False:
            print('O motor ja esta desligado!\n')
        else:
            self.__motorLigado = False
            print('O motor foi desligado\n')

 


    def mostraAtributos(self):
        print(self.__marca)
        print(self.__cor)
        print(self.__motorLigado)


class Moto(Veiculo):
    def __init__(self, marca: str, cor: str, motorLigado: bool = False, estilo: str = 'None'):
        super().__init__(marca, cor, motorLigado)
        self.__estilo = estilo
        print('Moto instanciada!\n')

    def mostraAtributos(self):
        print('Atributos da Moto\n-----------------')
        super().mostraAtributos()
        print(self.__estilo)


class Carro(Veiculo):
    def __init__(self, marca: str, cor: str, motorLigado: bool = False, portaMalasCheio: bool = False):
        super().__init__(marca, cor, motorLigado)
        self.__portaMalasCheio = portaMalasCheio
        print('Carro instanciado!\n')

    def enchePortaMalas(self):
        if self.__portaMalasCheio == True:
            print('O porta malas ja esta cheio!\n')
        else:
            self.__portaMalasCheio = True
            print('O porta malas foi preenchido!\n')
           
    def esvaziaPortaMalas(self):
        if self.__portaMalasCheio == False:
            print('O porta malas ja esta vazio!\n')
        else:
            self.__portaMalasCheio = False
            print('O porta malas foi esvaziado\n')

    def mostraAtributos(self):
        print('Atributos do Carro\n-----------------')
        super().mostraAtributos()
        print(self.__portaMalasCheio)

if __name__ == '__main__':
   moto = Moto('Honda', 'azul', False, 'trail') 
   carro = Carro('Peaugeut', 'cinza', False)
   moto.ligaMotor()
   moto.mostraAtributos()
   carro.enchePortaMalas()
   carro.ligaMotor()
   carro.mostraAtributos()

