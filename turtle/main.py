import prettytable
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ['pikachu','Charmander','squirtel'])
table.add_column("Type", ['electric','water','fire'])
print(table)