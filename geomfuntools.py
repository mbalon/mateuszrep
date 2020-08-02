class GeomTools:
    @staticmethod
    def find_middle_point_of_segment(point1: tuple, point2: tuple) -> tuple:
        return (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2

    @staticmethod
    def is_rectangle_seperate(rect1: tuple, rect2: tuple) -> bool:
        return rect1[0][0] + rect1[1] <= rect2[0][0] or rect1[0][1] + rect1[2] <= rect2[0][1] \
                or rect2[0][0] + rect2[1] <= rect1[0][0] or rect2[0][1] + rect2[2] <= rect2[0][1]
