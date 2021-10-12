cookbook = {
        'sandwich': {
            'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
            'meal': 'lunch',
            'prep_time': 10
            },
        'cake': {
            'ingredients': ['floor', 'sugar', 'eggs'],
            'meal': 'dessert',
            'prep_time': 60
            },
        'salad': {
            'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
            'meal': 'lunch',
            'prep_time': 15
            }
        }


def disp_recipe(recipe: str) -> str:
    try:
        format_string = f"""
Recipe for {recipe}
Ingredient List: {cookbook[recipe]['ingredients']}
To be eaten for {cookbook[recipe]['meal']}.
Takes {cookbook[recipe]['prep_time']} minutes to cooking.
"""
    except KeyError:
        format_string = "Recipe Not Found!"
    print(format_string)


def delete_recipe(recipe: str) -> dict:
    return cookbook.pop(recipe)


def add_recipe(recipe: str, ingredients: list,
               meal: str, prep_time: int) -> dict:
    dict_tmp = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time
        }
    cookbook[recipe] = dict_tmp
    return disp_recipe(recipe)


def all_recipe():
    for i in cookbook:
        disp_recipe(i)


if __name__ == '__main__':
    action = None
    while action != 5:
        action = input(f"""
Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
>> """)
        while action not in '12345':
            action = input(
                    """This option doesn't exist, please\r
type the corresponding number.
To exit, enter 5.\n>> """)
        action = int(action)
        if action == 1:
            text_ingr = "Put the ingredients separeted with comas:"
            add_recipe(
                    input("Enter the name of recipe: "),
                    [i.strip() for i in input(text_ingr).split(',')],
                    input("Enter with the type of the meal: "),
                    int(input("Enter with the time of preparation: "))
                    )
        elif action == 2:
            delete_recipe(input("The name of the recipe to delete: "))
        elif action == 3:
            disp_recipe(input("The name of the recipe to show: "))
        elif action == 4:
            all_recipe()
