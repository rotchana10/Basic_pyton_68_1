
# Functions


def myfullName(firstName= "Unknown", lastName="Forger"):
    return firstName + " " + lastName

print(myfullName("chin" , "chan"))
print(myfullName(firstName="chin"))
print(myfullName)
print(myfullName(lastName="chan"))
print(myfullName("Anna" , "Forger"))
print(myfullName("Fis" , "Forger"))
print(myfullName("Fia" , "Forger"))

def redpotion(hp):
    return hp + 50
def bluepotion(mp):
    return mp + 30

current_hp = 70
print("Current HP:", current_hp)
print("After using red potion, HP:" , current_hp)