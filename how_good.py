def better_than_average(class_points, your_points):
    for num in class_points:
        average=sum(class_points)/len(class_points)
        if average<your_points:
            return True
        else:
            return False

print(better_than_average([90,90,85,91,90],90))    