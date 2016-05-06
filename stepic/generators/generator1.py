class multifilter:
    def judge_half(pos, neg):
        pass
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        pass
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        pass

    def __init__(self, iterable, *funcs, judge=judge_any):
        pass
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
        
        pass
        # возвращает итератор по результирующей последовательности