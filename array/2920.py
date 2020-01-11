import sys;

nums = list(''.join(sys.stdin.readline().split()))

if nums == sorted(nums):
    print("ascending")
elif nums == sorted(nums, reverse=True):
    print("descending")
else:
    print("mixed")
