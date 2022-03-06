def insertion_sort(sample_list):
    for i in range(1, len(sample_list)):
        temp = sample_list[i]
        j = i - 1
        while temp < sample_list[j] and j > -1:
            sample_list[j+1] = sample_list[j]
            sample_list[j] = temp
            j -= 1
    return sample_list


print(insertion_sort([9, 8, 7, 6, 5, 4]))
