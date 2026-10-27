def fuzzy_control(temp):
    # Fuzzification
    cold = max(0, min(1, (25 - temp) / 15))
    hot = max(0, min(1, (temp - 20) / 15))

    # Fuzzy rules
    low_speed = cold
    high_speed = hot

    # Defuzzification
    speed = (low_speed * 20 + high_speed * 100) / (
        low_speed + high_speed
    ) if (low_speed + high_speed) else 50

    return speed


# Simulation
for temp in [10, 20, 25, 30, 35]:
    print(f"Temperature: {temp}°C -> Fan Speed: {fuzzy_control(temp):.2f}%")
