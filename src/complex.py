from logger import Logger


class Real:

    def __init__(self, value):
        self.value = ''
        self.negative = False
        self.multiplier = 1
        self.degree = 1
        log = Logger('./logs')

        if not '^' in value:
            mult = []
            val = []
            if value.startswith('-'):
                    self.negative = True
                    mult.append('-')

            for i in value:
                if i.isdigit():
                    mult.append(i)
                elif i == '.':
                    mult.append(i)
                elif i.isalpha():
                    val.append(i)
                else: 
                    print('Что-то непонятное')

            self.multiplier = float(''.join(mult)) if mult else 1
            self.value = ''.join(val) if val else ''

        else:
            mult = []
            val = []
            deg = []
            if value.startswith('-'):
                    self.negative = True
                    mult.append('-')


            i = value.split('^')
            for j in i[0]:
                if j.isdigit():
                    mult.append(j)
                elif j == '.':
                    mult.append(j)
                elif j.isalpha():
                    val.append(j)
                else: 
                   pass

            for j in i[1]:
                deg.append(j)


            self.multiplier = float(''.join(mult)) if mult != ['-'] and mult else 1
            self.value = ''.join(val) if val else ''
            self.degree = float(''.join(deg)) if deg else 1

    def __str__(self):
        if not self.negative:

            if self.multiplier == 0:
                return '0'
            elif self.degree == 0:
                return '1'
            elif self.degree != 1 and self.multiplier != 1:
                return f'{self.multiplier}{self.value}^{self.degree}'
            elif self.degree != 1:
                return f'{self.value}^{self.degree}'
            elif self.multiplier != 1:
                return f'{self.multiplier}{self.value}'
            else:
                return f'{self.value}'
        else: 
            if self.degree != 1 and self.multiplier != 1:
                return f'({self.multiplier}{self.value}^{self.degree})'

            elif self.degree != 1:
                return f'(-{self.value}^{self.degree})'

            elif self.degree == 0:
                return '1'

            elif self.multiplier == 0:
                return '0'
            else:
                return f'(-{self.value})'

    def __add__(self, other):
        if self.value == other.value and self.degree == other.degree:
            return Real(f'{self.multiplier + other.multiplier}{self.value}^{self.degree}')

        else: 
            return f'{str(self)}+{str(other)}'

    def __sub__(self, other):

        if self.value == other.value and self.degree == other.degree:
            return Real(f'{self.multiplier - other.multiplier}{self.value}^{self.degree}')

        else: 
            return f'{str(self)}-{str(other)}'

    def __mul__(self, other):
        if self.value == other.value:
            return Real(f'{self.multiplier*other.multiplier}{self.value}^{self.degree + other.degree}')
        else:
            return f'{str(self)}*{str(other)}'

    def __truediv__(self, other):
        if self.value == other.value:
            return Real(f'{round(self.multiplier/other.multiplier, 2)}{self.value}^{self.degree - other.degree}')
        else:
            return f'{str(self)}/{str(other)}'

class Imaginary(Real):
    def __init__(self, value):
        pass


class Complex:
    def __init__(self, real:Real = None, imag:Imaginary = None):
        pass



if __name__ == '__main__':
    a = Real('-2a^3')
    b = Real('-17a^2')

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)

    

    

