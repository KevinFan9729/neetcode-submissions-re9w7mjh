class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # easy if we can have a counter hashmap
        # that will be time of O(n) but space is O(n) due to the hashmap
        # O(1) space is non-trivial
        # can we do candidate and vote?
         # hmmm that works to find majority for element appear more than n/2 
         # now since we are searching for elements appear more than n/3 times
         # it means we at most have 2 elements
        
        # if you take three different elements (x, y, z all different), 
        # removing them cannot delete all occurrences of a true “> n/3” 
        # element.

        # So we maintain two “buckets” (A and B) with votes. 
        # Whenever we see a number that matches neither bucket 
        # and both buckets are occupied (both votes > 0), we do:
            # vote_a -= 1
            # vote_b -= 1
        # This is equivalent to “we just found a 
        # third distinct element, so we cancel one A, one B, 
        # and this new one” → a triple removal of 3 different items.

        # so we at most have two candidates
         # if the current number matches candidate A
            # increment its count
        # elif the current number matches candidate B
            # increment its count
        # if neither and counter is zero
            # update the candaite
        # if neither match and both are nonzero in count
            # decrement all counters
        # Time O(n)
        # Space O(1)
        candidate_a, candidate_b = None, None
        vote_a, vote_b = 0, 0
        for num in nums:
            if num == candidate_a:
                vote_a+=1
            elif num == candidate_b:
                vote_b+=1
            elif vote_a == 0: # if the counter is 0, update the candiate 
                candidate_a = num
                vote_a += 1
            elif vote_b == 0:
                candidate_b = num
                vote_b += 1
            elif vote_a >0 and vote_b >0:
                vote_a -= 1
                vote_b -= 1
        res = []
        check_a, check_b = 0, 0
        for num in nums:
            if candidate_a == num:
                check_a+=1
            elif candidate_b == num:
                check_b+=1
        if check_a > len(nums)//3:
            res.append(candidate_a)
        if check_b > len(nums)//3:
            res.append(candidate_b)
        return res
        