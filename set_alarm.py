def set_alarm(employed, vacation):
    return employed and not vacation

print(set_alarm(True, True))
print(set_alarm(True, False))
print(set_alarm(False, True))
print(set_alarm(False, False))