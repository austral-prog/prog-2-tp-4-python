# test sum

import pytest

from src.ej1 import Warehouse


def test_add_to_warehouse():
    warehouse = Warehouse(100, ['a', 'b', 'c'])

    warehouse.add(10, 'a')
    assert warehouse.has('a')
    assert warehouse.get('a') == 10


def test_add_invalid_product():
    warehouse = Warehouse(100, ['a', 'b', 'c'])

    warehouse.add(10, 'd')
    assert not warehouse.has('d')
    assert warehouse.get('d') == 0


def test_remove_product():
    warehouse = Warehouse(100, ['a', 'b', 'c'])

    warehouse.add(10, 'a')
    warehouse.remove(5, 'a')
    assert warehouse.has('a')
    assert warehouse.get('a') == 5
    warehouse.remove(5, 'a')
    assert not warehouse.has('a')
    assert warehouse.get('a') == 0


def test_list_products():
    warehouse = Warehouse(100, ['a', 'b', 'c'])

    warehouse.add(10, 'a')
    warehouse.add(20, 'b')
    warehouse.add(30, 'c')
    assert warehouse.list() == ['a', 'b', 'c']
