from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone
    
    @abstractmethod
    def getSalario(self):
        pass

class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorPorHora = valorPorHora

    def getSalario(self):
        return self.__horasTrabalhadas * self.__valorPorHora

class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorPorDia = valorPorDia

    def getSalario(self):
        return self.__diasTrabalhados * self.__valorPorDia

class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal

    def getSalario(self):
        return self.__valorMensal



if __name__ == "__main__":
    candidatas = [Horista("Ana", "3333-4444", 160, 12), Diarista("Roberta", "5555-3333", 20, 65), Mensalista("Isabela", "1111-2222", 1200)]
    salarios = []
    for candidata in candidatas:
        print("Nome: " + candidata.nome + " telefone: " + candidata.telefone + " salario: %d" % candidata.getSalario() )
        salarios = [candidata.getSalario()]

    print("O salario mais barato eh: %d" % min(salarios))

