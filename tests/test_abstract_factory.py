from src.patterns import abstract_factory

import pytest
from math import pi

class TestCircle:

    @pytest.mark.parametrize("radius", [1, 5, 200, -1, 0])
    def test_area(self, radius):
        if radius > 0:
            expected = pi * radius * radius
            actual = abstract_factory.ShapeFactory().get_shape(shapeType="circle", size=radius).get_area()
            assert pytest.approx(expected, 0.1) == actual
        else:
            with pytest.raises(ValueError) as e:
                abstract_factory.ShapeFactory().get_shape(shapeType="circle", size=radius).get_area()


    @pytest.mark.parametrize("radius", [1, 5, 200, -1, 0])
    def testperimeter(self, radius):
        if radius > 0:
            expected = 2 * pi * radius
            actual = abstract_factory.ShapeFactory().get_shape(shapeType="circle", size=radius).get_perimeter()
            assert pytest.approx(expected, 0.1) == actual
        else:
            with pytest.raises(ValueError) as e:
                abstract_factory.ShapeFactory().get_shape(shapeType="circle", size=radius).get_perimeter()


class TestSquare:

    @pytest.mark.parametrize("size", [1, 5, 200, -1, 0])
    def test_area(self, size):
        if size > 0:
            expected = size * size
            actual = abstract_factory.ShapeFactory().get_shape(shapeType="square", size=size).get_area()
            assert pytest.approx(expected, 0.1) == actual
        else:
            with pytest.raises(ValueError) as e:
                abstract_factory.ShapeFactory().get_shape(shapeType="square", size=size).get_area()

    @pytest.mark.parametrize("size", [1, 5, 200, -1, 0])
    def testperimeter(self, size):
        if size > 0:
            expected = 4 * size
            actual = abstract_factory.ShapeFactory().get_shape(shapeType="square", size=size).get_perimeter()
            assert pytest.approx(expected, 0.1) == actual
        else:
            with pytest.raises(ValueError) as e:
                abstract_factory.ShapeFactory().get_shape(shapeType="square", size=size).get_perimeter()
