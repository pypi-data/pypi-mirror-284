from .cifp_controlled_airspace_point import CIFPControlledAirspacePoint
from .cifp_functions import clean_value


class CIFPControlledAirspaceSegment:
    def __init__(self) -> None:
        self.multiple_code = None
        self.airspace_name = None
        self.points: list[CIFPControlledAirspacePoint] = []

    def from_lines(self, cifp_lines: list) -> None:
        initial_line = str(cifp_lines[0])
        self.multiple_code = initial_line[19:20].strip()
        self.airspace_name = initial_line[93:123].strip()

        for cifp_line in cifp_lines:
            point = CIFPControlledAirspacePoint()
            point.from_line(cifp_line)
            self.points.append(point)

    def to_dict(self) -> dict:
        points = []
        for item in self.points:
            points.append(item.to_dict())

        return {
            "multiple_code": clean_value(self.multiple_code),
            "airspace_name": clean_value(self.airspace_name),
            "points": points,
        }
