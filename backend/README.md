# MegaLoja Online API
Fornece as principais funções do e-commerce MegaLoja online.

## Estrutura da API
| Camada         | Responsabilidade                                                                      |
|----------------|---------------------------------------------------------------------------------------|
| `routes`       | Receber requisições HTTP e devolver respostas HTTP.                                   |
| `schemas`      | Definir os formatos de entrada e saída da API.                                        |
| `models`       | Representar as entidades e estruturas de dados do domínio e da persistência.          |
| `services`     | Implementar os casos de uso e as regras de negócio.                                   |
| `repositories` | Abstrair operações de persistência e consultas ao banco.                              |
| `integrations` | Comunicar-se com sistemas externos, como gateways de pagamento e serviços de estoque. |

## Entidades do Domínio
| Entidade    | Responsabilidade                                            |
|-------------|-------------------------------------------------------------|
| `Customer`  | Representa o cliente que realiza a compra.                  |
| `Product`   | Representa um produto comercializado.                       |
| `Store`     | Representa uma unidade física da loja.                      |
| `Inventory` | Representa a disponibilidade de produtos em uma unidade.    |
| `Order`     | Representa uma compra realizada.                            |
| `OrderItem` | Representa um produto e sua quantidade dentro de um pedido. |
| `Payment`   | Representa a operação financeira associada ao pedido.       |
| `Pickup`    | Representa as informações referentes à retirada.            |

# Referências de desenvolvimento:
1.  https://pydevtools.com/handbook/tutorial/getting-started-with-uv/
2.  https://pydevtools.com/handbook/how-to/how-to-translate-pip-commands-to-uv/
