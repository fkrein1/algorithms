# python3
number = int(input())
list = [int(x) for x in input().split()]
assert len(list) == number

# O(n)
def maximun_pairwise(list):
    max = 0
    index = 0
    for i in range(0, len(list)):
        if max < list[i]:
            max = list[i]
            index = i
    list.pop(index)

    second_max = 0
    for i in range(0, len(list)):
        if second_max < list[i]:
            second_max = list[i]

    print(max * second_max)

# O(nlogn)
def maximun_pairwise_sort(list):
  list.sort()
  print(list[-1] * list[-2])
