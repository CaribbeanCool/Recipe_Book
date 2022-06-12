# TEAMNAME: Los Joli Ranchel
# STUDENT1 NAME: ALEJANDRO A. PEREZ
# STUDENT1 ID: 802-21-1489
# STUDENT2 NAME: GABRIEL CALVENTE TENORIO
# STUDENT2 ID: 802-21-8215
# SECTION: 080 and 100
############      DEFINE CONSTANTS BELOW      ############

# THE FOLLOWING LIST CONTAINS THE UNITS OF THE INGREDIENTS
units = ['cups', 'tablespoons', '', 'cups',
         'teaspoons', 'teaspoons', 'slices', '']

# THE FOLLOWING LIST CONTAINS THE NAMES OF THE INGREDIENTS
ingredients = ['flour', 'sugar', 'eggs', 'milk',
               'cinnamon', 'baking powder', 'bread', 'fruits']

# YOU WILL USE THE FOLLOWING LIST TO SAVE THE INGREDIENTS
pantry = []

# THE FOLLOWING ARE EXAMPLES OF RECIPES - OBSERVE THE ORDER OF THE INGREDIENTS IS THE SAME THAN THE ORDER OF THE PANTRY

# banana pancakes require: 1 cup of flour, 2 tablespoons sugar, 1 egg, 1 cup of milk, 3 teaspoons cinnamon,
# 2 teaspoon baking powder, 0 bread, 2 fruits
banana_pancake_recipe = [1, 2, 1, 1, 3, 2, 0, 2]

# peach crepes require 1 cup of flour, 0 tablespoons sugar, 1 egg, 1 cup of milk, 2 teaspoons cinnamon,
# 0 teaspoon baking powder, 0 bread, 3 fruits
peach_crepe_recipe = [1, 0, 1, 1, 2, 0, 0, 3]

# apple pie requires 2 cups of flour, 4 tablespoons sugar, 2 eggs, 0.5 cup milk, 1 teaspoon cinnamon,
# 1 teaspoon baking powder, 0 bread, 5 fruits
apple_pie_recipe = [2, 4, 2, 0.5, 1, 1, 0, 5]

# french_toast_recipe requires 0.5 cups of flour, 3 tablespoons sugar, 3 eggs, 0.5 cup milk, 2 teaspoon cinnamon,
# 0 teaspoon baking powder, 8 bread, 0 fruits
french_toast_recipe = [0.5, 3, 3, 0.5, 2, 0, 8, 0]

# scrambled_eggs requires 0 cups of flour, 0 tablespoons sugar, 4 eggs, 0.5 cup milk, 0 teaspoon cinnamon,
# 0 teaspoon baking powder, 2 bread, 1.5 fruits
scrambled_eggs = [0, 0, 4, 0.5, 0, 0, 2, 1.5]

menu = [banana_pancake_recipe, peach_crepe_recipe,
        apple_pie_recipe, french_toast_recipe, scrambled_eggs]
menu_list = ["banana pancake", "peach crepe", "apple pie",
             "french toast", "scrambled eggs with toast and fruits"]

# The following funciton ask the user the ingredients in the pantry


def pantry_ingredients(units, ingredients):
    for i in range(len(units)):
        unit = units[i]
        if unit:
            unit += ' of '
        ingredient = ingredients[i]
        item = input(f'How many {str(unit)}{str(ingredient)} do you have? ')
        pantry.append(float(item))

# The following function show the ingredients of an exisiting pantry


def show_pantry():
    print(pantry[0], "cups of flour")
    print(pantry[1], "tablespoons of sugar")
    print(pantry[2], "eggs")
    print(pantry[3], "cups of milk")
    print(pantry[4], "teaspoons of cinnamon")
    print(pantry[5], 'teaspoons of baking powder')
    print(pantry[6], 'slices of bread')
    print(pantry[7], 'fruits')
    # write the body of the function that allow to print the content of the pantry


def show_recipe():
    p = z
    print('Ingredients needed for selected recipe: ')
    for i in range(len(p)):
        # * AQUI SE LE AÑADE LA CANTIDAD DE SERVINGS QUE INGRESO EL USUARIO A LA RECETA
        print(f'{p[i]} {units[i]} of {ingredients[i]}')
# The following function shows the recipe menu


def servings(x):
    y = []  # * ESTA ES UNA COPIA DE LA RECETA
    recipe = menu[rec-1]
    for p in range(len(recipe)):
        # * LE MULTIPLICA EL VALOR DE SERVINGS AL INDICE DE LA RECETA Y LO AÑADE A LA LISTA COPIA
        y.append(recipe[p] * x)
    return y


def recipe_menu():
    print("What would you like to cook? Here's the recipe book:")
    for i in range(len(menu_list)):
        print(i+1, ". ", menu_list[i], sep="")

    print(i+2, ". Nevermind, I don't want to cook anything (Exit).", sep="")
    return input("Select an option by typing its number here: ")

# The following functions verify if the option is valid


def valid_option(option):
    try:
        while True:
            if int(option) >= 1 and int(option) <= 6:
                return int(option)
            print('Only positive numbers from 1-6 are allowed.')
            option = int(input("Enter a possible option: "))
    except Exception:
        if option.isalpha() == True:
            print('Only numbers are allowed.')
            while True:
                option = int(input("Enter a number: "))
                if option < 0:
                    print('Only numbers are allowed.')
                    continue
                else:
                    return option
    # write the code to verify if the option is valid, if the option is valid get the recipe from
    # the list menu usind the list index, and return the recipe and break the loop, if option is 6 terminate the program
    # if the option is not valid keep asking the user to enter a valid option while showing the recipe menu
    # print("MUST COMPLETE FUNCTION!")

# The following function updates the pantry


def pantry_update():
    recipe = z  # * SE ESTA UTILIZANDO LA COPIA DE LA RECETA PARA HACER LOS CAMBIOS
    for p in range(len(pantry)):
        while recipe[p] > pantry[p]:
            print('Not enough ingredients...')
            y = float(
                input(f'You do not have enough {ingredients[p]}, please add more: '))
            pantry[p] = y
        pantry[p] -= recipe[p]
    print('Good Choice')
    # write the code to verify if there are enough ingredients in the pantry
    # to cook the selected recipe, use substraction of the pantry and recipe lists
    # if there is not enough element show a message that indicate there are not enough ingredients
    # if there is enough ingreidients then show a message and uptade the pantry
    # hint: you can replace the pantry with a new pantry
    # print("MUST COMPLETE FUNCTION!")

# YOU DON'T NEED TO MODIFY THE FOLLOWING LINES TO PERFORM THE REQUIERMENTS OF PHASE 1,
# IF YOUR FUCNITONS ARE IMPLENTED CORRECTELY THE OUTPUT WOULD CORRESPOND TO THE EXAMPLES GIVEN


# ? MAIN LOOP
# Prompt user for input of ingredients available
pantry_ingredients(units, ingredients)
cook = True
while cook:
    # Ask user what they'd like to make (from options)
    option = recipe_menu()
    rec = valid_option(option)
    print('You selected option', rec)
    if rec == 6:
        print('See you later!')
        break
    else:  # * SI LA OPCION NO ES 6, ME PIDE LA CANTIDAD DE LOS SERVINGS
        s = int(input('How many servings? '))
        z = servings(s)
    # Verify the selected option is valid
    show_recipe()
    # If the option is valid and want to cook
    pantry_update()
    # If sufficient ingredients remain, subtract ingredients used, and present remaining amount.
    print("Here's what's left in the pantry: ")
    show_pantry()
