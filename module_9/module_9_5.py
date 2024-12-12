class StepValueError(ValueError):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Iterator:

    def __init__(self, start, stop, step=1):
        self.start = start  # целое число, с которого начинается итерация.
        self.stop = stop  # целое число, на котором заканчивается итерация.
        self.pointer = start  # указывает на текущее число в итерации (изначально start)
        self.step = step  # шаг, с которым совершается итерация.
        if self.step == 0:
            raise StepValueError('Шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start - self.step
        return self

    def __next__(self):  # метод, увеличивающий атрибут pointer на step.
        # В зависимости от знака атрибута step итерация завершится либо когда pointer станет больше stop,
        # либо меньше stop. Учтите это при описании метода.
        self.pointer += self.step
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        return self.pointer


try:
    iter1 = Iterator(-5, 1)
    for i in iter1:
        print(i, end=' ')
except StepValueError as exc:
    print(exc.message)
