
class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, value):
        if value > 0:
            super(PositiveList, self).append(value)
        else:
            raise NonPositiveError()


_list = PositiveList()
_list.append(1)
print(_list)
_list.append(2)
_list.append(3)
_list.append(4)
print(_list)
_list.append(-3)
