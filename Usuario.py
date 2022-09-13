from CuentaBancaria import CuentaBancaria

class Usuario:

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.cuenta = CuentaBancaria(tasa_interes=0.02, balance=0) # Acá iba el balance cuenta
        self.cuentaAhorro = CuentaBancaria(tasa_interes=0.05, balance=0)
    
    def hacer_deposito(self, amount, tipo_cta):
        if tipo_cta == "c":
            self.cuenta.balance += amount
        elif tipo_cta == "a":
            self.cuentaAhorro.balance += amount
        else:
            print("Debe especificar un tipo de cuenta")
        return self

    def hacer_retiro(self,amount,tipo_cta):
        if tipo_cta == "c":
            self.cuenta.balance -= amount
        elif tipo_cta == "a":
            self.cuentaAhorro.balance -= amount
        else:
            print("Debe especificar un tipo de cuenta")
        return self
    
    def mostrar_balance_usuario(self):
        print(f"Cuenta Corriente\nUsuario: {self.nombre}, Balance: ${self.cuenta.balance}")
        print(f"Cuenta Ahorro\nUsuario: {self.nombre}, Balance: ${self.cuentaAhorro.balance}\n")
        return self

    def transfer_dinero(self,other_user,amount,tipo_cta, destino):
        if tipo_cta == "c":
            self.cuenta.balance -= amount
            if destino == 'c':
                other_user.cuenta.balance += amount
            elif destino == 'a':
                other_user.cuentaAhorro.balance += amount
            else:
                print("Debe especificar un tipo de cuenta")
        elif tipo_cta == "a":
            self.cuentaAhorro.balance -= amount
            if destino == 'c':
                other_user.cuenta.balance += amount
            elif destino == 'a':
                other_user.cuentaAhorro.balance += amount
            else:
                print("Debe especificar un tipo de cuenta")
        else:
            print("Debe especificar un tipo de cuenta")
        return self
