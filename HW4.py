'''2. Создать класс Fraction, который должен иметь два поля: числитель a и знаменатель b.
 Оба поля должны быть типа int. Реализовать методы: сокращение дробей, сравнение, сложение и умножение.'''


def get_int(num):
    if num.isdigit() and (num != '0'):
        return int(num)
    else:
        return get_int(input('Значение введено некорректно. Введите целое число, не равное нулю.'))


def nod(a, b):  # вычисляет НОД
    a = abs(a)
    b = abs(b)
    if a > b:
        a = a % b
    else:
        b = b % a
    if (a == 0) or (b == 0):
        return a + b
    else:
        return nod(a, b)


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.nod = nod(self.numerator, self.denominator)

    # блок сравнений
    def __lt__(self, other):
        if (self.numerator / self.denominator) < (other.numerator / other.denominator):
            return True
        else:
            return False

    def __le__(self, other):
        if (self.numerator / self.denominator) <= (other.numerator / other.denominator):
            return True
        else:
            return False

    def __eq__(self, other):
        if (self.numerator / self.denominator) == (other.numerator / other.denominator):
            return True
        else:
            return False

    def __ne__(self, other):
        if (self.numerator / self.denominator) != (other.numerator / other.denominator):
            return True
        else:
            return False

    def __gt__(self, other):
        if (self.numerator / self.denominator) > (other.numerator / other.denominator):
            return True
        else:
            return False

    def __ge__(self, other):
        if (self.numerator / self.denominator) >= (other.numerator / other.denominator):
            return True
        else:
            return False

    # блок арифметических операций
    def __add__(self, other):
        result_num = self.numerator * other.denominator + other.numerator * self.denominator
        result_denom = self.denominator * other.denominator
        return Fraction(result_num, result_denom)

    def __sub__(self, other):
        result_num = self.numerator * other.denominator - other.numerator * self.denominator
        result_denom = self.denominator * other.denominator
        return Fraction(result_num, result_denom)

    def __mul__(self, other):
        result_num = self.numerator * other.numerator
        result_denom = self.denominator * other.denominator
        return Fraction(result_num, result_denom)

    def __truediv__(self, other):
        result_num = self.numerator * self.denominator
        result_denom = self.denominator * other.numerator
        return Fraction(result_num, result_denom)

    def reduce(self):
        return Fraction(int(self.numerator / self.nod), int(self.denominator / self.nod))

    # перегружаем вывод
    def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

    def __repr__(self):
        return '{}/{}'.format(self.numerator, self.denominator)


if __name__ == '__main__':
    a = Fraction(get_int(input('Введите числитель: ')),
                 get_int(input('Введите знаменатель: ')))
    b = Fraction(get_int(input('Введите числитель: ')),
                 get_int(input('Введите знаменатель: ')))
    print('a = ', a)
    print('b = ', b)
    print('Сложение: a + b = {}, сокращённая дробь: {}'.format(a + b, (a + b).reduce()))
    print('Сложение: a - b = {}, сокращённая дробь: {}'.format(a - b, (a - b).reduce()))
    print('Умножение: a * b = {}, сокращённая дробь: {}'.format(a * b, (a * b).reduce()))
    print('Деление: a / b = {}, сокращённая дробь: {}'.format(a / b, (a / b).reduce()))
    print('a < b ? ', a < b)
    print('a >= b ? ', a >= b)
    print('a != b ? ', a != b)