import pytest

from correctivo import Correctivo
from maquina import Maquina
from preventivo import Preventivo


@pytest.fixture()
def maquina():
    maq = Maquina()
    maq.agregar_mantenimiento(Preventivo("1/1", "ANA", 5000, 2, 3000))
    maq.agregar_mantenimiento(Preventivo("1/1", "BETO", 10000, 1, 1))
    maq.agregar_mantenimiento(Correctivo("2/2", "CARI", 4000, 10, 8000))
    maq.agregar_mantenimiento(Correctivo("3/3", "DIEGO", 1000, 20, 2000))
    return maq


def test_gasto_preventivo_repuestos_mas_insumos():
    mantenimiento = Preventivo("1/1", "ANA", 5000, 2, 3000)
    assert mantenimiento.gasto_total() == 8000


def test_gasto_correctivo_repuestos_mas_tecnico():
    mantenimiento = Correctivo("2/2", "CARI", 4000, 10, 8000)
    assert mantenimiento.gasto_total() == 12000


def test_maquina_comienza_sin_mantenimientos():
    maq = Maquina()
    assert maq.suma_gastos() == 0
    assert maq.cantidad_mantenimientos_caros() == 0
    assert maq.rotura_mas_larga() is None


def test_agregar_mantenimientos(maquina):
    assert len(maquina.mantenimientos) == 4


def test_suma_gastos(maquina):
    # 8000 + 10001 + 12000 + 3000
    assert maquina.suma_gastos() == 33001


def test_cantidad_mantenimientos_caros(maquina):
    # solo 10001 y 12000 superan los $10.000
    assert maquina.cantidad_mantenimientos_caros() == 2


def test_caro_no_cuenta_el_justo_en_10000():
    maq = Maquina()
    maq.agregar_mantenimiento(Preventivo("1/1", "EDITA", 10000, 1, 0))
    assert maq.cantidad_mantenimientos_caros() == 0


def test_rotura_mas_larga(maquina):
    # el correctivo de DIEGO tiene la mayor duracion (20)
    assert maquina.rotura_mas_larga() == "3/3 DIEGO"


def test_rotura_mas_larga_no_considera_preventivos():
    maq = Maquina()
    maq.agregar_mantenimiento(Preventivo("1/1", "FEDE", 100, 1, 100))
    maq.agregar_mantenimiento(Correctivo("2/2", "GABO", 100, 30, 100))
    assert maq.rotura_mas_larga() == "2/2 GABO"


def test_rotura_mas_larga_selecciona_la_mayor():
    maq = Maquina()
    maq.agregar_mantenimiento(Correctivo("10/4", "HILDA", 1000, 7, 100))
    maq.agregar_mantenimiento(Correctivo("9/3", "INES", 1000, 15, 100))
    assert maq.rotura_mas_larga() == "9/3 INES"


def test_rotura_mas_larga_sin_correctivos():
    maq = Maquina()
    maq.agregar_mantenimiento(Preventivo("1/1", "JORGE", 100, 1, 100))
    assert maq.rotura_mas_larga() is None


def test_gasto_correctivo_solo_repuestos_sin_tecnico():
    mantenimiento = Correctivo("2/2", "KIKA", 4000, 5, 0)
    assert mantenimiento.gasto_total() == 4000