
def dirReduc(arr):
    '''
    Remove the redundancies from a direction array.
    '''
    # Initiate a stack.
    st = []

    # Store directions with their inverses.
    directions = {
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'EAST': 'WEST',
        'WEST': 'EAST'
    }
    # Loop over the elements of the array and update the stack accordingly.
    for elem in arr:
        # Empty stack cannot contain any invertible directions.
        if len(st) == 0:
            st.append(elem)
        else:
            # If the current element can be inverted, invert and remove from the stack.
            if st[-1] == directions[elem]:
                st.pop()
            # Otherwise, push it to the stack.
            else:
                st.append(elem)
    return st


def main():
    # inps = ["NORTH", "SOUTH", "WEST"]
    inps = input().split(' ')
    # print(inps)
    answer = dirReduc(inps)

    print(' '.join(answer))
    return answer


if __name__ == '__main__':
    main()

