from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

# Criando instâncias da classe Restaurante
restaurante_hotdog = Restaurante('HotDog', 'Cachorro Quente')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
bebida_suco.aplicar_Desconto()
prato_pao = Prato('Pão', 2.0, 'O melhor pão da cidade')
prato_pao.aplicar_Desconto()
restaurante_hotdog.adicionar_no_cardapio(bebida_suco)
restaurante_hotdog.adicionar_no_cardapio(prato_pao)

def main():
    restaurante_hotdog.exibir_cardapio  

if __name__ == '__main__':
    main()
