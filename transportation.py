def rental_car_cost(d):
    cost = d * 40
    if d >= 7:
        cost = cost - 50
    elif d >= 3:
        cost = cost - 20
    return cost

print(rental_car_cost(1))
print(rental_car_cost(2))
print(rental_car_cost(3))
print(rental_car_cost(6))
print(rental_car_cost(7))
print(rental_car_cost(10))