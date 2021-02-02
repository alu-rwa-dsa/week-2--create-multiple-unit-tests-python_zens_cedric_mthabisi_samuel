# This file contains the implementation of week2 questions
# Authors: Cédric Murairi, Mthabisi Ndlovu, Samuel Anumudu
# Thursday, 21 January 2021

# 6
def remove_extra_spaces(string):
    return ' '.join(filter(lambda x: x != "", string.split()))

# 7
def count_chars(string):
    char_counts = {}
    for char in string:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts

# 8
def nested_list_to_list(n_list):
    return list(set([el for lst in n_list for el in lst]))

# 9
def find_missing(list_a, list_b):
    """ Return an element in list_a that is not in list_b.
    
    list_b has all elements in list_a in the same order 
    except one missing element.
    """
    for el in list_a:
        if el not in list_b:
            return el
# 10
def unpack_int_to_list(num):
    final = []
    for current in range(1, num + 1):
        for _ in range(current):
            final.append(current)
    return final

def main():
    print(remove_extra_spaces("     Hello   there  I am here   "), "\n")
    print(count_chars("Hello there I am here"), "\n")
    print(nested_list_to_list([[1, 2, 1], [0, 1, 3], [2, 3, 5]]), "\n")
    print(find_missing([1, 2, 3, 5], [1, 3, 5]), "\n")
    print(unpack_int_to_list(4))

if __name__ == "__main__":
    main()
