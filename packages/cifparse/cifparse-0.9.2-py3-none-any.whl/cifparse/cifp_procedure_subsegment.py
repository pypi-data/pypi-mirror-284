from .cifp_functions import clean_value
from .cifp_procedure_point import CIFPProcedurePoint

# FOR TRANSITIONS OF PD/PE/PF AND HD/HE/HF


class CIFPProcedureSubsegment:
    def __init__(self) -> None:
        self.transition_id = None
        self.points: list[CIFPProcedurePoint] = []

    def from_lines(self, cifp_lines: list) -> None:
        initial = str(cifp_lines[0])
        transition_id = initial[20:25].strip()
        self.transition_id = transition_id

        for cifp_line in cifp_lines:
            cont_rec_no = int(cifp_line[38:39])
            if cont_rec_no == 0 or cont_rec_no == 1:
                self._cont0(cifp_line)

    def _cont0(self, cifp_line: str) -> None:
        point = CIFPProcedurePoint()
        point.from_line(cifp_line)
        self.points.append(point)

    def to_dict(self) -> dict:
        points = []
        for item in self.points:
            points.append(item.to_dict())

        return {"transition_id": clean_value(self.transition_id), "points": points}
