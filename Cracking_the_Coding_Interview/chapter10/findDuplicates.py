# Find Duplicates: You have an array with all the numbers from 1 to N, where N is at most 32,000. The
# array may have duplicate entries and you do not know what N is. With only 4 kilobytes of memory
# available, how would you print all duplicate elements in the array?

# sol:

# We have 4 kilobytes of memory which means we can address up to 8 * 4 * 2 10 bits. Note that 32 * 2 10
# bits is greater than 32000. We can create a bit vector with 32000 bits, where each bit represents one integer.