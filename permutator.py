import yaml  # Import the PyYAML library.
import csv  # Import the CSV document library.
import itertools  # Import Iteration library.
import random  # Import Random library.

# Opens the YAML file with all the flavors and settings.
settingsFile = open("settings.yaml")
# Load the YAML as an Object.
settings = yaml.load(settingsFile, Loader=yaml.FullLoader)
settingsFile.close()  # Close the YAML file.

# Flavor Profile Permutations.

initProfileDicts = {}
initProfileNumber = 0
initProfile = {}

# Generate initial Profiles from Choices.
for choices in settings["Profiles"]["Choices"]:
    if choices <= len(settings["Flavors"]):
        tempchoice = 0
        for flavors in settings["Flavors"]:
            initProfile[flavors] = 0
        keyList = list(initProfile)
        while tempchoice < choices:
            initProfile[keyList[tempchoice]] = 1
            tempchoice = tempchoice + 1
        initProfileNumber = initProfileNumber + 1
        initProfileDicts["profile"+str(initProfileNumber)] = initProfile
        initProfile = {}
    else:
        print("[PROFILES] Error at choice "+str(choices) +
              ": choices can't be larger than the number of flavor choices")

# Generate all Permutations from Initial Profiles.

tempProfilePermutations = []
finalProfilePermutations = []
profileDicts = {}
profileNumber = 0
tempProfile = {}

# Iterate Profile Permutations for each Initial Profile.
for profile in initProfileDicts:
    # Permutate the current Initial Profile.
    tempProfilePermutations = list(itertools.permutations(
        list(initProfileDicts[profile].values())))
    # Eliminate duplicate Permutations.
    tempProfilePermutations = list(dict.fromkeys(tempProfilePermutations))
    # Iterate to enable Mandatory Flavorss
    for tuples in tempProfilePermutations:
        tempList = []
        for flavors in settings["Flavors"]:
            if flavors in settings["Profiles"]["Mandatory"]:
                tempList.append(1)
            else:
                tempList.append(
                    tuples[list(settings["Flavors"]).index(flavors)])
        finalProfilePermutations.append(tuple(tempList))
    # Eliminate duplicate Permutations after Mandatory Flavors are enabled.
    finalProfilePermutations = list(dict.fromkeys(finalProfilePermutations))
    # Iterate a Profile for each unique Permutation.
    for tuples in finalProfilePermutations:
        # Iterate each Flavor value corresponding to the current unique Permutation.
        for flavors in settings["Flavors"]:
            if tuples[list(settings["Flavors"]).index(flavors)] == 1:
                tempProfile[flavors] = 1
            else:
                tempProfile[flavors] = 0
        profileNumber = profileNumber + 1
        # Add the finished Profile to the Dictionary
        profileDicts["Profile "+str(profileNumber)] = tempProfile
        tempProfile = {}

# Permutate all possible Combinations of Ingredients once.
ingredientPermutations = [dict(zip(settings["Flavors"], v))
                          for v in itertools.product(*settings["Flavors"].values())]

# Ingredient List Permutation Filtering by Profile.
ingredientList = []
ingredientDicts = {}
ingredientNumber = 0
tempIngredients = {}

for profiles in profileDicts:  # Iterate each Flavor Profile.
    # Iterate each Ingredient List permutation.
    for permutation in ingredientPermutations:
        for flavors in settings["Flavors"]:  # Iterate each Flavor Choice.
            # Check if the current Profile allows this Flavor to be added.
            if profileDicts[profiles][flavors] == 1:
                # Add the Ingredient from the Permutation.
                tempIngredients[flavors] = permutation[flavors]
            else:  # Flavor not allowed by the current Profile.
                # Don't add the Ingredient from the Permutation.
                tempIngredients[flavors] = "None"
        # Add Profile filtered Permutation to the Ingredient List.
        ingredientList.append(tempIngredients)
        tempIngredients = {}

random.shuffle(ingredientList)

for ingredients in ingredientList:  # Add all the permutations to a Dictionary.
    ingredientNumber = ingredientNumber + 1
    ingredientDicts["Permutation "+str(ingredientNumber)] = ingredients

# Create the CSV file for the resulting permutations.
csvFile = open("list.csv", "w", newline='')
# Set the Fields for the CSV.
fieldnames = list(settings["Flavors"])
# Create the Writer Object to write out CSV.
writer = csv.DictWriter(csvFile, fieldnames=fieldnames)

writer.writeheader()  # Write the field names header.
# Write all Permutations as Rows.
for permutation in ingredientDicts:
    writer.writerow(ingredientDicts[permutation])

csvFile.close()  # Close the CSV file.
