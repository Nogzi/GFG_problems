def BinarySearch(arr_len, arr, val):
    low = 0
    high = arr_len - 1
    txt = "Value: {} is at index: {}"
    while low <= high:
        mid = int((low + high)/2)
        if arr[mid] < val:
            low = mid +1
        elif arr[mid] > val:
            high = mid -1
        else:
            return print(txt.format(val, mid))
    return print("-1")

def main():
    arr = [1,2,3,4,5]
    K = 6
    BinarySearch(int(len(arr)), arr, K)


if __name__ == "__main__":
    main() 