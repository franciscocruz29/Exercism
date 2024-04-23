"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    new_cart = current_cart.copy()

    for item in items_to_add:
        if item in new_cart:
            new_cart[item] += 1
        else:
            new_cart[item] = 1
    return new_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    return add_item({}, notes)


def update_recipes(ideas, recipe_updates):
    """Update ideas dictionary with recipe updates.

    :param ideas: dict - dictionary containing recipe information.
    :param recipe_updates: iterable - list/tuple of tuples containing recipe updates.
    :return: dict - updated ideas dictionary.
    """
    return ideas | dict(recipe_updates)


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    # Initialize an empty dictionary to hold the combined information
    fulfillment_dictionary = {}

    # Iterate through each item in the user's shopping cart
    for item, quantity in cart.items():
        # Combine quantity from cart with isle and refrigeration information from isle_mapping
        fulfillment_dictionary[item] = [quantity, *aisle_mapping[item]]

    # Sort the fulfillment dictionary in reverse order based on items
    # Convert the sorted items back into a dictionary and return
    return dict(sorted(fulfillment_dictionary.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    # Iterate over each item in the fulfillment cart
    for key, value in fulfillment_cart.items():
        # Calculate the new inventory amount after fulfilling the order
        amount = store_inventory[key][0] - value[0]

        # If the new amount is 0, mark the item as "Out of Stock"
        if amount == 0:
            amount = "Out of Stock"

        # Update the store inventory with the new amount
        store_inventory[key] = [amount, *store_inventory[key][1:]]

    # Return the updated store inventory
    return store_inventory
