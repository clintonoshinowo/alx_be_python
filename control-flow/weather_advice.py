# weather_advice.py

# Prompt the user for weather input
# .lower() is used to make the input case-insensitive,
# so "Sunny", "SUNNY", or "sunny" will all be treated the same.
weather_condition = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Provide clothing recommendations based on the user's input
if weather_condition == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_condition == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_condition == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    # Handle unexpected input
    print("Sorry, I don't have recommendations for this weather.")
