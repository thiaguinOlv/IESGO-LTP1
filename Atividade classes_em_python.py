class Carro:
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.vendido = False  # Por padrão, o carro não foi vendido.

    def exibir_informacoes(self):
        status_venda = "Vendido" if self.vendido else "Não vendido"
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Status: {status_venda}")

    def vender(self):
        if not self.vendido:
            self.vendido = True
            print("O carro foi marcado como vendido.")
        else:
            print("O carro já foi vendido.")

    def ajustar_preco(self, novo_preco):
        if not self.vendido:
            self.preco = novo_preco
            print("O preço do carro foi ajustado.")
        else:
            print("Não é possível ajustar o preço de um carro vendido.")


# Exemplo de uso da classe Carro com 5 carros:
carro1 = Carro("Toyota", "Corolla", 2022, 75000.00)
carro2 = Carro("Ford", "Mustang", 2021, 100000.00)
carro3 = Carro("Honda", "Civic", 2023, 80000.00)
carro4 = Carro("Chevrolet", "Cruze", 2021, 70000.00)
carro5 = Carro("Volkswagen", "Golf", 2022, 65000.00)

# Exibindo informações dos carros
print("Informações dos carros:")
carro1.exibir_informacoes()
carro2.exibir_informacoes()
carro3.exibir_informacoes()
carro4.exibir_informacoes()
carro5.exibir_informacoes()

# Vendendo alguns carros e ajustando preços
carro1.vender()
carro3.vender()
carro5.vender()
carro2.ajustar_preco(95000.00)

# Exibindo informações atualizadas dos carros
print("\nInformações atualizadas dos carros:")
carro1.exibir_informacoes()
carro2.exibir_informacoes()
carro3.exibir_informacoes()
carro4.exibir_informacoes()
carro5.exibir_informacoes()
