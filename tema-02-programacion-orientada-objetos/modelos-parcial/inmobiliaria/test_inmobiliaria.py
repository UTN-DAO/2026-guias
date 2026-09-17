import pytest

from casa import Casa
from departamento import Departamento
from inmobiliaria import Inmobiliaria


@pytest.fixture()
def inmobiliaria():
    inm = Inmobiliaria()
    inm.agregar(Casa(1, "ANA", 100, 200000, 3, False))
    inm.agregar(Casa(2, "BETO", 160, 150000, 3, True))
    inm.agregar(Departamento(3, "CARI", 80, 300000, 50000, 5))
    inm.agregar(Departamento(4, "DIEGO", 70, 250000, 40000, 1))
    return inm


def test_alquiler_casa_sin_pileta():
    casa = Casa(1, "ANA", 100, 200000, 3, False)
    # 200000 + 3 * 30000
    assert casa.alquiler() == 290000


def test_alquiler_casa_con_pileta():
    casa = Casa(2, "BETO", 160, 150000, 3, True)
    # 150000 + 3 * 30000 + 100000
    assert casa.alquiler() == 340000


def test_alquiler_departamento_piso_inferior_al_tercero():
    depto = Departamento(4, "DIEGO", 70, 250000, 40000, 1)
    # 250000 + 20000 + 40000
    assert depto.alquiler() == 310000


def test_alquiler_departamento_planta_baja():
    depto = Departamento(5, "EDITA", 60, 180000, 30000, 0)
    # 180000 + 20000 + 30000
    assert depto.alquiler() == 230000


def test_alquiler_departamento_tercer_piso_sin_extra():
    depto = Departamento(6, "FEDE", 90, 220000, 35000, 3)
    # 220000 + 35000
    assert depto.alquiler() == 255000


def test_inmobiliaria_comienza_vacia():
    ins = Inmobiliaria()
    assert ins.suma_alquileres() == 0
    assert ins.cantidad_casas_premium() == 0
    assert ins.propietario_alquiler_mas_bajo() is None


def test_agregar_inmuebles(inmobiliaria):
    assert len(inmobiliaria.inmuebles) == 4


def test_suma_alquileres(inmobiliaria):
    # 290000 + 340000 + 350000 + 310000
    assert inmobiliaria.suma_alquileres() == 1290000


def test_cantidad_casas_premium(inmobiliaria):
    # solo la casa de BETO: más de 150 m2, más de 2 dormitorios y pileta
    assert inmobiliaria.cantidad_casas_premium() == 1


def test_casas_premium_no_cuenta_la_sin_pileta():
    ins = Inmobiliaria()
    ins.agregar(Casa(1, "ANA", 180, 200000, 3, False))
    assert ins.cantidad_casas_premium() == 0


def test_casas_premium_no_cuenta_superficie_menor_o_igual_150():
    ins = Inmobiliaria()
    ins.agregar(Casa(1, "GABO", 150, 200000, 4, True))
    ins.agregar(Casa(2, "HUGO", 120, 200000, 3, True))
    assert ins.cantidad_casas_premium() == 0


def test_casas_premium_no_cuenta_2_dormitorios_o_menos():
    ins = Inmobiliaria()
    ins.agregar(Casa(1, "INES", 200, 200000, 2, True))
    assert ins.cantidad_casas_premium() == 0


def test_casas_premium_no_cuenta_departamentos():
    ins = Inmobiliaria()
    depto = Departamento(1, "JORGE", 200, 200000, 30000, 1)
    ins.agregar(depto)
    assert ins.cantidad_casas_premium() == 0


def test_propietario_alquiler_mas_bajo(inmobiliaria):
    # el departamento de DIEGO (310000) es el más barato
    assert inmobiliaria.propietario_alquiler_mas_bajo() == "DIEGO"


def test_propietario_mas_bajo_considera_solo_departamentos():
    ins = Inmobiliaria()
    ins.agregar(Casa(1, "UNA CASA BARATA", 80, 50000, 1, False))
    ins.agregar(Departamento(2, "EL DEPTO MAS CARO", 80, 900000, 100000, 3))
    assert ins.propietario_alquiler_mas_bajo() == "EL DEPTO MAS CARO"


def test_propietario_mas_bajo_sin_departamentos():
    ins = Inmobiliaria()
    ins.agregar(Casa(1, "KIKA", 100, 200000, 3, False))
    assert ins.propietario_alquiler_mas_bajo() is None