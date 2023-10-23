# Population in 7 Continents Finder

# Display the list of continents
print("1. Asia")
print("2. North America")
print("3. South America")
print("4. Africa")
print("5. Europe")
print("6. Antarctica")
print("7. Oceania")

# Prompt the user to choose a continent
continent = int(input("Which continent's population do you want to see? Enter the number: "))

# Define population data for each continent
population_data = {
    1: "4,762,417,975",
    2: "379,530,629",
    3: "666,449,790",
    4: "1,470,500,688",
    5: "742,090,883",
    6: "5,000",
    7: "45,731,277"
}

# Check the user's choice and display the population
if continent in population_data:
    print(f"The population of the selected continent is {population_data[continent]}.")
else:
    print("Invalid selection. Please choose a valid continent.")
