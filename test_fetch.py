import random

def generate_random_number():
    random_number = random.randint(1, 10)
    return random_number

if __name__ == "__main__":
    random_result = generate_random_number()
    print(f"The randomly generated number is: {random_result}")
