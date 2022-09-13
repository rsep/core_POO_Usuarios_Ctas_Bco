from Usuario import Usuario

user1 = Usuario("Adrien",'adrien@codingdojo.com')
user2 = Usuario("Mr Nibbles",'nibbles@codingdojo.com')
user3 = Usuario("Michael",'michael@codingdojo.com')

# user1: 3 depositos, 1 giro, mostrar balances
user1.hacer_deposito(500,'c').hacer_deposito(250,'a').hacer_deposito(50,'a').hacer_retiro(360,'c').mostrar_balance_usuario()

# user2: 2 depositos, 2 giros, mostrar balances
user2.hacer_deposito(1000,'a').hacer_deposito(820,'c').hacer_retiro(900,'a').hacer_retiro(5,'a').mostrar_balance_usuario()

# user3: 1 deposito, 3 giros, mostrar balances
user3.hacer_deposito(5000,'c').hacer_retiro(150,'').hacer_retiro(380,'c').hacer_retiro(2800,'c').mostrar_balance_usuario()

print("transferir a user3, mostrar sus balances")
# user1: transferir a user3, mostrar sus balances
user1.transfer_dinero(user3,140,'c','c').mostrar_balance_usuario()
user3.mostrar_balance_usuario()