import pytest

from empresa import Empresa
from hiper import Hiper
from mini import Mini
from super import Super


@pytest.fixture()
def empresa():
    emp = Empresa()
    emp.agregar_sucursal(Hiper(1, 1000, 50000, 30000))
    emp.agregar_sucursal(Hiper(2, 1000, 20000, 20000))
    emp.agregar_sucursal(Super(3, 1000, 45000, False))
    emp.agregar_sucursal(Super(4, 1000, 44000, False))
    emp.agregar_sucursal(Super(5, 1000, 46000, True))
    emp.agregar_sucursal(Super(6, 1000, 45000, True))
    emp.agregar_sucursal(Mini(7, 1000, 50000, 10000))
    emp.agregar_sucursal(Mini(8, 1000, 40000, 5000))
    return emp


def test_resultado_comercial_hiper_suma_alquileres():
    hiper = Hiper(1, 1000, 50000, 30000)
    # facturacion + alquileres
    assert hiper.resultado_comercial() == 80000


def test_resultado_comercial_super_es_la_facturacion():
    super = Super(3, 1000, 45000, False)
    assert super.resultado_comercial() == 45000


def test_resultado_comercial_mini_resta_alquiler():
    mini = Mini(7, 1000, 50000, 10000)
    assert mini.resultado_comercial() == 40000


def test_hiper_rentable_solo_si_indice_mayor_50():
    assert Hiper(1, 1000, 50000, 30000).es_rentable() is True   # 80
    assert Hiper(2, 1000, 20000, 20000).es_rentable() is False  # 40


def test_super_tradicional_rentable_solo_si_indice_mayor_40():
    assert Super(1, 1000, 41000, False).es_rentable() is True   # 41
    assert Super(2, 1000, 40000, False).es_rentable() is False  # 40


def test_super_mayorista_rentable_solo_si_indice_mayor_45():
    assert Super(1, 1000, 46000, True).es_rentable() is True    # 46
    assert Super(2, 1000, 45000, True).es_rentable() is False   # 45


def test_mini_rentable_solo_si_indice_mayor_35():
    assert Mini(1, 1000, 50000, 10000).es_rentable() is True    # 40
    assert Mini(2, 1000, 40000, 5000).es_rentable() is False    # 35


def test_empresa_comienza_vacia():
    emp = Empresa()
    assert emp.suma_ganancia() == 0
    assert emp.cantidad_no_rentables() == 0
    assert emp.local_mas_rentable() is None


def test_agregar_sucursales(empresa):
    assert len(empresa.sucursales) == 8


def test_suma_ganancia(empresa):
    # 80000 + 40000 + 45000 + 44000 + 46000 + 45000 + 40000 + 35000
    assert empresa.suma_ganancia() == 375000


def test_cantidad_locales_no_rentables(empresa):
    # no rentables: hiper 2 (40), super 6 (45) y mini 8 (35)
    assert empresa.cantidad_no_rentables() == 3


def test_local_mas_rentable(empresa):
    local = empresa.local_mas_rentable()
    assert local.numero == 1
    assert local.tipo() == 1
    assert str(local) == "1 1"


def test_local_mas_rentable_con_un_solo_local():
    emp = Empresa()
    emp.agregar_sucursal(Super(15, 100, 40000, False))
    local = emp.local_mas_rentable()
    assert local.numero == 15
    assert local.tipo() == 2