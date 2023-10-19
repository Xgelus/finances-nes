from datetime import datetime
from finances import Transaction, settings

DEFAULT_AMMOUNT = 100.0
DEFAULT_CATEGORY = settings.CAT_CASA
DEFAULT_DESCRIPTION = 'Transação de testes.'

def get_transaction():
    """Gera uma transação de testes com valores pré definidos.
    
    Returns:
        Transaction: transação de testes.
    """
    return Transaction(DEFAULT_AMMOUNT, DEFAULT_CATEGORY, DEFAULT_DESCRIPTION)
    

def test_transction_instance():
    """Confere se os objetos são instanciados corretamente.
    """
    tr = get_transaction()
    assert isinstance(tr, Transaction)
    
def test_transction_atributes():
    """Confere os valores e tipos dos atributos
    """
    tr = get_transaction()
    
    # Confere os valores:
    assert tr.amount == DEFAULT_AMMOUNT, 'O valor da transação está incorreto.'
    assert tr.category == DEFAULT_CATEGORY, 'O valor da categoria está incorreto.'
    assert tr.description == DEFAULT_DESCRIPTION, 'A descrição está incorreta.'
    assert tr.date <= datetime.now(), 'A data da transação não pode estar no futuro.'
    
    # Confere os tipos
    assert type(tr.amount) is float, 'O valor da transação não é float.'
    assert type(tr.category) is int, 'O valor da categoria não é int.'
    assert type(tr.description) is str, 'A descrição não é str.'    
    assert type(tr.date) is datetime, 'O tipo da data está incorreto'
    
def test_transaction_print():
    """Confere se a descrição da transação está correta.
    """
    tr = get_transaction()
    assert str(tr) == f'Transação: {DEFAULT_DESCRIPTION} R$ {DEFAULT_AMMOUNT:.2f} ({settings.CAT_STRING[DEFAULT_CATEGORY]})'
    