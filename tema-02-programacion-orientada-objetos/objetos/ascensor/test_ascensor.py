import pytest
from ascensor import Ascensor


@pytest.fixture()
def a():
    return Ascensor(-2, 10, 5)


def test_ir_a_piso_valido(a):
    assert a.ir_a_piso(3) is True
    assert a.piso_actual == 3


def test_ir_a_piso_invalido(a):
    # al fallar no cambia el piso actual (sigue en 0 si no se movió antes)
    assert a.ir_a_piso(15) is False
    assert a.piso_actual == 0


def test_subir_personas(a):
    assert a.subir(3) == 3
    assert a.personas == 3
    assert a.subir(4) == 2  # solo entran 2 (capacidad 5)
    assert a.personas == 5


def test_subir_invalido(a):
    assert a.subir(0) == -1
    assert a.subir(-3) == -1
    assert a.personas == 0


def test_bajar_personas(a):
    a.subir(4)
    assert a.bajar(2) == 2
    assert a.personas == 2
    assert a.bajar(10) == 2  # bajan todas las que quedan
    assert a.personas == 0


def test_bajar_invalido(a):
    a.subir(2)
    assert a.bajar(0) == -1
    assert a.bajar(-1) == -1
    assert a.personas == 2



def test_constructor_piso_inicial_cero_dentro_de_rango():
    a1 = Ascensor(-2, 10, 5)
    assert a1.piso_actual == 0
    # 0 no está en rango [-10, -1], debe lanzar error
    with pytest.raises(ValueError):
        Ascensor(-10, -1, 3)
    # también debe lanzar error si el rango es [1, 10]
    with pytest.raises(ValueError):
        Ascensor(1, 10, 4)


def test_constructor_parametros_invalidos():
    with pytest.raises(ValueError):
        Ascensor(5, -1, 5)
    with pytest.raises(ValueError):
        Ascensor(-2, 10, 0)
