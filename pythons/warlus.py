# value = 15;
# rem = value % 2
# if(rem := value % 2):
#     print("Done ", rem)

avaliable_sizes = ["small", "medium", "large"]
if(requested_size := input("Enter size") in avaliable_sizes):
    print("avaliable")
else:
    print("Not avaliable")    