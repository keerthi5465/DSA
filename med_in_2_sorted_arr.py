class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        result = 0
        l1,l2,h1,h2 = float('inf'),float('inf'),0,0
        val = len(nums1) + len(nums2)
        if len(nums1) >= 1:
            l1 = min(nums1)
        else:
            l1 = 0
        if len(nums2) >= 1:
            l2 = min(nums2)
        else:
            l2 = 0
        if len(nums1) >= 1:
            h1 = max(nums1)
        if len(nums2) >= 1:
            h2 = max(nums2)
        low = l1 if l1 < l2 else l2
        high = h1 if h1 > h2 else h2
        while low < high:
            mid = (low + high) / 2
            if val % 2 == 0:
                for i in range(len(nums1)):
                    for j in range(len(nums2)):
                        if nums1[i] == mid and (mid + 1) in nums1 or nums2:
                            result = (nums1[i] + (mid + 1))  / 2.0
                        elif nums2[j] == mid and (mid + 1) in nums1 or nums2:
                            result = (nums2[j] + (mid + 1))  / 2.0
            else:
                if len(nums1) == 1 :
                        result = nums1[0]
                elif len(nums2) == 1:
                    result = nums2[0]
                if mid in nums1 or mid in nums2:
                    result = mid
            return result 
        return 0

        
        
        

k = Solution()
print(k.findMedianSortedArrays([], [1]))