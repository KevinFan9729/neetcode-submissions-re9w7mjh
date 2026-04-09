class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # use a hashmap of different bill
        # Time O(n)
        # Space O(n)
        money = defaultdict(int)

        for bill in bills:
            # if bill is $5 no need to give change
            # we only need to check the $10 and $20 case
            money[bill] += 1
            if bill == 10:
                # we need to give 5 dollar back
                if money[5]<=0:
                    return False
                money[5]-=1
            elif bill == 20:
                # two cases
                case1=False
                case2=False
                # case 1 we give one 10 and one 5
                # we prefer case 1 as case 2 uses more
                # $5 bills which are more flexible
                if money[10]>0:
                    if money[5]>0:
                        case1 = True
                # case 2 give three 5 bills
                if money[5]>=3:
                    case2=True
                if not (case1 or case2):
                    return False
                if case1:
                    money[10]-=1
                    money[5]-=1
                    continue
                elif case2:
                    money[5]-=3
        return True