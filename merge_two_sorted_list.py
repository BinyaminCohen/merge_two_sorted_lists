# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.


from itertools import zip_longest


class ListNode(object):
    def __init__(self, list1, list2):
        self.l1 = sorted(list1)
        self.l2 = sorted(list2)

    def merge_two_lists(self):

        merge_sorted_list = []
        for numL1, numL2 in zip_longest(self.l1, self.l2):

            if numL1 is None:
                merge_sorted_list.append(numL2)
                break

            elif numL2 is None:
                merge_sorted_list.append(numL1)
                break

            elif numL1 <= numL2:
                merge_sorted_list.append(numL1)
                merge_sorted_list.append(numL2)

            else:
                merge_sorted_list.append(numL2)
                merge_sorted_list.append(numL1)

        return merge_sorted_list


res1 = ListNode([1, 2, 4, 7], [1, 3, 4])
print(res1.merge_two_lists())

print()

res2 = ListNode([1, 2, 4], [1, 3, 4])
print(res2.merge_two_lists())

print()

res3 = ListNode([], [])
print(res3.merge_two_lists())

print()

res4 = ListNode([], [0])
print(res4.merge_two_lists())




