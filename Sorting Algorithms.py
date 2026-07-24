# sorting_algorithms



# 1. Bubble Sort

def bubble_sort(arr):
    arr = arr.copy()

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr



# 2. Selection Sort

def selection_sort(arr):
    arr = arr.copy()

    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr



# 3. Insertion Sort

def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def main():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    while True:
        print("\n===== Sorting Menu =====")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Sorted:", bubble_sort(numbers))

        elif choice == "2":
            print("Sorted:", selection_sort(numbers))

        elif choice == "3":
            print("Sorted:", insertion_sort(numbers))

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()