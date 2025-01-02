import random

def array_init(x):
    arr = x * [0]
    arr2 = [x for x in range(x)]    
    
    return print(arr,arr2)

def cars_manufacturer(x):
    cars = ["Audi", "BMW", "Chevrolet", "Fiat",
    "Ford", "Honda", "Hyundai", "Infiniti", "Jaguar", "Kia",
    "Land Rover", "Lexus", "Maserati", "Mazda", "Mercedes-Benz",
    "Mini", "Nissan", "Porsche", "Ram", "Subaru", "Tesla", "Toyota", "Volkswagen", "Volvo"]
    
    random.shuffle(cars)
    
    return [cars[i] for i in range(x)]

def bubble_sort(arr):
    for i in arr:
        for j in arr:
            if (arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

array_init(10)
random_cars = cars_manufacturer(10)
print(random_cars)
print(bubble_sort(random_cars))

