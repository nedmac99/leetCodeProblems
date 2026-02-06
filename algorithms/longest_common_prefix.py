'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
'''


#Basic solution
'''
words_with_prefix = ["cat", "car", "can"]
words_without_prefix = ["dark", "nickel", "street"]
split_words = [list(words) for words in words_with_prefix]
columns = list(zip(*split_words))
same_letter = [col[0] for col in columns if len(set(col)) == 1]
print(same_letter)
'''

#Self-written code
words = ["car","cat","can"]
split_words = []
same_letter = []

for w in words:
    split = list(w)
    split_words.append(split)

#Replace with section under this    
for i in split_words:
    print(i)

'''
columns = list(zip(*split_words))

for col in columns:
    if len(set(col)) == 1:
        same_letter.append(col[0])
'''