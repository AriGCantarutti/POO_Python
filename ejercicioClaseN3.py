class Empleado:
    def __init__(self, DNI, nombre, apellido, anio_ingreso, tipo_contrato):
        self.DNI = DNI
        self.nombre = nombre
        self.apellido = apellido
        self.anio_ingreso = anio_ingreso
        self.tipo_contrato = tipo_contrato

    def calcularSalarioTotal(self):
        pass

    def mostrarSalario(self):
        pass
    
class ConSalarioFijo(Empleado):
    def __init__(self, salarioFijo, DNI, nombre, apellido, anio_ingreso, tipo_contrato):
        super().__init__(DNI, nombre, apellido, anio_ingreso, tipo_contrato)
        self.salarioFijo = salarioFijo

    def calcularSalarioTotal(self):
        salarioTotal = 0
        if self.anio_ingreso < 2:
            return self.salarioFijo
        elif 2 < self.anio_ingreso < 5:
            salarioTotal = (self.salarioFijo * 0.05) + self.salarioFijo
            return salarioTotal
        else:
            salarioTotal = (self.salarioFijo * 0.1) + self.salarioFijo
            return salarioTotal

    def mostrarSalario(self):
        print(f'- {self.apellido}, {self.nombre} su salario es de: ${self.calcularSalarioTotal()}.')
    
class EmpAComision(Empleado):
    def __init__(self, salarioMinimo, numClientesCaptados, montoPorCliente, DNI, nombre, apellido, anio_ingreso, tipo_contrato):
        super().__init__(DNI, nombre, apellido, anio_ingreso, tipo_contrato)
        self.salarioMinimo = salarioMinimo
        self.numClientesCaptados = numClientesCaptados
        self.montoPorCliente = montoPorCliente
    
    def calcularSalarioTotal(self):
        salarioPorComision = 0
        salarioPorComision = self.numClientesCaptados * self.montoPorCliente

        if salarioPorComision < self.salarioMinimo:
            return self.salarioMinimo
        else:
            return salarioPorComision

    def mostrarSalario(self):
        print(f'- {self.apellido}, {self.nombre} su salario es de: ${self.calcularSalarioTotal()}.')

    def empleadoConMasClientes(self):
        print(f'\nEl empleado con mayor cantidad de clientes captados es: {self.apellido}, {self.nombre} con un total de {self.numClientesCaptados} de clientes.')


em1 = ConSalarioFijo(150000, "33123456", "Juan", "Campos", 3, "salarioFijo")
em2 = ConSalarioFijo(170000, "35789456", "Martín", "Cañas", 5, "salarioFijo")
em3 = ConSalarioFijo(145000, "36122333", "José", "Flores", 4, "salarioFijo")
em4 = ConSalarioFijo(180000, "25489756", "Silvia", "Vargas", 8, "salarioFijo")
em5 = ConSalarioFijo(190000, "21789632", "Romina", "Gomez", 1, "salarioFijo")

em6 = EmpAComision(130000, 2, 5000, "34123456", "Susana", "Gomez", 3, "aComision")
em7 = EmpAComision(130000, 5, 500, "24159874", "Marta", "Garcia", 3, "aComision")
em8 = EmpAComision(130000, 4, 1000, "38965784", "Daniel", "Cruz", 3, "aComision")
em9 = EmpAComision(130000, 3, 3000, "23489756", "Rita", "Salguero", 3, "aComision")
em10 = EmpAComision(130000, 1, 5000, "16897452", "Luz", "Trejo", 3, "aComision")

print('Los empleados con los que cuenta la empresa son: ')
em1.mostrarSalario()
em2.mostrarSalario()
em3.mostrarSalario()
em4.mostrarSalario()
em5.mostrarSalario()
em6.mostrarSalario()
em7.mostrarSalario()
em8.mostrarSalario()
em9.mostrarSalario()
em10.mostrarSalario()

em7.empleadoConMasClientes()
