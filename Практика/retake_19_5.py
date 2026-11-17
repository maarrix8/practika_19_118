score = 5
def local_demo():
    score = 100
    print(score)
def add_score():
    global score
    score += 2
def outer():
    counter = 0
    def inc():
        #nonlocal counter
        counter += 1
    inc()
    inc()
    return counter
print("до:",score)
local_demo()
add_score()
print("после:",score)
result_counter = outer()
print(result_counter)