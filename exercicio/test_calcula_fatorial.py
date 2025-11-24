import pytest
from calcula_fatorial import fatorial

@pytest.mark.parametrize("n, fatorial_esperado",[
    (0,1),
    (1,1),
    (2,2),
    (3,6),
    (5,120),
    (25,15511210043330985984000000),
    (29,8841761993739701954543616000000)
])

def test_calcula_fatorial(n,fatorial_esperado):
    assert fatorial(n) == fatorial_esperado

@pytest.mark.parametrize("n", [-1, -5, -10])
def test_calcula_fatorial_negativo(n):
    with pytest.raises(RecursionError):
        fatorial(n)