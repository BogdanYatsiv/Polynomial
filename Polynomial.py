class Iterator:
    """Клас для ітерування поліному"""
    def __init__(self,data,step=1):
        self.data = data
        self.step = step
        self.curr = 0
    def __next__(self):
        if self.curr == len(self.data):
            raise StopIteration
        else:
            item = self.data[self.curr]
            self.curr += self.step
            return item

class Polinom:
    """Клас що описує поліном, сає методи додавання поліномів, множення поліному на число
            та обчислення поліному"""
    def __init__(self,container = [],n = 0):
        """Конструктор поліному, заносить значення у власний контейнер"""
        container.sort(key = lambda x: x[1])
        self.values = container
        self.indexes = [x[1] for x in container]
        self.len = n

        if n < len(container):
            raise ValueError("To short polinom length")

    def __getitem__(self,i):
        """Перевантаження оператора [](читання)"""
        if i > 0 and i <= self.len:
            if i in self.indexes:
                for x in self.values:
                    if x[1] == i:
                        return x
            else:
                return 0
        else:
            return 0

    def __setitem__(self,index,value):
        """Перевантаження оператора [](запис)"""
        if index > 0 and index <= self.len:
            temp = list(map(list,self.values))
            if value != 0:
                if index in self.indexes:
                    for x in temp:
                        if x[1] == index:
                            x[0] = value
                else:
                    self.values.append((value,index))
                    self.values.sort(key = lambda x: x[1])
                    self.indexes.append(index)

            elif value == 0:
                if index in self.indexes:
                    for x in temp:
                        if x[1] == index:
                            temp.remove(x)
                else:
                    raise ValueError("Empty value")

        else:
            raise IndexError("Out of range!")

        self.values = list(map(tuple,temp))

    def __str__(self):
        """Перевантаження функціїї print() """
        if len(self.values) == 0:
            return "Polinom is empty"

        first = f"P_{self.len}(x) = "
        second = ""
        for x in self.values:
            if x[0]>0:
                second += f" + {x[0]}*x^{x[1]}"
            else: second += f"  {x[0]}*x^{x[1]}"

        return first + second[2:]

    def __call__(self,val,i):
        """Перевантаження оператора ()"""
        if i > 0 and i <= self.len:
            if i in self.indexes:
                for x in self.values:
                    if x[1] == i:
                        return x[0]*(val**i)
            else:
                return 0
        else:
            return IndexError("Out of range")

    def __mul__(self,other):
        """Перевантаження оператора * """
        if other == 0:
            self.values.clear()
        else:
            temp = list(map(list,self.values))
            temp = list(map(lambda x: (x[0]*other,x[1]),temp))
            self.values = list(map(tuple,temp))

    def __add__(self,other):
        """Перевантаження оператора +"""
        result = []
        a = 0
        b = 0

        if len(self.values) > len(other.values):
            n = self.len
        else: n = other.len

        while a < len(self.values) and b < len(other.values):
            if self.values[a][1] < other.values[b][1]:
                result.append(self.values[a])
                a += 1
            elif other.values[b][1] < self.values[a][1]:
                result.append(other.values[b])
                b += 1
            else:
                val = self.values[a][0] + other.values[b][0]
                if val != 0:
                    result.append((val,self.values[a][1]))
                    a += 1
                    b += 1

        if a < len(self.values):
            while a < len(self.values):
                result.append(self.values[a])
                a += 1
        if b < len(other.values):
            while b < len(other.values):
                result.append(other.values[b])
                b += 1

        return Polinom(result,n)


    def __iter__(self):
        """Перевантаження ітерування"""
        return Iterator(self.values)

    def __del__(self):
        print("Deleting polynome")


class PolynomeManager:
    def __init__(self,values,res=False):
        self.values = values
        self.poly = None
        self.res = res

    def __enter__(self):
        print("Work in progress")

        self.poly = Polinom(self.values,len(self.values))
        return self.poly

    def __exit__(self,*args):
        print("Work complited")

        self.poly = None
        return self.res