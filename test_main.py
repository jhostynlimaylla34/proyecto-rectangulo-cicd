import pytest
from main import calcular_area


def test_area_rectangulo():
    resultado = calcular_area(5, 4)
    assert resultado == 20


def test_area_con_decimales():
    resultado = calcular_area(2.5, 4)
    assert resultado == 10


def test_base_negativa():
    with pytest.raises(ValueError):
        calcular_area(-5, 4)


def test_altura_cero():
    with pytest.raises(ValueError):
        calcular_area(5, 0)
