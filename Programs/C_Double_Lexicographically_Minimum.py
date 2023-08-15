MAX_CHAR = 26;
 
# Function to count frequency of each char in the
# string. freq[0] for 'a',...., freq[25] for 'z'
def countFreq(str1, freq, len1):
 
    for i in range(len1):
        freq[ord(str1[i]) - ord('a')] += 1;
 
# Cases to check whether a palindr0mic
# string can be formed or not
def canMakePalindrome(freq, len1):
     
    # count_odd to count no of
    # chars with odd frequency
    count_odd = 0;
    for i in range(MAX_CHAR):
        if (freq[i] % 2 != 0):
            count_odd += 1;
 
    # For even length string
    # no odd freq character
    if (len1 % 2 == 0):
        if (count_odd > 0):
            return False;
        else:
            return True;
 
    # For odd length string
    # one odd freq character
    if (count_odd != 1):
        return False;
 
    return True;
 
# Function to find odd freq char and
# reducing its freq by 1returns "" if odd freq
# char is not present
def findOddAndRemoveItsFreq(freq):
 
    odd_str = "";
    for i in range(MAX_CHAR):
        if (freq[i]%2 != 0):
            freq[i]-=1;
            odd_str += chr(i+ord('a'));
            return odd_str;
    return odd_str;
 
# To find lexicographically first palindromic
# string.
def findPalindromicString(str1):
    len1 = len(str1);
 
    freq=[0]*MAX_CHAR;
    countFreq(str1, freq, len1);
 
    if (canMakePalindrome(freq, len1) == False):
        return "1";
 
    # Assigning odd freq character if present
    # else empty string.
    odd_str = findOddAndRemoveItsFreq(freq);
 
    front_str = "";
    rear_str = " ";
 
    # Traverse characters in increasing order
    for i in range(MAX_CHAR):
        temp = "";
        if (freq[i] != 0):
            ch = chr(i + ord('a'));
 
            # Divide all occurrences into two
            # halves. Note that odd character
            # is removed by findOddAndRemoveItsFreq()
            for j in range(1,int(freq[i]/2)+1):
                temp += ch;
 
            # creating front string
            front_str += temp;
 
            # creating rear string
            rear_str = temp+rear_str;
 
    # Final palindromic string which is
    # lexicographically first
    return (front_str + odd_str+rear_str);

for aa in range(int(input())):
    s=input()
    x=findPalindromicString(s)
    if(x!="1"):
       print(x)
       continue
    
    
    