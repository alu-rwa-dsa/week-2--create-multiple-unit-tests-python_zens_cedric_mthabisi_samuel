# This file contains the implementation of week2 questions
# Authors: Cédric Murairi, Mthabisi Ndlovu, Samuel Anumudu
# Thursday, 21 January 2021

# 6
def custom_trim(string):
    new = string.strip(' ').split(' ')
    new = list(filter(lambda x: x != '', new))
    return ' '.join(new)

# 7
def find_occurence(string):
    output_dict = {}
    for el in string.lower():
        if el not in output_dict.keys():
            output_dict[el] = list(string.lower()).count(el)
    return output_dict

# 8
def nested_list_to_list(n_list):
    return list(set([el for lst in n_list for el in lst]))

# 9
def find_missing(list1, list2):
    return list(set(list1) - set(list2))

# 10
def unpack_int_to_list(num):
    final = []
    for current in range(1, num + 1):
        for _ in range(1, current + 1):
            final.append(current)
    return final

def main():
    print(custom_trim("     Hello   there  I am here   "), "\n")
    print(find_occurence("Hello there I am here"), "\n")
    print(nested_list_to_list([[1, 2, 1], [0, 1, 3], [2, 3, 5]]), "\n")
    print(find_missing([1, 2, 3, 5], [1, 3, 5]), "\n")
    print(unpack_int_to_list(4))

if __name__ == "__main__":
    main()
