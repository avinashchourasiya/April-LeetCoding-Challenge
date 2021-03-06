# Brute Force approch O(n^2)
# max_count=0;
# arr=[0,1,1,0,0,0,0,0,1,1,0,1,0,0];
# for i in range(0,len(arr)):
#     zc = 0;
#     oc = 0;
#     for j in range(i,len(arr)):
#         if(arr[j]==0):
#             zc+=1;
#         else:
#             oc+=1;
#
#         if(zc==oc and zc+oc > max_count):
#             max_count=zc+oc;
#
# print(max_count)


# BEST APPROCH O(n)

# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         d = dict();
#         d[0] = -1;
#         arr = nums;
#         c = 0;
#         m = 0;
#
#         for index, num in enumerate(arr):
#             if (num == 0):
#                 c -= 1;
#             else:
#                 c += 1;
#
#             if (c in d):
#                 val = index - d[c];
#                 # print(d[c], index);
#                 m = max(m, val)
#             else:
#                 d[c] = index;
#         # print(d)
#         return (m)


#pracing again
#
# arr=[1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1];
# d=dict();
# c=0
# d[0]=-1;
# m=0;
# for index,num in enumerate(arr):
#     if(num==0):
#         c-=1;
#     else:
#         c+=1;
#     #
#     if(c in d):
#         val=index-d[c];
#         m=max(m,val);
#     else:
#         d[c]=index;
# print(m);



#kadanes algo
a = [-2, -3, 4, -1, -2, 1, 5, -3]
curr_max=a[0]
max_so_far=a[0];
for index , num in enumerate(a):
    curr_max=max(a[index],curr_max+a[index]);
    max_so_far=max(max_so_far,curr_max);
print(max_so_far);































































