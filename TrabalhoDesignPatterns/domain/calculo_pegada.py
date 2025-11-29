from abc import ABC, abstractmethod

# Interface Strategy
class EstrategiaCalculo(ABC):
    @abstractmethod
    def calcular_emissoes(self, consumo: float) -> float:
        pass

# Concrete Strategy: Escopo 1 (Emissões diretas - ex: Combustível Fóssil)
class CalculoEscopo1(EstrategiaCalculo):
    def calcular_emissoes(self, consumo: float) -> float:
        # Fator de emissão alto (ex: 2.5 kg CO2 por litro)
        return consumo * 2.5

# Concrete Strategy: Escopo 2 (Emissões indiretas - ex: Energia Elétrica)
class CalculoEscopo2(EstrategiaCalculo):
    def calcular_emissoes(self, consumo: float) -> float:
        # Fator da rede elétrica (ex: 0.09 kg CO2 por kWh)
        return consumo * 0.09

# Concrete Strategy: Escopo 3 (Outras indiretas - ex: Viagens corporativas)
class CalculoEscopo3(EstrategiaCalculo):
    def calcular_emissoes(self, consumo: float) -> float:
        # Fator médio para viagens (ex: 0.15 kg CO2 por km)
        return consumo * 0.15

# Context
class CalculadoraPegada:
    def __init__(self, estrategia: EstrategiaCalculo):
        self._estrategia = estrategia

    def definir_estrategia(self, estrategia: EstrategiaCalculo):
        self._estrategia = estrategia

    def calcular(self, consumo: float) -> float:
        return self._estrategia.calcular_emissoes(consumo)