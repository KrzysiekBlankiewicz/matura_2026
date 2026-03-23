def bubble_sort(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-i-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

def merge_sort(tab):
    if len(tab) <= 1:
        return tab

    pivot = len(tab)//2
    L = merge_sort(tab[:pivot])
    R = merge_sort(tab[pivot:])

    wynik = []
    i = 0
    j = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            wynik.append(L[i])
            i += 1
        else:
            wynik.append(R[j])
            j += 1

    while i < len(L):
        wynik.append(L[i])
        i += 1

    while j < len(R):
        wynik.append(R[j])
        j += 1

    return wynik


def insertion_sort(tab):
    for i in range(1, len(tab)):
        while i > 0 and tab[i-1] > tab[i]:
            tab[i], tab[i-1] = tab[i-1], tab[i]
            i = i-1
    return tab

import time

#bubble sort
bubble_start = time.time()
bubble_tab = [i for i in range(100, 0, -1)]
bubble = bubble_sort(bubble_tab)
bubble_end = time.time()

#merge sort
merge_start = time.time()
merge_tab = [i for i in range(100, 0, -1)]
merge = merge_sort(merge_tab)
merge_end = time.time()

#insertion sort
insertion_start = time.time()
insertion_tab = [i for i in range(100, 0, -1)]
insertion = insertion_sort(insertion_tab)
insertion_end = time.time()

#czasy
print(f"bubble sort: {str(bubble_end-bubble_start)}, merge sort: {str(merge_end-merge_start)}, insertion sort: {str(insertion_end-insertion_start)}")
