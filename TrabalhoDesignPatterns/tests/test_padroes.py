import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from strategies.calculo_pegada import CalculadoraPegada, CalculoEscopo1, CalculoEscopo2
from decorators.certificados import CreditoPadrao, CertificadoVerificacao, RastreabilidadeBlockchain
from observers.monitoramento import MonitorEmissoes, Observador

class TestDesignPatterns(unittest.TestCase):

    # Teste Strategy: Troca dinâmica
    def test_strategy_troca_dinamica(self):
        calc = CalculadoraPegada(CalculoEscopo1()) # Fator 2.5
        self.assertEqual(calc.calcular(10), 25.0)
        
        calc.definir_estrategia(CalculoEscopo2()) # Fator 0.09
        self.assertEqual(calc.calcular(100), 9.0)

    # Teste Decorator: Empilhamento de preços
    def test_decorator_soma_precos(self):
        credito = CreditoPadrao() # 50.0
        credito_verificado = CertificadoVerificacao(credito) # +15.0
        credito_completo = RastreabilidadeBlockchain(credito_verificado) # +25.0
        
        self.assertEqual(credito_completo.get_preco(), 90.0)
        self.assertIn("Blockchain", credito_completo.get_descricao())

    # Teste Observer: Notificação
    def test_observer_notificacao(self):
        class MockObserver(Observador):
            def __init__(self): self.notificado = False
            def atualizar(self, msg): self.notificado = True
            
        monitor = MonitorEmissoes(meta_maxima=50)
        mock_obs = MockObserver()
        monitor.adicionar_observador(mock_obs)
        
        monitor.registrar_emissao(30)
        self.assertFalse(mock_obs.notificado) # 30 < 50
        
        monitor.registrar_emissao(21) # Total 51 > 50
        self.assertTrue(mock_obs.notificado)

if __name__ == '__main__':
    unittest.main()