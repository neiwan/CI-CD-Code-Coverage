import my_lib
import pytest


# тест сортировки пузырьком
class TestSortBubble:
    # задаем числа в порядке возрастания
    @pytest.fixture()
    def minToMaxNumbers(self):
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # задаем числа в случайном порядке
    @pytest.fixture()
    def randomNumbers(self):
        return [38, 18, 0, 1, 4, 71, 3, 4, 9, 2]

    # задаем одинаковые числа
    @pytest.fixture()
    def equalNumbers(self):
        return [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    # задачем числа в порядке убывания
    @pytest.fixture()
    def maxToMin(self):
        return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # задачем числа с ошибкой, последний элемент типа str
    @pytest.fixture()
    def incorrectNumbers(self):
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, '10']

    # тестируем сортировку с числами по возрастанию
    def testMinToMaxNumbers(self, minToMaxNumbers):
        assert my_lib.bubbleSort(minToMaxNumbers) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # тестируем сортировку с числами в случайном порядке
    def testRandomNumbers(self, randomNumbers):
        assert my_lib.bubbleSort(randomNumbers) == [0, 1, 2, 3, 4, 4, 9, 18, 38, 71]

    # тестируем сортировку с одинаковыми числами
    def testEqualNumbers(self, equalNumbers):
        assert my_lib.bubbleSort(equalNumbers) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    # тестируем сортировку с числами по убыванию
    def testMaxToMin(self, maxToMin):
        assert my_lib.bubbleSort(maxToMin) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # тестируем сортировку с последним элементом массива типа str исключая ошибку
    def testIncorrectNumbers(self, incorrectNumbers):
        with pytest.raises(TypeError):
            my_lib.bubbleSort(incorrectNumbers)
