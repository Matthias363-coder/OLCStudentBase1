character_power = {
    'mario':50,
    'luigi':45,
    'bowser':80,
    'peach':40,
    'yoshi':55,
    'toad':30,
    'wario':70,
    'daisy':42,
    'waluigi':65,
    'donkey kong':75,
}

# how to retrieve value from dictionary
val_donkeykong = character_power["donkey kong"]
val_waluigi = character_power["waluigi"]
print(val_donkeykong)
print(val_waluigi)

# how to add a new key value to dictionary
character_power['shy guy'] = 29
print(character_power)


countries = {
    'japan':'Tokyo',
    'indonesia' : 'Jakarta',
    'china' : 'Beijing'
}

val_china = countries['china']
print(val_china)
val_japan = countries['japan']
print(val_japan)

# add a new country
countries['france'] = 'Paris'
print(countries)