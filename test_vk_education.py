# прошу понять и простить, делаю первый раз :)
import pytest

class TestFloat():
    floatData = 5.75

    # проверка на то что число имеет тип float
    def test_type(self):
        assert isinstance(self.floatData, float)

    # проверка на то, что в числе 2 знака после запятой
    def test_fraction_length(self):
        fraction_length = len(str(self.floatData).split(".")[1].rstrip("0"))
        assert fraction_length == 2

class TestStr():
    strData = 'string'

    # проверка на то что число имеет тип str
    def test_type(self):
        assert isinstance(self.strData, str)

    # проверка на то, что в строке записано целое неотрицательно число
    @pytest.mark.xfail
    @pytest.mark.parametrize("test_input", ['7', 'one', '-5', '(1.1)', '0'])
    def test_is_positive_int(self, test_input):
        assert int(test_input) >= 0

class TestDict():
    dictData =  {"+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"}

    # проверка на то что число имеет тип str
    def test_type(self):
        assert isinstance(self.dictData, dict)

    # проверка на то, что словарь не пустой
    def test_is_not_empty(self):
        assert len(self.dictData) > 0





