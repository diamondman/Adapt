from bitarray import bitarray

class JTAGStateMachine(object):
    states = {
        "_PRE5": ["_PRE5", "_PRE4"],
        "_PRE4": ["_PRE5", "_PRE3"],
        "_PRE3": ["_PRE5", "_PRE2"],
        "_PRE2": ["_PRE5", "_PRE1"],
        "_PRE1": ["_PRE5", "TLR"],
        "TLR": ["RTI", "TLR"],
        "RTI": ["RTI", "DRSCAN"],
        "DRSCAN": ["CAPTUREDR", "IRSCAN"],
        "CAPTUREDR": ["SHIFTDR","EXIT1DR"],
        "SHIFTDR": ["SHIFTDR","EXIT1DR"],
        "EXIT1DR": ["PAUSEDR","UPDATEDR"],
        "PAUSEDR": ["PAUSEDR","EXIT2DR"],
        "EXIT2DR": ["SHIFTDR","UPDATEDR"],
        "UPDATEDR": ["RTI","DRSCAN"],
        "IRSCAN": ["CAPTUREIR","TLR"],
        "CAPTUREIR": ["SHIFTIR","EXIT1IR"],
        "SHIFTIR": ["SHIFTIR","EXIT1IR"],
        "EXIT1IR": ["PAUSEIR","UPDATEIR"],
        "PAUSEIR": ["PAUSEIR","EXIT2IR"],
        "EXIT2IR": ["SHIFTIR","UPDATEIR"],
        "UPDATEIR": ["RTI","DRSCAN"]
        }

    def __init__(self):
        self._statestr = "_PRE5"

    def transition_bit(self, bit):
        choice = self.states.get(self._statestr, None)
        if choice is not None:
            self._statestr = choice[bit]

    @property
    def state(self):
        return self._statestr

    @state.setter
    def state(self, value):
        if value in self.states:
            self._statestr = value
        else:
            raise ValueError("%s is not a valid state for this state machine"%value)

    @classmethod
    def find_shortest_path(cls, start, end, path=None):
        path = (path or []) + [start]
        if start == end:
            return path
        if start not in cls.states:
            return None
        shortest = None
        for node in cls.states[start]:
            if node not in path:
                newpath = cls.find_shortest_path(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    @classmethod
    def get_steps_from_nodes_path(cls, path):
        steps = []
        last_node = path[0]
        for node in path[1:]:
            steps.append(cls.states.get(last_node).index(node))
            last_node = node
        return bitarray(steps)

    def calc_transition_to_state(self, newstate):
        if newstate not in self.states:
            raise ValueError("%s is not a valid state for this state machine"%newstate)

        path = self.find_shortest_path(self._statestr, newstate)
        if not path:
            raise ValueError("No path to the requested state.")
        res = self.get_steps_from_nodes_path(path)
        res.reverse()
        return res

    def __repr__(self):
        return "<%s (State: %s)>"%(self.__class__.__name__, self.state)
