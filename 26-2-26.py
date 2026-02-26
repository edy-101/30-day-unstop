class Car:
    def __init__(self, base, emi, time, discount):
        self.base = base
        self.emi = emi
        self.time = time
        self.discount = discount


def calculate_max_base_cost(N, K, M, cars):
    max_base = -1
    for car in cars:
        upfront = car.base - car.discount
        emi_total = car.emi * car.time
        
        can_buy = False
        
        if upfront <= K:
            can_buy = True
        
        if car.time <= M and emi_total <= K:
            can_buy = True
        
        if can_buy:
            max_base = max(max_base, car.base)
    
    return max_base



N, K, M = map(int, input().split())
cars = []
for _ in range(N):
    base, emi, time, discount = map(int, input().split())
    cars.append(Car(base, emi, time, discount))

result = calculate_max_base_cost(N, K, M, cars)
print(result)
