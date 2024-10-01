def generate_weighted_list(choices, weights):
    """
    Generates a weighted list from choices and weights to facilitate efficient sampling.

    This function creates a list where each choice appears a number of times proportional to its weight.
    By precomputing this list, the program can achieve faster and more efficient sampling using random index
    selection, avoiding the need to compute probabilities on-the-fly.

    Args:
        choices (list): List of choices to weight.
        weights (list): Corresponding weights for the choices.

    Returns:
        list: A weighted list where each item from the choices list appears multiple times based on its weight.

    Example:
        choices = ['A', 'B', 'C']
        weights = [1, 2, 3]
        generate_weighted_list(choices, weights)
        # Returns: ['A', 'B', 'B', 'C', 'C', 'C']
    """
    weighted_list = [
        item for item, weight in zip(choices, weights) for _ in range(weight)
    ]

    return weighted_list
