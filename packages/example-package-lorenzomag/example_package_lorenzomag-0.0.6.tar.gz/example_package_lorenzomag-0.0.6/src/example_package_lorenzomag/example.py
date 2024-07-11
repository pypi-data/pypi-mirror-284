import numpy as np

def add_one(number):
    return number + 1

def add_two(number):
    return number + 2

def main():
    print(add_one(1))
    print(add_two(1))
    
    # Works with numpy arrays!
    print(add_one(np.array([1, 2, 3])))
    print(add_two(np.array([1, 2, 3])))

if __name__ == "__main__":
    main()