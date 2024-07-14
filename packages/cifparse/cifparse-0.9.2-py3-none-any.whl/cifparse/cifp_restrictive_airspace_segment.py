from .cifp_restrictive_airspace_point import CIFPRestrictiveAirspacePoint
from .cifp_functions import clean_value


class CIFPRestrictiveAirspaceSegment:
    def __init__(self) -> None:
        self.multiple_code = None
        self.lower_limit = None
        self.lower_unit = None
        self.upper_limit = None
        self.upper_unit = None
        self.points: list[CIFPRestrictiveAirspacePoint] = []

    def from_lines(self, cifp_lines: list) -> None:
        initial_line = str(cifp_lines[0])
        self.multiple_code = initial_line[19:20].strip()
        self.lower_limit = initial_line[81:86].strip()
        self.lower_unit = initial_line[86:87].strip()
        self.upper_limit = initial_line[87:92].strip()
        self.upper_unit = initial_line[92:93].strip()

        ignored_terms = ["GND", "UNKNN", "UNLTD"]

        if self.lower_limit != "" and self.lower_limit not in ignored_terms:
            if self.lower_limit.startswith("FL"):
                self.lower_limit = f"{self.lower_limit[2:]}00"
            self.lower_limit = int(self.lower_limit)

        if self.upper_limit != "" and self.upper_limit not in ignored_terms:
            if self.upper_limit.startswith("FL"):
                self.upper_limit = f"{self.upper_limit[2:]}00"
            self.upper_limit = int(self.upper_limit)

        for cifp_line in cifp_lines:
            point = CIFPRestrictiveAirspacePoint()
            point.from_line(cifp_line)
            self.points.append(point)

    def to_dict(self) -> dict:
        points = []
        for item in self.points:
            points.append(item.to_dict())

        return {
            "multiple_code": clean_value(self.multiple_code),
            "lower_limit": clean_value(self.lower_limit),
            "lower_unit": clean_value(self.lower_unit),
            "upper_limit": clean_value(self.upper_limit),
            "upper_unit": clean_value(self.upper_unit),
            "points": points,
        }
