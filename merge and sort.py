def merge_lists(list1,list2):
    new_merge_list=list1+list2
    
    return new_merge_list
def sort_list(merged_list):
    merged_list.sort()

    return merged_list


merged_list=merge_lists(list1=[1,2,3,4,1] ,list2=[2,3,4,5,4,6])
print(merged_list)
sorted_merged_list=sort_list(merged_list)
print(sorted_merged_list)
