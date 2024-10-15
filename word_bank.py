# Generate a list of 100 words ramdomly for hangman
import random

# Word_bank would use
def hangman_word(word):
    words = [
        "apple", "banana", "grape", "orange", "pineapple", "strawberry", "kiwi", "watermelon", "mango", "peach",
        "pear", "plum", "cherry", "apricot", "blueberry", "raspberry", "melon", "papaya", "fig", "guava",
        "lemon", "lime", "nectarine", "tangerine", "pomegranate", "blackberry", "cantaloupe", "avocado", "dragonfruit", "coconut",
        "tomato", "cucumber", "lettuce", "carrot", "broccoli", "cauliflower", "spinach", "potato", "onion", "garlic",
        "pepper", "chili", "zucchini", "squash", "turnip", "radish", "beet", "pumpkin", "corn", "eggplant",
        "mushroom", "pea", "bean", "kale", "artichoke", "asparagus", "ginger", "cilantro", "parsley", "oregano",
        "basil", "rosemary", "thyme", "dill", "bayleaf", "sage", "chive", "mint", "tarragon", "fenugreek",
        "walnut", "almond", "cashew", "hazelnut", "pecan", "pistachio", "peanut", "macadamia", "brazilnut", "chestnut",
        "rice", "pasta", "bread", "bagel", "pizza", "sandwich", "burger", "biscuit", "muffin", "croissant",
        "doughnut", "pretzel", "cake", "brownie", "cookie", "pie", "cupcake", "tart", "waffle", "pancake"
    ]

    # Random suffle and select 1 word for each game
    word = random.sample(words, 1)
    return word.upper()