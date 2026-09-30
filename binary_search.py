def lower_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2 # left, right가 5, 6이면 mid는 11/2의 몫인 5가 됨
        print('mid: ', mid)
        print('left: ', left)
        print('right:', right)
        if arr[mid] < target:
            left = mid + 1
            print('if')
        else:
            right = mid
            print('else')

    return left # 값이 아니라 위치를 반환


nums = [0,1,2,3,4,5,6,7,8,9]
n = 5

print(lower_bound(nums, n))