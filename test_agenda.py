import sys
import os
import pytest
from datetime import datetime
from agenda import Agenda
from evento import Evento

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

@pytest.fixture
def agenda():   
    return Agenda()

def test_cadastrar_evento(agenda):    
    evento = Evento("Jogo 1", datetime.fromisoformat("2024-07-24 10:00"), datetime.fromisoformat("2024-07-24 11:00"))
    mensagem = agenda.adicionar_evento(evento)

    assert mensagem == "Evento Jogo 1 adicionado com sucesso"

def test_cadastrar_evento2(agenda):
    novo_evento = Evento("aaaa", datetime.fromisoformat("2024-07-24 11:30"), datetime.fromisoformat("2024-07-24 12:30"))
    mensagem = agenda.adicionar_evento(novo_evento)

    assert mensagem == "Evento aaaa adicionado com sucesso"

def test_cadastrar_evento3(agenda):
    novo_evento = Evento("Reunião Importante",  datetime.fromisoformat("2024-07-24 10:00"), datetime.fromisoformat("2024-07-24 11:00"))
    mensagem = agenda.adicionar_evento(novo_evento)
    
    assert mensagem == "Evento Reunião Importante adicionado com sucesso"
    
def test_mostrar_agenda(agenda):
    evento1 = Evento("Final dos 100m", "2024-07-24T10:00:00", "2024-07-24T11:00:00")
    evento2 = Evento("Final dos 200m", "2024-07-24T11:30:00", "2024-07-24T12:30:00")
    agenda.adicionar_evento(evento1)
    agenda.adicionar_evento(evento2)
    result = agenda.mostrar_agenda()
    expected_result = [
        "Final dos 100m: 2024-07-24 10:00 a 2024-07-24 11:00",
        "Final dos 200m: 2024-07-24 11:30 a 2024-07-24 12:30"
    ]
    assert result == expected_result

def test_remover_agenda(agenda):
    evento1 = Evento("Final dos 100m", datetime.fromisoformat("2024-07-24 10:00"), datetime.fromisoformat("2024-07-24 11:00"))
    agenda.adicionar_evento(evento1)
    mensagem = agenda.remover_evento(evento1)

    assert mensagem == "Evento removido com sucesso."