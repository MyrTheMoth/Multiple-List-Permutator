# Herb Sauce Permutator
A script that permutates all possible combinations of ingredients, given a bunch of flavor profiles and ingredients corresponding to each flavor to choose from.

It also makes sure that mandatory flavors are always chosen, and permutates profiles of flavors to skip.

---------

## Usage

Just run `permutator.py` with `settings.yaml` in the same folder and it will print a `list.csv` file with all possible permutations (shuffled, so you don't get tired of trying the same sauce bases in a streak).

---------

## Settings

The YAML File is broken into:

- Flavors: A nested list of Flavor Profiles, each including a list of of their respective ingredients

- Profiles: Options for how to Permutate the Flavor Profiles, which to always include, how many to include in total.

  - Mandatory: A list of Flavor Profiles to always include.

  - Choices: A list of the number of Flavors to include for each set of permutations.

Feel free to add your own flavors and ingredients, or replace them with whatever else you'd like to permutate!

---------

## Method

1. It Permutates all Flavor Profile Choices

If you have Flavors [A, B, C] it will permutate every combination based on the list of Choices in your settings file, such as [1, 1, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1], etc.

2. It clears duplicate permutations, as we only care for a single copy of each ordered flavor profile set.

3. It enables any mandatory flavor from any permutation where it may be disabled.

If given Flavors [A, B, C] and A is mandatory, any permutation where A is 0, it will be made 1.

4. It clears duplicates created from enabling all mandatory flavors on each permutation.

5. It permutates every possible ingredient combination for all flavors once.

Given Flavors [A, B, C] it will permutate every ingredient combination available under each flavor.

6. It creates a filtered set of the single all flavors permutation set, removing ingredients from Flavors disabled from each Flavor Profile choices.

Given Flavors [A, B, C], each permutation will have ingredients [X, Y, Z], and given the all flavor permutations, each of those will have an ingredient, for each flavor profile choice, those will be filtered to remove ingredients that the currently iterating choice have disabled.

As such, if the current iteration only has ingredients [A, B], the ingredient list [X, Y, Z] will be made [X, Y, None]

7. Print every permutation set to list.csv

8. Enjoy more combinations of possible sauces than there are average available days in a human's life span!

---------

## Inspiration

I was watching a certain video about making Pesto Sauce and the content creator added a pretty fun looking table at the end explaining different Mediterranean herb sauces are just combinations of the same flavor profiles or lack thereof, so I thought it'd be fun to make a way to iterate a bunch of permutations to try all kinds of sauces.

Video: (https://www.youtube.com/watch?v=qnZZ63D4T2Q)


