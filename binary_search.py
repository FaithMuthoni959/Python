def binary_search():
    key=77
    numbers={11,22,33,44,55,66,77,88,99}
    start=0

    end=len(numbers)
    found= False
    while start<=end:
        mid =(start + end)//2
        if numbers[mid]==key:
            print("Found Element at pos:", mid)
            found=True
            break
        elif key < numbers[mid]:
            end=mid - 1
        else:
            start=mid + 1
    if not found:
        print(f"{key} not found")