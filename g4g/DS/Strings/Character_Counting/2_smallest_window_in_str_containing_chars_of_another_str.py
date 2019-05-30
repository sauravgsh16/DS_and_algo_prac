'''
   Find the smallest window in a string containing all characters of
   another string

   Eg:
   Input: string = "this is a test string", pattern = "tist"
   Output: Minimum window is "t stri"

   Method 1:- Brute Force
   1) Generate all substrings of string1 ("this is a test string")
   2) For each substring, check whether the substring contains all characters of
      string2 ("tist")

   Method 2:- Efficient Solution
   1) First check if lenght of string is less than pattern, return False if yes
   2) Store occurrence of characters of pattern in a hash_pat arr.
   3) Start matching characters of pattern with the characters of string.
      i.e: increment count if a character matches
   4) Check if (count == lenght of pattern) this means window is found.
   5) If such window found, try to minimize it by removing extra characters from
      beginning of the current window.
   6) Update min-length
   7) Print the minimum lenght window
'''

no_of_chars = 256

def find_sub_string(string, pat):
    len1 = len(string)
    len2 = len(pat)

    # check if string lenght is less than pattern's length
    if len1 < len2:
        return False
    
    hash_pat = [0] * no_of_chars
    hash_str = [0] * no_of_chars

    # store occurrence of characters of pattern
    for i in range(len2):
        hash_pat[ord(pat[i])] += 1

    start, start_idx, min_len = 0, -1, float('inf')

    # Start traversing the string
    count = 0
    for i in range(len1):

        # count occurrence of chars of string
        hash_str[ord(string[i])] += 1

        #If string's char matches with pattern's char, then increment count
        if (hash_pat[ord(string[i])] != 0 and
            hash_str[ord(string[i])] <= hash_pat[ord(string[i])]):
            count += 1
        
        # if all the characters are matched
        if count == len2:

            # We try to minimize the window.
            # ie. we check if any character is 
            # occurring more no of times than
            # it's occurrence in the pattern. If yes, then we remove it from start
            # and also remove the useless characters.
            print hash_pat
            print hash_str
            while (hash_str[ord(string[start])] > hash_pat[ord(string[start])] 
                or hash_pat[ord(string[start])] == 0):

                if hash_str[ord(string[start])] > hash_pat[ord(string[start])]:
                    hash_str[ord(string[start])] -= 1
                start += 1

            # update window size
            len_window = i - start + 1
            if min_len > len_window:
                min_len = len_window
                start_idx = start
    
    if start_idx == -1:
        print "No such window"
    else:
        print string[start_idx: start_idx + min_len]


string = "this is a test string"
pat = "tist"

find_sub_string(string, pat)