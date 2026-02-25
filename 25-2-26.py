class Patient:
    def __init__(self, id, priority, time):
        self.id = id
        self.priority = priority
        self.time = time



# Placeholder function where user will implement the logic
def determine_visit_order(patients):
    # User should implement logic here
    # This function should return a list of integers representing the order of IDs
    patients.sort(key=lambda p: (-p.priority, p.time, p.id))
    return [p.id for p in patients]



if __name__ == "__main__":
    N = int(input())

    patients = []
    for _ in range(N):
        id, priority, time = map(int, input().split())
        patients.append(Patient(id, priority, time))

    # Call user logic function
    visit_order = determine_visit_order(patients)

    # Output the result
    print(" ".join(map(str, visit_order)))
