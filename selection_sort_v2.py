def selection_sort(sample_list):
    for i in range(len(sample_list)):
        min_index = i
        for j in range(i + 1, len(sample_list)):
            if sample_list[j] < sample_list[min_index]:
                min_index = j
        temp = sample_list[min_index]
        sample_list[min_index] = sample_list[i]
        sample_list[i] = temp
    return sample_list


print(selection_sort([8, 9, 2, 7, 3, 1]))
