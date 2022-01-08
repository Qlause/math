class LinearAlgebra:
    def __init__(self, value) -> None:
        self.value = value
        self.left = value.split('=')[0]
        self.right = value.split('=')[1]
        self.left_value, self.right_value, self.coefisien, self.constanta, self.variable = None, None, [], [], []
        self.left_opr, self.right_opr = None, None
        self.operation = {
                            '-': self.add,
                            '+': self.substract,
                            'x': self.divide,
                            '/': self.multiply
                        }
        
    def add(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b

    def divide(self, a, b):
        return a / b

    def multiply(self, a, b):
        return a * b
    
    def set(self):
        value_left = self.left
        value_right = self.right
        left = []
        right = []
        
        if value_right[0] != '+':
            value_right = '+' + value_right
        if value_left[0] != '+':
            value_left = '+' + value_left
        
        for i in value_left:
            if i in self.operation:
                left.append(i)
        
        for i in value_right:
            if i in self.operation:
                right.append(i)
                    
        for operate in self.operation:
            value_left = value_left.replace(operate, ' ')
            value_right = value_right.replace(operate, ' ')
        
        self.left_value = value_left.split()
        self.right_value =  value_right.split()
        self.left_opr = left
        self.right_opr = right
        
        self.findCoefisien()
        self.findConstanta()
        self.findVariable()
        
    def findCoefisien(self):
        
        for i in self.left_value:
            if 'y' in i:
                self.coefisien.append(i)     
        
        for i in self.right_value:
            if 'y' in i:
                self.coefisien.append(i)     
    
    def findConstanta(self):
        
        for i in self.left_value:
            if 'y' not in i:
                self.constanta.append(i)     
        
        for i in self.right_value:
            if 'y' not in i:
                self.constanta.append(i) 
    
    def findVariable(self):
        self.variable.append('y')
        
    def findy(self):
        
        isConstantaExist = True
        valueRight = int(self.right_value[0])
        while isConstantaExist:
            for i in range(0, len(self.left_value)):
                if 'y' not in self.left_value[i]:
                    valueRight = self.operation[self.left_opr[i]](valueRight, int(self.left_value[i]))
            
            valueRight = self.divide(valueRight, int(self.coefisien[0][0:-1]))
            print(f'y is {valueRight}')
            break