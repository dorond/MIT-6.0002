# From codereview.stackexchange.com                    
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

# partitions_list = []
# for partition in get_partitions([1, 2, 3, 4]):
#     partitions_list.append(partition)

# print(partitions_list)
# minimum = partitions_list[0]
# for p in partitions_list:
#     if len(p) < minimum:
#         minimum = p
# print(minimum)

# print([len(p) for p in partitions_list] if len(p))
        
