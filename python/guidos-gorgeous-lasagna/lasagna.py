EXPECTED_BAKE_TIME = 40

PREPARATION_TIME = 2

def bake_time_remaining(time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME-time

def preparation_time_in_minutes(layers):
    """
    Function takes the number of layers you want to add to the lasagna as an argument 
    and returns how many minutes you would spend making them.
    """
    return PREPARATION_TIME * layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """

    return elapsed_bake_time+(number_of_layers*2)
