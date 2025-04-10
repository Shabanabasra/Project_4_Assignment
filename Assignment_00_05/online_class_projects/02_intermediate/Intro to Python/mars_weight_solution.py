# 🚀 Planet Weight Calculator
# This program calculates a person's weight on different planets.

# Gravitational constants (relative to Earth's gravity)
gravity_factors = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Ask user for weight on Earth
earth_weight = float(input("Enter your weight on Earth (kg): "))

# Show Mars weight (Milestone #1)
mars_weight = earth_weight * gravity_factors["Mars"]
print(f"\n🪐 Your weight on Mars would be: {round(mars_weight, 2)} kg")

# Ask user to choose any planet (Milestone #2)
planet = input("\nEnter the name of a planet to find your weight there (e.g., Jupiter): ")

# Check and calculate weight for selected planet
if planet in gravity_factors:
    planet_weight = earth_weight * gravity_factors[planet]
    print(f"🌍 Your weight on {planet} would be: {round(planet_weight, 2)} kg")
else:
    print("⚠️ Invalid planet name. Please make sure the first letter is capitalized and the name is correct.")
