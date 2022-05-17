def smallestNumberSearch(arr):
    txt = "array: {}"
    if len(arr) == 1:
        return print(arr[0])

    if arr[int(len(arr)/2)] <= int(len(arr)/2 +1):
        print(txt.format(arr[:int(len(arr)/2)]))
        smallestNumberSearch(arr[:int(len(arr)/2)])
    else:
        print(txt.format(arr[int(len(arr)/2):]))
        smallestNumberSearch(arr[int(len(arr)/2)+1:])

def main():
    arr = [2,3,4,5,6,7,8,9,10,1]
    smallestNumberSearch(arr)



if __name__ == "__main__":
    main()