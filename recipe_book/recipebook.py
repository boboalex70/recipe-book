class Recipe:
    """Holds each recipe and the ingredients for the recipe.

    Recipe holds the name of a recipe and a list of ingredients.
    Each ingredient is a tuple of the ingredient name,
    amount of ingredient, and unit of measurement.
    """

    def __init__(self, name):
        """Inserts name and empty list of ingredients.

        :param name: Name of recipe.
        """
        self.name = name
        self.ingredients = []

    def update_name(self, new_name):
        """Updates the name of the recipe.

        :param new_name: New name for recipe.
        """
        self.name = new_name

    def add_ingredient(self, ingredient_name, amount, unit_of_measurement):
        """Adds an ingredient to the list of ingredients.

        :param ingredient_name: Name of ingredient.
        :param amount: Amount of ingredient.
        :param unit_of_measurement: Unit of measurement
        """
        self.ingredients.append((ingredient_name, amount, unit_of_measurement))

    def remove_ingredient_by_type(self, ingredient):
        """Remove ingredient from list of ingredients by the type it is.

        :param ingredient: Ingredient tuple to be removed.
        """
        try:
            self.ingredients.remove(ingredient)
        except ValueError:
            pass

    def remove_ingredient_by_index(self, index):
        """Removes an ingredient from ingredient list by index.

        :param index: Index of ingredient in list.
        """
        try:
            self.ingredients.pop(index)
        except IndexError:
            pass
