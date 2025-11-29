import sys
import os

# Ajusta o path para encontrar os módulos irmãos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from strategies.calculo_pegada import CalculadoraPegada, CalculoEscopo1, CalculoEscopo2, CalculoEscopo3
from decorators.certificados import CreditoPadrao, CertificadoVerificacao, RastreabilidadeBlockchain
from observers.monitoramento import MonitorEmissoes, EmailGerente, LogAuditoria

def main():
    while True:
        print("\n=== SISTEMA DE MERCADO DE CARBONO ===")
        print("1. Strategy: Calcular Pegada (Escopos 1, 2, 3)")
        print("2. Decorator: Cotar Crédito com Certificados")
        print("3. Observer: Monitorar Metas de Emissão")
        print("0. Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            consumo = float(input("Digite o consumo (litros/kWh/km): "))
            tipo = input("Tipo (1-Combustível, 2-Energia, 3-Viagem): ")
            
            calc = CalculadoraPegada(CalculoEscopo1()) # Default
            
            if tipo == '2': calc.definir_estrategia(CalculoEscopo2())
            elif tipo == '3': calc.definir_estrategia(CalculoEscopo3())
            
            res = calc.calcular(consumo)
            print(f"Pegada calculada: {res:.2f} kg CO2")

        elif opcao == '2':
            credito = CreditoPadrao()
            print(f"Base: {credito.get_descricao()} | R$ {credito.get_preco():.2f}")
            
            if input("Adicionar Verificação ISO? (s/n): ") == 's':
                credito = CertificadoVerificacao(credito)
            
            if input("Adicionar Blockchain? (s/n): ") == 's':
                credito = RastreabilidadeBlockchain(credito)
                
            print(f"FINAL: {credito.get_descricao()} | TOTAL: R$ {credito.get_preco():.2f}")

        elif opcao == '3':
            monitor = MonitorEmissoes(meta_maxima=100.0)
            monitor.adicionar_observador(EmailGerente())
            monitor.adicionar_observador(LogAuditoria())
            
            print("Meta definida em 100.0 kg CO2")
            while monitor.emissoes_atuais <= 100.0:
                val = float(input("Registrar nova emissão: "))
                monitor.registrar_emissao(val)
                if monitor.emissoes_atuais > 100.0:
                    print("--- Limite rompido, notificando observers ---")
                    break

        elif opcao == '0':
            break
            
        print("-" * 40)
        # REQUISITO OBRIGATÓRIO: NOME NO RODAPÉ
        print("Desenvolvido por: Lucas Gilmar da Silva")
        print("-" * 40)

if __name__ == "__main__":
    main()