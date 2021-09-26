import abc
from unittest import TestCase, main

class Calculadora (object):

	def calcular(self, n1, n2, operador):
	    operacaoFabrica = OperacaoFabrica()
	    operacao = operacaoFabrica.criar(operador)
	    if(operacao == None):
	    	return 0
	    else:
		    result = operacao.executar(n1, n2)
		    return result

class OperacaoFabrica(object):

	def criar(self, operador):
	    if(operador == 'soma'):
		    return Soma()
	    elif (operador == 'subtracao'):
		    return Subtracao()
	    elif (operador == 'divisao'):
		    return Divisao()
	    elif (operador == 'multiplicacao'):
		    return Multiplicacao()

class Operacao(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def executar(self, n1, n2):
	    pass
    
class Soma(Operacao):
    def executar(self, n1, n2):
        result = n1 + n2
        return result

class Subtracao(Operacao):
    def executar (self, n1, n2):
        result = n1 - n2
        return result

class Multiplicacao(Operacao):
    def executar (self, n1, n2):
        result = n1 * n2
        return result

class Divisao(Operacao):
    def executar (self, n1, n2):
        result = n1 / n2
        return result


class TestCase(TestCase):

    def test_soma(self):
        calculador = Calculadora()
        result = calculador.calcular(4, 4, 'soma')
        self.assertEqual(result, 8)

    def test_subtracao(self):
        calculador1 = Calculadora()
        result = calculador1.calcular(4, 4, 'subtracao')
        self.assertEqual(result, 0)

    def test_divisao(self):
        calculador1 = Calculadora()
        result = calculador1.calcular(4, 4, 'divisao')
        self.assertEqual(result, 1)

    def test_multiplicacao(self):
        calculador1 = Calculadora()
        result = calculador1.calcular(4, 4, 'multiplicacao')
        self.assertEqual(result, 16)    


calculador = Calculadora()
x = calculador.calcular(2,3, 'soma')
print(x)

if __name__ == '__main__':
    main()