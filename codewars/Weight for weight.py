# My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members
# is published and each month he is the last on the list which means he is the heaviest.
# I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers.
# The weight of a number will be from now on the sum of its digits.
# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.
# Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

# Example : input : "56 65 74 100 99 68 86 180 90"
#           output: "100 180 90 56 65 74 68 86 99"

def find_counter(arr):
    counter = 0
    for i in arr:
        if i == " ":
            counter += 1
    return counter

def find_int_str_sum(arr, int_array, str_array):
    i, j, int_sum, str_sum = 0, 0, 0, ""
    while i < len(arr):
        if arr[i] != " ":
            int_sum += int(arr[i])
            str_sum += arr[i]
        else:
            int_array[j] = int_sum
            str_array[j] = str(str_sum)
            int_sum, str_sum = 0, ""
            j += 1
        i += 1
    return int_array, str_array

def get_stable_dict(int_array, str_array):
    tup_dict_counter, stable_dict = 0, {}
    for i in range(len(int_array)):
        stable_dict[(tup_dict_counter, int_array[i])] = str_array[i]
        tup_dict_counter += 1
    return stable_dict

def merge(left, right):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]

def merge_sort(array):
    if len(array) < 2:
        return array
    return merge(merge_sort(array[:len(array)//2]), merge_sort(array[len(array)//2:]))

def get_right_value(int_array_sum_counter, stable_dict, int_array, str_array):
    for key, value in stable_dict.items():
        if key[1] == int_array[int_array_sum_counter]:
            str_array[int_array_sum_counter] = value
            stable_dict.pop(key)
            int_array_sum_counter += 1
            if int_array_sum_counter < len(int_array):
                return get_right_value(int_array_sum_counter, stable_dict, int_array, str_array)
            break
    return str_array

def turn_into_string(str_array):
    new_Str_arr = [0]*len(str_array)
    i = 0
    for num in str_array:
        new_Str_arr[i] = str(num)
        i += 1
    return new_Str_arr


def partition(array, start, end):
    if end is None:
        end = len(array)-1
    l, r = start, end-1
    while l < r:
        if array[l] <= array[end]:
            l += 1
        elif array[r] > array[end]:
            r -= 1
        else:
            array[l], array[r] = array[r], array[l]
    if array[l] > array[end]:
        array[l], array[end] = array[end], array[l]
        return l
    else:
        return end

def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start < end:
        pivot = partition(array, start, end)
        quicksort(array, start, pivot-1)
        quicksort(array, pivot+1, end)
    return array

def string_sorting(int_array, str_array):
    i, j = 0, 1
    while i < len(int_array) - 1 and j < len(int_array):
        if int_array[i] == int_array[j]:
            j += 1
        elif int_array[i] != int_array[j] and j - i > 1:
            str_array[i:j] = quicksort(str_array[i:j])
            i, j = j, j+1
        elif int_array[i] != int_array[j]:
            i += 1
            j += 1
    if j-i > 1 and j == len(int_array):
        str_array[i:j] = quicksort(str_array[i:j])
    return str_array

def turn_Into_one_string(str_array):
    one_string, i = "", 0
    for str in str_array:
        one_string += str
        if i < len(str_array)-1:
            one_string += " "
            i += 1
    return one_string

def order_weight(arr):
    if len(arr) == 0:
        return arr
    arr += " "
    counter = find_counter(arr)
    int_array = [0]*counter
    str_array = [0]*counter
    int_array, str_array = find_int_str_sum(arr, int_array, str_array)
    stable_dict = get_stable_dict(int_array, str_array)
    int_array = merge_sort(int_array)
    str_array = get_right_value(0, stable_dict, int_array, str_array)
    str_array = turn_into_string(str_array)
    string_sort = string_sorting(int_array, str_array)
    one_string = turn_Into_one_string(string_sort)
    return one_string
print(order_weight('2000 10003 1234000 44444444 9999 11 11 22 123'))
print(order_weight("1 5 100 100 77"))
