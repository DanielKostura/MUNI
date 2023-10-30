

def seat_permutations(elements: List[str]) -> List[str]:
    # Base condition
    if len(elements) == 0:
        return [[]]

    all_permutations = []

    # Take every element and put it as first, then combine rest
    for i in range(len(elements)):
        current_element = elements[i]
        remaining_elements = elements[:i] + elements[i+1:]

        # Recursive call to generate permutations of the remaining elements
        remaining_permutations = seat_permutations(remaining_elements)

        # Append the current element to each permutation of the remaining elements
        for permutation in remaining_permutations:
            all_permutations.append([current_element] + permutation)

    return all_permutations