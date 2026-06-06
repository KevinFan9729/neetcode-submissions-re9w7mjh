class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # can we sort the peopel array
        # [1,2,4,5]; limit 6
        # each boat takes 2 people
        # we probably want to take the fat person with the thin person if possible
        # or we can just take the fat person
        # [1,2,2,3,3] limit 3
        # two ptr apporch; left point at the beginning of the array and right points to the end of the array
        # Time O(nlogn)
        # Space O(n)
        people.sort()
        left, right = 0, len(people) - 1
        boat = 0
        while left <= right:
            combined = people[left] + people[right]
            if combined <= limit:
                left+=1
                right-=1
                boat +=1
            else:
                # only the fat person can be taken
                right-=1
                boat+=1
        return boat