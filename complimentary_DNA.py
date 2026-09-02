def DNA_strand(dna):
    result = ""
    for char in dna:
        if char == "A":
            result = result + "T"
        elif char == "T":
            result = result + "A"
        elif char == "C":
            result = result + "G"
        elif char == "G":
            result = result + "C"
    return result

print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))
print(DNA_strand("AAAA"))
print(DNA_strand("TAACG"))