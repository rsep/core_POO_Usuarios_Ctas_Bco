class CuentaBancaria:

    nombre_banco = "Primer Dojo Nacional"
    lista_cuentas = []

    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.lista_cuentas.append(self)

    # aumenta el balance de la cuenta en el monto dado
    def deposito(self, amount):
        self.balance += amount
        return self
    
    """
    disminuye el balance de la cuenta en el monto dado 
    si hay fondos suficientes; si no hay suficiente dinero,
    imprime el mensaje: "Fondos insuficientes: cobrando una
    tarifa de $5", y resta $5
    """
    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
            return self

    # imprime en la consola: por ejemplo, "Balance: $100"
    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")
        return self
    
    """
    aumenta el balance de la cuenta por el balance actual * 
    la tasa de interés (siempre que el balance sea positivo) 
    """
    def generar_interés(self):
        if self.balance > -1:
            self.balance += self.balance * self.tasa_interes
            return self
    
    @classmethod
    def imprimir_cuentas(cls):
        i = 0
        print(f"\n -------- \n Cuentas {CuentaBancaria.nombre_banco} \n --------\n")
        for cta in cls.lista_cuentas:
            print(f"Cuenta {i+1}: balance: ${cta.balance}")
            i+=1
        print(f"Total cuentas registradas: {len(cls.lista_cuentas)}")