from math import ceil
def compute_bus_fare(distance):
    if distance > 3:
        return 10 + (3*(distance-3))
    else:
        return 10

def compute_train_fare(distance):
    if distance > 5:
        return 20 + (2*(distance-5))
    else:
        return 20

def main():
    distance = ceil(float(input("Distance : ")))
    
    print(f"The bus fare is {compute_bus_fare(distance)}")
    print(f"The train fare is {compute_train_fare(distance)}")
    
    if compute_bus_fare(distance) == compute_train_fare(distance):
        print("You should take whatever you want.")
    elif compute_bus_fare(distance) < compute_train_fare(distance):
        print("You should take a bus.")
    else:
        print("You should take a train.")
main()