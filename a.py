nums = [0,1,0,3,12]

def run():
    left = 0  # points to position for next non-zero

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    print(nums)
if __name__ == "__main__":
    run()