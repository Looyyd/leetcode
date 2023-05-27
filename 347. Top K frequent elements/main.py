from test3 import test3

class OccurenceCounter():
    def __init__(self, num):
        self.counter = 0
        self.num = num

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # contains list with number and current counter
        occurences_dict = {}

        # contains hashes to most frequent
        most_frequent_hashes = []
        for num in nums:
            # hash
            current_h = hash(num)
            # add to counter
            if current_h in occurences_dict:
                occurrences = occurences_dict[current_h].counter + 1
                occurences_dict[current_h].counter = occurrences
            else:
                occurrences = 1
                occurences_dict[current_h] = OccurenceCounter(num)

            # check if counter more than most_frequent
            # if most_frequent not full, just add
            if len(most_frequent_hashes) < k:
                if current_h in most_frequent_hashes:
                    continue
                else:
                    most_frequent_hashes.append(current_h)
            else:
                already_in = 0
                smallest_candidate_hash = None
                smallest_candidate_hash_index = None
                #add only if better
                for index,frequent_h in enumerate(most_frequent_hashes):
                    if frequent_h == current_h:
                        already_in = 1
                        break
                    elif occurences_dict[frequent_h].counter < occurrences:
                        if smallest_candidate_hash == None:
                            smallest_candidate_hash = frequent_h
                            smallest_candidate_hash_index = index
                        elif occurences_dict[frequent_h].counter < smallest_candidate_hash:
                            smallest_candidate_hash = frequent_h

                if already_in:
                    continue
                elif smallest_candidate_hash ==None:
                    continue
                else:
                    most_frequent_hashes[smallest_candidate_hash_index] = current_h


        # return most frequent numbers
        most_frequent_numbers= []
        for h in most_frequent_hashes:
            most_frequent_numbers.append(occurences_dict[h].num)
        return  most_frequent_numbers


if __name__ == "__main__":
    s = Solution()
    test1 = [1, 1, 1, 2, 2, 3]
    k1 = 2

    test2 = [3,0,1,0]
    k2 = 1
    print(s.topKFrequent(test2,k2))

    test3 = test3
    k3 = 1069
    print(s.topKFrequent(test3,k3))

