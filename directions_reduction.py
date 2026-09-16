def dirReduc(arr):
    opposites = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }
    
    result = []
    for direction in arr:
        if result and result[-1] == opposites[direction]:
            result.pop()
        else:
            result.append(direction)
    
    return result

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["NORTH", "SOUTH", "EAST", "WEST"]))
print(dirReduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]))
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))
print(dirReduc([]))