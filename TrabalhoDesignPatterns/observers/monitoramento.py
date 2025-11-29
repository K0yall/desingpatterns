from abc import ABC, abstractmethod
from typing import List

# Observer Interface
class Observador(ABC):
    @abstractmethod
    def atualizar(self, mensagem: str):
        pass

# Concrete Observer A
class EmailGerente(Observador):
    def atualizar(self, mensagem: str):
        print(f"[EMAIL] Enviando alerta para o gerente: {mensagem}")

# Concrete Observer B
class LogAuditoria(Observador):
    def atualizar(self, mensagem: str):
        print(f"[LOG SISTEMA] Auditando evento crítico: {mensagem}")

# Subject (O Observável)
class MonitorEmissoes:
    def __init__(self, meta_maxima: float):
        self.meta_maxima = meta_maxima
        self.emissoes_atuais = 0.0
        self._observadores: List[Observador] = []

    def adicionar_observador(self, observador: Observador):
        self._observadores.append(observador)

    def registrar_emissao(self, valor: float):
        self.emissoes_atuais += valor
        print(f"Emissão registrada: {valor}. Total acumulado: {self.emissoes_atuais:.2f}")
        
        if self.emissoes_atuais > self.meta_maxima:
            self.notificar_observadores()

    def notificar_observadores(self):
        msg = f"ALERTA! A meta de {self.meta_maxima} foi excedida. Total atual: {self.emissoes_atuais:.2f}"
        for obs in self._observadores:
            obs.atualizar(msg)