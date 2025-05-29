import random

def generate_rssi(base=-60):
    noise = random.randint(-20, 5)
    return base + noise
