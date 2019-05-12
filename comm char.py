def find_common_characters(msg1,msg2):
   msg=list(set(msg1)&set(msg2))
   for i in msg:
       common_characters=i
       print(common_characters)
msg1="python"
msg2="Python"
common_characters=find_common_characters(msg1,msg2)
