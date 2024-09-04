def listSortCheck(listToCheck) -> bool:
    """
    Function to determine if provided list of ints is sorted numerically in either ascending or descending
    :param listToCheck: list of ints
    :return: bool
    """
    ascending, descending = True, True
    for ascCounter in range(len(listToCheck) - 1):
        if listToCheck[ascCounter] > listToCheck[ascCounter + 1]:
            ascending = False
            break
    for descCounter in range(len(listToCheck) - 1):
        if listToCheck[descCounter] < listToCheck[descCounter + 1]:
            descending = False
            break

    return ascending or descending


def main():
    listToCheck = [1,2,3,4,5]
    result = listSortCheck(listToCheck)
    if result:
        print(f"True: The List: {listToCheck} is in either ascending or descending order.")
    else:
        print(f"False - The List: {listToCheck} is not in either ascending or descending order.")


if __name__ == '__main__':
    main()