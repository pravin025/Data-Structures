def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def merge_sort(sample_list):
    if len(sample_list) == 1:
        return sample_list
    mid = int(len(sample_list) / 2)
    left = sample_list[:mid]
    right = sample_list[mid:]
    return merge(merge_sort(left), merge_sort(right))


print(merge_sort([9, 8, 7, 6, 5, 4, 10, 22, 20]))
