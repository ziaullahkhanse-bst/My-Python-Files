def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


print(are_you_playing_banjo("Ricky"))   
print(are_you_playing_banjo("robert"))  
print(are_you_playing_banjo("Alice"))   
print(are_you_playing_banjo("R"))       
print(are_you_playing_banjo("r"))       