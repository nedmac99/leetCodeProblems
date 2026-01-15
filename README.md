# 💻 LeetCode Solutions

My solutions to LeetCode algorithm challenges, focusing on clean code and optimal time/space complexity.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?logo=leetcode&logoColor=black)

---

## 📋 Problems Solved

| # | Problem | Difficulty | Solution | Key Concepts |
|---|---------|------------|----------|--------------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 Easy | [two_sum.py](two_sum.py) | Hash Map, Enumeration |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | 🟢 Easy | [palindrome.py](palindrome.py) | String Manipulation, Slicing |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | 🟢 Easy | [roman_to_interger.py](roman_to_interger.py) | Hash Map, Iteration |

---

## 🧠 Solution Highlights

### Two Sum
```python
# Uses hash map for O(n) time complexity
# Stores complement values for efficient lookup
def twoSum(self, nums, target):
    dict = {}
    for index, value in enumerate(nums):
        compliment = target - value
        if compliment in dict:
            return [dict[compliment], index]
        dict[value] = index
```

### Palindrome Number
```python
# Converts to string and uses slicing for reversal
def isPalindrome(self, nums):
    num_str = str(nums)
    return num_str == num_str[::-1]
```

---

## 📊 Progress

- **Easy:** 3 ✅
- **Medium:** 0
- **Hard:** 0

---

## 🚀 Running Solutions

```bash
# Clone the repository
git clone https://github.com/nedmac99/leetCodeProblems.git
cd leetCodeProblems

# Run any solution
python two_sum.py
```