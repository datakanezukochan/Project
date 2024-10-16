# Generate a list of 100 words ramdomly for hangman
import random

# Word_bank would use
def easy_words(word):
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

def hard_words(word):
    words = ["abstruse", "acquiesce", "acrimony", "adumbrate", "aegis", "ameliorate", "anachronistic", "antediluvian",
        "apocryphal", "ascetic", "asperity", "assiduous", "auspicious", "avarice", "baleful", "bellicose", "bilious",
        "blandishment", "bowdlerize", "calumny", "cantankerous", "capitulate", "castigate", "caterwaul", "cavil",
        "chicanery", "churlish", "circuitous", "circumscribe", "cogitate", "commensurate", "compunction", "concatenate",
        "concomitant", "conflagration", "contumacious", "corroborate", "cupidity", "debacle", "deleterious", "demagogue",
        "denigrate", "deprecate", "desultory", "diaphanous", "dichotomy", "didactic", "dissemble", "disparate", "disputatious",
        "dogmatic", "ebullient", "eclectic", "edacious", "effulgent", "egregious", "elucidate", "emend", "encomium",
        "enervate", "equivocate", "ersatz", "eschew", "excoriate", "exculpate", "execrable", "exigent", "exonerate",
        "expatiate", "expunge", "extirpate", "facetious", "fastidious", "fatuous", "feckless", "flummox", "fractious",
        "grandiloquent", "gregarious", "hackneyed", "hapless", "hegemony", "hermetic", "heterodox", "impecunious",
        "impugn", "inchoate", "indefatigable", "inimical", "insidious", "intransigent", "inveterate", "jejune",
        "juggernaut", "lachrymose", "laconic", "legerdemain", "lissome", "magnanimous", "malediction", "mendacious",
        "munificent", "nadir", "nefarious", "obdurate", "obfuscate", "obstreperous"]
    
    # Random suffle and select 1 word for each game
    word = random.sample(words, 1)
    return word.upper()

def idioms_list(idiom):
    idioms = ["break the ice", "a blessing in disguise", "a dime a dozen", "beat around the bush", "bite the bullet", "break a leg",
        "call it a day", "cut to the chase", "hit the sack", "let the cat out of the bag", "under the weather", "speak of the devil",
        "the ball is in your court", "burn the midnight oil", "cost an arm and a leg", "cry over spilled milk", "cut corners", 
        "devil's advocate", "elephant in the room", "feel under the weather", "give someone the cold shoulder", 
        "go the extra mile", "hit the nail on the head", "miss the boat", "jump on the bandwagon", "let the chips fall where they may", 
        "once in a blue moon", "pull someone's leg", "spill the beans", "the last straw", "the best of both worlds", 
        "to make a long story short", "take with a grain of salt", "bite off more than you can chew", "a penny for your thoughts", 
        "actions speak louder than words", "add fuel to the fire", "at the drop of a hat", "back to the drawing board", 
        "ballpark figure", "barking up the wrong tree", "beating a dead horse", "best of both worlds", "better late than never", 
        "between a rock and a hard place", "beyond a shadow of a doubt", "blow off steam", "break the bank", "burn bridges", 
        "by the skin of your teeth", "caught between two stools", "close but no cigar", "cross that bridge when you come to it", 
        "cut to the chase", "dead ringer", "easy does it", "every cloud has a silver lining", "everything but the kitchen sink", 
        "feel a bit under the weather", "get out of hand", "get your act together", "give the benefit of the doubt", 
        "hang in there", "hit the books", "hit the hay", "in the heat of the moment", "it takes two to tango", 
        "jump the gun", "kill two birds with one stone", "leave no stone unturned", "let sleeping dogs lie", "let the cat out of the bag", 
        "look before you leap", "make a long story short", "method to the madness", "miss the boat", "neck of the woods", 
        "no pain, no gain", "off the top of your head", "on the ball", "once in a blue moon", "open a can of worms", "out of the blue", 
        "piece of cake", "pull yourself together", "rain on someone’s parade", "saving grace", "see eye to eye", 
        "sit on the fence", "skeletons in the closet", "spill the beans", "steal someone’s thunder", "the ball is in your court", 
        "the early bird catches the worm", "the elephant in the room", "the whole nine yards", "throw in the towel", "time flies", 
        "up in the air", "we’ll cross that bridge when we come to it", "when pigs fly", "you can’t judge a book by its cover"
        ]

    # Random suffle and select 1 idiom for each game
    idiom = random.sample(idioms, 1)
    return idiom.upper()
