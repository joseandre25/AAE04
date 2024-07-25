from src.agenda import Agenda
from src.evento import Evento

def main():
    agenda = Agenda()
    
    while True:
        acao = input("Digite a ação (adicionar, remover, mostrar, sair): ").strip().lower()
        #funcao adicionar
        if acao == 'adicionar':
            nome = input("Digite o nome do evento: ").strip()
            inicio = input("Digite a hora de início (YYYY-MM-DD HH:MM): ").strip()
            termino = input("Digite a hora de término (YYYY-MM-DD HH:MM): ").strip()
            try:
                evento = Evento(nome, inicio, termino)
                resultado = agenda.adicionar_evento(evento)
                print(resultado)
            except ValueError as e:
                print(e)
        #funcao remover
        elif acao == 'remover':
            nome = input("Digite o nome do evento para remover: ").strip()
            resultado = agenda.remover_evento(nome)
            print(resultado)
        #funcao mostrar
        elif acao == 'mostrar':
            eventos = agenda.mostrar_agenda()
            for evento in eventos:
                print(evento)
        #funcao sair
        elif acao == 'sair':
            break
        
        else:
            print("Ação inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
