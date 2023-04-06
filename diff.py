from collections import Counter

# read in the first CSV file
with open('file1.csv', 'r') as f1:
    ids1 = f1.read().strip().split(';')

# read in the second CSV file
with open('file2.csv', 'r') as f2:
    ids2 = f2.read().strip().split(';')

# count the frequency of each ID in each file
freq1 = Counter(ids1)
freq2 = Counter(ids2)

# find the IDs that are in ids1 but not in ids2
diff_ids_1 = set()
for id in ids1:
    if id not in ids2:
        diff_ids_1.add(id)

# find the IDs that are in ids2 but not in ids1
diff_ids_2 = set()
for id in ids2:
    if id not in ids1:
        diff_ids_2.add(id)

# find the IDs that are in both files
intersect_ids = set(ids1) & set(ids2)

# find the IDs that are in both files but with different frequency
double_ids = set()
for id in intersect_ids:
    if freq1[id] != freq2[id]:
        double_ids.add(id)

# print out the results
print(f"IDs in file1 but not in file2: {diff_ids_1}")
print(f"IDs in file2 but not in file1: {diff_ids_2}")
print(f"IDs with different frequency in both files: {double_ids}")