from datetime import datetime
from evento import Evento

class Agenda:
    
    def __init__(self):
        self.eventos = []
    
    def adicionar_evento(self, evento):
        for e in self.eventos:
            if (evento.inicio < e.termino and evento.termino > e.inicio):
                raise ValueError("Evento tem conflito de horário com um ou mais eventos cadastrados")
            if (evento.nome == e.nome):
                raise ValueError("Evento tem o mesmo nome de outro evento cadastrado")
        self.eventos.append(evento)
        return f"Evento {evento.nome} adicionado com sucesso"
    
    def remover_evento(self, nome):
        for evento in self.eventos:
            if evento.nome == nome:
                self.eventos.remove(evento)
                return "Evento removido com sucesso."
        return "Evento não encontrado."
    
    def get_evento(self, nome):
        for evento in self.eventos:
            if evento.nome == nome:
                return evento
        return "Evento não encontrado."
    
    def mostrar_agenda(self):
        agenda_list = []
        for evento in self.eventos:
            agenda_list.append(f"{evento.nome}: {evento.inicio.strftime('%Y-%m-%d %H:%M')} a {evento.termino.strftime('%Y-%m-%d %H:%M')}")
        return agenda_list
