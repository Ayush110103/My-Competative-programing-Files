"""Rutvik has to make a new type of memory for a computer architecture project. In the memory process, they will be stored in key-value pairs. Where the key is unique for each process to identify it, and the value is nothing but process value. Memory is divided into blocks, and each block will be occupied by one process. Here, the size of memory is referred to as the number of blocks. A specific rule must be followed in order to store a process in a memory block. Rutvik will check memory performance based on the success ratio. The success ratio is nothing but a percentage of the keys we successfully found in memory.

Note: Here, the process key and value are stored in memory. To check whether a particular process is present or not in memory, we have to use the hash function. Print success ratio up to 2 decimal places.

Rules:

Each process ID (which is a key) stores data in one block of memory.

If a current key is already present in memory, it does not need to be stored in the block again.

Once all memory blocks have been filled, we must replace the least recently used key with the new key.

Whenever the particular key is not found, that will be considered a fault.

The following formula is used to calculate the success rate:

Success Ratio = ((total keys - fault) / total keys) * 100

Hint: Use the hash function (index = (key * 353) % size of memory); this function is used to identify a key. To implement the least-recently used feature on memory and not on the hash function.

"""
n,m=map(int,input().split())
li=list(map(int,input().split()))
l=[0]*n
fault=0
for i in range(m):
    if li[i] in l:
        l.remove(li[i])
        l.append(li[i])
    else:
        fault+=1
        l.pop(0)
        l.append(li[i])
print("%.2f"%((m-fault)/m*100))

  
    