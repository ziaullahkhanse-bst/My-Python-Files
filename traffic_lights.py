def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"

print(update_light("green"))
print(update_light("yellow"))
print(update_light("red"))