from cardano_helpers import __version__
from cardano_helpers import *

def test_version():
    assert __version__ == '0.1.0'

def test_transaction_instantiation():
    from .oura_transaction import oura_transaction
    tx = create_transaction_object(oura_transaction)
    assert tx
    assert isinstance(tx.outputs[0], UTXO)
    assert isinstance(tx.outputs[0].assets[0], Asset)
    assert isinstance(tx.inputs[0], Input) 