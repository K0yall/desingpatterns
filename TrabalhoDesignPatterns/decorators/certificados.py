from abc import ABC, abstractmethod

# Component Interface
class ICreditoCarbono(ABC):
    @abstractmethod
    def get_descricao(self) -> str:
        pass

    @abstractmethod
    def get_preco(self) -> float:
        pass

# Concrete Component
class CreditoPadrao(ICreditoCarbono):
    def get_descricao(self) -> str:
        return "Crédito de Carbono Padrão (1 ton)"

    def get_preco(self) -> float:
        return 50.00  # Preço base em Reais

# Base Decorator
class CreditoDecorator(ICreditoCarbono):
    def __init__(self, credito: ICreditoCarbono):
        self._credito = credito

    def get_descricao(self) -> str:
        return self._credito.get_descricao()

    def get_preco(self) -> float:
        return self._credito.get_preco()

# Concrete Decorator A: Verificação de Terceiros
class CertificadoVerificacao(CreditoDecorator):
    def get_descricao(self) -> str:
        return super().get_descricao() + " + Selo de Verificação ISO"

    def get_preco(self) -> float:
        return super().get_preco() + 15.00

# Concrete Decorator B: Rastreabilidade Blockchain
class RastreabilidadeBlockchain(CreditoDecorator):
    def get_descricao(self) -> str:
        return super().get_descricao() + " + Registro em Blockchain"

    def get_preco(self) -> float:
        return super().get_preco() + 25.00