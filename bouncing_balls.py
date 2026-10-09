def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    
    count = 0
    while h > window:
        count = count + 1
        h = h * bounce
        if h > window:
            count = count + 1
    
    return count

print(bouncing_ball(3, 0.66, 1.5))
print(bouncing_ball(3, 1, 1.5))
print(bouncing_ball(3, 0.5, 1.5))
print(bouncing_ball(30, 0.75, 1.5))
print(bouncing_ball(30, 0.4, 1.5))
print(bouncing_ball(0, 0.66, 1.5))
print(bouncing_ball(3, 0, 1.5))