from lib import bubbleSort
import pytest


# задаем числа в порядке возрастания
@pytest.fixture()
def minToMaxNumbers():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# задаем числа в случайном порядке
@pytest.fixture()
def randomNumbers():
    return [38, 18, 0, 1, 4, 71, 3, 4, 9, 2]


# задаем одинаковые числа

@pytest.fixture()
def equalNumbers():
    return [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


# задачем числа в порядке убывания
@pytest.fixture()
def maxToMin():
    return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# задачем числа с ошибкой, последний элемент типа str
@pytest.fixture()
def incorrectNumbers():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, '10']


# тестируем сортировку с числами по возрастанию
def test_MinToMaxNumbers(minToMaxNumbers):
    assert bubbleSort(minToMaxNumbers) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# тестируем сортировку с числами в случайном порядке
def test_RandomNumbers(randomNumbers):
    assert bubbleSort(randomNumbers) == [0, 1, 2, 3, 4, 4, 9, 18, 38, 71]


# тестируем сортировку с одинаковыми числами
def test_EqualNumbers(equalNumbers):
    assert bubbleSort(equalNumbers) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


# тестируем сортировку с числами по убыванию
def test_MaxToMin(maxToMin):
    assert bubbleSort(maxToMin) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# тестируем сортировку с последним элементом массива типа str исключая ошибку
def test_IncorrectNumbers(incorrectNumbers):
    with pytest.raises(TypeError):
        bubbleSort(incorrectNumbers)
