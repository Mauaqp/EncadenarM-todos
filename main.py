from User import User

alberto = User("Alberto", "Durer", 1000)
ernesto = User("Ernesto", "Valencia", 15000)
pedro = User ("Pedro", "Peraltilla", 300000)
paula = User("Paula", "Rodriguez", 50)

# Revisión con ENCADENAMIENTO DE MÉTODOS
paula.hacer_retiro(10).hacer_retiro(10).imprimeInfo()

# #Haz que el primer usuario haga 3 depósitos y 1 giro, y luego muestra sus balances

alberto.hacer_deposito(200).hacer_deposito(500).hacer_deposito(5).imprimeInfo()

# Haz que el segundo usuario haga 2 depósitos y 2 giros, y luego muestra sus balances
ernesto.imprimeInfo().hacer_deposito(150).hacer_deposito(745).hacer_retiro(1000).hacer_retiro(1450).imprimeInfo()

#Haz que el tercer usuario haga 1 depósito y 3 giros, y luego muestra sus balances
pedro.imprimeInfo().hacer_deposito(100).hacer_retiro(13).hacer_retiro(5).hacer_retiro(200).imprimeInfo()

# BONUS: Agrega un método transferir_dinero; 
# haz que el primer usuario transfiera dinero al tercer usuario y luego imprime los balances de ambos usuarios

ernesto.transferencia(paula, 12000).transferencia(pedro, 1200)

