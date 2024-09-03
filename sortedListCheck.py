def listSortCheck(listToCheck) -> bool:
    """
    Function to determine if provided list of ints is sorted numerically
    :param listToCheck: list of ints
    :return: bool
    """
    result = True
    for counter in range(len(listToCheck)):
        if counter == 0: # skips comparison for the first digit
            continue
        else:
            if listToCheck[counter] > listToCheck[counter - 1]:
                continue
            else:
                result = False
                break
    return result


def main():
    listToCheck = [1, 2, 3, 4, 5]
    result = listSortCheck(listToCheck)
    if result:
        print(f"True: The List: {listToCheck} is sorted.")
    else:
        print(f"False - The List: {listToCheck} is not sorted.")


if __name__ == '__main__':
    main()