class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = len(nums1)-1
        pos1=m-1
        pos2=n-1
        while(pos1>=0 and pos2>=0):
            if nums1[pos1]>nums2[pos2]:
                nums1[i]=nums1[pos1]
                pos1=pos1-1
            else:
                nums1[i]=nums2[pos2]
                pos2=pos2-1
            i=i-1
        while ((pos2)>=0):
            nums1[i]=nums2[pos2]
            pos2=pos2-1
            i=i-1

        return None            
