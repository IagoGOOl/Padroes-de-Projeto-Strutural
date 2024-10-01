class Cor:
    def aplicar_cor(self):
        pass

class Vermelho(Cor):
    def aplicar_cor(self):
        return "Vermelho"

class Azul(Cor):
    def aplicar_cor(self):
        return "Azul"

class Forma:
    def __init__(self, cor):
        self.cor = cor

    def desenhar(self):
        pass

class Circulo(Forma):
    def desenhar(self):
        return f"Círculo desenhado na cor {self.cor.aplicar_cor()}."

class Quadrado(Forma):
    def desenhar(self):
        return f"Quadrado desenhado na cor {self.cor.aplicar_cor()}."

if __name__ == "__main__":
    cor_vermelha = Vermelho()
    cor_azul = Azul()

    circulo_vermelho = Circulo(cor_vermelha)
    quadrado_azul = Quadrado(cor_azul)

    print(circulo_vermelho.desenhar())
    print(quadrado_azul.desenhar())     
