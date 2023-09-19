class Solution:
    def merge_(nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_temp=[]
        nums1_temp.append(nums1)
        len_list = m+n
        print(len_list)
        print(nums1_temp)
        for i in range(len_list-1):
            
            if nums1[i]>0 and nums1[i]<nums2[i]:
                nums1_temp.append(nums1[i]) 
                print(nums1_temp[i])  
            elif nums1_temp[i]==nums2[i]:
                nums1_temp.append(nums1[i])
                nums1_temp[i+1].append(nums2[i])

       

    result = merge_([1,2,3],3,[4,5,6],3)
