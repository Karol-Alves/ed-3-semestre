"""Ler a temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
-Uma função para ler e retornar o valor da temperatura (não recebe parametros)
-Uma função para fazer o cálculo (recebe como parametro a temperatura em graus Celsius)
-Uma função para mostrar o resultado, recebendo como parametro o valor e fazendo a impressão do resultado"""

# Função para ler a temperatura em graus Celsius
def lerTemperatura():
    temperaturaCelsius = float(input('Digite a temperatura em Celsius: '))
    return temperaturaCelsius

# Função para calcular a conversão para graus Fahrenheit
def calcularFahrenheit(temperaturaCelsius):
    fahrenheit = (9 * temperaturaCelsius + 160) / 5
    return fahrenheit

# Função para mostrar o resultado
def mostrarResultado(fahrenheit):
    print(f'A temperatura em Fahrenheit é {fahrenheit}')

# Função principal
def main():
    temperaturaCelsius = lerTemperatura()
    fahrenheit = calcularFahrenheit(temperaturaCelsius)
    mostrarResultado(fahrenheit)

main() #chama a função principal