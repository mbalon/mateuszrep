from geomfuntools import GeomTools


def test_find_middle_point_of_segment_1():
    x = (1, 0)
    y = (4, 0)

    output = GeomTools.find_middle_point_of_segment(x, y)

    assert output == (2.5, 0)


def test_find_middle_point_of_segment_2():
    x = (0, 0)
    y = (0, 4)

    output = GeomTools.find_middle_point_of_segment(x, y)

    assert output == (0, 2)

def test_find_middle_point_of_segment_3():
    x = (7, 0)
    y = (-1, 0)

    output = GeomTools.find_middle_point_of_segment(x, y)

    assert output == (3, 0)

def test_find_middle_point_of_segment_4():
    x = (0, 4)
    y = (0, 0)

    output = GeomTools.find_middle_point_of_segment(x, y)

    assert output == (0, 2)

def test_is_rectangle_separate_1():
    x = ((0, 0), 3, 3)
    y = ((4, 0), 4, 4)

    output = GeomTools.is_rectangle_separate(x, y)

    assert output == True

def test_is_rectangle_separate_2():
    x = ((0, 0), 3, 3)
    y = ((0, 0), 4, 4)

    output = GeomTools.is_rectangle_separate(x, y)

    assert output == False

def test_is_rectangle_separate_3():
    x = ((1, 1), 2, 2)
    y = ((0, 0), 4, 4)

    output = GeomTools.is_rectangle_separate(x, y)

    assert output == False

def test_is_rectangle_separate_4():
    x = ((0, 0), 4, 4)
    y = ((1, 1), 3, 3)

    output = GeomTools.is_rectangle_separate(x, y)

    assert output == False

