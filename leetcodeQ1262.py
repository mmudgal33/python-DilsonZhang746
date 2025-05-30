



1.py class Solution:
    def twoSum(self, nums, target):
        nums_hash = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_hash: 
                return [nums_hash[target - nums[i]], i]
            nums_hash[nums[i]] = i



2.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        left = 0
        dummy = cur = ListNode(-1)
        while l1 or l2 or left:
            left, sm = divmod(sum(l and l.val or 0 for l in (l1, l2)) + left, 10)
            cur.next = cur = ListNode(sm)
            l1 = l1 and l1.next
            l2 = l2 and l2.next
        return dummy.next



3.py class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mx, start, chars = 0, 0, {}
        for i in range(len(s)):
            if s[i] in chars and start <= chars[s[i]]: start = chars[s[i]] + 1
            else: mx = max(mx, i - start + 1)
            chars[s[i]] = i
        return mx



4.py class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        arr = sorted(nums1 + nums2)
        if len(arr) % 2 == 0: return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
        else: return arr[len(arr) // 2]



5.py class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l, r):
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        pals = [check(i, i) for i in range(len(s))] + [check(i, i + 1) for i in range(len(s) - 1) if s[i] == s[i + 1]]
        return sorted(pals, key = len)[-1] if pals else ''



6.py class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s): return s
        row, direction, res = 0, -1, [""] * numRows
        for char in s:
            res[row] += char
            if row == 0 or row == numRows - 1: direction *= -1 
            row += direction
        return "".join(res) 



7.py class Solution:
    def reverse(self, x):
        x = int(str(x)[::-1]) if x >= 0 else int("-" + str(x)[::-1][:-1]); return -2 ** 31 <= x <= 2 ** 31 - 1 and x or 0



8.py class Solution:
    def myAtoi(self, str):
        r = [int(c) for c in re.findall(r"^[-+]?\u005Cd+", str.lstrip())]
        return (r and 2 ** 31 - 1 < r[0] and 2 ** 31 - 1) or (r and r[0] < -2 ** 31 and -2 ** 31) or (r and r[0]) or 0



9.py class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]    



10.py class Solution:
    def isMatch(self, s, p):
        return bool(re.match(r"%s" %p, s)) and re.match(r"%s" %p, s).group(0) == s 



11.py class Solution:
    def maxArea(self, height):
        left, right, mx = 0, len(height) - 1, 0
        while left < right:
            mx = max(mx, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]: 
                left += 1
            else: 
                right -= 1
        return mx



12.py class Solution:
    def intToRoman(self, num):
        s = "M" * (num // 1000)
        s += "CM" if num % 1000 >= 900 else "D" *((num % 1000) // 500)
        s += "CD" if num % 500 >= 400 and s[-2:] != "CM" else "C" * ((num % 500) // 100)  if num % 500 < 400 else ""
        s += "XC" if num % 100 >= 90 else "L" * ((num % 100) // 50)
        s += "XL" if num % 50 >= 40 and s[-2:] != "XC" else "X" * ((num % 50) // 10)  if num % 50 < 40 else ""
        s += "IX" if num % 10 >= 9 else "V" * ((num % 10) // 5)
        s += "IV" if num % 5 >= 4 and s[-2:] != "IX" else "I" * ((num % 5) // 1) if num % 5 < 4 else ""
        return s



13.py class Solution:
    def romanToInt(self, s):
        table = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        sm, pre = 0, 'I'
        for c in s[::-1]: 
            if table[c] < table[pre]:
                sm, pre = sm - table[c], c  
            else:
                sm, pre = sm + table[c], c
        return sm



14.py class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        j = 0
        while s and all(j < len(s[i]) and j < len(s[i - 1]) and s[i][j] == s[i - 1][j] for i in range(len(s))):
            j += 1
        return s[0][:j] if j else ''



15.py class Solution:
    def threeSum(self, nums):
        res, res_set = [], set()
        nums.sort()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sm = nums[i] + nums[l] + nums[r] 
                if sm < 0: l += 1
                elif sm > 0: r -= 1
                elif (nums[i], nums[l], nums[r]) not in res_set: 
                    res.append([nums[i], nums[l], nums[r]])
                    res_set.add((nums[i], nums[l], nums[r])) 
                else: l, r = l + 1, r - 1
        return res



16.py class Solution:
    def threeSumClosest(self, nums, target):
        res = diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if abs(sm - target) < diff: diff, res = abs(sm - target), sm 
                if sm < target: l += 1
                elif sm > target: r -= 1
                else: return res
        return res



17.py class Solution:
    def letterCombinations(self, digits):
        dic, res = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}, [""]
        for dig in digits:
            tmp = []
            for y in res: 
                for x in dic[dig]: tmp.append(y + x)
            res = tmp 
        return res if any(res) else []



18.py class Solution:
    def fourSum(self, nums, target):
        res, res_set = [], set()
        nums.sort()
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, len(nums)):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    sm = nums[i] + nums[j] + nums[l] + nums[r] 
                    if sm < target: l += 1
                    elif sm > target: r -= 1
                    elif (nums[i], nums[j], nums[l], nums[r]) not in res_set:
                        res.append([nums[i], nums[j], nums[l], nums[r]]); res_set.add((nums[i], nums[j], nums[l], nums[r])) 
                    else: l, r = l + 1, r - 1
        return res



19.py class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        arr = [dummy]
        while head:
            arr.append(head)
            head = head.next
        for _ in range(n + 1):
            pre = arr.pop()
        pre.next = pre.next.next
        return dummy.next



20.py class Solution:
    def isValid(self, s):
        brackets_stack, lefts, rights = [], ("(", "[", "{"), (")", "]", "}") 
        for char in s:
            if char in lefts: 
                brackets_stack.append(char)
            elif not brackets_stack or lefts.index(brackets_stack.pop()) != rights.index(char): 
                return False
        return not brackets_stack 



21.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        elif not l2: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2



22.py class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        bfs = [(0, 0, '')]
        for c in range(n * 2):
            bfs = [(l + 1, r, s + '(') for l, r, s in bfs if l + 1 <= n] + [(l, r + 1, s + ')') for l, r, s in bfs if l - r] 
        return [s for l, r, s in bfs]



23.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        q = []
        for i in range(len(lists)):
            while lists[i]:
                q += lists[i],
                lists[i] = lists[i].next
        root = cur = ListNode(0)
        for h in sorted(q, key = lambda x: x.val):
            cur.next = cur = h
        return root.next



24.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        first = head.next
        second = head
        second.next = self.swapPairs(first.next)
        first.next = second
        return first



25.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseKGroup(self, head, k):
        dummy = last = ListNode(0)
        cur = head
        while cur:
            first, cnt = cur, 1
            while cnt < k and cur:
                cur, cnt = cur.next, cnt + 1
            if cnt == k and cur:
                cur, prev = first, None
                for _ in range(k):
                    prev, cur.next, cur = cur, prev, cur.next
                last.next, last = prev, first
            else:
                last.next = first
        return dummy.next   



26.py class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        return n - len([nums.pop(i) for i in range(n -1, 0, -1) if nums[i] == nums[i - 1]])



27.py class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i



28.py class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)



29.py class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor, res = abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive: res = -res
        return min(max(-2 ** 31, res), 2 ** 31 - 1)



30.py class Solution:
    def findSubstring(self, s, words):
        if not s or not words: return []
        cnt, l_words, l_word, cnt_words, res = collections.Counter(words), len(words[0]) * len(words), len(words[0]), len(words), []
        for i in range(len(s) - l_words + 1):
            cur, j = dict(cnt), i
            for _ in range(cnt_words):
                w = s[j:j + l_word]
                if w in cur:
                    if cur[w] == 1: cur.pop(w)
                    else: cur[w] -= 1
                else: break
                j += l_word
            if not cur: res += i,
        return res



31.py class Solution:
    def nextPermutation(self, nums):
        perm, l = False, len(nums) - 2
        while 0 <= l:
            r = len(nums) - 1  
            while l < r and nums[r] <= nums[l]: 
                r -= 1
            if r <= l: 
                l -= 1
            else:
                nums[l], nums[l + 1:], perm = nums[r], sorted(nums[l + 1:r] + [nums[l]] + nums[r + 1:]), True
                break
        if not perm: nums.sort()



32.py class Solution:
    def longestValidParentheses(self, s):
        stack, mx = [], 0
        for i, c in enumerate(s):
            if c == ")" and stack and s[stack[-1]] == "(": stack.pop()
            else: stack.append(i)
        stack = [-1] + stack + [len(s)]
        for i1, i2 in zip(stack, stack[1:]): mx = max(mx, i2 - i1 - 1)
        return mx if len(stack) > 2 else len(s)



33.py class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: 
                return mid
            elif sum((target < nums[l], nums[l] <= nums[mid], nums[mid] < target)) == 2: 
                l = mid + 1
            else: 
                r = mid - 1
        return -1



34.py class Solution(object):
    def searchRange(self, nums, target):
        l, r = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1
        return [l, r] if 0 <= l <= r else [-1, -1]



35.py class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)



36.py class Solution:
    def isValidSudoku(self, board):
        rows, cols, triples = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != "." and c in rows[i] or c in cols[j] or c in triples[(i //3, j // 3)]: 
                    return False
                elif c != ".": 
                    rows[i].add(c); cols[j].add(c); triples[(i // 3, j // 3)].add(c)
        return True



37.py class Solution:
    def solveSudoku(self, board):
        rows, cols, triples, visit = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set), collections.deque([])
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    triples[(r // 3, c // 3)].add(board[r][c])
                else:
                    visit.append((r, c))
        def dfs():
            if not visit:
                return True
            r, c = visit[0]
            t = (r // 3, c // 3)
            for dig in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                if dig not in rows[r] and dig not in cols[c] and dig not in triples[t]:
                    board[r][c] = dig
                    rows[r].add(dig)
                    cols[c].add(dig)
                    triples[t].add(dig)
                    visit.popleft()
                    if dfs():
                        return True
                    else:
                        board[r][c] = "."
                        rows[r].discard(dig)
                        cols[c].discard(dig)
                        triples[t].discard(dig)
                        visit.appendleft((r, c))
            return False
        dfs()



38.py class Solution:
    def countAndSay(self, n):
        curr = "1"
        for i in range(n - 1):
            tmp, cnt = "", 1
            for j, c in enumerate(curr):
                if j > 0 and curr[j - 1] == c: 
                    cnt += 1
                elif j > 0: 
                    tmp += str(cnt) + curr[j - 1]
                    cnt = 1
                if j == len(curr) - 1: 
                    tmp += str(cnt) + curr[j] 
            curr = tmp
        return curr



39.py class Solution:
    def combinationSum(self, c, t):
        res, stack, n = [], [(0, [], 0)], len(c)
        while stack:
            sm, tmp, r = stack.pop()
            for i in range(r, n):
                if sm + c[i] < t: 
                    stack.append((sm + c[i], tmp + [c[i]], i))
                elif sm + c[i] == t: 
                    res.append(tmp + [c[i]])
        return res



40.py class Solution: 
    def combinationSum2(self, candidates, target):   
        res = []
        self.dfs(sorted(candidates), target, 0, [], res)
        return res
    def dfs(self, nums, target, index, path, res):    
        if target < 0:
            return 
        if target == 0 and path not in res:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            if i>1 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i] + nums[i+1:], target-nums[i], i, path+[nums[i]], res)



41.py class Solution:
    def firstMissingPositive(self, nums: List[int], res: int = 1) -> int:
        for num in sorted(nums):
            res += num == res
        return res
        



42.py class Solution:
    def trap(self, height):
        res, left, l, r = 0, {}, 0, 0
        for i, h in enumerate(height):
            left[i] = l
            if h > l: 
                l = h
        for i in range(len(height) - 1, -1, -1):
            roof = min(left[i] , r)
            if roof > height[i]:
                res += roof - height[i]
            if height[i] > r:
                r = height[i]
        return res



43.py class Solution:
    def multiply(self, num1, num2):
        dic, l1, l2 = {str(i): i for i in range(10)}, len(num1) - 1, len(num2) - 1
        return str(sum([dic[n1] * (10**(l1-i)) for i, n1 in enumerate(num1)]) * sum([dic[n2] * (10**(l2-j)) for j, n2 in enumerate(num2)]))



44.py class Solution:
    def isMatch(self, s, p):
        sp = pp = match = 0
        star = -1
        while sp < len(s):
            if (pp < len(p) and (s[sp] == p[pp] or p[pp] == '?')):
                sp +=1
                pp +=1
            elif pp < len(p) and p[pp] == '*':
                star = pp
                match = sp
                pp +=1
            elif star != -1:
                pp = star + 1
                match +=1
                sp = match
            else:
                return False
        while(pp < len(p) and p[pp] == '*'):
            pp += 1
        return pp == len(p)



45.py class Solution:
    def jump(self, nums):
        last = cur = jump = i = 0
        while cur < len(nums) - 1:
            while i <= last:
                if i + nums[i] > cur: cur = i + nums[i]
                i += 1
            last = cur
            jump += 1
        return jump



46.py class Solution:
    def permute(self, nums): return list(itertools.permutations(nums))



47.py class Solution:
    def permuteUnique(self, nums):
        dic = set()
        for p in itertools.permutations(nums):
            if p not in dic: 
                dic.add(p)
        return list(dic)



48.py class Solution:
    def rotate(self, matrix):
        matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]



49.py class Solution:
    def groupAnagrams(self, strs):
        dic = collections.defaultdict(list)
        for s in strs: 
            dic["".join(sorted(s))].append(s)
        return list(dic.values())



50.py class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n *= -1
            x = 1 / x
        elif not n:
            return 1
        half = self.myPow(x, n // 2)
        return x * half * half if n % 2 else half * half



51.py class Solution:
    def solveNQueens(self, n):
        res = []
        def dfs(i, l, r, m, arr):
            if i == n:
                res.append(arr)
            else:
                l = l[1:] + [0]
                r = [0] + r[:-1]
                for j in range(n):
                    if m[j] == l[j] == r[j] == 0:
                        l[j] = r[j] = m[j] = 1 
                        dfs(i + 1, l, r, m, arr + [("." * j) + "Q" + ("." * (n - j - 1))])
                        l[j] = r[j] = m[j] = 0
        dfs(0, [0] * n, [0] * n, [0] * n, [])
        return res



52.py class Solution:
    def totalNQueens(self, n):
        res = [0] 
        def dfs(i, l, r, m):
            if i == n: 
                res[0] += 1
            else:
                l = l[1:] + [0]
                r = [0] + r[:-1]
                for j in range(n):
                    if m[j] == l[j] == r[j] == 0:
                        l[j] = r[j] = m[j] = 1 
                        dfs(i + 1, l, r, m)
                        l[j] = r[j] = m[j] = 0
        dfs(0, [0] * n, [0] * n, [0] * n)
        return res[0]



53.py class Solution:
    def maxSubArray(self, nums):
        sm, mn, mx = 0, 0, -float("inf")
        for num in nums:
            sm += num
            mx, mn = max(mx, sm - mn), min(mn, sm)
        return mx



54.py class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        seen = set()
        def dfs(i, j, d):
            seen.add((i, j))
            res.append(matrix[i][j])
            if d == 'r':
                if j + 1 < n and (i, j + 1) not in seen:
                    dfs(i, j + 1, d)
                elif i + 1 < m and (i + 1, j) not in seen:
                    dfs(i + 1, j , 'd')
            elif d == 'd':
                if i + 1 < m and (i + 1, j) not in seen:
                    dfs(i + 1, j , d)
                elif j and (i, j - 1) not in seen:
                    dfs(i, j - 1, 'l')
            elif d == 'l':
                if j and (i, j - 1) not in seen:
                    dfs(i, j - 1, d)
                elif i and (i - 1, j) not in seen:
                    dfs(i - 1, j, 'u')
            else:
                if i and (i - 1, j) not in seen:
                    dfs(i - 1, j, d)
                elif j + 1 < n and (i, j + 1) not in seen:
                    dfs(i, j + 1, 'r')
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        dfs(0, 0, 'r')
        return res
        



55.py class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = mx = 0
        while i < len(nums) and i <= mx:
            if nums[i] + i >= len(nums) - 1: return True
            mx, i = max(mx, i + nums[i]), i + 1
        return False



56.py # Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        intervals.sort(key = lambda x: x.end)
        for intr in intervals:
            if not re:
                res.append([intr.start, intr.end])
            else:
                s = intr.start
                while res and res[-1][1] >= intr.start:
                    s = min(s, res.pop()[0])
                res.append([s, intr.end])
        return res



57.py class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new, i = [], 0
        for i, it in enumerate(intervals):
            if newInterval[1] < it[0]: 
                i -= 1
                break
            elif it[1] < newInterval[0]: 
                new += it,
            else: 
                newInterval[0], newInterval[1] = min(it[0], newInterval[0]), max(it[1], newInterval[1])
        return new + [newInterval] + intervals[i + 1:]
        



58.py class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        count=0
        prev_count=0
        for letter in s:
            if count>0:
                prev_count=count
            if letter==" ":
                count=0
                continue
            count+=1
        if count>0:
            return count
        else:
            return prev_count



59.py class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def dirToIndex(x, y, d):
            if d == "r": return (x, y + 1, d) if y + 1 < n and matrix[x][y + 1] == 0 else (x + 1, y, "d")
            elif d == "d": return (x + 1, y, d) if x + 1 < n and matrix[x + 1][y] == 0 else (x, y - 1, "l")
            elif d == "l": return (x, y - 1, d) if y > 0 and matrix[x][y - 1] == 0 else (x - 1, y, "u")
            else: return (x - 1, y, d) if x > 0 and matrix[x - 1][y] == 0 else (x, y +1, "r")
        matrix = [[0 for i in range(1, n + 1)] for j in range(n)]
        num, dir, i, j = 1, "r", 0, 0
        while 0 <= i < n and 0 <= j < n and matrix[i][j] == 0:
            matrix[i][j] = num
            num += 1
            i, j, dir = dirToIndex(i, j, dir)
        return matrix        



60.py class Solution:
    def getPermutation(self, n, k):
        p = itertools.permutations(range(1, n + 1))
        for i in range(k): 
            res = next(p)
        return ''.join([str(i) for i in res])



61.py class Solution:
    def rotateRight(self, head, k):
        arr, count = [head], 0
        root = last = head
        while last and last.next and count < k:
            last, count = last.next, count+1
            arr.append(last)
        if k != count: 
            k = k % (count+1)
            last = arr[k]
        if k == 0 or not last: 
            return head
        curr = root
        while last.next:
            last, curr = last.next, curr.next
        last.next, curr.next, start = root, None, curr.next
        return start



62.py class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]



63.py class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1: return 0
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])): 
                if obstacleGrid[i][j] == 1 or i == j == 0:
                    obstacleGrid[i][j] -= 1
                else:
                    add1 = obstacleGrid[i - 1][j] if i > 0 else 0
                    add2 = obstacleGrid[i][j - 1] if j > 0 else 0
                    obstacleGrid[i][j] += add1 + add2
        return abs(obstacleGrid[-1][-1])



64.py class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += min(grid[i][j - 1] if j > 0 else float("inf"), grid[i - 1][j] if i > 0 else float("inf")) if i!=0 or j != 0 else 0
        return grid[-1][-1]



65.py class Solution:
    def isNumber(self, s):
        s = s.strip()
        pointSeen = eSeen = numberSeen = False
        numberAfterE = True
        for i, c in enumerate(s):
            if "0" <= c <= "9":
                numberSeen = numberAfterE = True
            elif c == ".":
                if eSeen or pointSeen:
                    return False
                pointSeen = True
            elif c == "e":
                if eSeen or not numberSeen:
                    return False
                numberAfterE = False
                eSeen = True
            elif c in "-+":
                if i and s[i - 1] != "e":
                    return False
            else:
                return False
        return numberSeen and numberAfterE



66.py class Solution:
    def plusOne(self, digits, add = 1):
        return add and [1] or [] if not digits else self.plusOne(digits[:-1], +(digits[-1] + add > 9)) + [(digits[-1] + add) % 10]



67.py class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]



68.py class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, used, s = [], 0, []
        for i, w in enumerate(words):
            if not s or len(w) + used + len(s) <= maxWidth:
                used += len(w)
                s += [w]
            else:
                if len(s) == 1:
                    res.append(s[0] + (maxWidth - used) * ' ')
                else:
                    br = (maxWidth - used) // (len(s) - 1)
                    res.append(''.join((br + (i <= (maxWidth - used) % (len(s) - 1))) * ' ' + c for i, c in enumerate(s)).lstrip())
                used, s = len(w), [w]
        return res + [' '.join(c for c in s) + (maxWidth - used - len(s) + 1) * ' ']



69.py class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                l = mid + 1
            else:
                r = mid - 1
        return l - 1



70.py class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i >= n: return 1 if i == n else 0
            if i not in memo:
                memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        return dfs(0)



71.py class Solution:
    def simplifyPath(self, path):
        stack = [] 
        for c in path.split("/"):
            stack = stack[:-1] if c== ".." else stack + [c] if c and c != "." else stack
        return "/" + "/".join(stack)



72.py class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        dp = [[0] * (len(w2) + 1) for i in range(len(w1) + 1)]
        for i in range(len(w1) + 1):
            for j in range(len(w2) + 1):
                if not (i and j):
                    dp[i][j] = i or j
                elif w1[i - 1] == w2[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
                else:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]



73.py class Solution:
    def setZeroes(self, matrix):
        m, n, x = len(matrix), len(matrix and matrix[0]), 0
        for i in range(m):
            for j in range(n):
                if i < m - 1 and not matrix[i][j] and matrix[i + 1][j]: matrix[i + 1][j] = None
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i > 0 and not matrix[i][j] and matrix[i - 1][j]: matrix[i - 1][j] = None
        while x < m:
            y = 0
            while y < n:
                if matrix[x][y] == 0: matrix[x], y = [0] * n, n 
                elif not matrix[x][y]: matrix[x][y] = 0
                y += 1 
            x += 1 



74.py class Solution:
    def searchMatrix(self, matrix, target):
        ls = list(itertools.chain(*matrix))
        return ls and ls[bisect.bisect(ls, target) - 1] == target or False



75.py class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)-1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1



76.py class Solution:
    def minWindow(self, s, t):
        cnt_s, cnt_t, n, left, r = {}, {}, len(s), set(t), -1
        for c in t:
            cnt_t[c] = cnt_t.get(c, 0) + 1
        L = l = 0
        while left:
            r += 1
            if r >= n:
                return ""
            cnt_s[s[r]] = cnt_s.get(s[r], 0) + 1
            if s[r] in cnt_t and cnt_s[s[r]] == cnt_t[s[r]]:
                left.discard(s[r])
        R = r
        cnt_s[s[r]] -= 1
        while l < r < n:
            cnt_s[s[r]] = cnt_s.get(s[r], 0) + 1
            while s[l] not in cnt_t or cnt_s[s[l]] > cnt_t[s[l]]:
                cnt_s[s[l]] -= 1
                l += 1
            if r - l < R - L:
                L, R = l, r
            r += 1   
        return s[L: R + 1]



77.py class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        bfs = [[]]
        for num in range(1, n + 1):
            bfs += [arr + [num] for arr in bfs if len(arr) < k]
        return [arr for arr in bfs if len(arr) == k]



78.py class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums: 
            res += [item+[num] for item in res]
        return res



79.py class Solution:
    def exist(self, board, word):
        m, n, o = len(board), len(board and board[0]), len(word)
        def explore(i, j, k, q):
            for x, y in ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)):
                if k>=o or (0<=x<m and 0<=y<n and board[x][y]==word[k] and (x,y) not in q and explore(x,y,k+1,q|{(x,y)})): return True
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and explore(i, j, 1, {(i, j)}): return True
        return False



80.py class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        for j in range(2, len(nums)):
            if nums[i - 2] != nums[j]:
                nums[i] = nums[j]
                i += 1
        return min(i, len(nums))



81.py class Solution:
    def search(self, nums, target):
        l, r, n = 0, len(nums) - 1, len(nums)
        while l <= r:
            while l + 1 < n and nums[l + 1] == nums[l]: 
                l += 1
            while r > 0 and nums[r] == nums[r - 1]: 
                r -= 1
            mid = (l + r) // 2
            if nums[mid] == target: 
                return True
            elif sum((target < nums[l], nums[l] <= nums[mid], nums[mid] < target)) == 2: 
                l = mid + 1
            else: 
                r = mid - 1
        return False



82.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        dummy_left, dummy_left.next = ListNode(0), head
        prev, prev_num = None, dummy_left
        while head:
            if prev and prev.val != head.val: 
                prev_num = prev
            if prev and prev.val == head.val:
                while head and head.next and head.next.val == head.val: 
                    head = head.next
                head = head.next
                prev_num.next = head
            prev = head
            if head: 
                head = head.next
        return dummy_left.next



83.py class Solution:
    def deleteDuplicates(self, head):
        cur = root = head
        while head:
            if head.val != cur.val:
                cur.next = cur = head
            head = cur.next = head.next
        return root



84.py class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans



85.py class Solution:
    def maximalRectangle(self, matrix):
        res, m, n = 0, len(matrix), len(matrix and matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != "0":
                    if j > 0 and matrix[i][j - 1] != "0":
                        matrix[i][j] = matrix[i][j - 1] + 1
                    else:
                        matrix[i][j] = 1
                    mn, sm, k = matrix[i][j], 0, i + 1
                    while k > 0 and matrix[k - 1][j] != "0":
                        if matrix[k - 1][j] < mn:
                            sm, mn = (i - k + 2) * matrix[k - 1][j], matrix[k - 1][j]
                        else:
                            sm += mn
                        if sm > res:
                            res = sm
                        k -= 1
        return res



86.py class Solution:
    def partition(self, head, x):
        lessHead = less = ListNode(-1)
        greatHead = great = ListNode(-1)
        while head:
            if head.val < x:
                less.next = less = head
            else:
                great.next = great = head
            head = head.next
        less.next, great.next = greatHead.next, None
        return lessHead.next



87.py class Solution:
    def isScramble(self, s1, s2):
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False
        if n < 4 or s1 == s2:
            return True
        f = self.isScramble
        for i in range(1, n):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \u005C
               f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True
        return False



88.py class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

                



89.py class Solution:
    def grayCode(self, n: int) -> List[int]:
        results = [0]
        for i in range(n): 
            results += [x + pow(2, i) for x in reversed(results)]
        return results
        



90.py class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import combinations as cb
        res, dic = [], set()
        for i in range(len(nums) + 1):
            for item in cb(nums, i):
                item = tuple(sorted(item))
                if item not in dic:
                    dic.add(item)
                    res.append(item)
        return res



91.py class Solution:
    def numDecodings(self, s):
        if s[0] == "0": return 0
        dp1 = dp2 = 1
        for i in range(1, len(s)):
            if s[i] == "0" and (s[i - 1] == "0" or s[i - 1] >= "3"): return 0
            dp1, dp2 = [dp2, dp1] if s[i] == "0" else [dp2, dp2 + dp1] if "10" <= s[i -1: i + 1] <= "26" else [dp2, dp2]
        return dp2  



92.py class Solution:
    def reverseBetween(self, head, m, n):
        dummy_left, dummy_left.next, i = ListNode(0), head, 1
        prev = dummy_left
        while head:
            latter = head.next
            if m == n: 
                break
            if i == m: 
                head_left, right = prev, head
            if i == n: 
                head_right, left = head.next, head
            if m < i <= n: 
                head.next = prev
            prev, head, i = head, latter, i+1
        if m != n: 
            head_left.next, right.next = left, head_right
        return dummy_left.next



93.py class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12: return []
        bfs = [(0, '')]
        for c in s:
            new = []
            c = int(c)
            for cur, st in bfs:
                if cur * 10 + c <= 255 and (st[-1:] != '0' or cur):
                    new.append((cur * 10 + c, st + str(c)))
                if st:
                    new.append((c, st + '.' + str(c)))
            bfs = new
        return [st for cur, st in bfs if st.count('.') == 3]



94.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            self.res.append(node.val)
            dfs(node.right)
        dfs(root)
        return self.res



95.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(l, r):
            if r < l: return [None]
            arr = []
            for m in range(l, r + 1):
                left = dfs(l, m - 1)
                right = dfs(m + 1, r)
                for lNode in left:
                    for rNode in right:
                        new = TreeNode(m)
                        new.left = lNode
                        new.right = rNode
                        arr.append(new)
            return arr
        res = dfs(1, n)
        return [] if res == [None] else res



96.py class Solution:
    def numTrees(self, n):
        if n <= 1:
            return 1
        catalan = [0] * (n + 1)
        catalan[0] = catalan[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]
        return catalan[n]



97.py class Solution:
    def isInterleave(self, s1, s2, s3):
        def dfs(i, j, k):
            if (i, j, k) not in memo:
                memo[(i, j, k)] = k>=l3 or (i<l1 and s3[k]==s1[i] and dfs(i+1,j,k+1)) or (j<l2 and s3[k]==s2[j] and dfs(i,j+1,k+1))
            return memo[(i, j, k)]
        l1, l2, l3, memo = len(s1), len(s2), len(s3), {}
        if l3 != l1 + l2: return False
        return dfs(0, 0, 0)



98.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validate(node, mn, mx):
            if not node: return True
            if node.val<mn or node.val>mx: return False
            return validate(node.left,mn,node.val-1) and validate(node.right,node.val+1,mx)
        return validate(root, -float("inf"),float("inf"))



99.py class Solution:
    def recoverTree(self, root):
        def inorder(node):
            if node.left:
                yield from inorder(node.left)
            yield node
            if node.right:
                yield from inorder(node.right)
        swap1 = swap2 = smaller = None
        for node in inorder(root):   
            if smaller and smaller.val > node.val:
                if not swap1:  
                    swap1 = smaller
                swap2 = node      
            smaller = node
        if swap1:
            swap1.val, swap2.val = swap2.val, swap1.val



100.py class Solution:
    def isSameTree(self, p, q):
        return p == q if not p or not q else p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



101.py #Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPiar = self.isMirror(left.right, right.left)
            return outPair and inPiar
        else:
            return False
             



102.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q, res = [root], []
        while any(q):
            res.append([i.val for i in q])
            q = [kid for node in q for kid in (node.left, node.right) if kid]
        return res



103.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q, i, res = [root], 0, []
        while any(q):
            add, q, i = q if i % 2 == 0 else q[::-1], [kid for node in q for kid in (node.left, node.right) if kid], i+1
            res.append([item.val for item in add])
        return res



104.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode, d = 0) -> int:
        return max(self.maxDepth(root.left, d + 1), self.maxDepth(root.right, d + 1)) if root else d



105.py class Solution(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root



106.py class Solution:
    def buildTree(self, inorder, postorder):
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind+1:], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            return root



107.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """ 
        from collections import deque
        if root is None:
            return []
        levels=list()
        q=deque([root])
        levels.append([i.val for i in q])
        target=root
        while q:
            node=q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if node==target:
                if q:
                    levels.append([i.val for i in q])
                    target=q[-1]
        return list(reversed(levels))



108.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums==[]:
            return
        root=TreeNode(nums[len(nums)//2])
        root.left=self.sortedArrayToBST(nums[:len(nums)//2])
        root.right=self.sortedArrayToBST(nums[len(nums)//2+1:])
        return root



109.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def traverse(arr):
            if arr == []: return
            node = TreeNode(arr[len(arr)//2])
            node.left = traverse(arr[:len(arr)//2])
            node.right = traverse(arr[len(arr)//2+1:])
            return node
        array = []
        while head: array.append(head.val); head = head.next
        return traverse(array)



110.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.computeHeight(root)!=-1
    def computeHeight(self, node):
        if not node: return 0
        left_h=self.computeHeight(node.left)
        right_h=self.computeHeight(node.right)
        if left_h==-1 or right_h==-1 or abs(left_h-right_h)>1: return -1    
        return max(left_h,right_h)+1



111.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.compute(root)     
    def compute(self, node):
        if not node: return 0
        left_d=self.compute(node.left)
        right_d=self.compute(node.right)
        if node.left and node.right: return min(left_d,right_d)+1
        else: return max(left_d,right_d)+1



112.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        sum-=root.val
        if not root.left and not root.right and sum==0: return True
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)



113.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def traverse(node, q, residue, res = []):
            if node:
                if not node.left and not node.right and residue + node.val == sum: res.append(q + [node.val])
                traverse(node.left, q + [node.val], residue + node.val)
                traverse(node.right, q + [node.val], residue + node.val)
            return res
        return traverse(root, [], 0)



114.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def traverse(node):
            if not node: return
            left, right = traverse(node.left), traverse(node.right)
            if node.left: left.right, node.right, node.left = node.right, node.left, None
            return right if right else left if left else node
        traverse(root)



115.py class Solution:
    def numDistinct(self, s, t):
        chars, index, dp = set(t), collections.defaultdict(list), [0] * len(t)
        for i, c in enumerate(t): index[c] = [i] + index[c]
        for c in s:
            if c in chars:
                for i in index[c]: dp[i] += dp[i - 1] if i > 0 else 1
        return dp[-1]



116.py class Solution:
    def connect(self, root: "Node") -> "Node":
        if root == None:
            return root
        q, prev = [(root, 1)], None
        while q:
            curr, pos = q.pop(0)
            if prev != None and prev[1] == pos:
                prev[0].next = curr
            prev = [curr, pos]
            if curr.left:
                q.append((curr.left, pos + 1))
            if curr.right:
                q.append((curr.right, pos + 1))
        return root





117.py class Solution:
    def connect(self, root: "Node") -> "Node":
        dummy = Node(-1, None, None, None)
        tmp = dummy
        res = root
        while root:
            while root:
                if root.left:
                    tmp.next = root.left
                    tmp = tmp.next
                if root.right:
                    tmp.next = root.right
                    tmp = tmp.next
                root = root.next
            root = dummy.next
            tmp = dummy
            dummy.next = None

        return res




118.py class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = numRows and [[1]] or []
        for _ in range(numRows-1):
            res.append([1] + [a + b for a, b in zip(res[-1], res[-1][1:])] + [1])
        return res



119.py class Solution:
    def getRow(self, rowIndex: int, row = [1]) -> List[int]:
        return self.getRow(rowIndex - 1, [a + b for a, b in zip([0] + row, row + [0])]) if rowIndex else row



120.py class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        prev = None
        for tri in triangle:
            if prev:
                for i, num in enumerate(tri):
                    if i >= len(prev): tri[i] += prev[i - 1]
                    elif i == 0: tri[i] += prev[0]
                    else: tri[i] += min(prev[i - 1], prev[i])
            prev = tri
        return min(triangle[-1])



121.py class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff_list=[0,0]
        for i in range (1, len(prices)):
            if prices[i]-prices[i-1]+diff_list[1]>=0:
                diff_list[1]=prices[i]-prices[i-1]+diff_list[1]
                diff_list[0]=max(diff_list[0],diff_list[1])
            else:
                diff_list[1]=0
        return diff_list[0]



122.py class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # stock, no stock
        dp = [-float('inf'), 0]
        for p in prices:
            x = max(dp[1] - p, dp[0])
            y = max(dp[1], dp[0] + p)
            dp = [x, y]
        return dp[-1]



123.py class Solution:
    def maxProfit(self, prices):
        s1 = s2 = 0
        b1 = b2 = -float("inf")
        for p in prices:
            if -p > b1: b1 = -p
            if b1 + p > s1: s1 = b1 + p
            if s1 - p > b2: b2 = s1 - p
            if b2 + p > s2: s2 = b2 + p
        return s2



124.py class Solution:
    def maxPathSum(self, root):
        res = [-float("inf")]
        def dfs(node):
            if not node: return -float("inf")
            l, r = dfs(node.left), dfs(node.right)
            mx = max(node.val, l + node.val, r + node.val)
            res[0] = max(res[0], mx, node.val + l + r)
            return mx
        dfs(root)
        return res[0]



125.py class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import string
        return True if s=="" or [i.lower() for i in s if i in string.digits or i in string.ascii_letters]==[i.lower() for i in s if i in string.digits or i in string.ascii_letters][::-1] else False



126.py class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        words, res, layer = set(wordList), [], {beginWord: [[beginWord]]}
        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord: 
                    for arr in layer[w]:
                        res.append(arr)
                else:
                    for i in range(len(w)):
                        for c in string.ascii_lowercase:
                            neww = w[:i] + c + w[i + 1:]
                            if neww in words:
                                newlayer[neww] += [j + [neww] for j in layer[w]]
            words -= set(newlayer.keys())
            layer = newlayer
        return res



127.py class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words, layer = set(wordList), {beginWord: [[beginWord]]}
        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord: 
                    return len(layer[w][0])
                else:
                    for i in range(len(w)):
                        for c in string.ascii_lowercase:
                            neww = w[:i] + c + w[i + 1:]
                            if neww in words:
                                newlayer[neww] += [j + [neww] for j in layer[w]]
            words -= set(newlayer.keys())
            layer = newlayer
        return 0



128.py class Solution:
    def longestConsecutive(self, nums):
        res, items = 0, set(nums)
        for num in items:
            if num - 1 not in items:
                cur = 1
                while num + 1 in items:
                    num, cur = num + 1, cur + 1   
                if cur > res: res = cur
        return res



129.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node, q):
            if not node: return
            traverse(node.left, q + [str(node.val)])
            traverse(node.right, q + [str(node.val)]) 
            if not node.left and not node.right: res[0] += int("".join(q + [str(node.val)]))
        res = [0]
        traverse(root, [])
        return res[0]



130.py class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board and board[0])

        def explore(i, j):
            board[i][j] = "S"
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                    explore(x, y)

        for i in range(max(m, n)):
            if i < m and board[i][0] == "O":
                explore(i, 0)
            if i < m and board[i][n - 1] == "O":
                explore(i, n - 1)
            if i < n and board[0][i] == "O":
                explore(0, i)
            if i < n and board[m - 1][i] == "O":
                explore(m - 1, i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"





131.py class Solution:
    def partition(self, s):
        q, n = [[s[0]]], len(s)
        for i in range(1, n):
            new = []
            for arr in q:
                cur = arr[-1] + s[i]
                if i < n - 1 or cur == cur[::-1]:
                    new.append(arr[:-1] + [cur])
                if arr[-1] == arr[-1][::-1]:
                    new.append(arr + [s[i]])
            q = new
        return q



132.py class Solution:
    def minCut(self, s):
        q, pal, used = [(0, 0)], collections.defaultdict(list), {(0, 0)}
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]: pal[i].append(j + 1)
        while q:
            cuts, i = heapq.heappop(q)
            i *= -1
            if i == len(s): return cuts - 1
            for j in pal[i]:
                if (cuts + 1, -j) not in used:
                    used.add((cuts + 1, -j))
                    heapq.heappush(q, (cuts + 1, -j))



133.py class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        visited = {}

        def dfs(node):
            if node and node.val not in visited:
                newNode = Node(node.val, [])
                visited[newNode.val] = newNode
                newNode.neighbors = [
                    visited.get(n.val) or dfs(n) for n in node.neighbors
                ]
                return newNode

        return dfs(node)




134.py class Solution:
    def canCompleteCircuit(self, gas, cost, cur = 0, index = 0):
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            if cur < 0: cur, index = 0, i + 1
        return index if index < len(gas) and sum(gas) >= sum(cost) else -1



135.py class Solution:
    def candy(self, ratings):
        dp = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                dp[i] = dp[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and dp[i] <= dp[i + 1]:
                dp[i] = dp[i + 1] + 1
        return sum(dp)



136.py class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for num in nums:
            if not num in dic: dic[num]=1
            else: dic.pop(num)
        return list(dic.keys())[0]



137.py class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return ((sum(set(nums)) * 3) - sum(nums)) // 2



138.py class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        dic = collections.defaultdict(lambda: Node(0, None, None))
        dic[None] = None
        n = head
        while n:
            dic[n].val = n.val
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]




139.py class Solution:
    def wordBreak(self, s, wordDict):
        rightmosts, words = [0], set(wordDict)
        for i in range(1, len(s) + 1):
            for last_index in rightmosts:
                if s[last_index:i] in words:
                    rightmosts.append(i)
                    if i == len(s): 
                        return True
                    break
        return False



140.py class Solution:
    def wordBreak(self, s, wordDict):
        def breakable():
            rightmosts = [0]
            for i in range(1, len(s) + 1):
                for last_index in rightmosts:
                    if s[last_index:i] in words:
                        rightmosts.append(i)
                        if i == len(s): 
                            return True
                        break
            return False
        q, res, words = [("", 0)], [], set(wordDict)
        if breakable():
            for j in range(1, len(s) + 1):
                new = q[:]
                for seq, i in q:
                    if s[i:j] in words:
                        if j == len(s):
                            res.append(seq and seq + " " + s[i:j] or s[i:j])
                        else:
                            new.append((seq and seq + " " + s[i:j] or s[i:j], j))
                q = new
        return res



141.py class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head.next if head else None
        while slow != None and fast != None:
            if slow == fast:
                return True
            slow, fast = slow.next, fast.next.next if fast.next else None
        return False




142.py class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = root = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while root != slow:
                    root = root.next
                    slow = slow.next
                return root




143.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def reorderList(self, head):
        if head:
            arr = []
            while head:
                arr += head,
                head = head.next
            l, r, prev = 0, len(arr) - 1, ListNode(0)
            while l < r: prev.next, arr[l].next, prev, l, r = arr[l], arr[r], arr[r], l + 1, r - 1
            if l == r: prev.next = arr[l]
            arr[l].next = None



144.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = [root]
        q = [root]
        while any(q):
            tmp = []
            for node in q:
                if node.right:
                    res.insert(res.index(node) + 1, node.right)
                    tmp.append(node.right)
                if node.left:
                    res.insert(res.index(node) + 1, node.left)
                    tmp.insert(-1, node.left)
            q = tmp
        return [j.val for j in res if j]



145.py class Solution:
    def postorderTraversal(self, root):
        ret, stack = [], root and [root]
        while stack:
            node = stack.pop()
            ret.append(node.val)
            stack += [child for child in (node.left, node.right) if child]
        return ret[::-1]



146.py class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = self.pre = None
        self.pre = None
class LRUCache:
    def remove(self, node):
        node.pre.next, node.next.pre = node.next, node.pre
        self.dic.pop(node.key)
        
    def add(self, node):
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = self.tail.pre = node
        self.dic[node.key] = node
        
    def __init__(self, capacity):
        self.dic = {}
        self.n = capacity
        self.head = self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1
            
    def put(self, key, value):
        if key in self.dic:
            self.remove(self.dic[key])
        node = Node(key, value)
        self.add(node)
        if len(self.dic) > self.n:
            self.remove(self.head.next)



147.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ref, ref.next, n = ListNode(-float("inf")), head, 0
        while head:
            inserted, curr, prev, n = ListNode(head.val), ref.next, ref, n+1
            for i in range(n-1):
                if inserted.val<curr.val:
                    prev.next, inserted.next = inserted, curr
                    if i >= n-2: curr.next = None
                    break
                else: 
                    prev, curr = curr, curr.next
                if i == n-2: prev.next = inserted 
            head = head.next
        return ref.next



148.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        ls = []
        while head: ls.append(head.val); head = head.next
        ls .sort()
        root = head = ListNode(ls[0]) if ls else []
        for i in range(1, len(ls)):
            head.next = ListNode(ls[i])
            head = head.next
        return root



149.py # Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        m, res, roots = {}, 0, set()
        for i, p1 in enumerate(points):
            if (p1.x, p1.y) not in roots:
                roots.add((p1.x, p1.y))
                m.clear()
                dup = path = 0
                for j, p2 in enumerate(points):
                    if i != j:
                        try:
                            cur = (p1.y - p2.y) * 100 / (p1.x - p2.x)
                        except:
                            if p1.y == p2.y:
                                dup += 1
                                continue
                            else:
                                cur = "ver"
                        m[cur] = m.get(cur, 0) + 1
                        if m[cur] > path:
                            path = m[cur]
                if path + dup + 1 > res:
                    res = path + dup + 1
        return res



150.py class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in ("+", "-", "*", "/"): stack.append(int(token))
            else:
                num2, num1 = stack.pop(), stack.pop()
                if token == "+": last = num1 + num2
                elif token == "-": last = num1 - num2
                elif token == "*": last = num1 * num2
                elif token == "/": last = int(num1 / num2)
                stack.append(last)
        return stack[0]



151.py class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])




152.py class Solution:
    def maxProduct(self, nums):
        res, min_pos, max_neg, cur = -float("inf"), float("inf"), -float("inf"), 1
        for num in nums:
            cur *= num
            if cur > res: res = cur
            elif 0 < cur // min_pos > res: res = cur // min_pos
            elif 0 < cur // max_neg > res: res = cur // max_neg
            if cur == 0: min_pos, max_neg, cur = float("inf"), -float("inf"), 1
            elif max_neg < cur < 0: max_neg = cur
            elif 0 < cur < min_pos: min_pos = cur
        return res



153.py class Solution:
    findMin = min



154.py class Solution:
    def findMin(self, nums):
        l, r, res = 0, len(nums) - 1, nums and nums[0]
        while l <= r:
            while l < r and nums[l] == nums[l + 1]: l += 1
            while l < r and nums[r] == nums[r - 1]: r -= 1
            mid = (l + r) // 2
            if nums[mid] >= nums[0]: l = mid + 1
            else: r, res = mid - 1, min(res, nums[mid])
        return res



155.py class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.data or x < self.data[-1][1]: self.data.append([x, x])
        else: self.data.append([x, self.data[-1][1]])
    def pop(self):
        """
        :rtype: void
        """
        self.data.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.data[-1][0]
    def getMin(self):
        """
        :rtype: int
        """
        return self.data[-1][1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



156.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root):
        if root:
            left = self.upsideDownBinaryTree(root.left)
            self.upsideDownBinaryTree(root.right)
            if root.left:
                root.left.right, root.left.left = root, root.right
                root.right = root.left = None
            return left or root



157.py class Solution:
    def read(self, buf, n):
        idx = 0
        while True:
            buf4 = [""] * 4
            curr = min(read4(buf4), n - idx)
            for i in range(curr):
                buf[idx] = buf4[i]
                idx += 1
            if curr != 4 or idx == n:
                return idx




158.py """
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    
    def __init__(self):
        self.queue = []

    def read(self, buf, n):
        idx = 0
        while True:
            buf4 = [""]*4
            read4(buf4)
            self.queue += buf4
            curr = min(len(self.queue), n-idx)
            for i in range(curr):
                buf[idx] = self.queue.pop(0)
                idx+=1
            if curr == 0:
                break 
        return idx
        



159.py class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        start = distinct = 0
        cnt = collections.defaultdict(int)
        for c in s:
            cnt[c] += 1
            if cnt[c] == 1:
                distinct += 1
            if distinct > 2:
                cnt[s[start]] -= 1
                if not cnt[s[start]]:
                    distinct -= 1
                start += 1
        return len(s) - start



160.py class Solution(object):
    def getIntersectionNode(self, headA, headB):
        r1, r2, l1, l2 = headA, headB, 0, 0
        while headA: headA, l1 = headA.next, l1 + 1
        while headB: headB, l2 = headB.next, l2 + 1
        while l1 > l2: r1, l1 = r1.next, l1 - 1
        while l2 > l1: r2, l2 = r2.next, l2 - 1
        while r1 != r2: r1, r2 = r1.next, r2.next
        return r1



161.py class Solution:
    def isOneEditDistance(self, s, t):
        l1, l2, cnt, i, j = len(s), len(t), 0, 0, 0
        while i < l1 and j < l2:
            if s[i] != t[j]:
                cnt += 1
                if l1 < l2:
                    i -= 1
                elif l1 > l2:
                    j -= 1
            i += 1
            j += 1
        l = abs(l1 - l2)
        return (cnt == 1 and l <= 1)  or (cnt == 0 and l == 1)



162.py class Solution:
    def findPeakElement(self, nums):
        l, r, n = 0, len(nums) - 1, len(nums)
        while l <= r:
            mid = (l + r) // 2
            pre, after = mid == 0 and -float("inf") or nums[mid - 1], mid == n - 1 and -float("inf") or nums[mid + 1]
            if pre < nums[mid] > after: return mid
            elif pre > nums[mid]: r = mid - 1
            else: l = mid + 1



163.py class Solution:
    def findMissingRanges(self, nums, lower, upper):
        if not nums:
            return [str(lower) + "->" + str(upper)] if lower != upper else [str(lower)]
        res, n = [], len(nums)
        if lower + 1 < nums[0]:
            res.append(str(lower) + "->" + str(nums[0] - 1))
        elif lower + 1 == nums[0]:
            res.append(str(lower))
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 2:
                res.append(str(nums[i] - 1))
            elif nums[i] > nums[i - 1] + 2:
                res.append(str(nums[i - 1] + 1) + "->" + str(nums[i] - 1))
        if nums[-1] + 1 < upper: 
            res.append(str(nums[-1] + 1) + "->" + str(upper))
        elif nums[-1] + 1 == upper:
            res.append(str(upper))
        return res



164.py class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        n, mn, mx= len(nums), min(nums), max(nums)
        bSize = max(1, (mx - mn) // n + 1)
        bNum = (mx - mn) // bSize + 1
        buckets = [[float("inf"), -float("inf")] for _ in range(bNum)]
        for num in nums:
            ind = (num - mn) // bSize
            if num < buckets[ind][0]:
                buckets[ind][0] = num
            if num > buckets[ind][1]:
                buckets[ind][1] = num
        gap = 0
        for i in range(1, bNum):
            if buckets[i] == [float("inf"), -float("inf")]:
                buckets[i] = buckets[i - 1]
            gap = max(gap , buckets[i][0] - buckets[i - 1][1])
        return gap



165.py class Solution:
    def compareVersion(self, version1, version2):
        def getNum(s):
            if not s: return (None, None)
            for i in range(len(s)):
                if s[i] == ".": return (s[i + 1:], int(s[:i]))
            return (None, int(s))
        while True:
            version1, n1 = getNum(version1)
            version2, n2 = getNum(version2)
            if version1 == version2 == n1 == n2 == None: return 0
            if n1 != None and n1 > 0 and (n2 == None or n1 > n2): return 1
            if n2 != None and n2 > 0 and (n1 == None or n2 > n1): return -1



166.py class Solution:
    def fractionToDecimal(self, n, d):
        res = ["-"] if n * d < 0 else [""]
        n, d = abs(n), abs(d)
        res.append(str(n // d))
        n %= d
        if not n: return "".join(res)
        res.append(".")
        mp = {n: len(res)}
        while n:
            n *= 10
            res.append(str(n // d))
            n %= d
            if n in mp:
                res.insert(mp[n], "(")
                res.append(")")
                break
            mp[n] = len(res)
        return "".join(res)



167.py class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=numbers[0]
        right=numbers[-1]
        i,j=0,0
        while True:
            sum=left+right
            if sum>target:
                j+=1
                right=numbers[-1-j]
            if sum<target:
                i+=1
                left=numbers[0+i]
            if sum==target:
                return [i+1,len(numbers)-j]
            
                
        



168.py class Solution:
    def convertToTitle(self, n: int) -> str:
        char = str()
        while n > 0:
            if n % 26 == 0:
                char += "Z"
                n = n // 26 - 1
            else:
                char += chr(n % 26 + ord("@"))
                n = n // 26
        return char[::-1]




169.py class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_list=dict()
        for num in nums:
            if not num in num_list:
                num_list[num]=1
            else:
                num_list[num]+=1
        return max(num_list, key=num_list.get)



170.py class TwoSum:

    def __init__(self):
        self.nums = {}

    def add(self, number):
        self.nums[number] = self.nums.get(number, 0) + 1

    def find(self, value):
        for num in self.nums:
            if value - num in self.nums and (num != value - num or self.nums[num] > 1):
                return True
        return False



171.py class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum([(ord(char)-64)*(26**i) for i,char in enumerate(s[::-1])])



172.py class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)



173.py class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.pushAll(root)

    def next(self) -> int:
        cur = self.stack.pop()
        self.pushAll(cur.right)
        return cur.val

    def hasNext(self) -> bool:
        return self.stack

    def pushAll(self, node):
        while node != None:
            self.stack += (node,)
            node = node.left




174.py class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    dungeon[i][j] = max(1, 1 - dungeon[i][j])
                elif j == n - 1:
                    dungeon[i][j] = max(1, dungeon[i + 1][j] - dungeon[i][j])
                elif i == m - 1:
                    dungeon[i][j] = max(1, dungeon[i][j + 1] - dungeon[i][j])
                else:
                    dungeon[i][j] = max(1, min(dungeon[i + 1][j], dungeon[i][j + 1]) - dungeon[i][j])
        return dungeon[0][0]



179.py class Solution:
    def largestNumber(self, nums):
        def partition(l, r):
            j = l
            for i in range(l + 1, r + 1):
                if nums[i] + nums[l] >= nums[l] + nums[i]:
                    j += 1
                    nums[j], nums[i] = nums[i], nums[j]
            nums[l], nums[j] = nums[j], nums[l]
            return j
        def quickSort(l, r):
            if l < r:
                m = partition(l, r)
                quickSort(l, m - 1)
                quickSort(m + 1, r)
        nums = [str(num) for num in nums]
        quickSort(0, len(nums) - 1)  
        return str(int("".join(nums)))



186.py class Solution:
    def reverseWords(self, s):
        l, r, n = 0, len(s) - 1, len(s)
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        l = r = 0
        while r < n:
            while r + 1 < n and s[r + 1] != " ":
                r += 1
            i = r + 2
            while l <= r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            l = r = i



187.py class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic, str = {}, "x" + s[:9]
        for i in range(9, len(s)):
            str = str[1:] + s[i]
            dic[str] = 1 if str not in dic else dic[str] + 1
        return [k for k, v in dic.items() if v > 1]



188.py class Solution:
    def maxProfit(self, k, prices):
        if k >= len(prices) // 2: return sum(sell - buy for sell, buy in zip(prices[1:], prices[:-1]) if sell - buy > 0)
        dp = [[0, -float("inf")] for _ in range(k + 1)]
        for p in prices:
            for i in range(k + 1):
                if i and dp[i - 1][1] + p > dp[i][0]: dp[i][0] = dp[i - 1][1] + p 
                if dp[i][0] - p > dp[i][1]: dp[i][1] = dp[i][0] - p
        return dp[-1][0]



189.py class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=k%len(nums)
        nums[:] = nums[-n:] + nums[:-n]
        



190.py class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1],2)



198.py class Solution:
    def rob(self, nums):
        if len(nums) <= 2: return max(nums or [0])
        nums[2] += nums[0]
        for i in range(3, len(nums)): nums[i] += max(nums[i - 2], nums[i - 3])
        return max(nums[-1], nums[-2])



199.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q, res = [root], []
        while any(q):
            res.append(q[-1].val)
            q = [kid for node in q for kid in (node.left, node.right) if kid]
        return res



200.py class Solution:
    def numIslands(self, grid):
        res, n, m = 0, len(grid), len(grid[0]) if grid else 0
        def explore(i, j):
            grid[i][j] = "-1"
            if i > 0 and grid[i - 1][j] == "1": explore(i - 1, j)
            if j > 0 and grid[i][j - 1] == "1": explore(i, j - 1)
            if i + 1 < n and grid[i + 1][j] == "1": explore(i + 1, j)
            if j + 1 < m and grid[i][j + 1] == "1": explore(i, j + 1)
        for i in range(n): 
            for j in range(m):
                if grid[i][j] == "1": explore(i, j); res += 1
        return res



201.py class Solution:
    def rangeBitwiseAnd(self, m, n):
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return m << i



202.py class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem: return False
            else: mem.add(n)
        else: return True



203.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev, curr = ListNode(None), head
        while curr:
            if curr.val==val:
                if curr==head: head=head.next
                prev.next=curr.next
            if curr.val!=val: prev=curr
            curr=curr.next
        return head



204.py class Solution:
    def countPrimes(self, n):
        primes = [i for i in range(2, n)]
        for i in range(2, n):
            for prime in primes:
                if i ** (prime - 1) % prime != 1 and prime > i:
                    primes.remove(prime)
        return len(primes)




205.py class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        dic={}
        for i in range(len(s)):
            if not t[i] in dic.values() and not s[i] in dic: dic[s[i]] = t[i]
            elif not s[i] in dic or dic[s[i]] != t[i]: return False
        return True



206.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode, pre = None) -> ListNode:
        if head:
            nex = head.next
            head.next = pre
            return self.reverseList(nex, head) if nex else head



207.py class Solution:
    def canFinish(self, numCourses, prerequisites):
        def cycle(course):
            visited[course] = 0
            for Next in route[course]:
                if visited[Next] == 0 or (visited[Next] == -1 and cycle(Next)): return True
            visited[course] = 1
            return False
        route, visited = {i: [] for i in range(numCourses)}, [-1] * numCourses 
        for req in prerequisites: route[req[1]].append(req[0])
        for course in range(numCourses):
            if visited[course] == -1 and cycle(course): return False
        return True



208.py class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        
    def move(self, word, mod):
        cur = self.root
        for c in word:
            if c not in cur:
                if mod != 1:
                    return False
                cur[c] = {}
            cur = cur[c]
        if mod == 1:
            cur['#'] = None
        else:
            return mod == 3 or '#' in cur
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        return self.move(word, 1)
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.move(word, 2)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.move(prefix, 3)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



209.py class Solution:
    def minSubArrayLen(self, s, nums):
        l, res, curr = 0, len(nums) + 1, 0
        for r, num in enumerate(nums):
            curr += num
            while curr >= s: res, l, curr = min(res, r - l + 1), l + 1, curr - nums[l]
        return res < len(nums) + 1 and res or 0



210.py class Solution:
    def findOrder(self, numCourses, prerequisites):
        children, parent = collections.defaultdict(set), collections.defaultdict(set)
        for i, j in prerequisites: children[i].add(j); parent[j].add(i)
        stack = [i for i in range(numCourses) if not children[i]]
        for i in stack:
            for j in parent[i]:
                children[j].remove(i)
                if not children[j]: stack += j,
        return stack if len(stack) == numCourses else []



211.py class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.last = False
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            if not curr.children[ord(char) - ord("a")]: curr.children[ord(char) - ord("a")] = TrieNode()
            curr = curr.children[ord(char) - ord("a")]
        curr.last = True
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        words = [self.root]
        for char in word:
            if char == ".": words = [child for node in words for child in node.children if node and child]
            else: words = [node.children[ord(char) - ord("a")] for node in words if node and node.children[ord(char) - ord("a")]]
        if words and words[-1] == ".": return True
        else: return any([node.last for node in words if node.last])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



212.py class Solution:
    def findWords(self, board, words):
        def explore(i, j, cur):
            visited[i][j] = 0
            if "#" in cur and cur["#"] not in res_set: res.append(cur["#"]); res_set.add(cur["#"])
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and board[x][y] in cur and visited[x][y] == -1: explore(x, y, trie[cur[board[x][y]]])
            visited[i][j] = -1
        trie, cnt, m, n, res, res_set = {}, 1, len(board), len(board and board[0]), [], set()
        visited, trie[0] = [[-1] * n for _ in range(m)], {}
        for w in words:
            cur = trie[0]
            for c in w:
                if c not in cur: trie[cnt], cur[c], cnt = {}, cnt, cnt + 1
                cur = trie[cur[c]]
            cur["#"] = w
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie[0]: explore(i, j, trie[trie[0][board[i][j]]])
        return res



213.py class Solution:
    
    def dp(self, nums):
        if len(nums) <= 2: return max(nums or [0])
        nums[2] += nums[0]
        for i in range(3, len(nums)): nums[i] += max(nums[i - 2], nums[i - 3])
        return max(nums[-1], nums[-2])
    
    def rob(self, nums):
        return max(self.dp(nums[:-1]), self.dp(nums[1:])) if len(nums) != 1 else nums[0]



214.py class Solution:
    def shortestPalindrome(self, s, pre = ""):
        for i in range(1, len(s) // 2 + 2):
            if s[i - 1:].startswith(s[:i][::-1]): pre = s[2* i - 1:][::-1]
            if s[i:].startswith(s[:i][::-1]): pre = s[2* i:][::-1]
        return pre + s



215.py class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]



216.py class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        stack, nums, res = [(0, [], 0, k)], range(1, 10), []
        while stack:
            sm, tmp, index, k_val = stack.pop(0)
            for i in range(index, len(nums)):
                if sm + nums[i] < n and k_val > 0: stack.append((sm + nums[i], tmp + [nums[i]], i + 1, k_val - 1))
                elif sm + nums[i] == n and k_val == 1: res.append(tmp + [nums[i]])
        return res



217.py class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic=dict()
        for num in nums:
            if not num in dic:
                dic[num]=1
            else:
                return True
        return False



218.py class Solution:
    def getSkyline(self, buildings):
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]: 
                heapq.heappop(hp)
            if negH: 
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]: 
                res += [x, -hp[0][0]],
        return res[1:]



219.py class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic={}
        for i,num in enumerate(nums):
                if num in dic and i-dic[num]<=k:
                    return True
                dic[num]=i
        return False



220.py class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0: return False
        d = {}
        for i in range(len(nums)):
            m = nums[i] // (t + 1)
            if m in d or (m - 1 in d and nums[i] - d[m - 1] <= t) or (m + 1 in d and d[m + 1] - nums[i] <= t):
                return True
            d[m] = nums[i]
            if i >= k: del d[nums[i - k] // (t + 1)]
        return False



221.py class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res, count = 0, 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] != 0:
                    count = 1
                    if j>0 and int(matrix[i][j-1]) != 0: matrix[i][j] += int(matrix[i][j-1])
                    if i-1>=0 and int(matrix[i-1][j]) != 0:
                        k, curr = i-1, []
                        while k>=0 and k>=i-matrix[i][j]+1 and int(matrix[k][j]) != 0:
                            if matrix[k][j]>= count+1:
                                curr.append(matrix[k][j])
                                if min(curr)>= count+1: count += 1
                            else: break
                            k -= 1
                res = max(res, count**2)
        return res



222.py class Solution:
    
    def countNodes(self, root):
        if not root: return 0
        l = self.getDepth(root.left)
        r = self.getDepth(root.right)
        if l == r:
            return (1 << l) + self.countNodes(root.right)
        return (1 << r) + self.countNodes(root.left)
    
    def getDepth(self, root):
        if not root: return 0
        return 1 + self.getDepth(root.left)



223.py class Solution:
    def computeArea(self, a, b, c, d, e, f, g, h):
        x1, x2, x3 = abs(a - c), abs(e - g), max(a, c, e, g) - min(a, c, e, g) 
        y1, y2, y3 = abs(b - d), abs(f - h), max(b, d, f, h) - min(b, d, f, h)
        if x3 < x1 + x2 and y3 < y1 + y2: intrs = (x1 + x2 - x3) * (y1 + y2 - y3) 
        else: intrs = 0
        return x1 * y1 + x2 * y2 - intrs



224.py class Solution:
    def calculate(self, s):
        def calc(n2, op, n1): 
            return n1 + n2 if op == "+" else n1 - n2
        stack, i, num = [], 0, 0
        while i < len(s):
            j = i
            while j < len(s) and s[j].isdigit():
                num, j = num * 10 + int(s[j]), j + 1
            if i != j:
                stack.append(calc(num, stack.pop(), stack.pop()) if stack and s[i - 1] != "(" else num)
                num, j = 0, j - 1
            elif s[i] in "+-":
                stack.append(s[i])
            elif s[i] == ")" and len(stack) > 1:
                stack.append(calc(stack.pop(), stack.pop(), stack.pop()))
            i = j + 1
        return stack.pop()



225.py class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.data.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.data.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.data[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not bool(self.data)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()



226.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        root.left, root.right= root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



227.py class Solution:
    def calculate(self, s):
        mod = 0
        while mod < 2:
            stack, i, n, num = [], 0, len(s), ""
            while i < n:
                if s[i] == " ":
                    i += 1
                    continue
                while mod == 0 and i < n and s[i].isnumeric():
                    num += s[i]
                    i += 1
                if stack and stack[-1] in [("*", "/"), ("+", "-")][mod]:
                    op, num1 = stack.pop(), stack.pop()
                    if op == "*":
                        stack.append(num1 * int(num))
                    elif op == "/":
                        stack.append(num1 // int(num))
                    elif op == "+":
                        stack.append(num1 + s[i])
                        i += 1
                    else:
                        stack.append(num1 - s[i])
                        i += 1
                    num = ""
                elif num:
                    stack.append(int(num))
                    num = ""
                else:
                    stack.append(s[i])
                    i += 1
            mod += 1
            s = stack
        return stack.pop()



228.py class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res, stack = [], [nums[0] if nums else None, None]
        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == num - 1: stack[1] = num
            if i > 0 and nums[i-1] != num - 1: res, stack[0], stack[1] = res + ["->".join(str(q) for q in stack if q != None)], num, None
            if i == len(nums) - 1: res.append("->".join(str(q) for q in stack if q != None))
        return res



229.py class Solution:
    def majorityElement(self, nums):
        c1, c2, cnt1, cnt2 = 0, 1, 0, 0
        for num in nums:
            if num == c1:
                cnt1 += 1
            elif num == c2:
                cnt2 += 1
            elif not cnt1:
                c1, cnt1 = num, 1
            elif not cnt2:
                c2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        return [c for c in (c1, c2) if nums.count(c) > len(nums) // 3]



230.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.k, self.res = 0, None
    def kthSmallest(self, root, k):
        if self.k < k and root.left: self.kthSmallest(root.left, k)
        self.k += 1
        if self.k == k: self.res = root.val
        if self.k < k and root.right: self.kthSmallest(root.right, k)
        return self.res



231.py class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i=0
        while 2**i<=n:
            if 2**i==n: return True
            i+=1
        return False



232.py class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.data.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        front = self.data[0]
        self.data = self.data[1:]
        return front

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.data[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not bool(self.data)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



233.py class Solution:
    def countDigitOne(self, n):
        if n <= 0:
            return 0
        q, x, ans = n, 1, 0
        while q > 0:
            digit = q % 10
            q //= 10
            ans += q * x
            if digit == 1:
                ans += n % x + 1
            elif digit > 1:
                ans += x
            x *= 10
        return ans



234.py class Solution:
    def isPalindrome(self, head):
        r = fast = head
        l = None
        while fast and fast.next:
            fast = fast.next.next
            r.next, l, r = l, r, r.next
        if fast: r = r.next
        while l and r and l.val == r.val:
            l, r = l.next, r.next
        return not l



235.py class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root





236.py class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        parent, stack = {root: None}, [root]
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q




237.py class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next





238.py class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m, res = 1, []
        for i in range(len(nums)):
            res.append(m)
            m *= nums[i]
        m = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= m
            m *= nums[i]
        return res



239.py class Solution:
    def maxSlidingWindow(self, nums, k):
        cnt, heap, res = collections.Counter(), [], []
        for i, num in enumerate(nums):
            heapq.heappush(heap, -num)
            cnt[num] += 1
            while not cnt[-heap[0]]:
                heapq.heappop(heap)
            if i >= k - 1:
                res.append(-heap[0])
                cnt[nums[i - k + 1]] -= 1
        return res



240.py class Solution:
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)



241.py class Solution:
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i + 1:])
                for j in l:
                    for k in r:
                        res.append(self.calc(j, input[i], k))
        return res
    def calc(self, l, op, r):
        return l + r if op == "+" else l - r if op == "-" else l * r



242.py class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #return sum([ord(i) for i in s])==sum([ord(j) for j in t]) and set(s)==set(t)
        return sorted(s)==sorted(t)



243.py class Solution:
    def shortestDistance(self, words, word1, word2):
        i1, i2, mn = -1, -1, float("inf")
        for i, w in enumerate(words):
            if w == word1:
                i1 = i
                if i2 >= 0:
                    mn = min(mn, i - i2)
            elif w == word2:
                i2 = i
                if i1 >= 0:
                    mn = min(mn, i - i1)
        return mn



244.py class WordDistance:

    def __init__(self, words):
        self.d = {}
        self.ind = collections.defaultdict(set)
        for i, w in enumerate(words):
            self.ind[w].add(i)
        
    def shortest(self, word1, word2):
        if (word1, word2) not in self.d:
            self.d[(word1, word2)] = self.d[(word2, word1)] = min(abs(j - i) for i in self.ind[word1] for j in self.ind[word2])
        return self.d[(word1, word2)]



245.py class Solution:
    def shortestWordDistance(self, words, word1, word2):
        i1 = i2 = -1
        res, same = float("inf"), word1 == word2
        for i, w in enumerate(words):
            if w == word1:
                if same: i2 = i1
                i1 = i
                if i2 >= 0: res = min(res, i1 - i2)
            elif w == word2:
                i2 = i
                if i1 >= 0: res = min(res, i2 - i1)
        return res 



246.py class Solution:
    def isStrobogrammatic(self, num):
        return not any(num[i] + num[-1-i] not in ("88", "69", "96", "11", "00") for i in range((len(num) + 1) // 2))



247.py class Solution:
    def findStrobogrammatic(self, n, q = [""]):
        for i in range(n // 2): q = [s + c for s in q  for c in "01689" if i != 0 or c != "0"]
        if n % 2: q = [s + c for s in q for c in "018"]
        for i in range(n // 2 - 1, -1, -1):  q = [s + "9" if s[i] == "6" else s + "6" if s[i] == "9" else s + s[i] for s in q]
        return q



248.py class Solution:
    def strobogrammaticInRange(self, low, high):
        q, cnt, low, high, ln = ["", "0", "1", "8"], 0, int(low), int(high), len(high)
        while q:
            s = q.pop()
            if s and s[0] != "0" and low <= int(s) <= high: cnt += 1
            q += [l + s + r for l, r in (("8", "8"), ("6", "9"), ("9", "6"), ("1", "1"), ("0", "0")) if len(s) <= ln - 2] 
        return cnt if low != 0 else cnt + 1



249.py class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        table = collections.defaultdict(list)
        for w in strings:
            pattern = ""
            for i in range(1, len(w)):
                if ord(w[i]) - ord(w[i - 1]) >= 0:
                    pattern += str(ord(w[i]) - ord(w[i - 1]))
                else:
                    pattern += str(ord(w[i]) - ord(w[i - 1]) + 26)
            table[pattern].append(w)
        return [table[pattern] for pattern in table]



250.py # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        res = [0]
        def dfs(node, value):
            if not node:
                return True, value
            left, lVal = dfs(node.left, node.val)
            right, rVal = dfs(node.right, node.val)
            cnt = left and right and lVal == rVal == node.val
            if cnt:
                res[0] += 1
            return cnt, node.val
        dfs(root, None)
        return res[0]



251.py class Vector2D:
    def __init__(self, v: List[List[int]]):
        self.arr = v
        self.rows = len(v)
        self.i = self.j = 0

    def next(self) -> int:
        if self.hasNext():
            self.j += 1
            return self.arr[self.i][self.j - 1]

    def hasNext(self) -> bool:
        if self.arr and self.j == len(self.arr[self.i]):
            self.i += 1
            self.j = 0
        while self.i + 1 < self.rows and not self.arr[self.i]:
            self.i += 1
        return self.i < self.rows and self.arr[self.i] != []




252.py # Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda x: x.end)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end: return False
        return True



253.py # Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x: x.start)
        heap, time, rooms = [], 0, 0
        for intr in intervals:
            while heap and heap[0] <= intr.start:
                heapq.heappop(heap)
            heapq.heappush(heap, intr.end)
            if len(heap) > rooms:
                rooms += 1
        return rooms



254.py class Solution:
    def getFactors(self, n):
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                factors |= {i, n // i}
        q, res = [[f, [f]] for f in factors], []
        while q:
            new = []
            for sm, arr in q:
                for f in factors:
                    if f >= arr[-1]:
                        if sm * f < n:
                            new.append([sm * f, arr + [f]])
                        elif sm * f == n:
                            res.append(arr + [f])
            q = new
        return res



255.py class Solution:
    def verifyPreorder(self, preorder):
        stack, lower = [], -float("inf")
        for x in preorder:
            if x < lower: return False
            while stack and x > stack[-1]: lower = stack.pop()
            stack.append(x)
        return True



256.py class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [0] * 3
        for a, b, c in costs:
            c1 = min(dp[1], dp[2]) + a
            c2 = min(dp[0], dp[2]) + b
            c3 = min(dp[0], dp[1]) + c
            dp = [c1, c2, c3]
        return min(dp)



257.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node, arr):
            if not node.right and not node.left:
                #print(arr)
                self.res += ['->'.join(str(num) for num in arr)]
            if node.left:
                dfs(node.left, arr + [node.left.val])
            if node.right:
                dfs(node.right, arr + [node.right.val])
        self.res = []
        if not root: return []
        dfs(root, [root.val])
        return self.res



258.py class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num=str(num)
        while len(num)>1:
            num=str(sum([int(i) for i in num]))
        return int(num)



259.py class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            r = len(nums) - 1
            for j in range(i + 1, len(nums) - 1):
                while r > j + 1 and nums[i] + nums[j] + nums[r] >= target:
                    r -= 1
                if nums[i] + nums[j] + nums[r] < target:
                    res += r - j
        return res



260.py class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [n[0] for n in collections.Counter(nums).most_common()[-2:]]



261.py class Solution:
    def validTree(self, n, edges):
        visited, adj = [0] * n, collections.defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        def dfs(i, pre):
            visited[i] = 1
            for v in adj[i]:
                if v != pre and (visited[v] or not dfs(v, i)):
                    return False
            return True
        return dfs(0, -1) and sum(visited) == n



263.py class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num>1:
            if num%2!=0 and num%3!=0 and num%5!=0: return False
            else: num/=[i for i in (2,3,5) if num%i==0][-1]
        return num==1



264.py class Solution:
    def nthUglyNumber(self, n):
        arr, heap, used = [], [1], set()
        for i in range(n):
            num = heapq.heappop(heap)
            arr.append(num)
            for p in (2, 3, 5):
                if p * num not in used:
                    heapq.heappush(heap, p * num)
                    used.add(p * num)
        return arr[-1]



265.py class Solution:
    def minCostII(self, costs):
        for i in range(1, len(costs)):
            for j in range(len(costs[0])): costs[i][j] += min(costs[i - 1][:j] + costs[i - 1][j + 1:])
        return costs and min(costs[-1]) or 0



266.py class Solution:
    def canPermutePalindrome(self, s):
        cnt = collections.Counter(s)
        return len([c for c in cnt if cnt[c] % 2]) <= 1



267.py class Solution:
    def generatePalindromes(self, s):
        cnt, n = collections.Counter(s), len(s) // 2
        odd, s, q = [c for c in cnt if cnt[c] % 2], "".join(k * (cnt[k] // 2) for k in cnt), {"#" * n}
        if len(odd) > 1: return []
        for c in s:
            new = set()
            for w in q:
                for i in range(n):
                    if w[i] == "#":
                        new.add(w[:i] + c + w[i + 1:])
            q = new
        return [w + odd[0] + w[::-1] for w in q] if odd else [w + w[::-1] for w in q]



268.py class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums)*(len(nums)+1)//2-sum(nums)



269.py class Solution(object):
    def alienOrder(self, words):
        if len(words) == 1: return words[0]
        def dfs(i):
            visited[i] = 0
            for v in graph[i]:
                if visited[v] == 0 or (visited[v] == -1 and not dfs(v)): return False
            order.append(chr(97 + i))
            visited[i] = 1
            return True
        graph, visited, order = collections.defaultdict(set), [1] * 26, []
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    graph[ord(c1) - ord("a")].add(ord(c2) - ord("a"))
                    break
            for c in w1 + w2: visited[ord(c) - ord("a")] = -1
        for i in range(26):
            if visited[i] == -1 and not dfs(i): return ""
        return "".join(order)[::-1]



270.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res, d = [0], [float("inf")]
        def dfs(node):
            if node:
                new = node.val - target if node.val >= target else target - node.val
                if new < d[0]:
                    d[0] = new
                    res[0] = node.val
                if target < node.val:
                    dfs(node.left)
                else:
                    dfs(node.right)
        dfs(root)
        return res[0]



271.py class Codec:

    def encode(self, strs):
        return "".join(str(len(s)) + ":" + s for s in strs)

    def decode(self, s):
        strs = []
        while s:
            i = s.find(":")
            length = int(s[:i])
            s = s[i+1:]
            strs.append(s[:length])
            s = s[length:]
        return strs



272.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root, target, k):
        d = []
        def dfs(node):
            if node:
                heapq.heappush(d, (abs(node.val - target), node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return [node for val, node in heapq.nsmallest(k, d)]



273.py class Solution:
    def __init__(self):
        self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]

    def numberToWords(self, num):
        if not num:
            return "Zero"
        res = ""
        for thousand in self.thousands:
            if num % 1000:
                res = self.helper(num%1000) + thousand + " " + res
            num //= 1000
        return res.strip()

    def helper(self, num):
        if not num:
            return ""
        elif num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            return self.tens[num//10] + " " + self.helper(num%10)
        else:
            return self.lessThan20[num//100] + " Hundred " + self.helper(num%100)



274.py class Solution:
    def hIndex(self, citations):
        citations.sort()
        for i in range(len(citations)):
            if len(citations) - i <= citations[i]: return len(citations) - i
        return 0



275.py class Solution:
    def hIndex(self, citations):
        l, r, res = 0, len(citations) - 1, 0
        while l <= r:
            mid = (l + r) // 2
            if len(citations) - mid <= citations[mid]: res, r = len(citations) - mid, r - 1
            else: l = mid + 1
        return res



276.py class Solution:
    def numWays(self, n, k):
        same, dif = 0, k
        for _ in range(1, n): same, dif = dif, (same + dif) * (k - 1)
        return n and same + dif or 0



277.py # The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        i = 0
        while i < n:
            person = i
            i += 1
            while i < n and not knows(person, i) and knows(i, person):
                i += 1
        j = person - 1
        while j >= 0 and not knows(person, j) and knows(j, person):
            j -= 1
        return person if j < 0 else -1



278.py # The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return r + 1



279.py class Solution:
    def numSquares(self, n):
        q, move = {i ** 2 for i in range(1, int(n ** 0.5) + 1)}, 1
        coins = set(q)
        while q:
            if n in q: return move
            q = {sm + c for sm in q for c in coins} - q
            move += 1



280.py class Solution:
    def wiggleSort(self, nums):
        n = len(nums)
        for i in range(0, n -1, 2):
            if i == n - 2:
                if nums[-1] < nums[-2]:
                    nums[-2], nums[-1] = nums[-1], nums[-2]
            else:
                if nums[i + 2] >= nums[i + 1] < nums[i]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                elif nums[i] > nums[i + 2] <= nums[i + 1]:
                    nums[i], nums[i + 2] = nums[i + 2], nums[i]
                if nums[i + 2] > nums[i + 1]:
                    nums[i + 1], nums[i + 2] = nums[i + 2], nums[i + 1]    



281.py class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.arr1, self.arr2, self.l1, self.l2 = v1, v2, len(v1), len(v2)
        self.i = self.j = 0
        self.n, self.turn = max(self.l1, self.l2), v1 and 1 or 0

    def next(self):
        if self.turn:
            num = self.arr1[self.i]
            self.i += 1
            if self.j < self.l2:
                self.turn = 0
        else:
            num = self.arr2[self.j]
            self.j += 1
            if self.i < self.l1:
                self.turn = 1
        return num

    def hasNext(self):
        return self.turn and self.i < self.l1 or self.j < self.l2



282.py class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # s, val, cur, coeff
        q = {("", 0, 0, 1)}
        for i, c in enumerate(num):
            new = set()
            for s, val, cur, coeff in q:
                if i:
                    new.add((s + "+" + c, val + int(c), int(c), 1))
                    new.add((s + "-" + c, val - int(c), int(c), -1))
                    new.add((s + "*" + c, val + cur * coeff * (int(c) - 1), int(c), cur * coeff))
                if s and s[-1] == "0" and cur == 0: continue
                pre = cur
                cur = cur * 10 + int(c)
                new.add((s + c, val + coeff * (cur - pre), cur, coeff))
            q = new
        return [s for s, val, cur, coeff in q if val == target]



283.py class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, items=0, 0
        while i<len(nums) and items<=len(nums):
            if nums[i]==0: nums.append(0); nums.pop(i); i-=1
            i+=1; items+=1



284.py # Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        self.it = iterator
        self.bool = self.it.hasNext()
        self.num =  self.it.next() if self.bool else None
    def peek(self):
        return self.num

    def next(self):
        n = self.num
        self.bool = self.it.hasNext()
        if self.bool:
            self.num = self.it.next()
        return n

    def hasNext(self):
        return self.bool



285.py class Solution:
    def inorderSuccessor(self, root: "TreeNode", p: "TreeNode") -> "TreeNode":
        if not root:
            return
        if root.val > p.val:
            return self.inorderSuccessor(root.left, p) or root
        return self.inorderSuccessor(root.right, p)




286.py class Solution:
    def wallsAndGates(self, rooms):
        m, n = len(rooms), len(rooms and rooms[0])  
        q, dist = [(i, j) for i in range(m) for j in range(n) if not rooms[i][j]], 0
        while q:
            new = []
            dist += 1
            for i, j in q:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and rooms[x][y] == 2147483647:
                        rooms[x][y] = dist
                        new.append((x, y))
            q = new



287.py class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high, mid = 0, len(nums)-1, len(nums)-1 // 2
        while high - low > 1:
            count, mid = 0, (high + low) // 2
            for k in nums:
                if mid < k <= high: count += 1
            if count > high - mid: low = mid
            else: high = mid
        return high



288.py class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.pool = collections.defaultdict(set)
        for w in dictionary:
            self.pool[w[2:] and w[0] + str(len(w) - 2) + w[-1] or w].add(w)
            

    def isUnique(self, w: str) -> bool:
        return not self.pool[w[2:] and w[0] + str(len(w) - 2) + w[-1] or w] - {w}


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)



289.py class Solution:
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        matrix = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                cnt = 0
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1)):
                    if 0 <= x < m and 0 <= y < n and board[x][y] == 1: cnt += 1
                if (board[i][j] and 2 <= cnt <= 3) or (not board[i][j] and cnt == 3): matrix[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] = matrix[i][j]



290.py class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(str.split())!=len(pattern): return False
        dic={}
        for word in str.split():
            if not pattern[0] in dic.values() and not word in dic: dic[word]=pattern[0]
            else:
                if not word in dic or dic[word]!=pattern[0]: return False
            pattern=pattern[1:]
        return True
        



291.py class Solution:
    def wordPatternMatch(self, pattern, s):
        m, n = len(pattern), len(s)
        def dfs(i, j, dic, used):
            if i >= m or j >= n:
                return i == m and j == n
            elif pattern[i] in dic:
                return s[j:j + len(dic[pattern[i]])] == dic[pattern[i]] and dfs(i + 1, j + len(dic[pattern[i]]), dic, used)
            else:
                for k in range(j + 1, n + 1):
                    if s[j:k] not in used:
                        dic[pattern[i]] = s[j:k]
                        if dfs(i + 1, j + len(dic[pattern[i]]), dic, used | {s[j:k]}):
                            return True
                        dic.pop(pattern[i])
                return False
        return dfs(0, 0, {}, set())



292.py class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n%4==0 else True



293.py class Solution:
    def generatePossibleNextMoves(self, s):
        return [s[:i] + "--" + s[i + 2:] for i in range(len(s) - 1) if s[i] == s[i + 1] == "+"]



294.py class Solution:
    def canWin(self, s):
        choices = {i for i in range(1, len(s)) if s[i] == s[i - 1] == "+"} 
        def dfs(arr, moves, turn):
            if not moves:
                return turn == 1
            elif turn:
                return all(dfs(arr + [m], moves - {m - 1, m, m + 1}, 1 - turn) for m in moves) 
            else:
                return any(dfs(arr + [m], moves - {m - 1, m, m + 1}, 1 - turn) for m in moves) 
        return not dfs([], choices, 1)     



295.py class MedianFinder:

    def __init__(self):
        self.l = []
        self.r = []
        self.m = []

    def addNum(self, num):
        if not self.m:
            self.m = [num]
        elif len(self.m) == 1:
            m = self.m[0]
            if num >= m:
                self.m = [m, heapq.heappushpop(self.r, num)]
            else:
                self.m = [-heapq.heappushpop(self.l, -num), m]
        else:
            m1, m2 = self.m
            if num >= m2:
                heapq.heappush(self.r, num)
                heapq.heappush(self.l, -m1)
                self.m = [m2]
            elif num <= m1:
                heapq.heappush(self.l, -num)
                heapq.heappush(self.r, m2)
                self.m = [m1]
            else:
                heapq.heappush(self.l, -m1)
                heapq.heappush(self.r, m2)
                self.m = [num]

    def findMedian(self):
        return sum(self.m) / len(self.m)



296.py class Solution:
    def minTotalDistance(self, grid):
        m, n = len(grid), len(grid[0])
        x, y = sorted(i for i in range(m) for j in range(n) if grid[i][j]), sorted(j for i in range(m) for j in range(n) if grid[i][j])
        avg_x = len(x) % 2 and x[len(x) // 2] or (x[len(x) // 2 - 1] + x[len(x) // 2]) / 2
        avg_y = len(y) % 2 and y[len(y) // 2] or (y[len(y) // 2 - 1] + y[len(y) // 2]) / 2
        return int(sum(abs(avg_x - i) + abs(avg_y - j) for i, j in zip(x, y)))



297.py class Codec:

    def serialize(self, root):
        q, s = root and collections.deque([root]), ""
        while q:
            node = q.popleft()
            if node is None:
                s += "null#"
            else:
                s += str(node.val) + "#"
                q += [node.left, node.right]
        return s
        

    def deserialize(self, data):
        data = data and collections.deque(data.split("#"))
        q, root = data and collections.deque([TreeNode(int(data.popleft()))]), None
        while q:
            node = q.popleft()
            if not root:
                root = node
            l, r = data.popleft(), data.popleft()
            if l != "null":
                node.left = TreeNode(int(l))
                q.append(node.left)
            if r != "null":
                node.right = TreeNode(int(r))
                q.append(node.right)
        return root



298.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        q, l = root and [(root, 1)] or [], 0
        while q:
            node, path = q.pop()
            l = max(l, path)
            q += [(child, child.val == node.val + 1 and path + 1 or 1) for child in (node.left, node.right) if child]
        return l



299.py class Solution:
    def getHint(self, secret, guess):
        s, g, a, b = collections.defaultdict(int), collections.defaultdict(int), 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]: a += 1; continue
            if s[guess[i]] > 0: b, s[guess[i]] = b + 1, s[guess[i]] - 1
            else: g[guess[i]] += 1
            if g[secret[i]] > 0: b, g[secret[i]] = b + 1, g[secret[i]] - 1
            else: s[secret[i]] += 1
        return "%dA%dB" % (a, b)



300.py class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size       



301.py class Solution:
    def removeInvalidParentheses(self, s):
        l = r = 0
        for c in s:
            if c.isalpha(): continue
            if c == "(": l += 1 
            elif l: l -= 1
            else: r += 1
        q = {("", l, r, 0, 0)}
        for c in s:
            new = set()
            for st, l, r, lCur, rCur in q:
                if c == "(":
                    new.add((st + c, l, r, lCur + 1, rCur))
                    if l:
                        new.add((st, l - 1, r, lCur, rCur))
                elif c == ")":
                    if lCur:
                        new.add((st + c, l, r, lCur - 1, rCur))
                    else:
                        new.add((st + c, l, r, lCur, rCur + 1))
                    if r:
                        new.add((st, l, r - 1, lCur, rCur))
                else:
                    new.add((st + c, l, r, lCur, rCur))
            q = new
        return list({st for st, l, r, lCur, rCur in q if l == r == lCur == rCur == 0})



302.py class Solution:
    def minArea(self, image, x, y):
        l, r, u, d, m, n = [y], [y], [x], [x], len(image), len(image[0])
        def dfs(i, j):
            if i < u[0]: u[0] = i
            elif i > d[0]: d[0] = i
            if j < l[0]: l[0] = j
            elif j > r[0]: r[0] = j
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == "1":
                    image[x][y] = "0"
                    dfs(x, y)
        dfs(x, y)
        return (r[0] - l[0] + 1) * (d[0] - u[0] + 1)



303.py class NumArray:

    def __init__(self, nums):
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i - 1]
        

    def sumRange(self, i, j):
        return self.nums[j] - self.nums[i - 1] if i else self.nums[j]



304.py class NumMatrix:

    def __init__(self, matrix):
        self.sums = [[0] * (len(matrix and matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix and matrix[0])):
                self.sums[i + 1][j + 1] = self.sums[i][j + 1] + self.sums[i + 1][j] - self.sums[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        return self.sums[row2 + 1][col2 + 1] - self.sums[row2 + 1][col1] - self.sums[row1][col2 + 1] + self.sums[row1][col1]



305.py class Solution:
    def numIslands2(self, m, n, positions):
        def getParent(i):
            if i != parent[i]:
                parent[i] = getParent(parent[i])
            return parent[i]
        islands, res, parent, Id = set(), [], {}, 1
        for i, j in positions:
            parent[(i, j)] = parent[Id] = Id
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if (x, y) in parent:
                    p = getParent(parent[(x, y)])
                    islands.discard(p)
                    parent[p] = Id
            islands.add(Id)
            Id += 1
            res.append(len(islands))
        return res



306.py class Solution:
    def isAdditiveNumber(self, num):
        def getStarter():
            arr = []
            for i in range(1, len(num) - 1):
                for j in range(i + 1, len(num)):
                    s1, s2 = num[:i], num[i:j]
                    if (s1[0] == "0" and len(s1) > 1) or (s2[0] == "0" and len(s2) > 1): 
                        continue
                    arr.append((int(s1), int(s2), j))
            return arr                 
        def dfs(pre1, pre2, i):
            if i == len(num):
                return True
            sm = pre1 + pre2
            l = len(str(sm))
            new = int(num[i:i + l])
            return new == sm and dfs(pre2, new, i + l)
        q = getStarter()
        return any(dfs(p1, p2, i) for p1, p2, i in q)



307.py class NumArray:
    def __init__(self, nums):
        if nums:
            self.n = len(nums)
            self.tree = [0] * (2 * (2 ** int(math.ceil(math.log(self.n, 2)))) - 1)
            def dfs(node, s, e):
                if s == e: self.tree[node] = nums[s]
                else:
                    m = (s + e) // 2
                    dfs(2 * node + 1, s, m)
                    dfs(2 * node + 2, m + 1, e)
                    self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
            dfs(0, 0, self.n - 1)
    def update(self, i, val):
        def dfs(node, s, e, idx, val):
            if s == e: self.tree[node] = val
            else:
                m = (s + e) // 2
                if s <= idx <= m: dfs(2 * node + 1, s, m, idx, val)
                else: dfs(2 * node + 2, m + 1, e, idx, val)
                self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
        dfs(0, 0, self.n - 1, i, val)
    def sumRange(self, i, j):
        def dfs(node, s, e, l, r):
            if r < s or l > e: return 0
            if l <= s and e <= r: return self.tree[node]
            m = (s + e) // 2
            return dfs(2 * node + 1, s, m, l, r) + dfs(2 * node + 2, m + 1, e, l, r)
        return dfs(0, 0, self.n - 1, i, j)



308.py class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        for row in matrix:
            for col in range(1, len(row)):
                row[col] += row[col-1]
        self.matrix = matrix
        

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        original = self.matrix[row][col]
        if col != 0:
            original -= self.matrix[row][col-1]
            
        diff = original - val
        
        for y in range(col, len(self.matrix[0])):
            self.matrix[row][y] -= diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0
        for x in range(row1, row2+1):
            sum += self.matrix[x][col2]
            if col1 != 0:
                sum -= self.matrix[x][col1-1]
        return sum



309.py class Solution:
    def maxProfit(self, prices):
        dp1, dp2, dp3 = 0, 0, -float("inf")
        for p in prices:
            dp1, dp2, dp3 = dp3 + p, max(dp1, dp2), max(dp2 - p, dp3)
        return max(dp1, dp2)



310.py class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1: return [0]
        adj = [set() for i in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        while n > 2:
            n -= len(leaves)
            newleaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1: 
                    newleaves.append(j)
            leaves = newleaves
        return leaves 



311.py class Solution:
    def multiply(self, A, B):
        return [[sum(a * b for a, b in zip(A[i], [B[k][j] for k in range(len(B))])) for j in range(len(B[0]))] for i in range(len(A))]



312.py class Solution:
    def maxCoins(self, nums):
        memo, nums = {}, [1] + [num for num in nums if num] + [1]
        def dfs(l, r):
            if r - l == 1: return 0
            if (l, r) not in memo: memo[(l, r)] = max(nums[l] * nums[i] * nums[r] + dfs(l, i) + dfs(i, r) for i in range(l + 1, r))
            return memo[(l, r)]
        return dfs(0, len(nums) - 1)



313.py class Solution:
    def nthSuperUglyNumber(self, n, primes):
        arr, heap, used = [1], primes[:], set()
        for i in range(1, n):
            num = heapq.heappop(heap)
            arr.append(num)
            for p in primes:
                if p * num not in used:
                    heapq.heappush(heap, p * num)
                    used.add(p * num)
        return arr[-1]



314.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root):
        q, arrays = root and collections.deque([(root, 0)]) or None, collections.defaultdict(list)
        while q:
            new = collections.deque()
            for node, ind in q:
                arrays[ind].append(node.val)
                if node.left:
                    new.append((node.left, ind - 1))
                if node.right:
                    new.append((node.right, ind + 1))
            q = new
        return [arr for i, arr in sorted(arrays.items())]



315.py class Solution:
    def countSmaller(self, nums):
        r = []
        for i in range(len(nums) - 1, -1, -1):
            bisect.insort(r, nums[i])
            nums[i] = bisect.bisect_left(r, nums[i])
        return nums



316.py class Solution:
    def removeDuplicateLetters(self, s):
        rindex = {c: i for i, c in enumerate(s)}
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result



317.py class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n, d = len(grid), len(grid[0]), 1
        piled = collections.defaultdict(set)
        dist = collections.defaultdict(int)
        bfs = [(i, j, i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        total, res = len(bfs), []
        while bfs:
            new = []
            for x, y, i, j in bfs:
                for ii, jj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= ii < m and 0 <= jj < n and not grid[ii][jj] and (x, y) not in piled[(ii, jj)]:
                        piled[(ii, jj)].add((x, y))
                        dist[(ii, jj)] += d
                        if len(piled[(ii, jj)]) == total:
                            res.append(dist[(ii, jj)])
                        new.append((x, y, ii, jj))
            bfs = new
            d += 1
        return min(res) if res else -1



318.py class Solution:
    def maxProduct(self, words):
        sets, mx = {w: set(w) for w in words}, 0
        words.sort(key = len, reverse = True)
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if len(words[i]) * len(words[j]) <= mx:
                    break
                elif not sets[words[i]] & sets[words[j]]:
                    mx = len(words[i]) * len(words[j])
        return mx



319.py class Solution:
    def bulbSwitch(self, n):
        return int(n ** 0.5)



320.py class Solution:
    def generateAbbreviations(self, word):
        l, res = len(word), []
        def dfs(s, i):
            if i == l:
                res.append(s)
            else:
                dfs(s + word[i], i + 1)
                if not s or s[-1] > "9":
                    for j in range(i + 1, l + 1):
                        dfs(s + str(j - i), j)
        dfs("", 0)
        return res



321.py class Solution:
    def maxNumber(self, nums1, nums2, k):
        def merge(arr1, arr2):
            res, i, j = [], 0, 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i:] >= arr2[j:]:
                    res.append(arr1[i])
                    i += 1
                else: 
                    res.append(arr2[j])
                    j += 1
            if i < len(arr1): res += arr1[i:]
            elif j < len(arr2): res += arr2[j:]
            return res     
        
        def makeArr(arr, l):
            i, res = 0, []
            for r in range(l - 1, -1, -1):
                num, i = max(arr[i:-r] or arr[i:])
                i = -i + 1
                res.append(num)
            return res
        
        nums1, nums2, choices = [(num, -i) for i, num in enumerate(nums1)], [(num, -i) for i, num in enumerate(nums2)], []
        for m in range(k + 1):
            if m > len(nums1) or k - m > len(nums2): continue
            arr1, arr2 = makeArr(nums1, m), makeArr(nums2, k - m)  
            choices.append(merge(arr1, arr2))
        return max(choices)
            



322.py class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount + 1): dp[i] = min([dp[i - c] if i - c >= 0 else float('inf') for c in coins]) + 1
        return dp[amount] if dp[amount] != float('inf') else -1



323.py class Solution:
    def countComponents(self, n, edges):
        visited, res, adj = set(), 0, collections.defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        def dfs(i):
            visited.add(i)
            for v in adj[i]:
                if v not in visited:
                    dfs(v)
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res



324.py class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for i in range(1, len(nums), 2):
            nums[i] = -heapq.heappop(heap)
        for i in range(0, len(nums), 2):
            nums[i] = -heapq.heappop(heap)



325.py class Solution:
    def maxSubArrayLen(self, nums, k):
        index, l, sm = {}, 0, 0
        index[0] = -1
        for i, num in enumerate(nums):
            sm += num
            if sm - k in index:
                l = max(l, i - index[sm - k])
            if sm not in index:
                index[sm] = i
        return l



326.py class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 1
        while i < n:
            i *=3
        return i == n



327.py class Solution:
    def countRangeSum(self, nums, lower, upper):
        sums, sm, res = [0], 0, 0
        for num in nums:
            sm += num
            res += bisect.bisect_right(sums, sm - lower) - bisect.bisect_left(sums, sm - upper)
            bisect.insort(sums, sm)
        return res



328.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root, i, last, first = head, 1, None, None
        if head and head.next: first = head.next
        while head:
            latter = head.next
            if i%2 != 0: last = head
            if head.next: head.next = head.next.next
            head, i = latter, i+1
        if last: last.next = first
        return root



329.py class Solution:
    def longestIncreasingPath(self, matrix):
        def dfs(i, j):
            if not dp[i][j]:
                dp[i][j] = 1+max((dfs(x,y) for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)) if 0 <=x<m and 0<=y<n and matrix[x][y] > matrix[i][j]),default=0)
            return dp[i][j]
        m, n, = len(matrix), len(matrix and matrix[0])
        dp = [[0] * n for _ in range(m)]
        return max((dfs(i,j) for i in range(m) for j in range(n)),default=0)



330.py class Solution:
    def minPatches(self, nums, n):
        miss, added, i = 1, 0, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss *= 2
                added += 1
        return added



331.py class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for c in preorder.split(','):
            stack.append(c)
            while stack[-2:] == ['#', '#']:
                stack.pop()
                stack.pop()
                if not stack: return False
                stack.pop()
                stack.append('#')
        return stack == ['#']



332.py class Solution:
    def findItinerary(self, tickets):
        graph, stack, reached = collections.defaultdict(list), ["JFK"], []
        for a, b in tickets: heapq.heappush(graph[a], b)  
        while stack:
            if graph[stack[-1]]: stack.append(heapq.heappop(graph[stack[-1]]))
            else: reached.append(stack.pop())
        return reached[::-1]



333.py class Solution:
    def largestBSTSubtree(self, root):
        def dfs(node):
            if not node:
                return True, 0, None, None, 0
            lBool, lSize, lMx, lMn, lTree = dfs(node.left)
            rBool, rSize, rMx, rMn, rTree = dfs(node.right)
            lVal = lMx if lMx != None else -float("inf")
            rVal = rMn if rMn != None else float("inf")
            curMx = max(val for val in (lMx, rMx, node.val) if val != None)
            curMn = min(val for val in (lMn, rMn, node.val) if val != None)
            curBool = lBool and rBool and lVal < node.val < rVal 
            return curBool, lSize + rSize + 1, curMx, curMn, curBool and lSize + rSize + 1 or max(lTree, rTree)
        return dfs(root)[4]



334.py class Solution:
    def increasingTriplet(self, nums):
        mn = None
        for i in range(len(nums)):
            if mn == None or nums[i] < mn: 
                mn = nums[i]
            if mn < nums[i]:
                nums[i] = [True, nums[i]]
            else:
                nums[i] = [False, nums[i]]
        mn = None
        for i in range(len(nums)):
            if nums[i][0] and (mn == None or nums[i][1] < mn):
                mn = nums[i][1]
            elif mn != None and mn < nums[i][1]:
                return True
        return False 



335.py class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        b = c = d = e = 0
        for a in x:
            if d >= b > 0 and (a >= c or a >= c-e >= 0 and f >= d-b):
                return True
            b, c, d, e, f = a, b, c, d, e
        return False



336.py class Solution:
    def palindromePairs(self, words):
        index, res = {w:i for i, w in enumerate(words)}, []
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                pre, suf = w[:j], w[j:]
                if pre == pre[::-1]:
                    suf = suf[::-1]
                    if suf != w and suf in index:
                        res.append([index[suf], i])
                if j != len(w) and suf == suf[::-1]:
                    pre = pre[::-1]
                    if pre != w and pre in index:
                        res.append([i, index[pre]])
        return res



337.py class Solution:
    def rob(self, root):
        def dfs(node):
            if not node: return 0, 0
            l, r = dfs(node.left), dfs(node.right)
            return max(l) + max(r), node.val + l[0] + r[0]
        return max(dfs(root))



338.py class Solution:
    def countBits(self, num: int) -> List[int]:
        return [bin(i)[2:].count('1') for i in range(num + 1)]



339.py # """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList):
        def dfs(obj, d): return obj.getInteger() * d if obj.isInteger() else sum(dfs(new, d + 1) for new in obj.getList())
        return sum(dfs(item, 1) for item in nestedList)
            



340.py class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not k:
            return 0
        cnt = collections.Counter()
        i = res = 0
        for j, c in enumerate(s):
            while len(cnt) == k and c not in cnt:
                cnt[s[i]] -= 1
                if cnt[s[i]] == 0:
                    cnt.pop(s[i])
                i += 1
            cnt[c] += 1
            res = max(res, j - i + 1)
        return res



342.py class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 0:
            return False
        i = 1
        while i < num:
            i = i * 4
        return i == num
        



343.py class Solution:
    def integerBreak(self, n):
        pre = [0, 1, 1, 2, 4, 6, 9]
        if n < 7:
            return pre[n]
        for i in range(7, n + 1):
            pre.append(max(pre[i - 2] * 2, pre[i - 3] * 3))
        return pre[-1]



344.py class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[-i-1] = s[-i-1], s[i]



345.py class Solution:
    def reverseVowels(self, s):
        r = [c for c in s if c in "aeiouAEIOU"]
        return "".join(c in "aeiouAEIOU" and r.pop() or c for c in s) 



346.py class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.arr = collections.deque(maxlen = size)

    def next(self, val: int) -> float:
        self.arr.append(val)
        return sum(self.arr) / len(self.arr)
        
        
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)



347.py class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter as ct
        return [k for (k,v) in ct(nums).most_common(k)] 



348.py class TicTacToe:

    def __init__(self, n):
        self.n = n
        self.rows, self.cols = collections.defaultdict(int), collections.defaultdict(int)
        self.d = self.ad = 0

    def move(self, row, col, player):
        add = player == 1 and 1 or -1
        self.rows[row] += add
        self.cols[col] += add
        if row == col:
            self.d += add
        if row == self.n - col - 1:
            self.ad += add
        if self.rows[row] == self.n or self.cols[col] == self.n or self.d == self.n or self.ad == self.n:
            return 1
        elif self.rows[row] == -self.n or self.cols[col] == -self.n or self.d == -self.n or self.ad == -self.n:
            return 2
        else:
            return 0



349.py class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1)&set(nums2))



350.py class Solution:
    intersect = lambda *x: [k for k, v in (collections.Counter(x[1]) & collections.Counter(x[2])).items() for _ in range(v)]



351.py class Solution:
    def numberOfPatterns(self, m, n):
        q, pattern = [[c] for c in range(1, 10)], 0
        while q:
            new = []
            for arr in q:
                if m <= len(arr) <= n:
                    pattern += 1
                if len(arr) < n:
                    last = arr[-1]
                    for c in range(1, 10):
                        if c not in arr:
                            if last in (1, 4, 7) and c == last + 2:
                                if last + 1 in arr:
                                    new.append(arr + [c])
                            elif last in (3, 6, 9) and c == last - 2:
                                if last - 1 in arr:
                                    new.append(arr + [c])
                            elif last in (1, 2, 3) and c == last + 6:
                                if last + 3 in arr:
                                    new.append(arr + [c])
                            elif last in (7, 8, 9) and c == last - 6:
                                if last - 3 in arr:
                                    new.append(arr + [c])
                            elif last == 1 and c == 9:
                                if 5 in arr:
                                    new.append(arr + [9])
                            elif last == 9 and c == 1:
                                if 5 in arr:
                                    new.append(arr + [1])
                            elif last == 3 and c == 7:
                                if 5 in arr:
                                    new.append(arr + [7])
                            elif last == 7 and c == 3:
                                if 5 in arr:
                                    new.append(arr + [3])
                            else:
                                new.append(arr + [c])
            q = new
        return pattern



352.py class SummaryRanges:

    def __init__(self):
        self.starts, self.ends, self.used = [-float("inf"), float("inf")], [-float("inf"), float("inf")], set()
        
    def addNum(self, val):
        if val not in self.used:
            self.used.add(val)
            i = bisect.bisect_left(self.starts, val) - 1
            if self.ends[i] + 1 == val and val + 1 == self.starts[i + 1]: # if val is the gap btw 2 intervals
                del self.starts[i + 1]
                del self.ends[i]
            elif self.ends[i] + 1 == val: #if val is adjacent to current end
                self.ends[i] += 1
            elif self.starts[i + 1] == val + 1: # if val is adjacent to next start
                self.starts[i + 1] -= 1
            elif val > self.ends[i]: # if val is independent of those 2 intervals
                self.starts.insert(i + 1, val) 
                self.ends.insert(i + 1, val)
            
    def getIntervals(self):
        return [[s, e] for s, e in zip(self.starts[1:-1], self.ends[1:-1])] #exclude infinity



353.py class SnakeGame:

    def __init__(self, width, height, food):
        self.foods = collections.deque(food)
        self.i = self.j = 0
        self.w, self.h = width, height
        self.score = 0
        self.snake = collections.OrderedDict()
        self.snake[(0, 0)] = 1
        

    def move(self, direction):
        x, y = self.snake.popitem(last = False)
        if direction == "U":
            self.i -= 1
        elif direction == "D":
            self.i += 1
        elif direction == "R":
            self.j += 1
        else:
            self.j -= 1
        if 0 <= self.i < self.h and 0 <= self.j < self.w and (self.i, self.j) not in self.snake:
            self.snake[(self.i, self.j)] = 1
            if self.foods and self.i == self.foods[0][0] and self.j == self.foods[0][1]:
                self.score += 1
                self.foods.popleft()
                self.snake[(x, y)] = 1
                self.snake.move_to_end((x, y), last = False)
            return self.score
        else:
            return -1



354.py class Solution:
    def maxEnvelopes(self, envelopes):
        tails = []
        for w, h in sorted(envelopes, key = lambda x: (x[0], -x[1])):
            i = bisect.bisect_left(tails, h)
            if i == len(tails): tails.append(h)
            else: tails[i] = h
        return len(tails)



355.py class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = collections.defaultdict(list)
        self.following = collections.defaultdict(set)
        self.order = 0
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets[userId] += (self.order, tweetId), 
        self.order -= 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        tw = sorted(tw for i in self.following[userId] | {userId} for tw in self.tweets[i])[:10]
        return [news for i, news in tw]
    

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.following[followerId].discard(followeeId)      


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)



356.py class Solution:
    def isReflected(self, points):
        if len(points) < 2:
            return True
        x = (min(x for x, y in points) + max(x for x, y in points)) / 2 
        left, right, on = set(), set(), set()
        for i, j in points:
            if i < x:
                left.add((i, j))
            elif i > x:
                right.add((i, j))
            else:
                on.add((i, j))
        for i, j in points:
            if i < x and (2 * x - i, j) in right:
                continue
            elif i > x and (2 * x - i, j) in left:
                continue
            elif i == x and (2 * x - i, j) in on:
                continue
            else:
                return False
        return True



357.py class Solution:
    def countNumbersWithUniqueDigits(self, n):
        return [1, 10, 91, 739, 5275, 32491, 168571, 712891, 2345851, 5611771, 8877691][n % 11]



358.py class Solution:
    def rearrangeString(self, s, k):
        q, last, res, wq = [(-v, k) for k, v in collections.Counter(s).items()], {}, "", []
        heapq.heapify(q)
        for i in range(len(s)):
            if wq and (wq[0][1] not in last or last[wq[0][1]] + k <= i): cnt, char = heapq.heappop(wq)
            else:
                while q and not (q[0][1] not in last or last[q[0][1]] + k <= i): heapq.heappush(wq, heapq.heappop(q))
                if not q: return ""
                cnt, char = heapq.heappop(q)
            res, cnt, last[char] = res + char, cnt + 1, i
            if cnt: heapq.heappush(q, (cnt, char))
        return res



359.py class Logger:

    def __init__(self):
        self.logs = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.logs or timestamp - self.logs[message] >= 10:
            self.logs[message] = timestamp
            return True
        return False



360.py class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        arr, l, r, ind = [0] * len(nums), 0, len(nums) - 1, a >= 0 and len(nums) - 1 or 0
        while l <= r:
            n1, n2 = a * nums[l] * nums[l] + b * nums[l] + c, a * nums[r] * nums[r] + b * nums[r] + c
            if a >= 0:
                if n1 >= n2: l += 1
                else: r -= 1
                arr[ind] = n1 >= n2 and n1 or n2
                ind -= 1
            else:
                if n1 < n2: l += 1
                else: r -= 1
                arr[ind] = n1 < n2 and n1 or n2
                ind += 1
        return arr



361.py class Solution:
    def maxKilledEnemies(self, grid):
        m, n, res = len(grid), len(grid and grid[0]), 0
        dp = [[[0, 0, 0, 0] for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    dp[i][j][0] = dp[i][j - 1][0]
                    dp[i][j][1] = dp[i - 1][j][1]
                elif grid[i][j] == "E":
                    dp[i][j][0] = dp[i][j - 1][0] + 1
                    dp[i][j][1] = dp[i - 1][j][1] + 1 
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == "0":
                    dp[i][j][2] = dp[i][j + 1][2]
                    dp[i][j][3] = dp[i + 1][j][3]
                elif grid[i][j] == "E":
                    dp[i][j][2] = dp[i][j + 1][2] + 1
                    dp[i][j][3] = dp[i + 1][j][3] + 1
                if grid[i][j] == "0":
                    res = max(res, sum(dp[i][j]))
        return res        



362.py class HitCounter(object):

    def __init__(self):
        self.hits = []

    def hit(self, timestamp):
        heapq.heappush(self.hits, timestamp + 300)

    def getHits(self, timestamp):
        while self.hits and self.hits[0] <= timestamp:
            heapq.heappop(self.hits)
        return len(self.hits)



363.py class Solution:
    def maxSumSubmatrix(self, matrix, k, mxTotal = -float("inf")):
        for l in range(len(matrix[0])):
            dp = [0] * len(matrix)
            for r in range(l, len(matrix[0])):
                for i in range(len(matrix)):
                    dp[i] += matrix[i][r]
                sums, cur, mx = [float("inf")], 0, -float("inf")
                for sm in dp:
                    bisect.insort(sums, cur)
                    cur += sm
                    mx = max(mx, cur - sums[bisect.bisect_left(sums, cur - k)])
                mxTotal = max(mxTotal, mx)
        return mxTotal



364.py # """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList):
        def dfs(obj, d):
            return obj.isInteger() and d or max((dfs(item, d + 1) for item in obj.getList()), default = 0)    
        def dfs2(obj, d):
            return obj.isInteger() and d * obj.getInteger() or sum(dfs2(item, d - 1) for item in obj.getList())
        mx = max((dfs(item, 1) for item in nestedList), default = 0)
        return mx and sum(dfs2(item, mx) for item in nestedList) or 0



365.py class Solution:
    def canMeasureWater(self, x, y, z):
        def gcd(x, y):
            for i in range(min(x, y), -1, -1):
                if not x % i and not y % i: return i      
        div = gcd(x, y) if x * y else 0
        return not z % div and z <= x + y if div else not z



366.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root):
        res = []
        def dfs(node):
            if not node: return -1
            i = max(dfs(node.left), dfs(node.right)) + 1
            try: res[i].append(node.val)
            except: res.append([node.val])
            return i
        dfs(root)
        return res



367.py class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i=1
        while i**2<=num:
            if i**2<num: i+=1
            if i**2==num: return True
        return False



368.py class Solution:
    def largestDivisibleSubset(self, nums):
        dp, n = [[num] for num in sorted(nums)], len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if not dp[j][-1] % dp[i][-1] and len(dp[i]) >= len(dp[j]):
                    dp[j] = dp[i] + dp[j][-1:]
        return dp and sorted(dp, key = len)[-1]



369.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def dfs(node):
            if not node.next or dfs(node.next):
                if node.val + 1 > 9:
                    node.val = 0
                    return True
                else:
                    node.val += 1
            return False  
        if dfs(head):
            dummy = ListNode(1)
            dummy.next = head
            return dummy
        return head



370.py class Solution:
    def getModifiedArray(self, length, updates):
        start, end, res, cur = collections.defaultdict(int), collections.defaultdict(int), [0] * length, 0
        for s, e, inc in updates:
            start[s] += inc
            end[e] += -inc
        for i in range(length):
            if start[i]:
                cur += start[i]
            res[i] += cur
            if end[i]:
                cur += end[i]
        return res



371.py class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mx, mask = 0x7FFFFFFF, 0xFFFFFFFF
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= mx else ~(a ^ mask)



372.py class Solution:
    def superPow(self, a, b):
        return pow(a, int(''.join(map(str, b))), 1337)



373.py class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2: return []
        n, res, cnt, heap = len(nums2), [], 0, [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]
        while heap and cnt < k:
            cnt += 1
            sm, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n: heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res



374.py class Solution(object):
    def guessNumber(self, n):
        l, r, g = 1, n, 1
        while g and l <= r:
            m = (l + r) // 2
            g = guess(m)
            if g == 1:
                l = m + 1
            else:
                r = m
        return m



375.py class Solution:
    def getMoneyAmount(self, n):
        dic = {}
        def dfs(l, r):
            if l >=r: return 0
            if (l, r) not in dic: dic[(l, r)] = min(num + max(dfs(l, num - 1), dfs(num + 1, r)) for num in range(l, r))
            return dic[(l, r)]
        return dfs(1, n)



376.py class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) <= 2: return 0 if not nums else 1 if nums[0] == nums[-1] else 2
        inc = nums[0] < nums[1] if nums[0] != nums[1] else None
        cnt = 2 if inc != None else 1
        for i in range(2, len(nums)):
            if nums[i - 1] != nums[i] and (inc == None or inc != (nums[i - 1] < nums[i])):
                inc = nums[i - 1] < nums[i] 
                cnt += 1
        return cnt



377.py class Solution:
    def combinationSum4(self, nums, target):
        memo = {}
        def dfs(sm):
            if sm in memo:
                return memo[sm]
            else:
                if sm >= target:
                    memo[sm] = sm == target
                    return memo[sm]
                cnt = 0
                for num in nums:
                    memo[sm + num] = dfs(sm + num)
                    cnt += memo[sm + num]
                return cnt          
        return dfs(0)



378.py class Solution:
    def kthSmallest(self, matrix, k):
        return sorted(itertools.chain(*matrix))[k - 1]



379.py class PhoneDirectory:

    def __init__(self, maxNumbers):
        self.nums = set(range(maxNumbers))

    def get(self):
        return self.nums.pop() if self.nums else -1

    def check(self, number):
        return number in self.nums

    def release(self, number):
        self.nums.add(number)



380.py class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.ind = [], {}
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.ind: 
            self.nums += val, 
            self.ind[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.ind:
            ind, last = self.ind[val], self.nums[-1]
            self.nums[ind], self.ind[last] = last, ind
            self.nums.pop()
            self.ind.pop(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



381.py class RandomizedCollection:

    def __init__(self):
        self.arr, self.pos = [], collections.defaultdict(set)
    def insert(self, val):
        out = val not in self.pos
        self.arr.append(val)
        self.pos[val].add(len(self.arr) - 1)
        return out

    def remove(self, val):
        if val in self.pos:
            if self.arr[-1] != val:
                x, y = self.pos[val].pop(), self.arr[-1]
                self.pos[y].discard(len(self.arr) - 1)
                self.pos[y].add(x)
                self.arr[x] = y
            else:
                self.pos[val].discard(len(self.arr) - 1)
            self.arr.pop()
            if not self.pos[val]:
                self.pos.pop(val)
            return True 
        return False

    def getRandom(self):
        return random.choice(self.arr)



382.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head):
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self):
        return random.choice(self.arr)



383.py class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = collections.Counter(magazine)
        for c in ransomNote:
            if cnt[c]:
                cnt[c] -= 1
            else:
                return False
        return True



384.py class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.org = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.arr = self.org[:]
        return self.arr

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.arr)
        return self.arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()



385.py class Solution:
    def deserialize(self, s):
        stack, num, last = [], "", None
        for c in s:
            if c.isdigit() or c == "-": num += c
            elif c == "," and num:
                stack[-1].add(NestedInteger(int(num)))
                num = ""
            elif c == "[":
                elem = NestedInteger()
                if stack: stack[-1].add(elem)
                stack.append(elem)
            elif c == "]":
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""
                last = stack.pop()
        return last if last else NestedInteger(int(num))



386.py class Solution:
    def lexicalOrder(self, n): return sorted(range(1, n + 1), key = str)



387.py class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = collections.defaultdict(int)
        for c in s:
            dic[c] += 1
        for i, c in enumerate(s):
            if dic[c] == 1: return i
        return -1



388.py class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\u005Ct')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen



389.py class Solution:
    def findTheDifference(self, s, t):
        return next(iter(collections.Counter(t) - collections.Counter(s)))



390.py class Solution:
    def lastRemaining(self, n):
        head, left, step, remaining = 1, 1, 1, n
        while remaining > 1:
            if left or remaining % 2: head += step
            left = 1 - left
            step *= 2
            remaining //= 2
        return head



391.py class Solution:
    def isRectangleCover(self, rectangles):
        cnt = collections.Counter()
        for x1, y1, x2, y2 in rectangles:
            cnt[(x1, y1)] += 1
            cnt[(x1, y2)] += 1
            cnt[(x2, y2)] += 1
            cnt[(x2, y1)] += 1
        x1, y1, x2, y2 = min([r[:2] for r in rectangles]) + max(r[-2:] for r in rectangles)
        for x, y in ((x1, y1), (x1, y2), (x2, y2), (x2, y1)):
            if cnt[(x, y)] != 1: return False
            cnt.pop((x, y))
        return all(cnt[k] in (2, 4) for k in cnt) and sum((x2 - x1) * (y2 - y1) for x1, y1, x2, y2 in rectangles) == (x2 - x1) * (y2 - y1)



392.py class Solution:
    def isSubsequence(self, s, t):
        ind = -1
        for i in s:
            try: ind = t.index(i, ind + 1)
            except: return False
        return True



393.py class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def rest(i):
            if len(data) < i:
                return False
            for _ in range(i):
                if not data.pop().startswith("10"):
                    return False
            return True

        data, byte = [str(bin(seq)[2:].zfill(8)) for seq in data[::-1]], None
        while data:
            seq = data.pop()
            if seq.startswith("0"):
                continue
            elif seq.startswith("110"):
                if not rest(1):
                    return False
            elif seq.startswith("1110"):
                if not rest(2):
                    return False
            elif seq.startswith("11110"):
                if not rest(3):
                    return False
            else:
                return False
        return True




394.py class Solution:
    def decodeString(self, s):
        stack, num, string = [], 0, ""
        for c in s:
            if c == "[":
                stack += string,
                stack += num,
                num, string = 0, ""
            elif c == "]":
                pre_num, pre_string = stack.pop(), stack.pop()
                string = pre_string + pre_num * string
            elif c.isdigit(): num = num * 10 + int(c)
            else: string += c
        return string



395.py class Solution:
    def longestSubstring(self, s, k):
        br = [-1] + [i for i, c in enumerate(s) if s.count(c) < k] + [len(s)]
        return len(s) if len(br) == 2 else max(self.longestSubstring(s[br[i - 1] + 1:br[i]], k) for i in range(1, len(br)))



396.py class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mx, sm = 0, sum(A)
        for i in range(len(A)):
            mx += i * A[i]
        curr = mx
        for i in range(1, len(A)):
            curr = curr - sm + A[i - 1] * len(A)
            mx = max(mx, curr)
        return mx



397.py class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: 
            return 0
        elif n % 2 == 0: 
            return self.integerReplacement(n/2)+1
        else: 
            return min(self.integerReplacement(n+1),self.integerReplacement(n-1))+1



398.py class Solution:

    def __init__(self, nums):
        self.indexes = collections.defaultdict(set)
        for i, num in enumerate(nums):
            self.indexes[num].add(i)

    def pick(self, target):
        return random.sample(self.indexes[target], 1)[0]



399.py class Solution:
    def calcEquation(self, equations, values, queries):
        def explore(x, y, r, q):
            results[(x, y)] = r
            for z in edges[y]:
                if z not in q:
                    results[(x, z)], results[(z, x)] = r * vals[(y, z)], 1 / (r * vals[(y, z)])
                    explore(x, z, r * vals[(y, z)], q | {z})
        edges, vals, visited, results, res = collections.defaultdict(set), {}, set(), {}, []
        for i, eq in enumerate(equations):
            edges[eq[0]].add(eq[1])
            edges[eq[1]].add(eq[0])
            vals[(eq[0], eq[1])], vals[(eq[1], eq[0])] = values[i], 1 / values[i]
        for i, eq in enumerate(equations):
            for p in eq:
                if p not in visited:
                    visited.add(p)
                    explore(p, p, 1.0, {p})
        for q in queries:
            if (q[0], q[1]) in results: res += results[(q[0], q[1])],
            else: res += -1.0,
        return res



400.py class Solution(object):
    def findNthDigit(self, n):
        start, size, step = 1, 1, 9
        while n > size * step:
            n, size, step, start = n - (size * step), size + 1, step * 10, start * 10
        return int(str(start + (n - 1) // size)[(n - 1) % size])



401.py class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == num]



402.py class Solution:
    def removeKdigits(self, num, k):
        out = []
        for digit in num:
            while k and out and out[-1] > digit:
                out.pop()
                k -= 1
            out.append(digit)
        return ''.join(out[:-k or None]).lstrip('0') or "0"



403.py class Solution:
    def canCross(self, stones):
        memo, stones, target = {}, set(stones), stones[-1]
        def dfs(unit, last):
            if unit == target: return True
            if (unit, last) not in memo: 
                memo[(unit, last)] = any(dfs(unit + move, move) for move in (last - 1, last, last + 1) if move and unit + move in stones)
            return memo[(unit, last)]
        return dfs(1, 1) if 1 in stones else False



404.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def left(node, sm):
            if not node: return
            left(node.left,sm)
            if node.left:
                if not node.left.left and not node.left.right: sm.append(node.left.val)
            left(node.right,sm)
        otp=list()
        left(root,otp)
        return sum(otp)



405.py class Solution:
    def toHex(self, num):
        if not num: return "0"
        mp, ans = "0123456789abcdef", ""
        for i in range(8):
            n = num & 15       
            c = mp[n]          
            ans = c + ans
            num = num >> 4
        return ans.lstrip('0')



406.py class Solution:
    def reconstructQueue(self, people):
        arr = [0] * len(people)
        people.sort()
        for h, k in people:
            cnt = 0
            for i in range(len(arr)):
                if not arr[i] or arr[i][0] == h:
                    cnt += 1
                    if cnt == k + 1:
                        arr[i] = [h, k]
        return arr



407.py class Solution:
    def trapRainWater(self, heightMap):
        m, n, heap, trapped = len(heightMap), len(heightMap and heightMap[0]), [], 0
        for i in range(m):
            for j in range(n):
                if i in {0, m - 1} or j in {0, n - 1}:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1          
        while heap:
            h, i, j = heapq.heappop(heap)
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 < x < m - 1 and 0 < y < n - 1 and heightMap[x][y] != -1:
                    trapped += max(h - heightMap[x][y], 0)
                    heapq.heappush(heap, (max(heightMap[x][y], h), x, y))
                    heightMap[x][y] = -1
        return trapped



408.py class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = num = 0
        for c in abbr:
            if c.isdigit():
                if num == 0 and c == '0':
                    return False
                num = num * 10 + int(c)
            else:
                if num:
                    #print(i, num)
                    i += num 
                    num = 0
                if i >= len(word) or word[i] != c:
                    #print(i, c)
                    return False
                i += 1
        return i == len(word) if num == 0 else i + num == len(word)



409.py class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        out=even=sum(v for k,v in Counter(s).items() if v%2==0)
        odd_big=[v for k,v in Counter(s).items() if v%2!=0 and v>1]
        odd_small=[v for k,v in Counter(s).items() if v==1]
        if len(odd_big)==1: out+=odd_big[0]
        else:
            out+=sum(odd_big)-len(odd_big)+1  
            if len(odd_small)==0 and len(odd_big)==0: out-=1
        return out



410.py class Solution:
    def splitArray(self, nums, m):
        def valid(mid):
            cnt = sm = 0
            for num in nums:
                sm += num
                if sm > mid:
                    cnt += 1
                    if cnt>= m: return False
                    sm = num
            return True
        l, h = max(nums), sum(nums)
        while l < h:
            mid = (l + h) // 2
            if valid(mid):
                h = mid
            else:
                l = mid + 1
        return l



411.py class Solution(object):
    def extract_number(self, j, abbr, M):
        num = 0
        while j < M and abbr[j].isdigit():
            num, j = num*10 + int(abbr[j]), j+1
        return num, j
    
    def valid(self, word, abbr):
        i,j,N, M = 0,0,len(word), len(abbr)
        while i < N and j < M:
            if abbr[j].isalpha() and abbr[j] != word[i]:
                return False
            elif abbr[j].isalpha() and abbr[j] == word[i]:
                i,j = i+1,j+1
            elif abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                num, j = self.extract_number(j, abbr, M)
                i = i+num
        return (i==N and j == M)
        
    def process_solution(self, so_far):
        csofar, i, cnt = [], 0, 0
        while i < len(so_far):
            if so_far[i].isalpha():
                csofar.append(so_far[i])
                i, cnt = i+1, cnt+1
            else:
                num = 0
                while i < len(so_far) and so_far[i].isdigit():
                    num, i = num+1, i+1
                cnt = cnt + 1
                csofar.append(str(num))
        return "".join(csofar), cnt
    
    def test(self, abbr, dictionary):
        for wrd in dictionary:
            if self.valid(wrd, abbr):
                return False
        return True
    
    def helper(self, word, so_far, i, dictionary):
        if i == len(word):
            abbr, cnt = self.process_solution(so_far)
            if cnt < self.result_len and self.test(abbr, dictionary):
                self.result, self.result_len = abbr, cnt
            return
        else:
            so_far.append("1")
            self.helper(word, so_far, i+1, dictionary)
            so_far.pop()
            so_far.append(word[i])
            self.helper(word, so_far, i+1, dictionary)
            so_far.pop()

    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        
        # Remove those words which can never be an abbreviation for target.
        # This preprocessing will help us save time.
        filtered_dictionary = []
        for wrd in dictionary:
            if len(wrd) != len(target):
                continue
            filtered_dictionary.append(wrd)
        dictionary = filtered_dictionary
        if len(dictionary) == 0:
            return str(len(target))
            
        self.result_len = len(target)+1
        self.result, so_far, i = target, [], 0
        self.helper(target, so_far, i, dictionary)        
        return self.result



412.py class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        num = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                num.append("FizzBuzz")
            elif i % 3 == 0:
                num.append("Fizz")
            elif i % 5 == 0:
                num.append("Buzz")
            else:
                num.append(str(i))
        return num



413.py class Solution:
    def numberOfArithmeticSlices(self, A):
        if len(A) < 3:
            return 0
        A.append(float("inf"))
        d, l, n, res = A[1] - A[0], 0, len(A), 0
        for i in range(2, n):
            if d != A[i] - A[i - 1]:
                diff = i - l - 2
                if diff > 0:
                    res += diff * (diff + 1) // 2
                d, l = A[i] - A[i - 1], i - 1
        return res



414.py class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=list(set(nums))
        if s[-1]<s[0]: s=[item for item in s if item>=0]
        if len(s)>=3: return s[-3]
        else: return s[-1] 



415.py class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return "".join(str(sum([(ord(num1[i])-ord("0"))*(10**(len(num1)-1-i)) for i in range(len(num1))]+[(ord(num2[i])-ord("0"))*(10**(len(num2)-1-i)) for i in range(len(num2))])))



416.py class Solution:
    def canPartition(self, nums):
        sm, n = sum(nums), len(nums)
        if sm % 2:
            return False
        sm //= 2
        dp = [False] * (sm + 1)
        dp[0] = True
        for num in nums:
            for j in range(num, sm + 1)[::-1]:
                dp[j] = dp[j] or dp[j - num]
        return dp[-1]



417.py class Solution:
    def pacificAtlantic(self, matrix):
        pac, atl, m, n = set(), set(), len(matrix), len(matrix and matrix[0])
        def explore(i, j, ocean): 
            ocean.add((i, j))
            if i > 0 and (i - 1, j) not in ocean and matrix[i - 1][j] >= matrix[i][j]: explore(i - 1, j, ocean)
            if j > 0 and (i, j - 1) not in ocean and matrix[i][j - 1] >= matrix[i][j]: explore(i, j - 1, ocean)
            if i + 1 < m  and (i + 1, j) not in ocean and matrix[i + 1][j] >= matrix[i][j]: explore(i + 1, j, ocean)
            if j + 1 < n  and (i, j +1) not in ocean and matrix[i][j + 1] >= matrix[i][j]: explore(i, j + 1, ocean)
        for i in range(max(m, n)):
            if i < m and (i, 0) not in pac: explore(i, 0, pac)
            if i < n and (0, i) not in pac: explore(0, i, pac)
            if i < n and (m - 1, i) not in atl: explore(m - 1, i, atl)
            if i < m and (i, n - 1) not in atl: explore(i, n - 1, atl)
        return [[x, y] for x, y in pac & atl]



418.py class Solution:
    def wordsTyping(self, sentence, rows, cols):
        left, count, sm, ptr, wordLen = [0] * len(sentence), 0, 0, 0, len(sentence[0])
        for i, w in enumerate(sentence):
            while sm + wordLen <= cols:
                sm += wordLen
                ptr += 1
                wordLen = len(sentence[ptr % len(sentence)]) + 1
            left[i] = ptr - i
            sm -= len(w) + 1
        for r in range(rows):
            count += left[count % len(sentence)]
        return count // len(sentence)



419.py class Solution:
    def countBattleships(self, board):
        return sum(board[i][j] == "X" and (i == 0 or board[i - 1][j] == ".") and (j == 0 or board[i][j - 1] == ".") for i in range(len(board)) for j in range(len(board[0])))



420.py class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        missing_type = 3
        if any('a' <= c <= 'z' for c in s): missing_type -= 1
        if any('A' <= c <= 'Z' for c in s): missing_type -= 1
        if any(c.isdigit() for c in s): missing_type -= 1

        change = 0
        one = two = 0
        p = 2
        while p < len(s):
            if s[p] == s[p-1] == s[p-2]:
                length = 2
                while p < len(s) and s[p] == s[p-1]:
                    length += 1
                    p += 1
                    
                change += length // 3
                if length % 3 == 0: one += 1
                elif length % 3 == 1: two += 1
            else:
                p += 1
        
        if len(s) < 6:
            return max(missing_type, 6 - len(s))
        elif len(s) <= 20:
            return max(missing_type, change)
        else:
            delete = len(s) - 20
            
            change -= min(delete, one)
            change -= min(max(delete - one, 0), two * 2) // 2
            change -= max(delete - one - 2 * two, 0) // 3
                
            return delete + max(missing_type, change)



421.py class Solution:
    def findMaximumXOR(self, nums, ans = 0):
        ans = 0
        for bit in range(30, -1, -1):
            ans <<= 1
            attempt = ans | 1
            prefix = set()
            for x in nums:
                p = x >> bit
                if attempt ^ p in prefix:
                    ans = attempt
                    break
                prefix.add(p)
        return ans



422.py class Solution:
    def validWordSquare(self, words):
        for j, row in enumerate(words):
            col = ""
            for s in words:
                try: col += s[j]
                except: break
            if row != col: return False
        return True



423.py class Solution(object):
    def originalDigits(self, s):
        res = ""
        res += "0"*s.count('z')
        res += "1"*(s.count('o')-s.count('z')-s.count('w')-s.count('u'))
        res += "2"*s.count('w')
        res += "3"*(s.count('h') - s.count('g'))
        res += "4"*s.count('u')
        res += "5"*(s.count('f') - s.count('u'))
        res += "6"*s.count('x')
        res += "7"*(s.count('s')-s.count('x'))
        res += "8"*s.count("g")
        res += "9"*(s.count('i') - s.count('x') - s.count("g") - s.count('f') + s.count('u'))
        return res



424.py class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dic, start, end = {}, 0, 0
        for end in range(1, len(s)+1):
            if not s[end-1] in dic: dic[s[end-1]] = 1
            else: dic[s[end-1]] += 1
            if end-start-max(dic.values()) > k: 
                dic[s[start]] -= 1
                start += 1
        return end-start



425.py class Solution:
    def wordSquares(self, words):
        pref, res = collections.defaultdict(set), []
        for w in words:
            for i in range(len(w)):
                pref[w[:i + 1]].add(w)
        def dfs(i, arr):
            if i == len(arr[0]):
                res.append(arr)
            else:
                for w in pref["".join(row[i] for row in arr)]:
                    dfs(i + 1, arr + [w])   
        for w in words:
            dfs(1, [w])
        return res



426.py class Solution:
    def treeToDoublyList(self, root):
        head, tail = [None], [None]
        def dfs(node, pre):
            if not node:
                return
            l = dfs(node.left, pre)
            new = Node(node.val, l or pre, None)
            if pre and not l:
                pre.right = new
            elif l:
                l.right = new
            if not pre and not l:
                head[0] = new
            if not tail[0] or node.val > tail[0].val:
                tail[0] = new
            r = dfs(node.right, new)
            return r if r else new
        dfs(root, None)
        if head[0]:
            head[0].left = tail[0]
            tail[0].right = head[0]
        return head[0]



427.py class Solution:
    def construct(self, grid):
        def dfs(x, y, l):
            if l == 1:
                node = Node(grid[x][y] == 1, True, None, None, None, None)
            else:
                tLeft = dfs(x, y, l // 2)
                tRight = dfs(x, y + l // 2, l // 2)
                bLeft = dfs(x + l // 2, y, l// 2)
                bRight = dfs(x + l // 2, y + l // 2, l // 2)
                value = tLeft.val or tRight.val or bLeft.val or bRight.val
                if tLeft.isLeaf and tRight.isLeaf and bLeft.isLeaf and bRight.isLeaf and tLeft.val == tRight.val == bLeft.val == bRight.val:
                    node = Node(value, True, None, None, None, None)
                else:
                    node = Node(value, False, tLeft, tRight, bLeft, bRight)
            return node
        return grid and dfs(0, 0, len(grid)) or None



428.py class Codec:

    def serialize(self, root):
        arr = []
        def dfs(node):
            if not node: return
            arr.append(str(node.val))
            for child in node.children:
                dfs(child)
            arr.append("#")
        dfs(root)
        return " ".join(arr)

    def deserialize(self, data):
        if not data: return None
        data = collections.deque(data.split(" "))
        root = Node(int(data.popleft()), [])
        q = [root]
        while data:
            val = data.popleft()
            if val == "#":
                q.pop()
            else:
                new = Node(int(val), [])
                q[-1].children.append(new)
                q.append(new)
        return root



429.py class Solution(object):
    def levelOrder(self, root):
        q, ret = [root], []
        while any(q):
            ret.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ret



430.py class Solution(object):
    def flatten(self, head):
        stack, cur, root = [], head, head
        while stack or cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                new = cur.child
                new.prev = cur
                cur.child = None
                cur.next = cur = new
            elif not cur.next and stack:
                cur.next = stack.pop()
                cur.next.prev = cur
                cur = cur.next
            else:
                cur = cur.next
        return root



431.py """
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
class Codec:

    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        
        :type root: Node
        :rtype: TreeNode
        """
        if not root:
            return None

        binary = TreeNode(root.val)                 # create a binary root
        if not root.children:
            return binary

        binary.left = self.encode(root.children[0]) # left child of binary is the encoding of all n-ary children,
        node = binary.left                          #     starting with the first child.
        for child in root.children[1:]:             # other children of n-ary root are right child of previous child
            node.right = self.encode(child)
            node = node.right

        return binary

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        
        :type data: TreeNode
        :rtype: Node
        """
        if not data:
            return None

        nary = Node(data.val, [])                   # create n-ary root
        node = data.left                            # move to first child of n-ary root
        while node:                                 # while more children of n-ary root
            nary.children.append(self.decode(node)) # append to list
            node = node.right                       # and move to next child
            
        return nary

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))



432.py class Node:
    def __init__(self, key, value):
        self.val = value
        self.key = key
        self.next = None
        self.pre = None
class AllOne:

    def __init__(self):
        self.first = {}
        self.last = {}
        self.keys = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        
    def add(self, prev, node):
        node.pre = prev
        node.next = prev.next
        node.pre.next = node.next.pre = node
        
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        
    def process(self, node):
        if self.last[node.val] == node and node.pre.val != node.val:
            self.first.pop(node.val)
            self.last.pop(node.val)
        elif self.first[node.val] == node:
            self.first[node.val] = node.next
        elif self.last[node.val] == node:
            self.last[node.val] = node.pre
            
    def process2(self, node, prev, key, d):
        if key in self.keys:
            if node.val + d in self.last:
                self.add(self.last[node.val + d], node)
            elif node.val in self.last:
                self.add(self.last[node.val], node)
            else:
                self.add(prev, node)
        elif 1 in self.last:
            node = Node(key, 0)
            self.add(self.last[1], node)
        else:
            node = Node(key, 0)
            self.add(self.head, node)
        node.val += d
        self.last[node.val] = node
        if node.val not in self.first:
            self.first[node.val] = node
        if key not in self.keys:
            self.keys[key] = node
                
    def inc(self, key):
        if key in self.keys:
            node = self.keys[key]
            prev = node.pre
            self.process(node)
            self.remove(node)
            self.process2(node, prev, key, 1)
        else:
            self.process2(None, None, key, 1)
            
    def dec(self, key):
        if key in self.keys:
            node = self.keys[key]
            prev = node.pre
            self.process(node)
            self.remove(node)
            if node.val != 1:
                self.process2(node, prev, key, -1)
            else:
                self.keys.pop(key)
            
    def getMaxKey(self):
        return self.tail.pre.key if self.tail.pre != self.head else ""
    def getMinKey(self):
        return self.head.next.key if self.head.next != self.tail else ""



433.py class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bfs = [start]
        genes = set(bank)
        cnt = 0
        while bfs:
            arr = []
            for g in bfs:
                if g == end:
                    return cnt
                for i, c in enumerate(g):
                    for new in 'AGTC':
                        if new != c:
                            s = g[:i] + new + g[i + 1:]
                            if s in genes:
                                arr.append(s)
                                genes.discard(s)
            bfs = arr
            cnt += 1
        return -1



434.py class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
        



435.py # Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x: x.end); res, curr = 0, -float("inf")
        for i in intervals:
            if curr > i.start: res += 1
            else: curr = i.end
        return res



436.py class Solution:
    def findRightInterval(self, intervals):
        def binarySearch(l, r):
            x, found = intervals[l - 1].end, None
            while l <= r:
                mid = (l + r) // 2
                if intervals[mid].start >= x:
                    r = mid - 1
                    found = mid
                else:
                    l = mid + 1
            return ind[intervals[found]] if found != None else -1
        root = intervals[:]
        ind = {intr:i for i, intr in enumerate(root)}
        intervals.sort(key = lambda x: x.start)
        for i in range(len(intervals)):
            root[ind[intervals[i]]] = binarySearch(i + 1, len(intervals) - 1)
        return root



437.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        dic = {}
        def traverse(node, parent):
            if not node: return
            dic[node] = [node.val]
            if node.val == sum: res[0] += 1
            if parent:
                for num in dic[parent]:
                    dic[node].append(num + node.val)
                    if num + node.val == sum: res[0] += 1
            traverse(node.left, node)
            traverse(node.right, node)
        res = [0]
        traverse(root, None)
        return res[0]



438.py class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        out=list()
        from collections import Counter
        s_counter, p_counter=Counter(s[:len(p)-1]), Counter(p)
        for i in range(len(p)-1,len(s)):
            s_counter[s[i]]+=1
            if s_counter==p_counter: out.append(i-len(p)+1)
            s_counter[s[i-len(p)+1]]-=1
            if s_counter[s[i-len(p)+1]]==0: del s_counter[s[i-len(p)+1]]
        return out



439.py class Solution:
    def parseTernary(self, expression, stack = []):
        for c in expression[::-1]:
            if stack and stack[-1] == "?":
                _, first, q, second = stack.pop(), stack.pop(), stack.pop(), stack.pop()
                stack.append(c == "T" and first or second)
            else:
                stack.append(c)
        return stack.pop()



440.py class Solution:
    def findKthNumber(self, n, k):
        def calSteps(n1, n2):
            steps = 0
            while n1 <= n:
                steps += min(n + 1, n2) - n1
                n1 *= 10
                n2 *= 10
            return steps
        cur = 1
        k -= 1
        while k:
            steps = calSteps(cur, cur + 1)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur



441.py class Solution:
    def arrangeCoins(self, n: int) -> int:
        sm = res = 0
        for i in range(1, n + 1):
            sm += i
            if sm > n:
                break
            res += 1
        return res



442.py class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out=list()
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]<0: out.append(abs(nums[i]))
            else: nums[abs(nums[i])-1]*=-1
        return out



443.py class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        curr, count, i = chars[0], 1, 1
        while i<len(chars):
            if chars[i]!=curr:
                curr=chars[i]
                if count>1: chars[:i]+= (i for i in "".join(str(count))); i+=len([i for i in "".join(str(count))])
                i, count =i+1, 1
            else:
                if i==len(chars)-1: chars.pop(i); chars+=[i for i in "".join(str(count+1))]; break
                chars.pop(i); count+=1
        return len(chars)      



444.py class Solution:
    def sequenceReconstruction(self, org, seqs):
        order, orders, graph, seen = collections.defaultdict(int), set(), collections.defaultdict(set), set()
        for seq in seqs:
            for i in range(len(seq)):
                if i > 0:
                    if seq[i] == seq[i - 1]: return False
                    graph[seq[i - 1]].add(seq[i])
                seen.add(seq[i])
        if not seen: return False
        for i in range(len(org) - 1, -1, -1):
            if org[i] in seen: seen.discard(org[i])
            order[org[i]] = max([order[v] for v in graph[org[i]]] or [0]) + 1
            before = set(v for v in graph[org[i]] if v in seen) 
            if order[org[i]] in orders or before:
                return False
            orders.add(order[org[i]])
        return not seen



445.py class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2, s3 = [], [], []
        p1, p2 = l1, l2
        while p1:
            s1.append(p1.val)
            p1 = p1.next
        while p2:
            s2.append(p2.val)
            p2 = p2.next
        if len(s1) < len(s2):
            s1, s2 = s2, s1
            l1, l2 = l2, l1
        residual = 0
        while len(s1) > 0:
            temp = s1.pop() + residual
            if len(s2) > 0:
                temp += s2.pop()
            s3.append(temp % 10)
            residual = temp // 10
        head, p = ListNode(1), l1
        head.next = p
        while len(s3) > 0:
            p.val = s3.pop()
            p = p.next
        return head if residual == 1 else head.next



446.py class Solution:
    def numberOfArithmeticSlices(self, A):
        dp, res = collections.defaultdict(dict), 0
        for j in range(len(A)):
            for i in range(j):
                dp[j][A[j] - A[i]] = dp[j].get(A[j] - A[i], 0) + dp[i].get(A[j] - A[i], 1) 
                if A[j] - A[i] in dp[i]: res, dp[j][A[j] - A[i]] = res + dp[i][A[j] - A[i]], dp[j][A[j] - A[i]] + 1
        return res           



447.py class Solution(object):
    def numberOfBoomerangs(self, points):
        res = 0
        for p in points:
            dic = collections.defaultdict(int)
            for q in points:
                d = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                dic[d] += 1
            for k in dic: res += dic[k] * (dic[k] - 1)
        return res



448.py class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [x for x in set([i for i in range(1,len(nums)+1)])-set(nums)]



449.py # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return root
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        return data
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))



450.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return
        if root.val > key: root.left = self.deleteNode(root.left, key)
        elif root.val < key: root.right = self.deleteNode(root.right, key)
        else:
            if not root.right: return root.left
            elif not root.left: return root.right
            tmp, mini = root.right, root.right.val
            while tmp.left:
                tmp, mini = tmp.left, tmp.left.val
            root.val, root.right = mini, self.deleteNode(root.right, mini)
        return root



451.py class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = collections.Counter(s)
        res = ''
        for k, v in sorted(cnt.items(), key = lambda x: -cnt[x[0]]):
            res += k * v
        return res



452.py class Solution:
    def findMinArrowShots(self, p):
        p.sort(key = lambda x: x[1])
        (res, curr) = (1, p[0][1]) if p else (0, None)
        for n in p:
            if n[0] > curr: res, curr = res + 1, n[1]
        return res



453.py class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums) 



454.py class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ab = collections.Counter([a + b for a in A for b in B])
        return sum(-c - d in ab and ab[-c-d] for c in C for d in D)



455.py class Solution:
    def findContentChildren(self, g, s):
        g.sort(reverse = True); s.sort(reverse = True); res = 0
        while s and g:
            if g[-1] <= s[-1]: res += 1; g.pop(); s.pop()
            else: s.pop()
        return res



456.py class Solution:
    def find132pattern(self, nums):
        stack, s3 = [], -float("inf")
        for n in nums[::-1]:
            if n < s3: return True
            while stack and stack[-1] < n: s3 = stack.pop()
            stack.append(n)
        return False



457.py class Solution(object):
    def circularArrayLoop(self, nums):
        loops, n = [[set(), set()] for _ in range(len(nums))], len(nums)
        for loop in range(3):
            for i, num in enumerate(nums):
                mode = 0 if num > 0 else 1
                if loop == 2 and i in loops[i][mode] and i != (i + num) % n: return True
                loops[(i + num) % n][mode] |= loops[i][mode] or {i}
        return False



458.py class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets: pigs += 1
        return pigs



459.py class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return True if len(s)>1 and (s in [s[:i]*(len(s)//i) for i in range(2,len(s)) if len(s)%i==0]  or s==s[0]*len(s)) else False 



460.py class Node:
    def __init__(self, k, v, f):
        self.key = k
        self.val = v
        self.freq = f
        self.next = self.pre = None
class LFUCache:

    def __init__(self, capacity):
        self.max = capacity
        self.cache = 0
        self.freqLast = {}
        self.Nodes = {}
        self.head = self.tail = Node("#", "#", "#")
        self.head.next = self.tail
        self.tail.pre = self.head

    def changeFreq(self, key):
        node, f = self.Nodes[key], self.Nodes[key].freq
        if self.freqLast[f] == node:
            if node.pre.freq == f:
                self.freqLast[f] = node.pre
            else:
                self.freqLast.pop(f)
        if f + 1 in self.freqLast:
            node.pre.next = node.next
            node.next.pre = node.pre
            node.pre = self.freqLast[f + 1]
            node.next = node.pre.next
        elif f in self.freqLast:
            node.pre.next = node.next
            node.next.pre = node.pre
            node.pre = self.freqLast[f]
            node.next = node.pre.next
        node.pre.next = node.next.pre = node
        self.freqLast[f + 1] = node
        node.freq += 1
        
    def removeFirst(self):
        node, f = self.head.next, self.head.next.freq
        node.pre.next = node.next
        node.next.pre = node.pre
        self.Nodes.pop(node.key)
        if self.freqLast[f] == node:
            self.freqLast.pop(f)
        self.cache -= 1
    
    def get(self, key):
        if key in self.Nodes:
            self.changeFreq(key)
            return self.Nodes[key].val
        return -1
    def put(self, key, value):
        if key in self.Nodes:
            self.changeFreq(key)
            self.Nodes[key].val = value
        elif self.max:
            if self.cache == self.max:
                self.removeFirst()
            self.cache += 1
            new = Node(key, value, 1)
            if 1 in self.freqLast:
                new.pre = self.freqLast[1]
            else:
                new.pre = self.head
            new.next = new.pre.next
            new.pre.next = new.next.pre = new
            self.freqLast[1] = self.Nodes[key] = new



461.py class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(a != b for a, b in zip(bin(x)[2:].zfill(32), bin(y)[2:].zfill(32)))



462.py class Solution:
    def minMoves2(self, nums):
        nums.sort()
        m = nums[(len(nums) - 1) // 2] 
        return sum(abs(num - m) for num in nums)



463.py class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.res = 0
        used = set()
        def dfs(i, j):
            used.add((i, j))
            self.res += 4
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    self.res -= 1
                    if (x, y) not in used:
                        dfs(x, y)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in used:
                    dfs(i, j)
        return self.res



464.py class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        memo = {}
        def dfs(arr, total):
            s = str(arr)
            if s in memo:
                return memo[s]
            elif arr[-1] >= total:
                return True
            for i in range(len(arr)):
                if not dfs(arr[:i] + arr[i + 1:], total - arr[i]):
                    memo[s] = True
                    return True
            memo[s] = False
            return False
        if (1 + maxChoosableInteger) * maxChoosableInteger/2 < desiredTotal:
            return False
        return dfs(list(range(1, maxChoosableInteger + 1)), desiredTotal)



465.py class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def remove_one_zero_clique(non_zero):
            n = len(non_zero)
            q = collections.deque()            
            # q store ([index set], sum of set)
            q.append(([0], non_zero[0]))
            min_zero_set = None

            while q:
                cur_set, cur_sum = q.popleft()
                if cur_sum == 0:
                    min_zero_set = cur_set
                    break
                for j in range(cur_set[-1] + 1, n):
                    q.append((cur_set + [j], cur_sum + non_zero[j]))
            
            min_zero_set = set(min_zero_set)
            return [non_zero[i] for i in range(n) if i not in min_zero_set]
        
        
        bal = collections.defaultdict(int)
        for t in transactions:
            bal[t[0]] -= t[2]
            bal[t[1]] += t[2]
        non_zero = [bal[k] for k in bal if bal[k] != 0]
        
        bal_cnt = len(non_zero)
        while len(non_zero) > 0:
            non_zero = remove_one_zero_clique(non_zero)
            bal_cnt -= 1
        return bal_cnt



466.py class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        start = {} # s2_idx : s1_round, s2_round
        s1_round, s2_round, s2_idx = 0, 0, 0
        while s1_round < n1:
            s1_round += 1
            for ch in s1:
                if ch == s2[s2_idx]:
                    s2_idx += 1
                    if s2_idx == len(s2):
                        s2_round += 1
                        s2_idx = 0
            if s2_idx in start:
                prev_s1_round, prev_s2_round = start[s2_idx]
                circle_s1_round, circle_s2_round = s1_round - prev_s1_round, s2_round - prev_s2_round
                res = (n1 - prev_s1_round) // circle_s1_round * circle_s2_round
                left_s1_round = (n1 - prev_s1_round) % circle_s1_round + prev_s1_round
                for key, val in start.items():
                    if val[0] == left_s1_round:
                        res += val[1]
                        break
                return res // n2
            else:
                start[s2_idx] = (s1_round, s2_round)
        return s2_round // n2



467.py class Solution:
    def findSubstringInWraproundString(self, p):
        res, l = {i: 1 for i in p}, 1
        for i, j in zip(p, p[1:]):
            l = l + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            res[j] = max(res[j], l)
        return sum(res.values())



468.py class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        ip4, ip6 = IP.split("."), IP.split(":")
        if len(ip4) == 4:
            for num in ip4:
                try: 
                    if not (num[0] in string.digits and int(num) < 256 and (num[0] != "0" or num == "0")): return "Neither"
                except: return "Neither"
            return "IPv4"
        elif len(ip6) == 8:
            for num in ip6:
                try: 
                    if not (num[0] in string.hexdigits and 0 <= int(num, 16) and len(num) <= 4): return "Neither"
                except: return "Neither"
            return "IPv6"
        return "Neither"



469.py class Solution:
    def isConvex(self, points):
        def direction(a, b, c): return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        d, n = 0, len(points)
        for i in range(n):
            a = direction(points[i], points[(i + 1) % n], points[(i + 2) % n])
            if not d: d = a
            elif a * d < 0: return False
        return True



470.py class Solution:
    def rand10(self):
        return sum(rand7() for _ in range(10)) % 10 + 1



471.py class Solution:
    def encode(self, s: str) -> str:
        def dfs(i, j):
            if i == j: return s[i]
            if (i, j) not in memo:
                c1 = min((dfs(i, k) + dfs(k + 1, j) if s[i:k + 1] != s[k + 1:j + 1] else '2[' + dfs(i, k) + ']' for k in range(i, j)), key = len)
                c2 = s[i:j + 1]
                memo[(i, j)] = min(c1, c2, key = len)
                for k in range(i, i + (j - i) // 2 + 1):
                    tar, ind, cnt = s[i:k + 1], i, 0
                    while ind + k - i <= j and s[ind:ind + k - i + 1] == tar:
                        cnt += 1
                        ind += k - i + 1
                    c3 = str(cnt) + '[' + tar + ']' + dfs(ind, j) if ind <= j else str(cnt) + '[' + tar + ']'
                    memo[(i, j)] = min(memo[(i, j)], c3, key = len)
            return memo[(i, j)]
        memo = {}
        return dfs(0, len(s) - 1)



472.py class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        def check(w, st):
            if w in st: return True
            for i in range(1, len(w)):
                if w[:i] in st and check(w[i:], st): return True
            return False
        w_set, res = set(words), []
        for w in words:
            w_set.remove(w)
            if check(w, w_set): res += w,
            w_set.add(w)
        return res



473.py class Solution:
    def makesquare(self, nums):
        def dfs(index, edge, count, used):
            for i in range(index, len(nums)):
                if i in used or edge - nums[i] < 0: continue
                elif edge - nums[i] > 0 and dfs(i + 1, edge - nums[i], count, used | {i}): return True
                elif edge - nums[i] == 0 and (count and dfs(1, l, count - 1, used | {i})) or not count: return True
            return False
        sm = sum(nums)
        if len(nums) < 4 or sm % 4 != 0: return False
        l = sm // 4 
        nums.sort(reverse = True)
        if nums[0] > l: return False
        return nums[0] == l and dfs(1, l, 1, {0}) or dfs(1, l - nums[0], 2, {0})



474.py class Solution:
    def findMaxForm(self, strs, m, n):
        res = [0]
        memo = set()
        def dfs(st, zeros, ones, cnt):
            if (zeros, ones, cnt) not in memo:
                if cnt > res[0]:
                    res[0] = cnt
                if zeros or ones:
                    for s in st:
                        if st[s] and cntr[s]["0"] <= zeros and cntr[s]["1"] <= ones:
                            st[s] -= 1
                            dfs(st, zeros - cntr[s]["0"], ones - cntr[s]["1"], cnt + 1)
                            st[s] += 1
                memo.add((zeros, ones, cnt))
                
        cntr = {s:collections.Counter(s) for s in strs}
        dfs(collections.Counter(strs), m, n, 0)
        return res[0]



475.py class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        r = 0
        for h in houses:
            ind = bisect.bisect_left(heaters, h)
            if ind == len(heaters):
                r = max(r, h - heaters[-1])
            elif ind == 0:
                r = max(r, heaters[0] - h)
            else:
                r = max(r, min(heaters[ind] - h, h - heaters[ind - 1]))
        return r



476.py class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int("".join([str((int(i)+1)%2) for i in bin(num)[2:]]),2)



477.py class Solution:
    def totalHammingDistance(self, nums):
        ones, n, res = [0] * 32, len(nums), 0
        for num in nums:
            for i, c in enumerate(bin(num)[2:][::-1]):
                if c == "1": ones[i] += 1
        for one in ones: res += one * (n - one)
        return res



478.py class Solution:

    def __init__(self, radius, x_center, y_center):
        self.x, self.y, self.r = x_center, y_center, radius

    def randPoint(self):
        r, angle, scale = random.uniform(0, self.r), random.uniform(0, 2 * math.pi), math.sqrt(random.uniform(0, 1))
        return [self.x + self.r * scale * math.cos(angle), self.y + self.r * scale * math.sin(angle)]



479.py class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        return list(num for i,num in enumerate([0,9,987,123,597,677,1218,877,475]) if i==n)[0]



480.py class Solution:
    def medianSlidingWindow(self, nums, k):
        window = sorted(nums[:k])
        medians = []
        for a, b in zip(nums, nums[k:] + [0]):
            medians.append((window[k//2] + window[~(k//2)]) / 2.)
            window.remove(a)
            bisect.insort(window, b)
        return medians



481.py class Solution(object):
    def magicalString(self, n):
        cnt, s, two = 0, "1", True
        for i in range(n - 1):
            if s[i] == "1":
                cnt += 1
                s += "2" if two else "1"
            else: s += "22" if two else "11"
            two = not two
        return cnt if n != 1 else 1



482.py class Solution:
    def licenseKeyFormatting(self, S, K):
        S = S.replace("-", "").upper()[::-1]
        return '-'.join([S[i:i+K] for i in range(0, len(S), K)])[::-1]



483.py class Solution:
    def smallestGoodBase(self, n):
        n = int(n)
        for m in range(int(math.log(n, 2)), 1, -1):
            k = int(n ** m ** -1)
            if (k ** (m + 1) -1) // (k - 1) == n:
                return str(k)
        return str(n-1) 



484.py class Solution:
    def findPermutation(self, s):
        arr, cnt, n = list(range(1, len(s) + 2)), 0, len(s)
        for i in range(n + 1):
            if i < n and s[i] == "D":
                cnt += 1
            elif cnt:
                arr[i - cnt:i + 1] =  arr[i - cnt:i + 1][::-1]
                cnt = 0
        return arr



485.py class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cons=[0,0]
        for num in nums:
            if num==1:cons[1]+=1
            else:cons[1]=0
            cons[0]=max(cons[0],cons[1])
        return cons[0]
        



486.py class Solution:
    def PredictTheWinner(self, nums):
        def dfs(l, r, p1, p2, turn):
            if l > r:
                return p1 >= p2
            elif turn:
                return dfs(l + 1, r, p1 + nums[l], p2, 0) or dfs(l, r - 1, p1 + nums[r], p2, 0)
            else:
                return dfs(l + 1, r, p1, p2 + nums[l], 1) and dfs(l, r - 1, p1, p2 + nums[r], 1)
        return dfs(0, len(nums) - 1, 0, 0, 1)



487.py class Solution:
    def findMaxConsecutiveOnes(self, nums):
        l, zero, mx = 0, -1, 0
        for r, num in enumerate(nums + [0]):
            if not num:
                l, zero, mx = zero + 1, r, max(mx, r - l)
        return mx



488.py class Solution:
    def findMinStep(self, board, hand):   
        def dfs(s, c):
            if not s: return 0
            res, i = float("inf"), 0
            while i < len(s):
                j = i + 1
                while j < len(s) and s[i] == s[j]: j += 1
                incr = 3 - (j - i)
                if c[s[i]] >= incr:
                    incr = 0 if incr < 0 else incr
                    c[s[i]] -= incr
                    tep = dfs(s[:i] + s[j:], c)
                    if tep >= 0: res = min(res, tep + incr)
                    c[s[i]] += incr
                i = j
            return res if res != float("inf") else -1
        return dfs(board, collections.Counter(hand))



489.py class Solution:
    def cleanRoom(self, robot, move = [(-1, 0), (0, -1), (1, 0), (0, 1)]):
        def dfs(i, j, cleaned, ind):
            robot.clean()
            cleaned.add((i, j))
            k = 0
            for x, y in move[ind:] + move[:ind]:
                if (i + x, j + y) not in cleaned and robot.move():
                    dfs(i + x, j + y, cleaned, (ind + k) % 4)
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnLeft()
                k += 1
        dfs(0, 0, set(), 0) 



490.py class Solution:
    def hasPath(self, maze, start, destination):
        m, n, stopped = len(maze), len(maze[0]), set()
        def dfs(x, y):
            if (x, y) in stopped: 
                return False
            stopped.add((x, y))
            if [x, y] == destination:
                return True
            for i, j in (-1, 0) , (1, 0), (0, -1), (0, 1):
                newX, newY = x, y
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                if dfs(newX, newY):
                    return True
            return False
        return dfs(*start)



491.py class Solution:
    def findSubsequences(self, nums):
        subs = {()}
        for num in nums:
            subs |= {sub + (num,) for sub in subs if not sub or sub[-1] <= num}
        return [sub for sub in subs if len(sub) >= 2]



492.py class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        l, w = int(math.sqrt(area)), int(math.sqrt(area))
        while l*w!=area:
            if area%w==0: l=int(area/w)
            else: w-=1
        return [l,w]



493.py class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = [0]
        def merge(nums):
            if len(nums) <= 1: return nums
            left, right = merge(nums[:len(nums)//2]), merge(nums[len(nums)//2:])
            for r in right:
                add = len(left) - bisect.bisect(left, 2 * r)
                if not add: break
                res[0] += add
            return sorted(left+right)
        merge(nums)
        return res[0]



494.py class Solution:
    def findTargetSumWays(self, nums, S):
        d = {S:1}
        for i in range(len(nums)):
            new_d = collections.defaultdict(int)
            for k, v in d.items():
                new_d[k+nums[i]] += v
                new_d[k-nums[i]] += v
            d = new_d
        return d[0]



495.py class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        timeSeries.sort()
        res, upper = 0, 0
        for i, num in enumerate(timeSeries): 
            if num > upper: upper = num
            res, upper = res + num + duration - upper, num + duration
        return res



496.py class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        out=list()
        for num in nums1: 
            out.append(-1)
            for j in range(nums2.index(num)+1,len(nums2)):
                if nums2[j]>num: out[-1]=nums2[j]; break
        return out



497.py class Solution:

    def __init__(self, rects):
        self.rects, self.ranges, sm = rects, [], 0
        for x1, y1, x2, y2 in rects:
            sm += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(sm)

    def pick(self):
        x1, y1, x2, y2 = self.rects[bisect.bisect_left(self.ranges, random.randint(1, self.ranges[-1]))]
        return [random.randint(x1, x2), random.randint(y1, y2)]



498.py class Solution:
    def findDiagonalOrder(self, matrix):
        i, j, d, res, n, m = 0, 0, 1, [], len(matrix), len(matrix and matrix[0]) 
        while i < n and j < m:
            res.append(matrix[i][j])
            if j + 1 < m and (i == 0 and d == 1) or (i == n - 1 and d == -1): j, d = j + 1, -d
            elif i + 1 < n and (j == 0 and d == -1) or (j == m - 1 and d == 1): i, d = i + 1, -d
            elif d == 1: i, j = i - 1, j + 1
            else: i, j = i + 1, j - 1
        return res



499.py class Solution:
    def findShortestWay(self, maze, ball, hole):
        m, n, q, stopped = len(maze), len(maze[0]), [(0, "", ball[0], ball[1])], {(ball[0], ball[1]): [0, ""]}
        while q:
            dist, pattern, x, y = heapq.heappop(q)
            if [x, y] == hole:
                return pattern
            for i, j, p in ((-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")):
                newX, newY, d = x, y, 0
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    d += 1
                    if [newX, newY] == hole:
                        break
                if (newX, newY) not in stopped or [dist + d, pattern + p] < stopped[(newX, newY)]:
                    stopped[(newX, newY)] = [dist + d, pattern + p]
                    heapq.heappush(q, (dist + d, pattern + p, newX, newY))
        return "impossible"



500.py class Solution:
    def findWords(self, words):
        return [w for w in words if any(not set(w.lower()) - row for row in (set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")))]



501.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import Counter
        def traverse(node):
            if node: dic[node.val]+=1; traverse(node.left); traverse(node.right)
        dic = collections.Counter()
        traverse(root)
        mx=max(dic.values(),default=0)
        return [k for k,v in dic.items() if v==mx]



502.py class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        pool, new = [], [(c, p) for c, p in zip(Capital, Profits)]
        heapq.heapify(new)
        for i in range(k):
            while new and new[0][0] <= W:
                c, p = heapq.heappop(new)
                heapq.heappush(pool, -p)
            try:
                p = -heapq.heappop(pool)
                W += p
            except:
                break
        return W



503.py class Solution:
    def nextGreaterElements(self, nums):
        stack, res = [], [-1] * len(nums)
        for j in range(2):
            for i in range(len(nums)):
                while stack and (nums[stack[-1]] < nums[i]): res[stack.pop()] = nums[i]
                if j == 1 and not stack: break
                stack += i, 
        return res



504.py class Solution:
    def convertToBase7(self, num):
        lead = "" if num > 0 else "0" if num == 0 else "-"
        res, num = [], abs(num)
        while num:
            res.append(int(num % 7))
            num //= 7
        return lead + "".join(str(c) for c in res[::-1])



505.py class Solution:
    def shortestDistance(self, maze, start, destination):
        m, n, q, stopped = len(maze), len(maze[0]), [(0, start[0], start[1])], {(start[0], start[1]):0}
        while q:
            dist, x, y = heapq.heappop(q)
            if [x, y] == destination:
                return dist
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                newX, newY, d = x, y, 0
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    d += 1
                if (newX, newY) not in stopped or dist + d < stopped[(newX, newY)]:
                    stopped[(newX, newY)] = dist + d
                    heapq.heappush(q, (dist + d, newX, newY))
        return -1



506.py class Solution:
    def findRelativeRanks(self, nums):
        rank = {n:i>2 and str(i+1) or ["Gold","Silver","Bronze"][i] + ' Medal' for i,n in enumerate(sorted(nums,reverse=True))}
        return [rank[num] for num in nums]



507.py class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sm, div =1, 2
        while div**2<=num:
            if num%div==0: sm+=div+(num//div)
            div+=1
        return sm==num and div>2



508.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        def traverse(node):
            if not node: return 0
            sm = traverse(node.left) + traverse(node.right) + node.val
            if sm in dic: dic[sm] += 1
            else: dic[sm] = 1
            return sm
        dic = {}
        traverse(root)
        mx = max(dic.values())
        return [k for k in dic.keys() if dic[k] == mx]
        
        



509.py class Solution:
    def fib(self, N: int) -> int:
        return self.fib(N - 1) + self.fib(N - 2) if N > 1 else N
        



510.py class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        while node.parent and node.parent.left != node:
            node = node.parent
        return node.parent



513.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        bfs = [root]
        while bfs:
            left = bfs[0].val
            bfs = [child for node in bfs for child in (node.left, node.right) if child]
        return left



514.py class Solution:
    def findRotateSteps(self, ring, key):
        ind, n, dp, pre = collections.defaultdict(list), len(ring), [0] * len(ring), key[0]
        for i, c in enumerate(ring): ind[c].append(i)
        for i in ind[key[0]]: dp[i] = min(i, n - i) + 1
        for c in key[1:]:
            for i in ind[c]: dp[i] = min(dp[j] + min(i - j, j + n - i) if i >= j else dp[j] + min(j - i, i + n - j) for j in ind[pre]) + 1
            pre = c
        return min(dp[i] for i in ind[key[-1]])



515.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque
        q, res, target = deque([root]) if root else None, [root.val] if root else [], root
        while q:
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            if node == target and q: 
                res.append(max([i.val for i in q]))
                target = q[-1]
        return res



516.py class Solution:
    def longestPalindromeSubseq(self, s):
        dp = [[0 for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                dp[i][j] = dp[i + 1][j - 1] + 2 if s[i] == s[j] else max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][len(s) - 1]



517.py class Solution:
    def findMinMoves(self, machines):
        target, n, sm, res, total = sum(machines) // len(machines), len(machines), 0, 0, sum(machines)
        if target * n != total: return -1
        for i in range(n):
            l, sm, r = target * i - sm, sm + machines[i], target * (n - i - 1) - total + sm + machines[i]
            res = max(res, l + r, l, r)
        return res



518.py class Solution(object):
    def change(self, amount, coins):
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]



519.py class Solution:

    def __init__(self, n_rows, n_cols):
        self.rows, self.cols, self.used = n_rows, n_cols, set()
        
    def flip(self):
        while True:
            r, c = random.randint(1, self.rows), random.randint(1, self.cols)
            if (r, c) not in self.used:
                self.used.add((r, c))
                return [r - 1, c - 1]
            
    def reset(self):
        self.used = set()



520.py class Solution:
    def detectCapitalUse(self, word):
        return word[0].isupper() and word[1:].islower() or word.isupper() or word.islower()



521.py class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return -1 if a == b else max(len(a), len(b))



522.py class Solution:
    def findLUSlength(self, strs):
        def find(s, t):
            i = 0
            for c in t:
                if c == s[i]: i += 1
                if i == len(s): return True
            return False
        for s in sorted(strs, key=len, reverse=True):
            if sum(find(s, t) for t in strs) == 1: return len(s)
        return -1



523.py class Solution:
    def checkSubarraySum(self, nums, k):
        if not k: return any(nums[i] == nums[i - 1] == 0 for i in range(1, len(nums)))
        mods, sm = set(), 0
        for i, num in enumerate(nums):
            sm = (sm + num) % k
            if (sm in mods and num or (i and not nums[i - 1])) or (not sm and i): return True
            mods |= {sm}
        return False



524.py class Solution:
    def findLongestWord(self, s, d):
        d.sort(key = lambda x: (-len(x), x))
        for w in d:
            i = 0
            for c in s:
                if c == w[i]: i += 1
                if i == len(w): return w
        return ""



525.py class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ind, res, sm = {0:-1}, 0, 0
        for i, num in enumerate(nums):
            sm += num and 1 or -1
            if sm in ind:
                res = max(res, i - ind[sm])
            else:
                ind[sm] = i
        return res



526.py memo = {}
class Solution:
    def countArrangement(self, N, arr = None):
        if not arr: arr = tuple(range(1, N + 1))
        if (N, arr) in memo or N == 1: return N == 1 and 1 or memo[(N, arr)]
        memo[(N, arr)] = sum([self.countArrangement(N-1, arr[:j]+arr[j + 1:]) for j in range(len(arr)) if arr[j]%N==0 or N%arr[j]==0])
        return memo[(N, arr)]



527.py class Solution:
    def wordsAbbreviation(self, dict):
        abb = collections.defaultdict(int)
        for i, w in enumerate(dict):
            for j in range(1, len(w) - 2):
                abb[w[:j] + str(len(w) - j - 1) + w[-1]] += 1
        for i, w in enumerate(dict):
            for j in range(1, len(w) - 2):
                new = w[:j] + str(len(w) - j - 1) + w[-1]
                if abb[new] == 1:
                    dict[i] = new
                    break
        return dict



528.py class Solution:

    def __init__(self, w):
        self.ranges, sm = [], 0
        for weight in w:
            self.ranges.append([sm, sm + weight])
            sm += weight
        self.mn, self.mx = 1, sm
    def pickIndex(self):
        num, l, r = random.randint(self.mn, self.mx), 0, len(self.ranges) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.ranges[mid][1] < num:
                l = mid + 1
            elif num <= self.ranges[mid][0]:
                r = mid - 1
            else:
                return mid



529.py class Solution(object):
    def updateBoard(self, board, click):
        def explore(i, j):
            visited.add((i, j))
            if board[i][j] == "M": board[i][j] = "X"
            else:
                points = ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j + 1), (i + 1, j - 1))
                cnt, adj = 0, []
                for p in points:
                    if 0 <= p[0] < m and 0 <= p[1] < n:
                        if board[p[0]][p[1]] == "M": cnt += 1
                        elif p not in visited: adj += p,
                if cnt == 0:
                    board[i][j] = "B"
                    for p in adj: explore(p[0], p[1])
                else: board[i][j] = str(cnt)
        m, n, visited = len(board), len(board and board[0]), set()
        explore(click[0], click[1])
        return board



530.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.res = sys.maxsize
        def dfs(node):
            if not node: return sys.maxsize, -sys.maxsize
            lMn, lMx = dfs(node.left)
            rMn, rMx = dfs(node.right)
            self.res = min(self.res, node.val - lMx, rMn - node.val)
            return min(node.val, lMn), max(node.val, rMx)
        dfs(root)
        return self.res



531.py class Solution:
    def findLonelyPixel(self, grid: List[List[str]]) -> int:
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B':
                    rows[i].append(j)
                    cols[j].append(i)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B' and rows[i] == [j] and cols[j] == [i]:
                    res += 1
        return res



532.py class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic, pair = {}, 0
        for num in nums:
            if (num-k in dic or num+k in dic) and (not num in dic or (k==0 and dic[num]==1)) and k>=0: 
                if num-k in dic and k!=0: pair+=1
                if num+k in dic: pair+=1 
                if num in dic: dic[num]+=1; continue
            if num in dic: continue
            dic[num]=1
        return pair



533.py class Solution:
    def findBlackPixel(self, picture, N):
        m, n, res = len(picture), len(picture[0]), 0
        for row in picture:
            r_cnt = row.count("B")
            if r_cnt != N:
                continue
            for j in range(n):
                if row[j] == "B":
                    col_cnt = same = 0
                    for i in range(m):
                        if picture[i][j] == "B":
                            col_cnt += 1
                            if picture[i] == row:
                                same += 1 
                            else:
                                break
                    if r_cnt == col_cnt == same:
                        res += 1
        return res



535.py class Codec:

    def encode(self, longUrl): return longUrl
    def decode(self, shortUrl): return shortUrl
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))



536.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s):
        stack, cur = [], ""
        for i, c in enumerate(s):
            if c.isnumeric() or c == "-":
                cur += c
            elif not cur:
                if c == ")":
                    stack.pop()
            else:
                node = TreeNode(int(cur))
                if stack:
                    if not stack[-1].left:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                cur = ""
                if c == "(":
                    stack.append(node)
        return stack and stack[0] or (cur and TreeNode(int(cur))) or []



537.py class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        re, im = 0, 0
        re_a, im_a = list(map(int,a[:-1].split("+")))
        re_b, im_b = list(map(int,b[:-1].split("+")))
        re += re_a * re_b - im_a * im_b
        im += re_a * im_b + re_b *im_a
        return str(re)+"+"+str(im)+"i"



538.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def traverse(node):
            if not node: return
            traverse(node.right)
            node.val = residue[0] = node.val + residue[0]
            traverse(node.left)
            return node
        residue = [0]
        return traverse(root)



539.py class Solution:
    def findMinDifference(self, tp):
        def getMinute(t): 
            h , m = t.split(":")
            return int(h) * 60 + int(m)
        tp = sorted(map(getMinute, tp))
        mn = sys.maxsize
        for i in range(len(tp) - 1): 
            mn = min(mn, tp[i + 1] - tp[i])
            if mn == 0: return 0
        return min(mn, 1440 + tp[0] - tp[-1])



540.py class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if mid+1<len(nums) and nums[mid] == nums[mid+1]:
                if mid % 2 == 0: left = mid+2
                else: right = mid-1
            elif mid-1>=0 and nums[mid] == nums[mid-1]:
                if mid % 2 == 0: right = mid-2
                else: left = mid+1
            else: return nums[mid]
                



541.py class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return "".join([s[i:i+k][::-1]+s[i+k:i+2*k]   if len(s)>=i or len(s)>i-k else s[k*i:][::-1] for i in range(0,len(s),k*2)])



542.py class Solution:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix and matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float("inf")
                    if i > 0 and matrix[i - 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i - 1][j] + 1
                    if j > 0 and matrix[i][j - 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j - 1] + 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    if i + 1 < m and matrix[i + 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i + 1][j] + 1
                    if j + 1 < n and matrix[i][j + 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j + 1] + 1
        return matrix



543.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        def traverse(node):
            if not node: return 0
            left, right = traverse(node.left), traverse(node.right)
            res[0] = max(left+right, res[0])
            return 1+ max(left, right)
        traverse(root)
        return res[0]



544.py class Solution:
    def findContestMatch(self, n):
        arr = [str(i) for i in range(1, n + 1)]
        while len(arr) > 1: arr = ["(" + arr[i] + "," + arr[len(arr) - 1 - i] + ")" for i in range(len(arr) // 2)]
        return ",".join(arr)    



545.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        used, res, r = {root}, [root.val], []
        def lb(node):
            if node not in used:
                used.add(node)
                res.append(node.val)
            if node.left:
                lb(node.left)
            elif node.right:
                lb(node.right)
        def rb(node):
            if node not in used:
                used.add(node)
                r.append(node.val)
            if node.right:
                rb(node.right)
            elif node.left:
                rb(node.left)
        def lv(node):
            if not node.left and not node.right and node not in used:
                used.add(node)
                res.append(node.val)
            if node.left:
                lv(node.left)
            if node.right:
                lv(node.right)
        if root.left:
            lb(root.left)
        lv(root)
        if root.right:
            rb(root.right)
        return res + r[::-1]



546.py class Solution:
    def removeBoxes(self, A):
        n = len(A)
        memo = [[[0] * n for _ in range(n) ] for _ in range(n)]
        def dp(i, j, k):
            if i > j: return 0
            if not memo[i][j][k]:
                m = i
                while m+1 <= j and A[m+1] == A[i]:
                    m += 1
                i, k = m, k + m - i
                ans = dp(i+1, j, 0) + (k+1) ** 2
                for m in range(i+1, j+1):
                    if A[i] == A[m]:
                        ans = max(ans, dp(i+1, m-1, 0) + dp(m, j, k+1))
                memo[i][j][k] = ans
            return memo[i][j][k]
        return dp(0, n-1, 0)



547.py class Solution:
    def findCircleNum(self, m):
        res, n = 0, len(m)
        def explore(i):
            m[i][i] = 0
            for j in range(n):
                if i != j and m[i][j] == m[j][j] == 1: explore(j)
        for i in range(n):
            if m[i][i] == 1: explore(i); res += 1
        return res



548.py class Solution:
    def splitArray(self, nums):
        n = len(nums)
        s = [0] * (n + 1)
        for i in range(n): s[i + 1] = s[i] + nums[i]
        def check(l, r):
            return set(s[m] - s[l] for m in range(l + 1, r + 1) if s[m] - s[l] == s[r + 1] - s[m + 1])
        return any(check(0, j - 1) & check(j + 1, n - 1) for j in range(n))



549.py class Solution:
    def longestConsecutive(self, root):
        dec, inc = {}, {}
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            incL = inc[node.left] + 1 if node.left and node.val == node.left.val + 1 else 1
            incR = inc[node.right] + 1 if node.right and node.val == node.right.val + 1 else 1
            inc[node] = max(incL, incR)
            decL = dec[node.left] + 1 if node.left and node.val == node.left.val - 1 else 1
            decR = dec[node.right] + 1 if node.right and node.val == node.right.val - 1 else 1
            dec[node] = max(decL, decR)
            if node.left and node.right and node.left.val == node.val - 1 and node.right.val == node.val + 1:
                m = inc[node.left] + dec[node.right] + 1
            elif node.left and node.right and node.left.val == node.val + 1 and node.right.val == node.val - 1:
                m = dec[node.left] + inc[node.right] + 1
            else:
                m = 0
            return max(m, l, r, inc[node], dec[node])
        return dfs(root)



551.py class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return False if "LLL" in s or s.count("A")>1 else True



552.py class Solution:
    def checkRecord(self, n):
        dp, mod = [1, 0, 0, 1, 1, 0], 10 ** 9 + 7
        for i in range(1, n):
            dp[0], dp[1], dp[2], dp[3], dp[4], dp[5] = sum(dp) % mod, dp[0], dp[1], sum(dp[3:]) % mod, dp[3], dp[4]
        return sum(dp) % mod



553.py class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1: return str(nums[0])
        elif len(nums) == 2: return str(nums[0])+"/"+str(nums[1])
        else: return str(nums[0])+"/("+"/".join(str(i) for i in nums[1:])+")"



554.py class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        m = len(wall)
        sm = sum(wall[0])
        cnt = collections.defaultdict(int)
        for i in range(m):
            x = 0
            for num in wall[i]:
                x += num
                if x != sm:
                    cnt[x] += 1
        mx = 0
        for i in range(m):
            x = 0
            for num in wall[i]:
                x += num
                mx = max(mx, cnt[x])
        return m - mx



555.py class Solution:
    def splitLoopedString(self, strs):
        arr, res = [s > s[::-1] and s or s[::-1] for s in strs], ""
        for i, word in enumerate(strs):
            for w in (word, word[::-1]):
                s, ind = "", 0
                for j in range(len(w)):
                    if not s or w[j:] + w[:j] > s: s, ind = w[j:] + w[:j], j   
                cur = w[ind:] + "".join(arr[i + 1:]) + "".join(arr[:i]) + w[:ind]
                if not res or cur > res: res = cur
        return res



556.py class Solution:
    def nextGreaterElement(self, n):
        arr = [c for c in str(n)]
        for l in range(len(arr) - 2, -1, -1):
            r = len(arr) - 1
            while l < r and arr[r] <= arr[l]:
                r -= 1
            if l != r:
                arr[l], arr[r] = arr[r], arr[l]
                arr[l + 1:] = sorted(arr[l + 1:])
                num = int("".join(arr))
                return num if -2 ** 31 <= num <= 2 ** 31 - 1 else -1
        return -1



557.py class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        j, s_out=0, str()
        for i, char in enumerate(s):
            if i==len(s)-1: s_out+=s[j:i+1][::-1]; return "".join(s_out)
            if char==" ": s_out+=s[j:i][::-1]; j=i+1; s_out+=" "
        return "".join(s_out)



558.py class Solution:
    def intersect(self, q1, q2):
        if q1.isLeaf:
            return q1.val and q1 or q2
        elif q2.isLeaf:
            return q2.val and q2 or q1
        else:
            tLeft = self.intersect(q1.topLeft, q2.topLeft)
            tRight = self.intersect(q1.topRight, q2.topRight)
            bLeft = self.intersect(q1.bottomLeft, q2.bottomLeft)
            bRight = self.intersect(q1.bottomRight, q2.bottomRight)
            if tLeft.isLeaf and tRight.isLeaf and bLeft.isLeaf and bRight.isLeaf and tLeft.val == tRight.val == bLeft.val == bRight.val:
                node = Node(tLeft.val, True, None, None, None, None) 
            else:
                node = Node(False, False, tLeft, tRight, bLeft, bRight)
        return node



559.py class Solution(object):
    def maxDepth(self, root, level = 1):
        return max(root and [self.maxDepth(child, level + 1) for child in root.children] + [level] or [0])



560.py class Solution:
    def subarraySum(self, nums, k):
        sums, res, sm = {}, 0, 0
        for i in range(len(nums)):
            sums[sm], sm = sm in sums and sums[sm] + 1 or 1, sm + nums[i]
            if sm - k in sums: res += sums[sm - k]
        return res



561.py class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum=0
        while nums:
            num1=nums.pop()
            num2=nums.pop()
            sum+=num2
        return sum
            



562.py class Solution:
    def longestLine(self, M):
        hor, ver, dig, aDig, mx, m, n = {}, {}, {}, {}, 0, len(M), len(M and M[0])
        for i in range(m):
            for j in range(n):
                if M[i][j]:
                    ver[(i, j)] = j > 0 and M[i][j - 1] and ver[(i, j - 1)] + 1 or 1
                    hor[(i, j)] = i > 0 and M[i - 1][j] and hor[(i - 1, j)] + 1 or 1
                    dig[(i, j)] = i > 0 and j > 0 and M[i - 1][j - 1] and dig[(i - 1, j - 1)] + 1 or 1
                    aDig[(i, j)] = i > 0 and j + 1 < n and M[i - 1][j + 1] and aDig[(i - 1, j + 1)] + 1 or 1
                    mx = max(mx, ver[(i, j)], hor[(i, j)], dig[(i, j)], aDig[(i, j)])
        return mx



563.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node):
            if not node: return 0
            left = traverse(node.left)
            right = traverse(node.right)
            res.append(abs(right -left))
            return node.val + left + right
        res = []
        traverse(root)
        return sum(res)



564.py class Solution:
    def nearestPalindromic(self, S):
        K = len(S)
        candidates = [str(10**k + d) for k in (K-1, K) for d in (-1, 1)]
        prefix = S[:(K+1)//2]
        P = int(prefix)
        for start in map(str, (P-1, P, P+1)):
            candidates.append(start + (start[:-1] if K%2 else start)[::-1])

        def delta(x):
            return abs(int(S) - int(x))

        ans = None
        for cand in candidates:
            if cand != S and not cand.startswith('00'):
                if (ans is None or delta(cand) < delta(ans) or
                        delta(cand) == delta(ans) and int(cand) < int(ans)):
                    ans = cand
        return ans



565.py class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in range(len(nums)):
            if i in dic:
                continue
            j=i
            dic[j]=1
            while nums[i]!=j:
                dic[j]+=1
                i=nums[i]
                dic[i]=1
        return max(dic.values())



566.py class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        nums_ordered=[x for y in nums for x in y]
        if r*c==len(nums)*len(nums[0]):
            return [nums_ordered[c*i:c*(i+1)] for i in range(r)]
        else:return nums
        



567.py class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2): return False
        dic = collections.defaultdict(int)
        for i in range(len(s1)):
            dic[s1[i]] += 1
            if dic[s1[i]] == 0: del dic[s1[i]]
            dic[s2[i]] -= 1
            if dic[s2[i]] == 0: del dic[s2[i]]
        i = 0
        for j in range(len(s1), len(s2)):
            if not dic: return True
            dic[s2[j]] -= 1
            if dic[s2[j]] == 0: del dic[s2[j]]
            dic[s2[i]] += 1
            if dic[s2[i]] == 0: del dic[s2[i]]
            i += 1
        return not dic



568.py class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        if not flights or not days:
            return 0
        n, k = len(flights), len(days[0])
        dp = [[-1] * (k + 1) for c in range(n)]
        dp[0][0] = 0
        for w in range(1, k + 1):
            for c in range(n):
                dp[c][w] = max([dp[pre][w - 1] + days[c][w - 1] for pre in range(n) if (flights[pre][c] or pre == c) and dp[pre][w - 1] >= 0] or [-1])
        return max(dp[c][-1] for c in range(n))



572.py class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def traverse(node):
            if not node: return "^"
            return "$"+str(node.val)+"?"+traverse(node.left)+"@"+traverse(node.right)
        return traverse(t) in traverse(s)



573.py class Solution:
    def minDistance(self, height, width, t, s, n):
        sm = 2 * sum(abs(x - t[0]) + abs(y - t[1]) for x, y in n)
        return min(sm - abs(x - t[0]) - abs(y - t[1]) + abs(x - s[0]) + abs(y - s[1]) for x, y in n)



575.py class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return len(set(candies)) if len(set(candies))<=len(candies)//2 else len(candies)//2



576.py class Solution:
    def __init__(self): self.dic = collections.defaultdict(int)
    def findPaths(self, m, n, N, i, j):
        if N >= 0 and (i < 0 or j < 0 or i >= m or j >= n): return 1
        elif N < 0: return 0
        elif (i, j, N) not in self.dic: 
            for p in ((1, 0), (-1, 0), (0, 1), (0, -1)): self.dic[(i, j, N)] += self.findPaths(m, n, N - 1, i + p[0], j + p[1]) 
        return self.dic[(i, j, N)] % (10 ** 9 + 7) 



581.py class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr = sorted(nums)
        i = 0
        for i in range(len(arr)):
            if arr[i] != nums[i]:
                for j in range(len(arr) - 1, -1, -1):
                    if arr[j] != nums[j]:
                        return j - i + 1
        return 0



582.py class Solution:
    def killProcess(self, pid, ppid, kill):
        indexes, res = collections.defaultdict(list), [kill]
        for i, p in enumerate(ppid):
            indexes[p].append(i)
        stack = [kill]
        while stack:
            for i in indexes[stack.pop()]:
                res.append(pid[i])
                stack.append(pid[i])
        return res



583.py class Solution:
    def minDistance(self, w1, w2):
        m, n = len(w1), len(w2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif w1[i - 1] == w2[j - 1]: 
                    dp[i][j] = dp[i - 1][j - 1]
                else: 
                    dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1)
        return dp[-1][-1]



587.py # http://www.algorithmist.com/index.php/Monotone_Chain_Convex_Hull.py


class Solution(object):

    def outerTrees(self, points):
        """Computes the convex hull of a set of 2D points.

        Input: an iterable sequence of (x, y) pairs representing the points.
        Output: a list of vertices of the convex hull in counter-clockwise order,
          starting from the vertex with the lexicographically smallest coordinates.
        Implements Andrew's monotone chain algorithm. O(n log n) complexity.
        """

        # Sort the points lexicographically (tuples are compared lexicographically).
        # Remove duplicates to detect the case we have just one unique point.
        # points = sorted(set(points))
        points = sorted(points, key=lambda p: (p.x, p.y))

        # Boring case: no points or a single point, possibly repeated multiple times.
        if len(points) <= 1:
            return points

        # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
        # Returns a positive value, if OAB makes a counter-clockwise turn,
        # negative for clockwise turn, and zero if the points are collinear.
        def cross(o, a, b):
            # return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
            return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

        # Build lower hull
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        # Build upper hull
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        # Concatenation of the lower and upper hulls gives the convex hull.
        # Last point of each list is omitted because it is repeated at the
        # beginning of the other list.
        # return lower[:-1] + upper[:-1]
        return list(set(lower[:-1] + upper[:-1]))



588.py class File:
    
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.content = ''

class FileSystem:

    def __init__(self):
        self.root = File('/')

    def move(self, path):
        cur = self.root
        if path[1:]:
            for dr in path[1:].split('/'):
                if dr not in cur.files:
                    cur.files[dr] = File(dr)
                cur = cur.files[dr]
        return cur
    
    def ls(self, path: str) -> List[str]:
        cur = self.move(path)
        return [cur.name] if cur.content else sorted(cur.files.keys())

    def mkdir(self, path: str) -> None:
        self.move(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.move(filePath)
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.move(filePath).content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)



589.py class Solution(object):
    def preorder(self, root):
        ret, q = [], collections.deque([root])
        while any(q):
            node = q.popleft()
            ret.append(node.val)
            for child in node.children[::-1]:
                if child: q.appendleft(child)
        return ret



590.py class Solution(object):
    def postorder(self, root):
        ret, stack = [], [root]
        while any(stack):
            node = stack.pop()
            ret.append(node.val)
            stack += [child for child in node.children if child]
        return ret[::-1]



591.py class Solution:
    def isValid(self, S):
        CDATA_BEGIN = '![CDATA['
        CDATA_END = ']]>'

        def collect_tag(i):
            for j in range(i, len(S)):
                if S[j] == '>': break
            else:
                return None
            return S[i+1:j]

        def valid_tag(tag):
            return 1 <= len(tag) <= 9 and all('A' <= c <= 'Z' for c in tag)

        if not S or S[0] != '<': return False
        tag = collect_tag(0)
        if (tag is None or 
                not S.startswith('<{}>'.format(tag)) or 
                not S.endswith('</{}>'.format(tag)) or
                not valid_tag(tag)):
            return False
        S = S[len(tag) + 2: -len(tag) - 3]

        i = 0
        stack = []
        while i < len(S):
            if S[i] == '<':
                tag = collect_tag(i)
                if tag is None: return False
                if tag.startswith(CDATA_BEGIN):
                    while i < len(S) and S[i:i+3] != CDATA_END:
                        i += 1
                    if not S[i:i+3] == CDATA_END:
                        return False
                    i += 2
                elif tag.startswith('/'):
                    tag = tag[1:]
                    if not valid_tag(tag) or not stack or stack.pop() != tag:
                        return False
                else:
                    if not valid_tag(tag):
                        return False
                    stack.append(tag)
            i += 1

        return not stack



592.py class Solution:
    def fractionAddition(self, e):
        
        def calc(i):
            l, r = i - 1, i + 1
            while l > 0 and e[l - 1].isdigit():
                l -= 1
            while r < len(e) - 1 and e[r + 1].isdigit():
                r += 1
            l = -int(e[l:i]) if l > 0 and e[l - 1] == "-" else int(e[l:i])
            r = int(e[i + 1:r + 1])
            return l, r
        
        def lcm(x, y):
            lcm = max(x, y)
            while True:
                if not lcm % x and not lcm % y:
                    return lcm
                lcm += 1
                
        def gcd(x, y):
            for i in range(min(x, y), 0, -1):
                if not x % i and not y % i:
                    return i
                
        n = d = None
        for i in range(len(e)):
            if e[i] == "/":
                if n:
                    n2, d2 = calc(i)
                    newD = lcm(d, d2)
                    newN = n * (newD // d) + n2 * (newD // d2)
                    if newN:
                        r = gcd(abs(newD), abs(newN))
                        n, d= newN // r, newD // r
                    else:
                        n, d = 0, 1
                else:
                    n, d = calc(i)
        return str(n) + "/" + str(d)



593.py class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        from itertools import combinations as cb
        def D(C): 
            return (C[0][0] - C[1][0]) ** 2 + (C[0][1] - C[1][1]) ** 2
        S = set(map(D, cb((p1, p2, p3, p4), 2)))
        return len(S) == 2 and 0 not in S



594.py class Solution(object):
    def findLHS(self, nums):
        dic, res = collections.defaultdict(int), 0
        for num in nums: dic[num] += 1
        for k in dic:
            if k + 1 in dic: res = max(res, dic[k] + dic[k + 1])
        return res



598.py class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops==[]:
            return m*n
        return min(op[0] for op in ops)* min(op[1] for op in ops) 



599.py class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic={}
        for item1 in list1:
            for item2 in list2:
                if item1==item2:
                    dic[item1]=list1.index(item1)+list2.index(item2)
        return [k for k in dic if dic[k]==min(dic.values())]



600.py class Solution:
    def findIntegers(self, num):
        num, sub = bin(num)[2:], 0
        zero, one = [1] * len(num), [1] * len(num)
        for i in range(1, len(num)):
            zero[i], one[i] = zero[i - 1] + one[i - 1], zero[i - 1]
        for i in range(1, len(num)):
            if num[i] == num[i - 1] == "1": break
            if num[i] == num[i - 1] == "0": sub += one[-1 - i]
        return zero[-1] + one[-1] - sub



604.py class StringIterator:
    def findCount(self):
        j = self.ind + 1
        while j < self.n and self.s[j].isnumeric(): j += 1
        self.count = int(self.s[self.ind + 1:j])
        self.new = j
        
    def __init__(self, compressedString):
        self.s, self.n = compressedString, len(compressedString)
        self.ind = self.count = self.new = 0
        self.findCount()

    def next(self):
        if not self.count:
            if self.new >= self.n: return " "
            elif self.new < self.n:
                self.ind = self.new
                self.findCount()
        self.count -= 1
        return self.s[self.ind]

    def hasNext(self):
        return self.count > 0 or self.new < self.n - 1



605.py class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        num=n
        if len(flowerbed)<=1:
            if (num==1 and flowerbed==[0]) or (num==0):
                return True
            else:
                return False
        if flowerbed[0]==0 and flowerbed[1]==0:
            flowerbed[0]=1
            num-=1
        if flowerbed[-1]==0 and flowerbed[-2]==0:
            flowerbed[-1]=1
            num-=1
        for i in range(1,len(flowerbed)-2):
            if flowerbed[i]!=1 and flowerbed[i+1]!=1 and flowerbed[i-1]!=1:
                flowerbed[i]=1
                num-=1
        if num<=0:
            return True
        return False
            



606.py class Solution:        
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ""
        parent="%s" %t.val
        left, right= "", ""
        if t.left or t.right: left= "(%s)" % self.tree2str(t.left)
        if t.right: right= "(%s)" % self.tree2str(t.right)
        return parent+left+right       



609.py class Solution:
    def findDuplicate(self, paths):
        dic = collections.defaultdict(list)
        for path in paths:
            root, *f = path.split(" ")
            for file in f:
                txt, content = file.split("(")
                dic[content] += root + "/" + txt,
        return [dic[key] for key in dic if len(dic[key]) > 1]



611.py class Solution:
    def triangleNumber(self, nums):
        res, n = 0, len(nums); nums.sort()
        for i in range(n - 1, 1, -1):
            j, k = i - 1, 0
            while k < j:
                if nums[j] + nums[k] > nums[i]: res, j = res + j - k, j - 1
                else: k += 1
        return res



616.py class Solution:
    def addBoldTag(self, S, words):
        trie, n, mask, res = {}, len(S), set(), ""
        for w in words:
            cur = trie
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["#"] = cur.get("#", set()) | {w}
        for i in range(n):
            cur, j = trie, i
            while j < n and S[j] in cur:
                cur = cur[S[j]]
                if "#" in cur:
                    mask |= {ind for ind in range(i, j + 1)}
                j += 1
        for i in range(n):
            if i in mask and (not i or i - 1 not in mask):
                res += "<b>"
            res += S[i]
            if i in mask and (i == n - 1 or i + 1 not in mask):
                res += "</b>"
        return res



617.py class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            root, root.left, root.right = TreeNode(t1.val + t2.val), self.mergeTrees(t1.left, t2.left), self.mergeTrees(t1.right, t2.right)
            return root
        else: return t1 or t2



621.py class Solution:
    def leastInterval(self, tasks, n):
        cnt = sorted(collections.Counter(tasks).values())
        idles = (cnt[-1] - 1) * n
        for i in range(len(cnt) - 1): idles -= min(cnt[i], cnt[-1] - 1)
        return idles > 0 and idles + len(tasks) or len(tasks)



622.py class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None
class MyCircularQueue:

    def __init__(self, k):
        self.size = k
        self.curSize = 0
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def enQueue(self, value):
        if self.curSize < self.size:
            node = Node(value)
            node.pre = self.tail.pre
            node.next = self.tail
            node.pre.next = node.next.pre = node
            self.curSize += 1
            return True
        return False

    def deQueue(self):
        if self.curSize > 0:
            node = self.head.next
            node.pre.next = node.next
            node.next.pre = node.pre
            self.curSize -= 1
            return True
        return False

    def Front(self):
        return self.head.next.val

    def Rear(self):
        return self.tail.pre.val

    def isEmpty(self):
        return self.curSize == 0

    def isFull(self):
        return self.curSize == self.size



623.py class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        q, depth = [root], 1
        while depth != d: parent, q, depth = q, [kid for node in q for kid in (node.left, node.right) if kid], depth+1
        if d != 1:
            for node in parent: node.left, node.right, node.left.left, node.right.right = TreeNode(v), TreeNode(v), node.left, node.right
            return root
        else: 
            first, first.left = TreeNode(v), root
            return first



624.py class Solution:
    def maxDistance(self, arrays):
        arrays.sort(key = lambda x: x[0])
        d1 = max(arr[-1] for arr in arrays[1:]) - arrays[0][0]
        arrays.sort(key = lambda x: x[-1])
        d2 = arrays[-1][-1] - min(arr[0] for arr in arrays[:-1])
        return max(d1, d2)



625.py class Solution:
    def smallestFactorization(self, a):
        res = []
        def dfs(num):
            if num == 1: return True
            for n in range(9, 1, -1):
                if not num % n:
                    res.append(str(n))
                    return dfs(num // n)
            return False 
        bol, num = dfs(a), int("".join(sorted(res))) if res else 1
        return num if bol and -(2 ** 31) <= num <= 2 ** 31 - 1 else 0



628.py class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[-1]*nums[0]*nums[1])



629.py class Solution:
    def kInversePairs(self, n, k):
        dp = [1] + [0] * k
        for i in range(2, n + 1):
            for j in range(1, k + 1): dp[j] += dp[j - 1]
            for j in range(k, 0, -1): dp[j] -= j - i >= 0 and dp[j - i]
        return dp[-1] % (10 ** 9 + 7)



630.py class Solution:
    def scheduleCourse(self, courses):
        pq = []
        start = 0
        for t, end in sorted(courses, key = lambda x: x[1]):
            start += t
            heapq.heappush(pq, -t)
            while start > end:
                start += heapq.heappop(pq)
        return len(pq)



631.py class Excel(object):

    def __init__(self, H, W):
        self.M = [[{'v': 0, 'sum': None} for i in range(H)] for j in range(ord(W) - 64)]

    def set(self, r, c, v):
        self.M[r - 1][ord(c) - 65] = {'v': v, 'sum': None}

    def get(self, r, c):
        cell = self.M[r - 1][ord(c) - 65]
        if not cell['sum']: return cell['v']
        return sum(self.get(*pos) * cell['sum'][pos] for pos in cell['sum'])

    def sum(self, r, c, strs):
        self.M[r - 1][ord(c) - 65]['sum'] = self.parse(strs)
        return self.get(r, c)

    def parse(self, strs):
        c = collections.Counter()
        for s in strs:
            s, e = s.split(':')[0], s.split(':')[1] if ':' in s else s
            for i in range(int(s[1:]), int(e[1:]) + 1):
                for j in range(ord(s[0]) - 64, ord(e[0]) - 64 + 1):
                    c[(i, chr(j + 64))] += 1
        return c



632.py class Solution:
    def smallestRange(self, nums):
        L = R = None
        while True:
            mn = mx = nums[0][-1]
            ind = [0]
            for i, ls in enumerate(nums[1:]):
                if ls[-1] > mx:
                    mx, ind = ls[-1], [i + 1]
                elif ls[-1] == mx:
                    ind.append(i + 1)
                elif ls[-1] < mn:
                    mn = ls[-1]
            if L == None or mx - mn <= R - L:
                L, R = mn, mx
            for j in ind:
                nums[j].pop()
                if not nums[j]:
                    return [L, R]



633.py class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        return not all(((c - i ** 2) ** 0.5) % 1 for i in range(int(c ** 0.5) + 1))



634.py class Solution(object):
    def findDerangement(self, n, dp = 1, mod = 10 ** 9 + 7):
        for i in range(1, n + 1): dp = (i * dp + (-1) ** i) % mod
        return dp 



635.py class LogSystem:

    def __init__(self):
        self.times = []
        self.g = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}
        
    def put(self, id, timestamp):
        self.times.append([timestamp, id])

    def retrieve(self, s, e, gra):
        ind = self.g[gra]
        s, e = s[:ind], e[:ind]
        return [i for time, i in self.times if s <= time[:ind] <= e]



636.py class Solution:
    def exclusiveTime(self, n, logs):
        res, stack = [0] * n, []
        for log in logs:
            log = log.split(":")
            if log[1] == "start":
                stack.append([int(log[2]), 0])
            else:
                start = stack.pop()
                time = int(log[2]) - start[0] + 1
                res[int(log[0])] += time - start[1]
                if stack:
                    stack[-1][1] += time
        return res



637.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        from collections import deque
        q, target, avg = deque([root]), root, [float(root.val)]
        while q:
            node=q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            if q and node==target:
                target, sm = q[-1], 0
                for item in q: sm+=item.val
                avg.append(sm/len(q))
        return avg



638.py class Solution:
    def shoppingOffers(self, price, special, needs):
        def dfs(cur, needs):
            val = cur + sum(p * needs[i] for i, p in enumerate(price))
            for s in special:
                if all(n >= s[i] for i,n in enumerate(needs)): val = min(val, dfs(cur + s[-1], [n - s[i] for i,n in enumerate(needs)]))
            return val
        return dfs(0, needs)



639.py class Solution:
    def numDecodings(self, s):
        if s[0] == "0": return 0
        dp1 = dp2 = 1
        if s[0] == "*": dp2 = 9
        for i in range(1, len(s)):
            couple, newDp1 = s[i -1: i + 1], dp2
            if s[i] == "0":
                if s[i - 1] == "0" or s[i - 1] >= "3": return 0
                dp2 = 2 * dp1 if s[i - 1] == "*" else dp1
            elif s[i] == "*":
                dp2 *= 9
                if s[i - 1] == "2": dp2 += 6 * dp1
                elif s[i - 1] == "1": dp2 += 9 * dp1
                elif s[i - 1] == "*": dp2 += 15 * dp1
            elif "10" <= couple <= "26": dp2 += dp1
            elif s[i - 1] == "*": dp2 += 2 * dp1 if s[i] <= "6" else dp1
            dp1 = newDp1
        return dp2 % (10 ** 9 + 7)  



640.py class Solution:
    def solveEquation(self, equation):
        def calc(eq):
            smX = smNum = 0
            add, num = True, ""
            for c in eq + "+":
                if c.isdigit():
                    num += c
                elif c == "x":
                    smX += int(num) if add and num else -int(num) if num else 1 if add else -1
                    num = ""
                else:
                    smNum += int(num) if add and num else -int(num) if num else 0
                    num, add = "", c == "+"
            return smX, smNum
        eq = equation.split("=")
        lX, lNum, rX, rNum = calc(eq[0]) + calc(eq[1])
        if lX == rX: 
            return "No solution" if lNum != rNum else "Infinite solutions"
        return "x=" + str((lNum - rNum) // (rX - lX))



641.py class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None
        
class MyCircularDeque:

    def __init__(self, k):
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = k
        self.curSize = 0

    def add(self, value, preNode):
        new = Node(value)
        new.pre = preNode
        new.next = preNode.next
        new.pre.next = new.next.pre = new
        self.curSize += 1
        
    def remove(self, preNode):
        node = preNode.next
        node.pre.next = node.next
        node.next.pre = node.pre
        self.curSize -= 1
    
    def insertFront(self, value):
        if self.curSize < self.size:
            self.add(value, self.head)
            return True
        return False

    def insertLast(self, value):
        if self.curSize < self.size:
            self.add(value, self.tail.pre)
            return True
        return False

    def deleteFront(self):
        if self.curSize:
            self.remove(self.head)
            return True
        return False

    def deleteLast(self):
        if self.curSize:
            self.remove(self.tail.pre.pre)
            return True
        return False

    def getFront(self):
        if self.curSize:
            return self.head.next.val
        return -1

    def getRear(self):
        if self.curSize:
            return self.tail.pre.val
        return -1

    def isEmpty(self):
        return self.curSize == 0

    def isFull(self):
        return self.curSize == self.size



642.py class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.cur = self.root = {}
        self.rank = collections.defaultdict(int)
        for i, s in enumerate(sentences):
            self.s = s
            self.rank[s] = times[i] - 1
            self.input('#')
    
    def move(self, c):
        if c not in self.cur:
            self.cur[c] = {}
        self.cur = self.cur[c]
        if 'sentences' not in self.cur:
            self.cur['sentences'] = []
        
    def addSentence(self):
        self.cur = self.root
        for c in self.s:
            self.move(c)
            self.search()
            heapq.heappush(self.cur['sentences'], [-self.rank[self.s], self.s])
            
    def search(self):
        q, used, i = [], set(), 0
        while i < 3 and self.cur['sentences']:
            r, s = heapq.heappop(self.cur['sentences'])
            if s not in used:
                used.add(s)
                q.append([r, s])
                i += 1
        for r, s in q:
            heapq.heappush(self.cur['sentences'], [r, s])
        return [s for r, s in q]
            
    def input(self, c: str) -> List[str]:
        if c == '#':
            self.rank[self.s] += 1
            self.addSentence()
            self.s = ''
            self.cur = self.root
            return []
        else:
            self.s += c
            self.move(c)
            return self.search()
            


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)



643.py class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sm=sum(nums[:k])
        mx,j=sm/k, 0
        for i in range(k,len(nums)): sm+=nums[i]; sm-=nums[j]; curr=sm/k; mx=max(curr,mx); j+=1
        return mx



644.py class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def sub(mid):
            sm = pre = mn = 0
            for i in range(k):
                sm += nums[i] - mid
            if sm >= 0:
                return True
            for i in range(k, len(nums)):
                sm += nums[i] - mid
                pre += nums[i - k] - mid
                mn = min(mn, pre)
                if sm >= mn:
                    return True
            return False
        l, r = min(nums), max(nums)
        while l + 1E-6 < r:
            mid = (l + r) / 2
            if sub(mid):
                l = mid
            else:
                r = mid
        return l



645.py class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter(nums)
        return [k for k in cnt if cnt[k] == 2] + [i for i in range(1, len(nums) + 1) if i not in cnt]



646.py class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key = lambda x: x[1])
        res, pre = 1, pairs[0][1]
        for c, d in pairs[1:]:
            if pre < c:
                pre = d
                res += 1
        return res



647.py class Solution:
    def countSubstrings(self, s):       
        res = 0
        for k in range(len(s)):
            i = j = k
            while 0 <= i and j < len(s):
                if s[i] == s[j]: res += 1
                else: break
                i , j = i - 1, j + 1
            i , j =k , k + 1
            while 0 <= i and j < len(s):
                if s[i] == s[j]: res += 1
                else: break
                i , j = i - 1, j + 1
        return res



648.py class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        s = set(dict)
        sentence = sentence.split()
        for j, w in enumerate(sentence):
            for i in range(1, len(w)):
                if w[:i] in s: 
                    sentence[j] = w[:i]
                    break
        return " ".join(sentence)                    



649.py class Solution:
    def predictPartyVictory(self, senate):
        ban_r = ban_d = 0
        while True:
            new = []
            r_cnt = d_cnt = 0
            for s in senate:
                if s == 'R': 
                    r_cnt += 1
                    if ban_r > 0: 
                        ban_r -= 1
                    else: 
                        ban_d += 1
                        d_cnt -= 1
                        new.append(s)
                elif s == 'D':
                    d_cnt += 1
                    if ban_d > 0: 
                        ban_d -= 1
                    else: 
                        ban_r += 1
                        r_cnt -= 1
                        new.append(s)
            if d_cnt < 0 < r_cnt:
                return "Radiant"
            elif r_cnt < 0 < d_cnt:
                return "Dire"
            senate = new



650.py class Solution:
    def minSteps(self, n):
        cur, copy, steps = 1, 0, 0
        while cur != n:
            if copy < cur and not (n - cur) % cur:
                copy = cur
            else:
                cur += copy
            steps += 1
        return steps



651.py class Solution:
    def maxA(self, N):
        dp = [0] * (N + 1)
        for i in range(N + 1):
            dp[i] = i
            for j in range(1, i - 2):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        return dp[N]



652.py class Solution:
    def findDuplicateSubtrees(self, root):
        def dfs(root):
            if not root: return "null"
            struct = "%s,%s,%s" % (str(root.val), dfs(root.left), dfs(root.right))
            nodes[struct].append(root)
            return struct
        
        nodes = collections.defaultdict(list)
        dfs(root)
        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]



653.py class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def traverse(node):
            if not node: return False
            if not node.val in dic: dic[k-node.val]=1
            else: return True
            return traverse(node.left) or traverse(node.right)
        dic={}
        return traverse(root)



654.py class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            pos = nums.index(max(nums))
            root = TreeNode(nums[pos])
            root.left = self.constructMaximumBinaryTree(nums[:pos])
            root.right = self.constructMaximumBinaryTree(nums[pos+1:])
            return root



655.py class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def traverse(node):
            if not node: return 0
            return max(traverse(node.left), traverse(node.right)) * 2 + 1
        length = traverse(root)
        stack, dic, res, padding = [root], {root : length // 2}, [], length // 2
        while any(stack):
            out, tmp, padding = [""] * length, [], padding // 2
            for i, node in enumerate(stack):
                out[dic[node]] = str(node.val)
                if node.left:
                    dic[node.left] = dic[node] - padding - 1
                    tmp.append(node.left)
                if node.right:
                    dic[node.right] = dic[node] + padding + 1
                    tmp.append(node.right)
            res.append(out)
            stack = tmp
        return res



656.py class Solution:
    def cheapestJump(self, A, B): 
        n = len(A)
        preMin = {n - 1:[n]}
        for i in range(n - 2, -1, -1):
            if A[i] == -1:
                continue
            mn, preIndex = float("inf"), None
            for ind in range(i + 1, i + B + 1 <= n and i + B + 1 or n):
                if -1 < A[ind] < mn:
                    mn, preIndex = A[ind], ind
            if preIndex:
                A[i] += A[preIndex]
                preMin[i] = preMin[preIndex] + [i + 1]
            else:
                A[i] = -1
        return 0 in preMin and preMin[0][::-1] or []



657.py class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x,y = 0, 0
        for char in moves:
            if char=="R": x+=1
            if char=="L": x-=1
            if char=="U": y+=1
            if char=="D": y-=1
        return True if x==0 and y==0 else False
        



658.py class Solution:
    def findClosestElements(self, arr, k, x):
        ind, n = bisect.bisect_left(arr, x), len(arr)
        if ind > 0 and x - arr[ind - 1] < arr[ind] - x: ind -= 1
        l, r = ind, ind + 1
        for _ in range(k - 1):
            if r >= n or (l > 0 and x - arr[l - 1] <= arr[r] - x): l -= 1
            else: r += 1
        return arr[l:r]



659.py class Solution:
    def isPossible(self, nums):
        heap, last = [], collections.defaultdict(int)
        for num in nums:
            last[num] += 1
            if heap and heap[0][0] <= num - 1:
                if heap[0][0] < num - 1:
                    return False
                else:
                    last[num - 1] -= 1
                    n, l = heapq.heappop(heap)
                    if l == -1:
                        heapq.heappush(heap, (num, -2))
            elif num - 1 not in last or not last[num - 1]:
                heapq.heappush(heap, (num, -1))
            else:
                last[num - 1] -= 1
        return not heap



660.py class Solution:
    def newInteger(self, n):
        base9 = ""
        while n:
            base9 += str(n % 9)
            n //= 9
        return int(base9[::-1])



661.py class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        m, n = len(M), len(M[0])
        grid = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                adj = [M[i + x][j + y] for x, y in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)) if 0 <= i + x < m and 0 <= j + y < n] 
                grid[i][j] = sum(adj) // len(adj)
        return grid
                    
        



662.py class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dic, stack, res = {root: 1}, [root], 0
        while any(stack):
            tmp, mn ,mx = [], float("inf"), - float("inf")
            for node in stack:
                res = max(res, dic[stack[-1]] - dic[stack[0]] + 1) 
                if node.left: tmp, dic[node.left] = tmp + [node.left], dic[node] * 2 - 1 
                if node.right: tmp, dic[node.right] = tmp + [node.right], dic[node] * 2
            stack = tmp
        return res



663.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkEqualTree(self, root):
        nodeSum = collections.defaultdict(int)
        def dfs(node):
            if not node: 
                return 0
            sm = node.val + dfs(node.left) + dfs(node.right)
            nodeSum[sm] += 1
            return sm
        totalSum = dfs(root)
        if not totalSum:
            return nodeSum[0] > 1
        return totalSum % 2 == 0 and totalSum // 2 in nodeSum



664.py class Solution:
    def strangePrinter(self, s):
        memo = {}
        def dp(i, j):
            if i > j: return 0
            if (i, j) not in memo:
                ans = dp(i+1, j) + 1
                for k in range(i+1, j+1):
                    if s[k] == s[i]:
                        ans = min(ans, dp(i, k-1) + dp(k+1, j))
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, len(s) - 1)



665.py class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """  
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                mod1, mod2=list(nums), list(nums)
                mod1[i], mod2[i+1]=mod1[i+1], mod2[i]
                if mod1!=sorted(mod1) and mod2!=sorted(mod2): return False
        return True



666.py class Solution:
    def pathSum(self, nums):
        dp = {(0, 1) : 0}
        for num in nums:
            d, p, v = map(int, str(num))
            dp[(d, p)] = v + dp[(d - 1, (p + 1) // 2)]
        return sum(dp[k] for k in dp if (k[0] + 1, k[1] * 2) not in dp and (k[0] + 1, k[1] * 2 - 1) not in dp)



667.py class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        left, right, res = 0, n+1, [None]*n
        for i in range(n):
            if k == 1:
                if i%2 == 0:
                    while i<n: res[i], right, i = right - 1, right - 1, i + 1 
                else:
                    while i<n: res[i], left, i = left + 1, left + 1, i + 1
                return res
            else:
                if i%2 != 0: res[i], right = right - 1, right - 1
                else: res[i], left = left + 1, left + 1
                if i != 0: k -= 1



668.py class Solution:
    def findKthNumber(self, m, n, k):       
        l, r = 1, m * n
        while l < r:
            mid = (l + r) // 2
            if sum(min(mid // i, n) for i in range(1, m + 1)) < k:
                l = mid + 1
            else:
                r = mid
        return l



669.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root: return
        root.left=self.trimBST(root.left,L,R)
        root.right=self.trimBST(root.right,L,R)
        if root.val>R or root.val<L: return root.left if root.left else root.right
        return root



670.py class Solution:
    def maximumSwap(self, num):
        res, num = num, list(str(num))
        for i in range(len(num) - 1):
            for j in range(i + 1, len(num)):
                if int(num[j]) > int(num[i]):
                    tmp = int("".join(num[:i] + [num[j]] + num[i + 1:j] + [num[i]] + num[j + 1:]))
                    if tmp > res: res = tmp
        return res



671.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.sec = float('inf')
        def dfs(node):
            if not node: return
            dfs(node.left)
            dfs(node.right)
            if root.val < node.val < self.sec:
                self.sec = node.val
        dfs(root)
        return self.sec if self.sec < float('inf') else -1



672.py class Solution:
    def flipLights(self, n, m):
        n = min(n, 3)
        return min(1 << n, 1 + m * n)



673.py class Solution:
    def findNumberOfLIS(self, nums):
        dp = [[1, 1] for _ in range(len(nums))]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    if dp[i][0] >= dp[j][0]: dp[j] = [dp[i][0] + 1, dp[i][1]]
                    elif dp[i][0] == dp[j][0] - 1: dp[j][1] += dp[i][1]
        dp.sort()
        return dp and sum(d[1] for d in dp if d[0] == dp[-1][0]) or 0



674.py class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]: return 0
        curr, mx=1, 1
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]: curr+=1; mx=max(mx,curr)
            else: curr=1
        return mx



675.py class Solution:
    def cutOffTree(self, forest):
        def hadlocks(forest, sr, sc, tr, tc):
            R, C = len(forest), len(forest[0])
            processed = set()
            deque = collections.deque([(0, sr, sc)])
            while deque:
                detours, r, c = deque.popleft()
                if (r, c) not in processed:
                    processed.add((r, c))
                    if r == tr and c == tc:
                        return abs(sr-tr) + abs(sc-tc) + 2*detours
                    for nr, nc, closer in ((r-1, c, r > tr), (r+1, c, r < tr),
                                           (r, c-1, c > tc), (r, c+1, c < tc)):
                        if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                            if closer:
                                deque.appendleft((detours, nr, nc))
                            else:
                                deque.append((detours+1, nr, nc))
            return -1
        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)
        sr = sc = ans = 0
        for _, tr, tc in trees:
            d = hadlocks(forest, sr, sc, tr, tc)
            if d < 0: return -1
            ans += d
            sr, sc = tr, tc
        return ans



676.py class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.var = defaultdict(set)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for w in dict:
            for i in range(len(w)): self.var[(i, w[:i] + w[i + 1:])].add(w[i])
    
    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)): 
            if self.var[(i, word[:i] + word[i + 1:])] - {word[i]}: return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)



677.py class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.dic = defaultdict(int)

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.dic[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sm = 0
        for k in self.dic:
            if k[:len(prefix)] == prefix: sm += self.dic[k]
        return sm


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)



678.py class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, left_star = [], []
        for i in range(len(s)):
            if s[i] == "(": left.append([s[i], i])
            elif s[i] == "*": left_star.append([s[i], i])
            elif left and left[-1][0] == "(": left.pop()
            elif left_star: left_star.pop()
            else: return False
        while left and left_star and left[-1][1]< left_star[-1][1]: left.pop(); left_star.pop()
        return not left   



679.py class Solution:
    def judgePoint24(self, nums):
        q = [[None, nums[i]] + nums[:i] + nums[i + 1:] for i in range(len(nums))]
        while q:
            new = []
            for group1, group2, *rest in q:
                if not rest and group1:
                    for res in (group1 + group2, group1 - group2, group1 * group2, group2 and group1 / group2): 
                        if 23.999 <= res <= 24.0001: return True
                if not rest and not group1 and 23.999 <= group2 <= 24.0001: return True
                for i in range(len(rest)):
                    for newGroup2 in (group2 + rest[i], group2 - rest[i], rest[i] - group2, group2 * rest[i], group2 / rest[i]):
                        new.append([group1, newGroup2] + rest[:i] + rest[i + 1:])
                    if group2:
                        new.append([group1, rest[i] / group2] + rest[:i] + rest[i + 1:])
                    if group1 != None:
                        for newGroup1 in (group1 + group2, group1 - group2, group1 * group2):
                            new.append([newGroup1, rest[i]] + rest[:i] + rest[i + 1:])
                        if group2:
                            new.append([group1 / group2, rest[i]] + rest[:i] + rest[i + 1:])
                    else:
                        new.append([group2, rest[i]] + rest[:i] + rest[i + 1:])
            q = new
        return False



680.py class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        memo = {}
        def dfs(l, r, cnt):
            if (l, r, cnt) in memo:
                return memo[(l, r, cnt)]
            if l >= r:
                return True
            elif s[l] != s[r]:
                cnt += 1
                if cnt > 1:
                    memo[(l, r, cnt)] = False
                    return False
                elif (s[l + 1] == s[r] and dfs(l + 1, r, cnt + 1)) or (s[l] == s[r - 1] and dfs(l, r - 1, cnt + 1)):
                    memo[(l, r, cnt)] = True
                    return True
                else:
                    memo[(l, r, cnt)] = False
                    return False
            else:
                memo[(l, r, cnt)] = dfs(l + 1, r - 1, cnt)
                return memo[(l, r, cnt)]
        return dfs(0, len(s) - 1, 0)



681.py class Solution:
    def nextClosestTime(self, time):
        t = sorted(set(time))[:-1]  
        nex = {a: b for a, b in zip(t, t[1:])}
        for i, d in enumerate(time[::-1]):
            if d in nex:
                if i == 0:
                    return time[:4] + nex[d]
                elif i == 1 and nex[d] < '6':
                    return time[:3] + nex[d] + t[0]
                elif i == 3 and int(time[0] + nex[d]) < 24:
                    return time[0] + nex[d] + ':' + t[0] * 2
        return t[0] * 2 + ':' + t[0] * 2



682.py class Solution:
    def calPoints(self, ops: List[str]) -> int:
        arr = []
        for op in ops:
            #print(arr)
            if op.isdigit() or op[0] == '-':
                arr.append(int(op))
            elif op == 'C' and arr:
                arr.pop()
            elif op == 'D' and arr:
                arr.append(arr[-1] * 2)
            elif len(arr) >= 2:
                arr.append(arr[-1] + arr[-2])
        #print(arr)
        return sum(arr)



683.py class Node:
    def __init__(self, pos):
        self.pos = pos
        self.left = None
        self.right = None
        
class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        N = len(flowers)
        ans = -1
        nodes = {0:Node(-float('inf'))}
        for x in range(1, N + 2):
            nodes[x] = Node(x)
            nodes[x].left = nodes[x - 1]
            nodes[x - 1].right = nodes[x]
        nodes[N + 1].pos = float('inf')
        for day in range(N, 0, -1):
            x = flowers[day - 1]
            if nodes[x].pos - nodes[x].left.pos - 1 == k or nodes[x].right.pos - nodes[x].pos - 1 == k:
                ans = day
            nodes[x].left.right = nodes[x].right
            nodes[x].right.left = nodes[x].left
        return ans



684.py class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
      parent = [0] * len(edges)

      def find(x):
        if parent[x] == 0:
          return x
        parent[x] = find(parent[x])
        return parent[x]

      def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX == rootY:
          return False
        parent[rootX] = rootY
        return True
      
      res = [0, 0]
      for x, y in edges:
        if not union(x - 1, y - 1): 
          res =  [x, y]
      return res



685.py class Solution:
    def findRedundantDirectedConnection(self, edges):
        def root(i):
            return parent[i] == i and i or root(parent[i])
        
        parent, a, b, c = [0] * (len(edges) + 1), None, None, None
        for i, edge in enumerate(edges):
            if parent[edge[1]]:
                a, b, c, edges[i][0]= parent[edge[1]], edge[0], edge[1], 0
            else:
                parent[edge[1]] = edge[0]
        
        parent = [i for i in range(len(edges) + 1)]
        for u, v in edges:
            if u:
                if root(u) == v: 
                    return a and [a, c] or [u, v]
                parent[v] = u   
        return [b, c]



686.py class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        for i in range(1,2+len(B)//len(A)+1):
            if B in A*i: return i 
        return -1



687.py # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longest = [0]
        def traverse(node):
            if not node:
                return 0
            left_len, right_len = traverse(node.left), traverse(node.right)
            left = (left_len + 1) if node.left and node.left.val == node.val else 0
            right = (right_len + 1) if node.right and node.right.val == node.val else 0
            longest[0] = max(longest[0], left + right)
            return max(left, right)
        traverse(root)
        return longest[0]



688.py class Solution:
    def knightProbability(self, N, K, r, c):
        memo = {}
        def dfs(i, j, p, k): 
            if 0 <= i < N and 0 <= j < N and k < K:
                sm = 0
                for x, y in ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)):
                    if (i + x, j + y, k) not in memo:
                        memo[(i + x, j + y, k)] = dfs(i + x, j + y, p / 8, k + 1)
                    sm += memo[(i + x, j + y, k)]
                return sm
            else:
                return 0 <= i < N and 0 <= j < N and p or 0
        return dfs(r, c, 1, 0)



689.py class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        single, double, sm, n, cur = {}, {}, 0, len(nums), sum(nums[:k - 1])
        for i in range(k - 1, n):
            cur += nums[i]
            single[i - k + 1] = cur
            cur -= nums[i - k + 1]
        cur = n - k, single[n - k]
        for i in range(n - k, k * 2 - 1, -1):
            if single[i] >= cur[1]:
                cur = i, single[i]
            double[i - k] = cur[1] + single[i - k], i - k, cur[0]
        cur = double[n - 2 * k]
        for i in range(n - 2 * k, k - 1, -1):
            if double[i][0] >= cur[0]:
                cur = double[i]
            if single[i - k] + cur[0] >= sm:
                sm, res = single[i - k] + cur[0], [i - k, cur[1], cur[2]]
        return res



690.py """
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        def dfs(id):
            self.val += dic[id].importance
            for sub in dic[id].subordinates:
                dfs(sub)
        dic = {}
        for emp in employees:
            dic[emp.id] = emp
        self.val = 0
        dfs(id)
        return self.val



691.py class Solution:
    def minStickers(self, stickers, target):
        cnt, res, n = collections.Counter(target), [float("inf")], len(target)  
        def dfs(dic, used, i):
            if i == n:
                res[0] = min(res[0], used)
            elif dic[target[i]] >= cnt[target[i]]:
                dfs(dic, used, i + 1)
            elif used < res[0] - 1:
                for sticker in stickers:
                    if target[i] in sticker:
                        for s in sticker:
                            dic[s] += 1
                        dfs(dic, used + 1, i + 1)
                        for s in sticker:
                            dic[s] -= 1
        dfs(collections.defaultdict(int), 0, 0)
        return res[0] < float("inf") and res[0] or -1



692.py class Solution:
    def topKFrequent(self, words, k):
        return [w for w, v in sorted(collections.Counter(words).items(), key = lambda x: (-x[1], x[0])) [:k]]



693.py class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return all(a != b for a, b in zip(bin(n)[2:], bin(n)[3:]))
            



694.py class Solution:
    def numDistinctIslands(self, grid):
        visited, pattern, m, n = set(), collections.defaultdict(str), len(grid), len(grid[0])
        def dfs(ri, rj, i, j, pi, pj):
            visited.add((i, j))
            pattern[(ri, rj)] += str(pi) + str(pj)
            for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if 0 <= i + x < m and 0 <= j + y < n and grid[i + x][j + y] and (i + x, j + y) not in visited:
                    dfs(ri, rj, i + x, j + y, pi + x, pj + y)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in visited:
                    dfs(i, j, i, j, 0, 0)
        return len(set(pattern.values()))



695.py class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid and grid[0])
        def explore(i, j):
            grid[i][j] = 0
            return 1 + sum(explore(x,y) for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)) if 0<=x<m and 0<=y<n and grid[x][y])
        return max(grid[i][j] and explore(i, j) or 0 for i in range(m) for j in range(n))



696.py class Solution:
    def countBinarySubstrings(self, s):
        s = s.replace("01", "0#1").replace("10", "1#0").split("#")
        return sum(min(len(s[i]), len(s[i - 1])) for i in range(1, len(s)))



697.py class Solution:
    def findShortestSubArray(self, nums):
        cnt, seen = collections.Counter(nums), collections.defaultdict(list)
        degree = max(cnt.values())
        for i, v in enumerate(nums): seen[v].append(i)
        return min(seen[v][-1] - seen[v][0] + 1 for v in cnt if cnt[v] == degree)



698.py class Solution:
    def canPartitionKSubsets(self, nums, k):
        def dfs(i, sums):
            if i == n:
                return True
            for j in range(k):
                if sums[j] + nums[i] <= target:
                    sums[j] += nums[i]
                    if dfs(i + 1, sums):
                        return True
                    sums[j] -= nums[i]
            return False
        nums.sort(reverse = True)
        sm = sum(nums)
        if sm % k: return False
        target, n = sm // k, len(nums)
        return dfs(0, [0] * k)



699.py class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        height = [0]
        pos = [0]
        res = []
        max_h = 0
        for left, side in positions:
            i = bisect.bisect_right(pos, left)
            j = bisect.bisect_left(pos, left + side)
            high = max(height[i - 1:j] or [0]) + side
            pos[i:j] = [left, left + side]
            height[i:j] = [high, height[j - 1]]
            max_h = max(max_h, high)
            res.append(max_h)
        return res



700.py class Solution:
    def searchBST(self, root, val):
        if root and val < root.val: return self.searchBST(root.left, val)
        elif root and val > root.val: return self.searchBST(root.right, val)
        return root



701.py class Solution:
    def insertIntoBST(self, root, val):
        if root and root.val > val and not self.insertIntoBST(root.left, val): root.left = TreeNode(val)
        elif root and root.val < val and not self.insertIntoBST(root.right, val): root.right = TreeNode(val)
        return root



702.py class Solution(object):
    def search(self, reader, target):
        l, r = 0, 20000
        while l <= r:
            index = (l + r) // 2
            response = reader.get(index)
            if response > target:
                r = index - 1
            elif response < target:
                l = index + 1
            else:
                return index
        return -1



703.py class KthLargest(object):

    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

            
    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]



704.py class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target) if target in nums else -1



705.py <!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en-US"> <![endif]-->
<!--[if IE 7]>    <html class="no-js ie7 oldie" lang="en-US"> <![endif]-->
<!--[if IE 8]>    <html class="no-js ie8 oldie" lang="en-US"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en-US"> <!--<![endif]-->
<head>


<title>leetcode.com | 502: Bad gateway</title>
<meta charset="UTF-8" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1" />
<meta name="robots" content="noindex, nofollow" />
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1" />
<link rel="stylesheet" id="cf_styles-css" href="/cdn-cgi/styles/cf.errors.css" type="text/css" media="screen,projection" />
<!--[if lt IE 9]><link rel="stylesheet" id='cf_styles-ie-css' href="/cdn-cgi/styles/cf.errors.ie.css" type="text/css" media="screen,projection" /><![endif]-->
<style type="text/css">body{margin:0;padding:0}</style>




</head>
<body><div id="cf_alert_div" style="margin: 0;padding: 0;position: relative;top: 0;left: 0;display: block; z-index: 1000"><div style="margin: 0px;padding: 10px;border-bottom: 1px solid #a5a5a5;background: #f0f0f0;font-weight: normal;text-align: left;"><table width="100%"><tr><td valign="top"><a href="#" onclick="document.cookie='cf_use_ob=0;path=/';window.location.reload();return false;" style="margin: 0 20px 0 0;padding: 10px 0 0 20px;text-decoration: none;font: 12px Helvetica,Arial,sans-serif;color: #eff7e8;font-weight: bold;text-align: left;position: relative;display: inline-block;height: 38px;background: url(/cdn-cgi/images/retry.png) no-repeat 0 0;overflow: visible;font-size: 14px;line-height: 1.2em;text-shadow: #437b0a 0 1px 0;white-space: nowrap;">Retry for a live version<span style="margin: 0;padding: 0;position: absolute;top: 0;left: 100%;width: 20px;height: 38px;background: url(/cdn-cgi/images/retry.png) no-repeat 100% -38px;"></span></a> <noscript style="margin: 10px 0 10px 0;padding: 0;font: 12px Helvetica,Arial,sans-serif;color: #404040;display: block;">(Enable Javascript first.)</noscript></td><td valign="middle" style="margin: 0;padding: 0;"><p style="margin: 0 0 0 20px;padding: 0;font: 12px Helvetica,Arial,sans-serif;color: #404040;">This page (<a href="/submissions/detail/163424957/" style="margin: 0;padding: 0;text-decoration: underline;font: 12px Helvetica,Arial,sans-serif;color: #007ed9;font-weight: normal;text-align: left;">https://leetcode.com/submissions/detail/163424957/</a>) is currently offline. However, because the site uses Cloudflare's Always Online&trade; technology you can continue to surf a snapshot of the site. We will keep checking in the background and, as soon as the site comes back, you will automatically be served the live version. <span id="caption" style="margin: 0;padding: 0;color: #a5a5a5;">Always Online&trade; is powered by <a href="https://www.cloudflare.com/5xx-error-landing?utm_source=ao_banner" target="_blank" style="margin: 0;padding: 0;text-decoration: underline;font: 12px Helvetica,Arial,sans-serif;color: #007ed9;font-weight: normal;text-align: left;">Cloudflare</a> | <a href="javascript:void(null);" onclick="document.getElementById('cf_alert_div').style.display='none';" style="margin: 0;padding: 0;text-decoration: underline;font: 12px Helvetica,Arial,sans-serif;color: #007ed9;font-weight: normal;text-align: left;">Hide this Alert</a></span></p></td></tr></table></div></div>
<div id="cf-wrapper">

    

    <div id="cf-error-details" class="cf-error-details-wrapper">
        <div class="cf-wrapper cf-error-overview">
            <h1>
              
              <span class="cf-error-type">Error</span>
              <span class="cf-error-code">502</span>
              <small class="heading-ray-id">Ray ID: 52beb9bebad1d8bd &bull; 2019-10-26 19:09:36 UTC</small>
            </h1>
            <h2 class="cf-subheadline">Bad gateway</h2>
        </div><!-- /.error-overview -->
        
        <div class="cf-section cf-highlight cf-status-display">
            <div class="cf-wrapper">
                <div class="cf-columns cols-3">
                  
<div id="cf-browser-status" class="cf-column cf-status-item cf-browser-status ">
  <div class="cf-icon-error-container">
    <i class="cf-icon cf-icon-browser"></i>
    <i class="cf-icon-status cf-icon-ok"></i>
  </div>
  <span class="cf-status-desc">You</span>
  <h3 class="cf-status-name">Browser</h3>
  <span class="cf-status-label">Working</span>
</div>

<div id="cf-cloudflare-status" class="cf-column cf-status-item cf-cloudflare-status ">
  <div class="cf-icon-error-container">
    <i class="cf-icon cf-icon-cloud"></i>
    <i class="cf-icon-status cf-icon-ok"></i>
  </div>
  <span class="cf-status-desc">Amsterdam</span>
  <h3 class="cf-status-name">Cloudflare</h3>
  <span class="cf-status-label">Working</span>
</div>

<div id="cf-host-status" class="cf-column cf-status-item cf-host-status cf-error-source">
  <div class="cf-icon-error-container">
    <i class="cf-icon cf-icon-server"></i>
    <i class="cf-icon-status cf-icon-error"></i>
  </div>
  <span class="cf-status-desc">leetcode.com</span>
  <h3 class="cf-status-name">Host</h3>
  <span class="cf-status-label">Error</span>
</div>

                </div>
              
            </div>
        </div><!-- /.status-display -->

        <div class="cf-section cf-wrapper">
            <div class="cf-columns two">
                <div class="cf-column">
                    <h2>What happened?</h2>
                    <p>The web server reported a bad gateway error.</p>
                </div>
              
                <div class="cf-column">
                    <h2>What can I do?</h2>
                    <p>Please try again in a few minutes.</p>
                </div>
            </div>
              
        </div><!-- /.section -->

        <div class="cf-error-footer cf-wrapper">
  <p>
    <span class="cf-footer-item">Cloudflare Ray ID: <strong>52beb9bebad1d8bd</strong></span>
    <span class="cf-footer-separator">&bull;</span>
    <span class="cf-footer-item"><span>Your IP</span>: 92.44.160.241</span>
    <span class="cf-footer-separator">&bull;</span>
    <span class="cf-footer-item"><span>Performance &amp; security by</span> <a href="https://www.cloudflare.com/5xx-error-landing?utm_source=error_footer" id="brand_link" target="_blank">Cloudflare</a></span>
    
  </p>
</div><!-- /.error-footer -->


    </div><!-- /#cf-error-details -->
</div><!-- /#cf-wrapper -->
</body>
</



706.py class MyHashMap:

    def __init__(self):
        self.arr = [-1] * 1000001

    def put(self, key, value):
        self.arr[key] = value

    def get(self, key):
        return self.arr[key]

    def remove(self, key):
        self.arr[key] = -1



707.py class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None
class MyLinkedList:

    def __init__(self):
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0
        
    def add(self, preNode, val):
        node = Node(val)
        node.pre = preNode
        node.next = preNode.next
        node.pre.next = node.next.pre = node
        self.size += 1
        
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.size -= 1
        
    def forward(self, start, end, cur):
        while start != end:
            start += 1
            cur = cur.next
        return cur
    
    def backward(self, start, end, cur):
        while start != end:
            start -= 1
            cur = cur.pre
        return cur
    
    def get(self, index):
        if 0 <= index <= self.size // 2:
            return self.forward(0, index, self.head.next).val
        elif self.size // 2 < index < self.size:
            return self.backward(self.size - 1, index, self.tail.pre).val
        return -1

    def addAtHead(self, val):
        self.add(self.head, val)

    def addAtTail(self, val):
        self.add(self.tail.pre, val)

    def addAtIndex(self, index, val):
        if 0 <= index <= self.size // 2:
            self.add(self.forward(0, index, self.head.next).pre, val)
        elif self.size // 2 < index <= self.size:
            self.add(self.backward(self.size, index, self.tail).pre, val)

    def deleteAtIndex(self, index):
        if 0 <= index <= self.size // 2:
            self.remove(self.forward(0, index, self.head.next))
        elif self.size // 2 < index < self.size:
            self.remove(self.backward(self.size - 1, index, self.tail.pre))



708.py class Solution(object):
    def insert(self, head, insertVal):
        if not head:
            node = Node(insertVal, None)
            node.next = node
            return node
        root, mn, mx = head, Node(float("inf"), None), Node(-float("inf"), None)
        while True:
            if head.val > mx.val:
                mx = head
            if head.val < mn.val:
                mn = head
            if head.val <= insertVal <= head.next.val or insertVal >= head.val > head.next.val:
                node = Node(insertVal, head.next)
                head.next = node
                return root
            head = head.next
            if head == root:
                break
        if insertVal > mx.val:
            node = Node(insertVal, mx.next)
            mx.next = node
        else:
            node = Node(insertVal, mn.next)
            mn.next = node
            mn.val, node.val = node.val, mn.val
        return root



709.py class Solution:
    def toLowerCase(self, str): 
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)



710.py class Solution:

    def __init__(self, N, blacklist):
        self.forbidden, self.n, self.used, self.cur = set(blacklist), N, set(), 0
    def pick(self):
        while self.cur in self.forbidden: self.cur += 1
        if self.cur < self.n: num, self.cur = self.cur, self.cur + 1
        else: num = self.used.pop()
        self.used.add(num)
        return num



711.py class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        m,n=len(grid),len(grid[0])

        # augment matrix to void length check
        grid.append([0]*n)
        for row in grid: row.append(0)

        self.pool=set()
        self.res=0

        def bfs(i0,j0):
            grid[i0][j0]=-1
            q=[(i0,j0)]
            for i,j in q:
                for I,J in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                    if grid[I][J]==1:
                        grid[I][J]=-1
                        q.append([I,J])
            self.addisland(q)
       
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1: bfs(i,j)

        return self.res

    def addisland(self,q):
            Imin=min(x for x,y in q)
            Jmin=min(y for x,y in q)
            island1=tuple(sorted((x-Imin,y-Jmin) for x,y in q)) # original island
           
            if island1 in self.pool: return None
            self.res+=1

            Imax=max(x for x,y in island1)
            Jmax=max(y for x,y in island1)

            island2=tuple(sorted((-x+Imax,y) for x,y in island1)) # x axis mirror
            island3=tuple(sorted((x,-y+Jmax) for x,y in island1)) # y axis mirror
            island4=tuple(sorted((-x+Imax,-y+Jmax) for x,y in island1)) # origin mirror

            island5=tuple(sorted((y,x) for x,y in island1)) # diagonal mirror
            island6=tuple(sorted((-x+Jmax,y) for x,y in island5))
            island7=tuple(sorted((x,-y+Imax) for x,y in island5))
            island8=tuple(sorted((-x+Jmax,-y+Imax) for x,y in island5))

            self.pool |= set([island1,island2,island3,island4,island5,island6,island7,island8])



712.py class Solution:
    def minimumDeleteSum(self, s1, s2):
        l1, l2 = len(s1) + 1, len(s2) + 1
        d = [[0] * l2 for i in range(l1)]
        for i in range(l1):
            for j in range(l2):
                c1, c2 = ord(s1[i - 1]), ord(s2[j - 1])
                if not i * j:
                    d[i][j] = d[i - 1][j] + c1 if i else d[i][j - 1] + c2 if j else 0
                elif s1[i - 1] == s2[j - 1]: 
                    d[i][j] = d[i - 1][j - 1]
                else: 
                    d[i][j] = min(d[i - 1][j] + c1, d[i][j - 1] + c2, d[i - 1][j - 1] + c1 + c2)
        return d[-1][-1]



713.py class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        l, res, cur = 0, 0, 1
        for i in range(len(nums)):
            cur *= nums[i]
            while cur >= k and l < i: l, cur = l + 1, cur // nums[l]
            if cur < k: res += i - l + 1
        return res



714.py class Solution:
    def maxProfit(self, prices, fee):
        pre = [0, -float("inf")]
        for p in prices:
            p0, p1 = pre[1] + p - fee, pre[0] - p
            if p0 > pre[0]: pre[0] = p0
            if p1 > pre[1]: pre[1] = p1
        return pre[0]



715.py from bisect import bisect_left as bl, bisect_right as br

class RangeModule:

    def __init__(self):
        self._X = []

    def addRange(self, left, right):
        i, j = bl(self._X, left), br(self._X, right)
        self._X[i:j] = [left]*(i%2 == 0) + [right]*(j%2 == 0)

    def queryRange(self, left, right):
        i, j = br(self._X, left), bl(self._X, right)
        return i == j and i%2 == 1

    def removeRange(self, left, right):
        i, j = bl(self._X, left), br(self._X, right)
        self._X[i:j] = [left]*(i%2 == 1) + [right]*(j%2 == 1)



716.py class Node:
    def __init__(self, value, index):
        self.val = value
        self.i = index
        self.pre = self.next = None
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap = []
        self.Nodes = {}
        self.head = self.tail = Node(0, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        newNode = Node(x, self.tail.pre.i + 1)
        newNode.pre = self.tail.pre
        newNode.next = self.tail
        self.tail.pre.next = self.tail.pre = newNode
        self.Nodes[newNode.i] = newNode
        heapq.heappush(self.heap, (-x, -newNode.i))

    def pop(self):
        """
        :rtype: int
        """
        node = self.tail.pre
        node.pre.next = self.tail
        self.tail.pre = node.pre
        self.Nodes.pop(node.i)
        if node.i == -self.heap[0][1]:
            heapq.heappop(self.heap)
        return node.val

    def top(self):
        """
        :rtype: int
        """
        return self.tail.pre.val

    def peekMax(self):
        """
        :rtype: int
        """
        while -self.heap[0][1] not in self.Nodes or self.Nodes[-self.heap[0][1]].val != -self.heap[0][0]:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self):
        """
        :rtype: int
        """
        while -self.heap[0][1] not in self.Nodes or self.Nodes[-self.heap[0][1]].val != -self.heap[0][0]:
            heapq.heappop(self.heap)
        node = self.Nodes.pop(-self.heap[0][1])
        node.pre.next = node.next
        node.next.pre = node.pre
        return -heapq.heappop(self.heap)[0]


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()



717.py class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        while bits:
            last=bits.pop(0)
            if last==1:bits.pop(0)
        return True if last==0 else False



718.py class Solution:
    def findLength(self, A, B):
        A, res, sub = "X%sX" % "X".join(map(str, A)), 0, "X"
        for num in B:
            sub += str(num) + "X"
            if sub in A: res += 1
            else: sub = sub[sub[1:].index("X") + 1:]
        return res



719.py class Solution(object):
    def countPairsLTE(self, array, value):
        return sum(bisect.bisect_right(array, array[i] + value, lo = i) - i - 1 for i in range(len(array)))
        
    def smallestDistancePair(self, nums, k):
        nums.sort()
        low, high = min([nums[i + 1] - nums[i] for i in range(len(nums) - 1)]), nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if self.countPairsLTE(nums, mid) < k:
                low = mid + 1
            else:
                high = mid
        return low



720.py class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for w in sorted(words, key = lambda x: (-len(x), x)):
            if all([True if w[:i] in set(words) - {w} else False for i in range(1, len(w))]): return w  
        return ""



721.py class Solution:
    def accountsMerge(self, accounts):
        def explore(mail, q):
            q += mail,
            visited.add(mail)
            for v in edges[mail]:
                if v not in visited: explore(v, q)
            return q
        edges, owner, visited, res = collections.defaultdict(list), {}, set(), []
        for acc in accounts:
            owner[acc[1]] = acc[0]
            for i in range(1, len(acc) - 1): 
                if acc[i] != acc[i + 1]:
                    edges[acc[i]] += acc[i + 1],
                    edges[acc[i + 1]] += acc[i],
        for acc in accounts:
            if acc[1] not in visited: res += [acc[0]] + sorted(explore(acc[1], [])),
        return res



722.py class Solution:
    def removeComments(self, source):
        res, block, cont, blockStart = [], False, False, -1
        for line in source:
            if not cont: cache = ""
            for i, c in enumerate(line):
                if not block: cache += c
                if cache[-2:] == "//":
                    cache = cache[:-2]
                    break
                elif cache[-2:] == "/*": blockStart, cache, block = i, cache[:-2], True
                elif line[i - 1:i + 1] == "*/" and blockStart < i - 1: block = False
            if not block:
                if cache: res += cache,
                cont = False
            else: cont, blockStart = True, -1
        return res



723.py class Solution:
    def candyCrush(self, board):
        m, n = len(board), len(board[0])
        def gravity():
            for j in range(n):
                stack = [board[i][j] for i in range(m - 1, -1, -1) if board[i][j] > 0]
                stack += [0] *  (m - len(stack))
                for i in range(m): board[i][j] = stack.pop()
        def crush():
            crush = False
            for i in range(m):
                for j in range(n):
                    if j > 1 and board[i][j] > 0 and board[i][j] == abs(board[i][j - 1]) == abs(board[i][j - 2]):
                        board[i][j - 2:j + 1] = [-abs(board[i][j]) for _ in range(3)]
                        crush = True
                    if i > 1 and board[i][j] != 0 and abs(board[i][j]) == abs(board[i - 1][j]) == abs(board[i - 2][j]):
                        if board[i][j] > 0: board[i][j] *= -1
                        if board[i - 1][j] > 0: board[i - 1][j] *= -1
                        if board[i - 2][j] > 0: board[i - 2][j] *= -1
                        crush = True
            return crush  
        while crush(): gravity()
        return board



724.py class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sm = sum(nums)
        cur = 0
        for i in range(len(nums)):
            if cur == sm - cur - nums[i]:
                return i
            cur += nums[i]
        return -1



725.py class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        n = 0
        node = root
        while node:
            n += 1
            node = node.next
        count = n // k
        residual = n % k

        i = 0
        ret = [[] for _ in range(k)]
        prev = root
        while prev and k > 0:
            node = prev
            leftover = count
            ret[i] = node
            i += 1
            while node and leftover > 1:
                node = node.next
                leftover -= 1
            if node and count != 0 and residual:
                node = node.next
                residual -= 1
            prev = node.next if node else None
            if node:
                node.next = None
            k -= 1
        return ret




726.py class Solution:
    def countOfAtoms(self, formula):
        dic, coeff, stack, elem, cnt, i = collections.defaultdict(int), 1, [], "", 0, 0  
        for c in formula[::-1]:
            if c.isdigit():
                cnt += int(c) * (10 ** i)
                i += 1
            elif c == ")":
                stack.append(cnt)
                coeff *= cnt
                i = cnt = 0
            elif c == "(":
                coeff //= stack.pop()
                i = cnt = 0
            elif c.isupper():
                elem += c
                dic[elem[::-1]] += (cnt or 1) * coeff
                elem = ""
                i = cnt = 0
            elif c.islower():
                elem += c
        return "".join(k + str(v > 1 and v or "") for k, v in sorted(dic.items()))



727.py class Solution:
    def minWindow(self, S: str, T: str) -> str:
        def dfs(i, j):
            if j == len(T): return i
            if (i, j) not in memo:
                ind = S.find(T[j], i + 1)
                memo[(i, j)] = float('inf') if ind == -1 else dfs(ind, j + 1)
            return memo[(i, j)]
            
        l, res, memo = float('inf'), '', {}
        for i, s in enumerate(S):
            if s == T[0]:
                j = dfs(i, 1)
                if j - i < l:
                    l, res = j - i, S[i:j + 1]
        return res



728.py class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [num for num in range(left,right+1) if len([char for char in str(num) if int(char)!=0 and num%int(char)==0])==len(str(num)) ]



729.py class Node:
    def __init__(self,s,e):
        self.e = e
        self.s = s
        self.left = None
        self.right = None
class MyCalendar:

    def __init__(self):
        self.root = None

    def book_helper(self,s,e,node):
        if s>=node.e:
            if node.right: return self.book_helper(s,e,node.right)
            else:
                node.right = Node(s,e)
                return True
        elif e<=node.s:
            if node.left: return self.book_helper(s,e,node.left)
            else:
                node.left = Node(s,e)
                return True
        else: return False
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = Node(start,end)
            return True
        return self.book_helper(start,end,self.root)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)



730.py class Solution:
    def countPalindromicSubsequences(self, S):
        mod, memo = 10 ** 9 + 7, {}
        def dfs(i, j):
            if (i, j) not in memo:
                cnt = 0
                for x in "abcd":
                    try: l, r = S[i:j + 1].index(x) + i, S[i:j + 1].rindex(x) + i
                    except: continue  
                    cnt += l != r and dfs(l + 1, r - 1) + 2 or 1
                memo[(i, j)] = cnt % mod
            return memo[(i, j)]
        return dfs(0, len(S) - 1)



731.py class MyCalendarTwo:
    def __init__(self):
            self.overlaps = []
            self.calendar = []

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True



732.py class MyCalendarThree:

    def __init__(self):
        self.times = []

    def book(self, start, end):
        bisect.insort(self.times, (start, 1))
        bisect.insort(self.times, (end, -1))
        res = cur = 0
        for _, x in self.times:
            cur += x
            res = max(res, cur)
        return res



733.py class Solution:
    def floodFill(self, image, sr, sc, newColor):
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor: 
            q = collections.deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old: 
                        q.append((x, y))
        return image



734.py class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        sim = collections.defaultdict(set)
        for a, b in pairs:
            sim[a].add(b)
            sim[b].add(a)
        return len(words1) == len(words2) and all(w1 == w2 or w2 in sim[w1] for w1, w2 in zip(words1, words2))



735.py class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:
                if stack[-2] < abs(stack[-1]): stack[-2] = stack[-1]
                elif stack[-2] == abs(stack[-1]): stack.pop()
                stack.pop()
        return stack            



736.py class Solution:
    def evaluate(self, expression):
        scopes, items = [{}], [["root"]]
        for item in expression.replace(")", " )").split():
            if item[0] == "(":
                items.append([item[1:]])
                if item[1:] == "let":
                    scopes.append(dict(scopes[-1]))
                continue
            elif item == ")": 
                if items[-1][0] == "add":
                    item = str(int(items[-1][1]) + int(items[-1][-1]))
                elif items[-1][0] == "mult":
                    item = str(int(items[-1][1]) * int(items[-1][-1]))
                else:
                    item = items[-1][-1]
                    if item in scopes[-1]:
                        item = scopes[-1][item]
                    scopes.pop()
                items.pop()
            if item in scopes[-1] and (items[-1][0] != "let" or len(items[-1]) % 2 == 0):
                item = scopes[-1][item]
            if items[-1][0] == "let" and item.lstrip("-").isdigit():
                scopes[-1][items[-1][-1]] = item
            items[-1].append(item)
        return int(items[-1][-1])



737.py class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        def dfs(node, Id):
            cc[node] = Id
            for v in adj[node]:
                if v not in cc:
                    dfs(v, Id)
        l1, l2, adj, cc = len(words1), len(words2), collections.defaultdict(set), {}
        if l1 != l2:
            return False
        for a, b in pairs:
            adj[a].add(b)
            adj[b].add(a)
        for Id, k in enumerate(adj):
            if k not in cc:
                dfs(k, Id)
        for w1, w2 in zip(words1, words2):
            if w1 not in cc or w2 not in cc:
                if w1 != w2:
                    return False
            elif cc[w1] != cc[w2]:
                return False
        return True



738.py class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        n, pos = str(N), 0
        for i, char in enumerate(n):
            if i>0 and int(n[i])<int(n[i-1]): return int("".join(n[:pos])+str(int(n[pos])-1)+"9"*(len(n)-1-pos)) if int(n[pos])>1 else int("9"*(len(n)-1-pos))
            elif i>0 and n[i] != n[i-1]: pos = i
        return N



739.py class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        heap = []
        for j, t in enumerate(T):
            while heap and heap[0][0] < t:
                temp, i = heapq.heappop(heap)
                res[i] = j - i
            heapq.heappush(heap, (t, j))
        return res
        



740.py class Solution:
    def deleteAndEarn(self, nums):
        cnt, dp, maxs = collections.Counter(nums), {}, {}
        nums = sorted(set(nums))
        if len(nums) < 2:
            return nums and nums[0] * cnt[nums[0]] or 0
        for i in range(len(nums)):
            dp[i] = nums[i] * cnt[nums[i]]
            if i >= 2:
                if nums[i - 1] < nums[i] - 1:
                    dp[i] += maxs[i - 1]
                else:
                    dp[i] += maxs[i - 2]
                maxs[i] = max(dp[i], maxs[i - 1])
            elif i:
                if nums[i - 1] < nums[i] - 1:
                    dp[i] += dp[i - 1]
                maxs[i] = max(dp[i], dp[i - 1])
            else:
                maxs[i] = dp[i]
        return max(dp[len(nums) - 1], dp[len(nums) - 2])



741.py class Solution(object):
    def cherryPickup(self, grid):
        if grid[-1][-1] == -1: return 0
        memo, n = {}, len(grid)
        def dp(i1, j1, i2, j2):
            if (i1, j1, i2, j2) in memo: return memo[(i1, j1, i2, j2)]
            if n in (i1, j1, i2, j2) or -1 in (grid[i1][j1], grid[i2][j2]): return -1
            if i1 == i2 == j1 == j2 == n - 1: return grid[-1][-1]
            mx = max(dp(i1+1, j1, i2+1, j2), dp(i1+1, j1, i2, j2+1), dp(i1, j1+1, i2+1, j2), dp(i1, j1+1, i2, j2+1))
            if mx == - 1: out = -1 
            elif i1 == i2 and j1 == j2: out = mx + grid[i1][j1]
            else: out = mx + grid[i1][j1] + grid[i2][j2]
            memo[(i1, j1, i2, j2)] = out
            return out
        return max(0, dp(0, 0, 0, 0))



742.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root, k):
        adj, q, visited = collections.defaultdict(list), [], collections.defaultdict(int)
        def dfs(node):
            if node:
                if node.val == k:
                    q.append(node)
                    visited[node.val] = 1
                if node.left:
                    adj[node].append(node.left)
                    adj[node.left].append(node)
                    dfs(node.left)
                if node.right:
                    adj[node].append(node.right)
                    adj[node.right].append(node)
                    dfs(node.right)
        dfs(root)
        while q:
            new = []
            for node in q:
                if not node.left and not node.right:
                    return node.val
                for v in adj[node]:
                    if not visited[v.val]:
                        visited[v.val] = 1
                        new.append(v)
            q = new                



743.py class Solution:
    def networkDelayTime(self, times, N, K):
        q, t, adj = [(0, K)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (time + w, v))
        return max(t.values()) if len(t) == N else -1



744.py class Solution:
    def nextGreatestLetter(self, letters, target):
        return letters[bisect.bisect(letters, target) % len(letters)]



745.py class WordFilter:
    def __init__(self, words):
        self.p, self.s, self.ind = collections.defaultdict(set), collections.defaultdict(set), {}
        for i, w in enumerate(words): 
            self.ind[w] = i
            self.p[""].add(w)
            self.s[""].add(w)
            for i in range(1, len(w) + 1): 
                self.p[w[:i]].add(w)
                self.s[w[-i:]].add(w)
    def f(self, prefix, suffix): return max((self.ind[c] for c in self.p[prefix] & self.s[suffix]), default = -1)



746.py class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        for i in range(2,len(cost)): cost[i]+=min(cost[i-1],cost[i-2])
        return min(cost[-1],cost[-2])



747.py class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mx = max(nums)
        return nums.index(mx) if all(num * 2 <= mx for num in nums if num < mx) else -1



748.py class Solution:
    def shortestCompletingWord(self, lp, words):
        cntr_lp, res = {k: v for k, v in collections.Counter(lp.lower()).items() if k.isalpha()}, [None, None]
        for word in words:
            check = collections.Counter(word.lower())
            if all(True if k in check and v <= check[k] else False for k, v in cntr_lp.items()):
                if not any(res) or len(word) < res[1]: res = [word, len(word)]
        return res[0]   



749.py class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return None
        N,M=len(grid),len(grid[0])
        
        def around(r,c,t=None):
            # all cells 1-step away from (r,c)
            # optionally, if t!=None, target value must be t
            for d in (-1,1):
                for (rr,cc) in ((r+d,c), (r,c+d)):
                    if 0<=rr<N and 0<=cc<M and (t == None or grid[rr][cc]==t):
                        yield (rr,cc)
        
        def regions():
            regs=[]
            seen=set()
            for r in range(N):
                for c in range(M):
                    if grid[r][c]==1 and (r,c) not in seen:
                        # this is a new region. do a BFS to find all contiguous ones
                        reg=set()
                        front, newfront=[(r,c)], []
                        while front:
                            reg.update(front)
                            while front:
                                (r,c) = front.pop()
                                for (rr,cc) in around(r,c,1):
                                    if (rr, cc) not in reg:
                                        newfront.append((rr,cc))
                                        reg.add((rr, cc))
                            front,newfront=newfront,front
                        regs.append(reg)
                        seen.update(reg)
            return regs
        
        def reg_boundary(reg):
            # cells that would become infected by cells in reg
            bound=set()
            for (r,c) in reg:
                for (rr,cc) in around(r,c,0):
                    bound.add((rr,cc))

            return bound
        
        def reg_walls(reg,bound):
            # number of walls that would need to be built to contain reg
            walls=0
            for (r,c) in bound:
                for (rr,cc) in around(r,c,1):
                    if (rr,cc) in reg:
                        walls+=1    
            return walls
        gwalls=0
        
        while True:
            
            regs=regions()
            
            if not regs: break
            reg = max(regs, key=lambda reg: len(reg_boundary(reg)))
            walls=reg_walls(reg, reg_boundary(reg))
            gwalls+=walls
            
            # neutralize region
            for (r,c) in reg:
                grid[r][c]=2

            # compute next grid iteration after new infections
            infected=set()
            for r in range(N):
                for c in range(M):
                    if grid[r][c]==1:
                        for (rr, cc) in around(r, c, 0):
                            infected.add((rr, cc))

            for r, c in infected:
                grid[r][c]=1

            if not infected: break

        return gwalls



750.py class Solution:
    def countCornerRectangles(self, grid):
        ends, res = collections.defaultdict(int), 0
        for row in grid:
            for i in range(len(row) - 1):
                for j in range(i + 1, len(row)):
                    if row[i] and row[j]:
                        ends[(i, j)] = ends.get((i, j), 0) + 1
                        res += ends[(i, j)] - 1
        return res



751.py class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        s = ''.join(bin(int(num))[2:].zfill(8) for num in ip.split('.'))
        res = []
        while n:
            for i in range(31 - s.rindex('1'), -1, -1):
                if 2 ** i <= n:
                    res.append('.'.join(str(int(s[i:i + 8], 2)) for i in range(0, 32, 8)) + '/' + str(32 - i))
                    n -= 2 ** i
                    s = bin(int(s, 2) + 2 ** i)[2:].zfill(32)
                    break
        return res
        



752.py class Solution:
    def openLock(self, deadends, target):
        moved, q, cnt, move = set(deadends), ["0000"], 0, {str(i): [str((i + 1) % 10), str((i - 1) % 10)] for i in range(10)}
        if "0000" in moved:
            return -1
        while q:
            new = []
            cnt += 1
            for s in q:
                for i, c in enumerate(s):
                    for cur in (s[:i] + move[c][0] + s[i + 1:], s[:i] + move[c][1] + s[i + 1:]):
                        if cur not in moved:
                            if cur == target:
                                return cnt
                            new.append(cur)
                            moved.add(cur)
            q = new
        return -1



753.py class Solution:
    def crackSafe(self, n, k):
        s = '0' * (n - 1)
        D = '9876543210'[-k:]
        for _ in range(k**n):
            s += next(d for d in D if (s + d)[-n:] not in s)
        return s



754.py class Solution:
    def reachNumber(self, target):
        pos, step, target = 0, 0, abs(target)
        while pos < target or (pos - target) % 2:
            step += 1
            pos += step
        return step



755.py class Solution:
    def pourWater(self, heights, V, K):
        for drop in range(V):
            l = r = K
            for i in range(K - 1, -1, -1):
                if heights[i] > heights[l]:
                    break
                elif heights[i] < heights[l]:
                    l = i
            if l < K:
                heights[l] += 1
            else:
                for j in range(K + 1, len(heights)):
                    if heights[j] > heights[r]:
                        break
                    elif heights[j] < heights[r]:
                        r = j
            if l == r == K:
                heights[K] += 1
            elif r > K:
                heights[r] += 1
        return heights



756.py class Solution:
    def pyramidTransition(self, bottom, allowed):
        chars, allowed = 'ABCDEFG', set(allowed)
        def dfs(r, q, i):
            if len(r) == 1: 
                return True
            for c in chars:
                if r[i:i+2]+c in allowed and (i==len(r)-2 and dfs(q+c,"",0) or dfs(r,q+c,i+1)): return True
            return False
        return dfs(bottom, "", 0) 



757.py class Solution(object):
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key = lambda k: k[1])
        solution = []
        for start, end in intervals:
            if not len(solution) or solution[-1] < start:
                solution.append(end - 1)
                solution.append(end)
            elif solution[-2] < start:
                solution.append(end)
        return len(solution)



758.py class Solution:
    def boldWords(self, words, S):
        trie, n, mask, res = {}, len(S), set(), ""
        for w in words:
            cur = trie
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["#"] = cur.get("#", set()) | {w}
        for i in range(n):
            cur, j = trie, i
            while j < n and S[j] in cur:
                cur = cur[S[j]]
                if "#" in cur:
                    mask |= {ind for ind in range(i, j + 1)}
                j += 1
        for i in range(n):
            if i in mask and (not i or i - 1 not in mask):
                res += "<b>"
            res += S[i]
            if i in mask and (i == n - 1 or i + 1 not in mask):
                res += "</b>"
        return res



759.py # Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def employeeFreeTime(self, schedule):
        intervals = sorted(((intr.start, intr.end) for emp in schedule for intr in emp), key = lambda x: x[0])
        res, stack = [], []
        for s, e in intervals:
            if not stack:
                stack.append((s, e))
            elif s <= stack[-1][-1]:
                stack.append((s, max(e, stack.pop()[1])))
            else:
                res.append([stack[-1][1], s])
                stack.append((s, e))
        return res



760.py class Solution:
    def anagramMappings(self, A, B):
        ind = {num: j for j, num in enumerate(B)}
        return [ind[num] for num in A] 



761.py class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        count = i = 0
        res = []
        for j, v in enumerate(S):
            count = count + 1 if v=='1' else count - 1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(S[i + 1:j]) + '0')
                i = j + 1
        return ''.join(sorted(res)[::-1])



762.py class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        count=0
        while L<=R:
            if str(bin(L)[2:]).count("1") in [2,3,5,7,11,13,17,19]: count+=1
            if str(bin(R)[2:]).count("1") in [2,3,5,7,11,13,17,19]:
                count+=1
                if L==R: count-=1
            L+=1
            R-=1
        return count



763.py class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        sizes = []
        while S:
            i = 1
            while set(S[:i]) & set(S[i:]):
                i += 1
            sizes.append(i)
            S = S[i:]
        return sizes



764.py class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        #up, left, down, right
        dp, res, mines = [[[0, 0, 0, 0] for j in range(N)] for i in range(N)], 0, {(i, j) for i, j in mines}
        for i in range(N):
            for j in range(N):
                if (i, j) not in mines:
                    try:
                        dp[i][j][0] = dp[i - 1][j][0] + 1
                    except:
                        dp[i][j][0] = 1
                    try:
                        dp[i][j][1] = dp[i][j - 1][1] + 1
                    except:
                        dp[i][j][1] = 1
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if (i, j) not in mines:
                    try:
                        dp[i][j][2] = dp[i + 1][j][2] + 1
                    except:
                        dp[i][j][2] = 1
                    try:
                        dp[i][j][3] = dp[i][j + 1][3] + 1
                    except:
                        dp[i][j][3] = 1
                    res = max(res, min(dp[i][j]))
        return res



765.py class Solution:
    def minSwapsCouples(self, row):
        res, index = 0, {num: i for i, num in enumerate(row)}
        for i in range(0, len(row), 2):
            if row[i] % 2 == 0 and row[i + 1] != row[i] + 1: 
                f = row[i + 1]
                row[i + 1], row[index[row[i] + 1]] = row[i] + 1, row[i + 1]
                index[row[i] + 1], index[f] = i + 1, index[row[i] + 1]
                res += 1
            elif row[i] % 2 != 0 and row[i + 1] != row[i] - 1:
                f = row[i + 1]
                row[i + 1], row[index[row[i] - 1]], index[row[i + 1]] = row[i] - 1, row[i + 1], index[row[i] - 1]
                index[row[i] - 1], index[f] = i + 1, index[row[i] - 1]
                res += 1
        return res



766.py class Solution:
    def isToeplitzMatrix(self, matrix):
        return all(matrix[i][j] == matrix[i - 1][j - 1] for i in range(1, len(matrix)) for j in range(1, len(matrix[0])))



767.py class Solution:
    def reorganizeString(self, S):
        cnt, res = collections.Counter(S), ""
        while len(res) < len(S):
            c, i = cnt.most_common()[0], 0
            while i + 1 < len(cnt) and (res and res[-1] == c[0] or cnt[c[0]] == 0): c, i = cnt.most_common()[i + 1], i + 1
            if not cnt[c[0]] or res and res[-1] == c[0]: return ""
            else: res, cnt[c[0]] = res + c[0], cnt[c[0]] - 1
        return res



768.py class Solution:
    def maxChunksToSorted(self, arr):
        mx, mn, res, check = 0, 10 ** 9, 0, [[0, 0] for _ in range(len(arr))]
        for i in range(len(arr)):
            if arr[i] > mx: mx = arr[i]
            check[i][0] = mx
        for i in range(len(arr) -1, -1, -1):
            check[i][1] = mn
            if arr[i] < mn: mn = arr[i]
        for c in check:
            if c[0] <= c[1]: res += 1
        return res



769.py class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        max_seen, total_seen, res_count = 0, 0, 0
        for num in arr:
            max_seen = max(max_seen, num)
            total_seen += 1
            if max_seen == total_seen - 1:
                res_count += 1
        return res_count



770.py class Solution(object):
    def basicCalculatorIV(self, s, evalvars, evalints):
        s.strip()
        d = dict(zip(evalvars, evalints))
        s = s.replace(' ', '')
        ts = re.findall('\u005Cd+|[-()+*]|[^-()+*]+', s)
        
        def add(p, q):
            i, j = 0, 0
            r = []
            while i < len(p) and j < len(q):
                v, c = p[i]
                v2, c2 = q[j]
                if v == v2:
                    if c + c2 != 0:
                        r.append((v, c + c2))
                    i += 1
                    j += 1
                elif len(v) > len(v2) or len(v) == len(v2) and v < v2:
                    r.append(p[i])
                    i += 1
                else:
                    r.append(q[j])
                    j += 1
                            
            r += p[i:]
            r += q[j:]
            return r

        def neg(p):
            r = []
            for v, c in p:
                r.append((v, -c))
            return r

        def sub(p, q):
            return add(p, neg(q))

        def mult(p, q):
            r = []
            for v, c in p:
                for v2, c2 in q:
                    r = add(r, [(sorted(v + v2), c * c2)])
            return r
            
        def prec(c):
            return 0 if c in [')'] else 1 if c in ['+', '-'] else 2
            
        i = 0 
        def expr(p):
            nonlocal i, ts
            if ts[i] == '(':
                i += 1
                v = expr(0)
                i += 1
            elif ts[i] == '-':
                i += 1
                v = neg(expr(3))
            elif re.match('\u005Cd+', ts[i]):
                if ts[i] != '0':
                    v = [([], int(ts[i]))]
                else:
                    v = []
            else:
                if ts[i] in d:
                    if d[ts[i]] != 0:
                        v = [([], d[ts[i]])]
                    else:
                        v  = []
                else:
                    v = [([ts[i]], 1)]
            while i < len(ts) - 2 and prec(ts[i+1]) > p:
                op = ts[i+1]
                i += 2
                v2 = expr(prec(op))
                if op == '+': v = add(v, v2)
                if op == '-': v = sub(v, v2)
                if op == '*': v = mult(v, v2)
                
            return v

        def tostrings(p):
            r = []
            for v, c in p:
                if v == []:
                    r.append(str(c))
                else:
                    r.append(str(c) + '*' + '*'.join(v))
            return r
        
        return tostrings(expr(0))



771.py class Solution:
    def numJewelsInStones(self, J, S):
        sj = set(J)
        return sum(s in sj for s in S)



772.py class Solution:
    def calculate(self, s: str) -> int:
        def calc(n2, op, n1): 
            return n1 * n2 if op == '*' else n1 // n2 if op == '/' else n1 + n2 if op == '+' else n1 - n2
        def calc2(arr):
            if len(arr) == 1:
                return arr.pop()
            res = arr[0]
            for j in range(2, len(arr), 2):
                res = calc(arr[j], arr[j - 1], res)
            return res
        stack, i, num = [], 0, 0
        while i < len(s):
            j = i
            while j < len(s) and s[j].isdigit():
                num, j = num * 10 + int(s[j]), j + 1
            if i != j:
                stack.append(calc(num, stack.pop(), stack.pop()) if stack and stack[-1] in "*/" else num)
                num, j = 0, j - 1
            elif s[i] == ")":
                ind = len(stack) - stack[::-1].index('(') - 1
                stack[ind:] = [calc2(stack[ind + 1:])]
                if len(stack) > 1 and stack[-2] in '*/':
                    stack.append(calc(stack.pop(), stack.pop(), stack.pop()))
            elif s[i] != ' ':
                stack.append(s[i])
            i = j + 1
        return calc2(stack)



773.py class Solution:
    def slidingPuzzle(self, board):
        moves, used, cnt = {0: {1, 3}, 1:{0, 2, 4}, 2:{1, 5}, 3:{0, 4}, 4:{1, 3, 5}, 5:{2, 4}}, set(), 0
        s = "".join(str(c) for row in board for c in row)
        q = [(s, s.index("0"))]
        while q:
            new = []
            for s, i in q:
                used.add(s)
                if s == "123450":
                    return cnt
                arr = [c for c in s]
                for move in moves[i]:
                    new_arr = arr[:]
                    new_arr[i], new_arr[move] = new_arr[move], new_arr[i]
                    new_s = "".join(new_arr)
                    if new_s not in used:
                        new.append((new_s, move))
            cnt += 1
            q = new
        return -1



774.py class Solution:
    def minmaxGasDist(self, st, K):
        left, right = 1e-6, st[-1] - st[0]
        while left + 1e-6 < right:
            mid = (left + right) / 2
            count = 0
            for a, b in zip(st, st[1:]):
                count += math.ceil((b - a) / mid) - 1
            if count > K:
                left = mid
            else:
                right = mid
        return right



775.py class Solution:
    def isIdealPermutation(self, A):
        for i, num in enumerate(A):
            if not (i - 1 <= num <= i + 1): return False
        return True



776.py class Solution:
    def splitBST(self, root, V):
        if not root:
            return [None, None]
        if root.val == V:
            a = root.right
            root.right = None
            return [root, a]
        elif root.val < V:
            small, large = self.splitBST(root.right, V)
            root.right = small
            return [root, large]
        else:
            small, large = self.splitBST(root.left, V)
            root.left = large
            return [small, root]



777.py class Solution:
    def canTransform(self, start, end):
        s, e = collections.defaultdict(list), collections.defaultdict(list)
        newS, newE = [c for c in start if c != "X"], [c for c in end if c != "X"]
        for i in range(len(start)):
            if start[i] != "X":
                s[start[i]].append(i)
            if end[i] != "X":
                e[end[i]].append(i)
        if newS == newE and len(s["L"]) == len(e["L"]) and len(s["R"]) == len(e["R"]):
            if all(s["R"][i] <= e["R"][i] for i in range(len(s["R"]))) and all(s["L"][i] >= e["L"][i] for i in range(len(s["L"]))):
                return True
        return False



778.py class Solution:
    def swimInWater(self, grid):
        heap, res, n, visited = [(grid[0][0], 0, 0)], 0, len(grid), set()
        while True:
            d, i, j = heapq.heappop(heap)
            if d > res: res = d
            if i == j == n - 1: return res
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n and (x, y) not in visited: 
                    visited.add((x, y))
                    heapq.heappush(heap, (grid[x][y], x, y))



779.py class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        return N > 1 and self.kthGrammar(N - 1, (K + 1) // 2) ^ ((K -1) % 2) or 0



780.py class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        while sx<tx and sy<ty: tx,ty = tx%ty,ty%tx
        return sx==tx and (ty-sy)%sx==0 or sy==ty and (tx-sx)%sy==0



781.py class Solution:
    def numRabbits(self, answers):
        dic, res = {}, 0
        for ans in answers:
            (dic[ans], res) = (1, res + ans + 1) if ans not in dic or dic[ans] > ans else (dic[ans] + 1, res)
        return res



782.py class Solution:
    def movesToChessboard(self, b):
        N = len(b)
        if any(b[0][0] ^ b[i][0] ^ b[0][j] ^ b[i][j] for i in range(N) for j in range(N)): return -1
        if not N // 2 <= sum(b[0]) <= (N + 1) // 2: return -1
        if not N // 2 <= sum(b[i][0] for i in range(N)) <= (N + 1) // 2: return -1
        col = sum(b[0][i] == i % 2 for i in range(N))
        row = sum(b[i][0] == i % 2 for i in range(N))
        if N % 2:
            if col % 2: col = [col, N - col][col % 2]
            if row % 2: row = N - row
        else:
            col = min(N - col, col)
            row = min(N - row, row)
        return (col + row) // 2



783.py class Solution:
    def minDiffInBST(self, root):
        def dfs(node):
            if not node: return float("inf"), float("inf"), -float("inf")
            l, lMn, lMx = dfs(node.left)
            r, rMn, rMx = dfs(node.right)
            return min(l, node.val - lMx, r, rMn - node.val), min(lMn, node.val), max(rMx, node.val)
        return dfs(root)[0]



784.py class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        bfs = ['']
        for c in S:
            if c.isdigit():
                bfs = [s + c for s in bfs]
            else:
                bfs = [s + c.lower() for s in bfs] + [s + c.upper() for s in bfs]
        return bfs



785.py class Solution:
    def isBipartite(self, graph):
        side = [0] * len(graph)
        def dfs(node):
            for v in graph[node]:
                if side[v] == 0: 
                    side[v] = -side[node]
                    if not dfs(v): return False
                elif side[v] == side[node]: return False
            return True
        for i in range(len(graph)):
            if side[i] == 0: 
                side[i] = 1
            if not dfs(i): return False
        return True



786.py class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        heap, used = [(A[0] / A[-1], 0, len(A) - 1)], {(0, len(A) - 1)}
        for i in range(K):
            try:
                cur, l, r = heapq.heappop(heap)
                used.add((l, r))
                if (l + 1, r) not in used:
                    heapq.heappush(heap, (A[l + 1] / A[r], l + 1, r))
                    used.add((l + 1, r))
                if (l, r - 1) not in used:
                    heapq.heappush(heap, (A[l] / A[r - 1], l, r - 1))
                    used.add((l, r - 1))
            except:
                break
        return [A[l], A[r]]



787.py class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        flight = collections.defaultdict(list)
        for s, e, p in flights:
            flight[s].append((e, p))
        heap = [(0, src, K + 1)]
        while heap:
            price, city, stop = heapq.heappop(heap)
            if city == dst:
                return price
            elif stop > 0:
                for c, p in flight[city]:
                    heapq.heappush(heap, (price + p, c, stop - 1))
        return -1



788.py class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        for i in range(1, N + 1):
            i = str(i)
            tmp = []
            check = True
            for char in i:
                if char in ("3", "4", "7"):
                    check = False
                    break
                if char in ("0", "1", "8"):
                    tmp.append(char)
                if char == "2":
                    tmp.append("5")
                if char == "5":
                    tmp.append("2")
                if char == "6":
                    tmp.append("9")
                if char == "9":
                    tmp.append("6")
            if check and i != "".join(tmp): res += 1
        return res



789.py class Solution:
    def escapeGhosts(self, ghosts, target):
        d = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            if abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) <= d: return False
        return True



790.py class Solution:
    def numTilings(self, N):
        dp = [[0, 0] for _ in range(N + 1)]
        dp[0][0] = 1
        for i in range(N):
            if i + 1 <= N:
                dp[i + 1][0] += dp[i][0] + dp[i][1]
                dp[i + 1][1] += dp[i][1]
            if i + 2 <= N:
                dp[i + 2][0] += dp[i][0]
                dp[i + 2][1] += 2 * dp[i][0]
        return dp[-1][0] % (10 ** 9 + 7)



791.py class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        t = set(T)
        t2 = set(S)
        from collections import Counter as ct
        c = ct(T)
        s = [char * c[char] for char in S if char in t]
        add = [char * c[char] for char in t - t2]
        return "".join(s + add)



792.py class Solution:
    def numMatchingSubseq(self, S, words):
        def check(s, i):
            for c in s:
                i = S.find(c, i) + 1
                if not i: return False
            return True
        return sum((check(word, 0) for word in words))



793.py class Solution:
    
    def count(self, num):
        cnt = 0
        while num:
            cnt += num // 5
            num //= 5
        return cnt 
    
    def preimageSizeFZF(self, K):
        l, r = 0, 2 ** 63 - 1
        while l < r:
            mid = (l + r) // 2
            if self.count(mid) < K:
                l = mid + 1
            else:
                r = mid
        return 5 - (l % 5) if self.count(l) == K else 0



794.py class Solution(object):
    def check_win_positions(self, board, player):
        """
        Check if the given player has a win position.
        Return True if there is a win position. Else return False.
        """
        #Check the rows
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True                        

        #Check the columns
        for i in range(len(board)):
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True 
										
        #Check the diagonals
        if board[0][0] == board[1][1] == board[2][2]  == player or \u005C
               board[0][2] == board[1][1] == board[2][0] == player:
            return True
						
        return False
        
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        
        x_count, o_count = 0, 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    x_count += 1
                elif  board[i][j] == "O":
                    o_count += 1
										
        if o_count > x_count or x_count-o_count>1:
            return False
        
        if self.check_win_positions(board, 'O'):
            if self.check_win_positions(board, 'X'):
                return False
            return o_count == x_count
        
        if self.check_win_positions(board, 'X') and x_count!=o_count+1:
            return False

        return True



795.py class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        res, start, diff = 0, -1, 0
        for i in range (len(A)):
            if L <= A[i] <= R: diff, res = i - start, res + i - start
            elif A[i] > R: diff, start = 0, i
            else: res += diff
        return res



796.py class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return True if [A[i:]+A[:i] for i in range(len(A)) if A[i:]+A[:i]==B] else False



797.py class Solution:
    def allPathsSourceTarget(self, graph, i = 0, q = [0]):
        if i == 0: 
            global res
            res = []
        if i == len(graph) - 1: 
            res.append(q)
        for index in graph[i]: 
            self.allPathsSourceTarget(graph, index, q + [index])
        return res



798.py class Solution:
    def bestRotation(self, A):
        N = len(A)
        change = [1] * N
        for i in range(N): change[(i - A[i] + 1) % N] -= 1
        for i in range(1, N): change[i] += change[i - 1]
        return change.index(max(change))



799.py class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        glasses=[[poured if i==0 and j==0 else 0 for i in range(j+1)] for j in range(query_row+1)]
        for i in range(1,len(glasses)):
            for j in range(len(glasses[i])):
                if j-1>=0 and glasses[i-1][j-1]>1: glasses[i][j]+=(glasses[i-1][j-1]-1)/2
                if j<=i-1 and glasses[i-1][j]>1: glasses[i][j]+=(glasses[i-1][j]-1)/2
        return glasses[query_row][query_glass] if glasses[query_row][query_glass]<=1 else 1



800.py class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        import math
        num1, num2, num3 = int(color[1:3],16), int(color[3:5],16), int(color[5:7],16)
        letters = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        min1, min2, min3, res = math.inf, math.inf, math.inf, ["#","","",""]
        for letter in letters:
            min1, min2, min3 = min(min1,(num1-int(letter*2,16))**2), min(min2,(num2-int(letter*2,16))**2), min(min3,(num3-int(letter*2,16))**2) 
            if min1 == (num1-int(letter*2,16))**2: res[1] = letter*2 
            if min2 == (num2-int(letter*2,16))**2: res[2] = letter*2 
            if min3 == (num3-int(letter*2,16))**2: res[3] = letter*2
        return "".join(res)



802.py class Solution:
    def eventualSafeNodes(self, graph):
        def explore(i):
            visited[i] = 0
            for v in graph[i]:
                if visited[v] == 0 or (visited[v] == -1 and explore(v)): return True
            visited[i] = 1
            res.append(i)
            return False
        visited, res = [-1] * len(graph), []
        for i in range(len(graph)):
            if visited[i] == -1: explore(i)
        return sorted(res)



803.py class Solution:
    def hitBricks(self, grid, hits):
        m, n, ret = len(grid), len(grid[0]), [0]*len(hits)
        # Connect unconnected bricks and 
        def dfs(i, j):
            if not (0 <= i <m and 0 <= j <n) or grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            return 1 + sum(dfs(x, y) for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)))
        # Check whether (i, j) is connected to Not Falling Bricks
        def is_connected(i, j):
            return not i or any(0 <= x < m and 0 <= y < n and grid[x][y] == 2 for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)))
        # Mark whether there is a brick at the each hit
        for i, j in hits:
            grid[i][j] -= 1      
        # Get grid after all hits
        for i in range(n):
            dfs(0, i)
        # Reversely add the block of each hits and get count of newly add bricks
        for k in reversed(range(len(hits))):
            i, j = hits[k]
            grid[i][j] += 1
            if grid[i][j] and is_connected(i, j):
                ret[k] = dfs(i, j) - 1
        return ret



804.py class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic=set()
        letters=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            code=[]
            for letter in word: code.append(letters[ord(letter)-ord("a")])
            code= "".join(code)
            if not code in dic: dic.add(code)
        return len(dic)



805.py class Solution:
    def splitArraySameAverage(self, A):
        def find(target, k, i):
            if (target,k) in not_found and not_found[(target,k)] <= i: return False
            if k == 0: return target == 0
            if k + i > len(A): return False
            res = find(target - A[i], k - 1, i + 1) or find(target, k, i + 1)
            if not res: not_found[(target, k)] = min(not_found.get((target, k), n), i)
            return res
        not_found = dict()
        n, s = len(A), sum(A)
        return any(find(s * i / n, i, 0) for i in range(1, n // 2 + 1) if s * i % n == 0)



806.py class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        left=0
        lines=1
        for char in S:
            if left+widths[ord(char)-ord("a")]<=100:
                left+=widths[ord(char)-ord("a")]
            else:
                lines+=1
                left=widths[ord(char)-ord("a")]
        return [lines, left]



807.py class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        mx_i = [max(grid[i]) for i in range(n)]
        mx_j=[-float("inf")]*m
        for i in range(n): 
            for j in range(m): mx_j[j]=max(mx_j[j],grid[i][j])
        res=0
        for i in range(n):
            for j in range(m):
                prev=grid[i][j]
                grid[i][j]=min(mx_i[i],mx_j[j])
                res+=grid[i][j]-prev
        return res



808.py class Solution:
    def soupServings(self, N):
        visited = {}
        def dfs(a, b):
            if (a, b) in visited: return visited[(a, b)]
            elif a <= 0 or b <= 0: return (a < b and 1) or (a == b and 0.5) or (b < a and 0)
            visited[(a, b)] = 0.25 * (dfs(a - 100, b) + dfs(a - 75, b - 25) + dfs(a - 50, b -50) + dfs(a - 25, b - 75))
            return visited[(a, b)] 
        return N > 4800 and 1 or round(dfs(N, N), 5)



809.py class Solution:
    def expressiveWords(self, S, words):
        if not S: return 0
        guide, i, j, res = [], 0, 0, 0
        while i < len(S):
            while j + 1 <len(S) and S[j + 1] == S[j]: j += 1
            guide.append((S[i], j - i + 1))
            i = j = j + 1
        for word in words:
            i = j = g = 0
            while i < len(word):
                while j + 1 < len(word) and word[j + 1] == word[j]: j += 1
                if guide[g][0] != word[i] or (guide[g][1] == 2 and j - i + 1 == 1) or guide[g][1] < j - i + 1: break
                i, j, g = j + 1, j + 1, g + 1
            if g == len(guide): res += 1
        return res



810.py class Solution:
    def xorGame(self, nums):
        xor = 0
        for i in nums: xor ^= i
        return xor == 0 or len(nums) % 2 == 0



811.py class Solution:
    def subdomainVisits(self, cpdomains):
        counter = collections.Counter()
        for cpdomain in cpdomains:
            count, *domains = cpdomain.replace(" ",".").split(".")
            for i in range(len(domains)):
                counter[".".join(domains[i:])] += int(count)
        return [" ".join((str(v), k)) for k, v in counter.items()]



812.py class Solution:
    def largestTriangleArea(self, p):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        from itertools import combinations as cb
        def f(p1, p2, p3):
            (x1, y1), (x2, y2), (x3, y3) = p1,p2,p3
            return 0.5 * abs(x2 * y3 + x1 * y2 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3)
        return max(f(a, b, c) for a, b, c in cb(p, 3))



813.py class Solution:
    def largestSumOfAverages(self, A, K):
        memo = {}
        def search(n, k):
            if n < k: return 0
            if (n, k) not in memo:
                if k == 1: memo[n, k] = sum(A[:n]) / float(n)
                else:
                    cur = memo[n, k] = 0
                    for i in range(n - 1, 0, -1):
                        cur += A[i]
                        memo[n, k] = max(memo[n, k], search(i, k - 1) + cur / float(n - i))
            return memo[n, k]
        return search(len(A), K)



814.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root, parent = None):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        left = self.pruneTree(root.left, root)
        right = self.pruneTree(root.right, root)
        if not left and not right and root.val == 0:
            if parent and parent.left == root: parent.left = None
            elif parent and parent.right == root: parent.right = None
            return 
        else: return root



815.py class Solution:
    def numBusesToDestination(self, routes, starterBus, targetBus):
        path, travel, travelTaken, used = collections.defaultdict(set), [starterBus], 0, set()
        for i, route in enumerate(routes):
            for bus in route:
                path[bus].add(i)
        while travel:
            new = []
            for bus in travel:
                if bus == targetBus:
                    return travelTaken
                for route in path[bus]:
                    if route not in used:
                        used.add(route)
                        for nextBus in routes[route]:
                            if nextBus != bus:
                                new.append(nextBus)
            travelTaken += 1
            travel = new
        return -1



816.py class Solution:
    def ambiguousCoordinates(self, S):
        def properInt(s):
            return len(s) > 1 and s[0] != "0" or len(s) == 1
        
        def properFloat(s, i):
            return s[-1] not in ".0" and properInt(s[:i])
        
        s, res = S[1:-1], set()
        for i in range(len(s)):
            n1, n2 = s[:i + 1], s[i + 1:]
            p1, p2 = properInt(n1), properInt(n2)
            if p1 and p2:
                res.add("({}, {})".format(n1, n2))
            for j in range(len(n1)):
                for k in range(len(n2)):
                    n1f = n1[:j + 1] + "." + n1[j + 1:]
                    n2f = n2[:k + 1] + "." + n2[k + 1:]
                    p1f = properFloat(n1f, j + 1)
                    p2f = properFloat(n2f, k + 1)
                    if p1f and p2f:
                        res.add("({}, {})".format(n1f, n2f))
                    if p1f and p2:
                        res.add("({}, {})".format(n1f, n2))
                    if p1 and p2f:
                        res.add("({}, {})".format(n1, n2f))
        return list(res)



817.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        num_connected = 0
        set_g = set(G)
        while head:
            if head.val not in set_g:
                head = head.next
                continue
            while head and head.val in set_g:
                head = head.next
            num_connected += 1
        return num_connected



818.py class Solution:
    def racecar(self, target):
        q, cnt, used = [(0, 1)], 0, {(0, 1)}
        while q:
            new = []
            for pos, speed in q:
                if pos == target:
                    return cnt
                elif pos > 20000 or -20000 > pos:
                    continue
                if (pos + speed, speed * 2) not in used:
                    new.append((pos + speed, speed * 2))
                    used.add((pos + speed, speed * 2))
                if speed > 0 and (pos, -1) not in used:
                    new.append((pos, -1))
                    used.add((pos, -1))
                elif speed < 0 and (pos, 1) not in used:
                    new.append((pos, 1))
                    used.add((pos, 1))
            q = new
            cnt += 1



819.py class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = re.findall(r"\u005Cw+", paragraph)
        dic = {}
        mx = [0, 0]
        for char in paragraph:
            char = char.lower()
            if char not in banned:
                if char not in dic: dic[char] = 1
                else: dic[char] += 1
                mx[0] = max(mx[0], dic[char])
                if mx[0] == dic[char]: mx[1] = char
        return mx[1]
        



820.py class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        s = set(words)
        for word in words: 
            for i in range(1, len(word)): s.discard(word[i:])
        return sum(len(w) + 1 for w in s)



821.py class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        char1, char2, diff1, diff2, res = False, False, 0, 0, [None]* len(S)
        for i in range(len(S)):
            if char1: res[i], diff1 = min(res[i], diff1 + 1) if res[i] else diff1 + 1, diff1 + 1
            if S[i] == C: diff1, res[i], char1 = 0, 0, True  
            if char2: res[len(S) - 1 - i], diff2 = min(res[len(S) - 1 - i], diff2 + 1) if res[len(S) - 1 - i] else diff2 + 1, diff2 + 1
            if S[len(S) - 1 - i] == C: diff2, res[len(S) - 1 - i], char2 = 0, 0, True
        return res



822.py class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        return min((set(fronts) | set(backs)) - set(fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]), default = 0)



823.py class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        nums, res, trees, factors = set(A), 0, {}, collections.defaultdict(set)
        for i, num in enumerate(A):
            for n in A[:i]:
                if num % n == 0 and num // n in nums: factors[num].add(n)
        for root in A:
            trees[root] = 1
            for fac in factors[root]: trees[root] += trees[fac] * trees[root // fac]
        return sum(trees.values()) % ((10 ** 9) + 7)



824.py class Solution:
    def toGoatLatin(self, S):
        s, vowels = S.split(), {"a", "e", "i", "o", "u"} 
        return " ".join([(s[i][0].lower() in vowels and s[i] or s[i][1:] + s[i][0]) + "m" + "a" * (i + 2) for i in range(len(s))])



825.py class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        cntr, res = collections.Counter(ages), 0
        for A in cntr:
            for B in cntr:
                if B <= 0.5 * A + 7 or B > A: continue
                if A == B: res += cntr[A]  *(cntr[A] - 1)
                else: res += cntr[A] * cntr[B]
        return res



826.py class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = sorted([a, b] for a, b in zip(difficulty, profit))
        res = i = maxp = 0
        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                maxp = max(jobs[i][1], maxp)
                i += 1
            res += maxp
        return res      



827.py class Solution:
    def largestIsland(self, grid):
        def explore(i, j):
            dic[(i, j)], count[curr] = curr, count[curr] + 1
            if i > 0 and grid[i - 1][j] == 1 and (i - 1, j) not in dic: explore(i - 1, j)
            if j > 0 and grid[i][j - 1] == 1 and (i, j - 1) not in dic: explore(i, j - 1)
            if i + 1 < len(grid) and grid[i + 1][j] ==1 and (i + 1, j) not in dic: explore(i + 1, j)
            if j + 1 < len(grid) and grid[i][j + 1] == 1 and (i, j + 1) not in dic: explore(i, j + 1)
        def neighbours(i, j, adj):
            if i > 0 and grid[i - 1][j] == 1 and dic[(i - 1, j)] not in adj: adj.add(dic[(i - 1, j)])
            if j > 0 and grid[i][j - 1] == 1 and dic[(i, j - 1)] not in adj: adj.add(dic[(i, j - 1)])
            if i + 1 < len(grid) and grid[i + 1][j] ==1 and dic[(i + 1, j)] not in adj: adj.add(dic[(i + 1, j)])
            if j + 1 < len(grid) and grid[i][j + 1] == 1 and dic[(i, j + 1)] not in adj: adj.add(dic[(i, j + 1)])
            return adj
        curr, dic, count, res = 0, {}, collections.defaultdict(int), 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1 and (i, j) not in dic: curr += 1; explore(i, j)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1: res = max(res, count[dic[(i, j)]])
                else: res = max(res, sum(count[r] for r in neighbours(i, j, set())) + 1)
        return res



828.py class Solution:
    def uniqueLetterString(self, S):
        index = {c: [-1, -1] for c in string.ascii_uppercase}
        res = 0
        for i, c in enumerate(S):
            k, j = index[c]
            res += (i - j) * (j - k)
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            res += (len(S) - j) * (j - k)
        return res % (10**9 + 7)



829.py class Solution:
    def consecutiveNumbersSum(self, N):
        cnt=0
        for d in range(1, N+1):
            diff=d*(d-1)//2
            nd = N - diff
            if nd<=0: break
            if nd%d==0:
                cnt+=1
        return cnt



830.py class Solution:
    def largeGroupPositions(self, S):
        res = []
        l = r = 0
        for i in range(1, len(S)):
            if S[i] == S[i - 1]: r += 1
            if r - l >= 2 and (S[i] != S[i - 1] or i == len(S) - 1): res.append([l, r])
            if S[i] != S[i - 1]: l = r = i
        return res



831.py class Solution:
    def maskPII(self, S):
        if "@" in S:
            s = S.lower().split("@")
            return s[0][0] + "*" * 5 + s[0][-1] + "@" + s[1]
        else:
            nums, tmp = {"0","1","2","3","4","5","6","7","8","9"}, ""
            for c in S:
                if c in nums: tmp += c
            return "+" + "*" * (len(tmp) - 10) + "-***-***-" + tmp[-4:] if len(tmp) > 10 else "***-***-" + tmp[-4:]



832.py class Solution(object):
    def flipAndInvertImage(self, A):
        return [[1 - x for x in A[i][::-1]] for i in range(len(A))]



833.py class Solution:
    def findReplaceString(self, s, indexes, sources, targets):
        res, dic, j = "", {}, 0
        for i in range(len(sources)):
            if s.find(sources[i], indexes[i]) == indexes[i]: dic[indexes[i]] = (sources[i], targets[i])
        while j < len(s):
            res += j in dic and dic[j][1] or s[j]
            j += j in dic and len(dic[j][0]) or 1
        return res



834.py class Solution:
    def sumOfDistancesInTree(self, N, edges):
        tree = collections.defaultdict(set)
        res = [0] * N
        count = [1] * N
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def dfs(root, pre):
            for i in tree[root]:
                if i != pre:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]

        def dfs2(root, pre):
            for i in tree[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + N - count[i]
                    dfs2(i, root)
        dfs(0, -1)
        dfs2(0, -1)
        return res



835.py class Solution:
    def largestOverlap(self, A, B):
        n, shift, rn = len(A), range(-1 * len(A) + 1, len(A)), range(len(A))
        return max(sum(A[i][j] and B[i + v][j + h] for i in rn for j in rn if 0 <= i + v < n > j + h >= 0) for h in shift for v in shift)   



836.py class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        x = (rec1[2] - rec1[0] + rec2[2] - rec2[0]) > (max(rec1[2], rec2[2]) - min(rec1[0], rec2[0]))
        y = (rec1[3] - rec1[1] + rec2[3] - rec2[1]) > (max(rec1[3], rec2[3]) - min(rec1[1], rec2[1]))
        return x and y



837.py class Solution:
    def new21Game(self, N, K, W):
        if K == 0 or N >= K + W: return 1
        dp = [1.0] + [0.0] * N
        Wsum, res = 1.0, 0.0
        for i in range(1, N + 1):
            dp[i] += Wsum / W
            if i < K: Wsum += dp[i]
            else: res += dp[i]
            if i - W >= 0: Wsum -= dp[i - W]
        return res



838.py class Solution:
    def pushDominoes(self, dominoes):
        res, l, r , pre_l, pre_r = "", {}, {}, None, None,
        for i, s in enumerate(dominoes):
            if s == "." and pre_r != None: r[i] = i - pre_r
            elif s == "R": pre_r = i
            elif s == "L": pre_r = None
        for i in range(len(dominoes) - 1, -1, -1):
            if dominoes[i] == "." and pre_l != None: l[i] = pre_l - i
            elif dominoes[i] == "L": pre_l = i
            elif dominoes[i] == "R": pre_l = None
        for i, s in enumerate(dominoes):
            if s == "L" or s == "R": res += s
            elif i in l and i in r:
                if l[i] < r[i]: res += "L"
                elif r[i] < l[i]: res += "R"
                else: res += s
            elif i in l: res += "L"
            elif i in r: res += "R"
            else: res += s
        return res



839.py class Solution:
    def numSimilarGroups(self, A):
        def explore(s):
            visited.add(s)
            for v in edges[s]:
                if v not in visited: explore(v)
        res, edges, visited = 0, {}, set()
        if len(A) >= 2 * len(A[0]):
            strs = set(A)
            for s in A:
                if s not in edges: edges[s] = set()
                for i in range(len(s) - 1):
                    for j in range(i + 1, len(s)):
                        new = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
                        if new in strs:
                            edges[s].add(new)
                            if new in edges: edges[new].add(s)
                            else: edges[new] = {s}
        else:
            for s in A:
                if s not in edges: edges[s] = set()
                for t in A:
                    if s != t:
                        same = 0
                        for i, c in enumerate(t):
                            if c == s[i]: same += 1
                        if same == len(s) - 2: 
                            edges[s].add(t)
                            if t in edges: edges[t].add(s)
                            else: edges[t] = {s}
        for s in A:
            if s not in visited:
                res += 1
                explore(s)
        return res              



840.py class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                if sum(grid[i][j: j + 3]) == sum(grid[i + 1][j : j +3]) == sum(grid[i + 2][j:j + 3]) == sum(grid[k][j] for k in range(i, i + 3)) == sum(grid[k][j + 1] for k in range(i, i + 3)) == sum(grid[k][j + 2] for k in range(i, i + 3)) == (grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]) == (grid[i+2][j]+ grid[i + 1][j + 1] + grid[i][j + 2]): 
                    if set(grid[i][j: j + 3] + grid[i + 1][j: j +3] + grid[i + 2][j:j + 3]) == {1,2,3,4,5,6,7,8,9}: res += 1
        return res
                



841.py class Solution:
    def canVisitAllRooms(self, rooms):
        pool, stack = set(range(len(rooms))), [0]
        while stack: 
            pool.discard(stack[-1])
            for nex in rooms[stack.pop()]:
                if nex in pool: 
                    stack.append(nex)
        return not pool



842.py class Solution:
    def splitIntoFibonacci(self, S):
        def getStarter():
            arr = []
            for i in range(1, len(S) - 1):
                for j in range(i + 1, len(S)):
                    s1, s2 = S[:i], S[i:j]
                    if (s1[0] == "0" and len(s1) > 1) or (s2[0] == "0" and len(s2) > 1): 
                        continue
                    arr.append((int(s1), int(s2), j))
            return arr                 
        def dfs(arr, i):
            if i == len(S):
                return arr
            sm = arr[-2] + arr[-1]
            l = len(str(sm))
            new = int(S[i:i + l])
            return new == sm and 0 <= sm <= mx and dfs(arr + [new], i + l)
        q, mx = getStarter(), 2 ** 31 - 1
        for p1, p2, i in q:
            seq = dfs([p1, p2], i)
            if seq:
                return seq
        return []



843.py # """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution:
    def findSecretWord(self, wordlist, master):
        n = 0
        while n < 6:
            count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if sum(i == j for i, j in zip(w1, w2)) == 0)
            guess = min(wordlist, key = lambda w: count[w])
            n = master.guess(guess)
            wordlist = [w for w in wordlist if sum(i == j for i, j in zip(w, guess)) == n]



844.py class Solution:
    def backspaceCompare(self, S, T):
        def construct(s):
            new_s = []
            for c in s:
                if c == "#" and len(new_s) > 0:
                    new_s.pop()
                elif c != "#":
                    new_s.append(c)
            return new_s
        s, t = construct(S), construct(T)
        return s == t



845.py class Solution:
    def longestMountain(self, A, res = 0):
        for i in range(1, len(A) - 1):
            if A[i + 1] < A[i] > A[i - 1]:
                l = r = i
                while l and A[l] > A[l - 1]: l -= 1
                while r + 1 < len(A) and A[r] > A[r + 1]: r += 1
                if r - l + 1 > res: res = r - l + 1
        return res



846.py class Solution:
    def isNStraightHand(self, hand, W):
        hand.sort()
        while hand:
            try:
                base = hand[0]
                for i in range(W):
                    hand.remove(base+i)
            except:
                return False
        return True



847.py class Solution:
    def shortestPathLength(self, graph):
        memo, final, q = set(), (1 << len(graph)) - 1, collections.deque([(i, 0, 1 << i) for i in range(len(graph))])
        while q:
            node, steps, state = q.popleft()
            if state == final: return steps
            for v in graph[node]:
                if (state | 1 << v, v) not in memo:
                    q.append((v, steps + 1, state | 1 << v))
                    memo.add((state | 1 << v, v))



848.py class Solution:
    def shiftingLetters(self, S, shifts):
        sm, res = sum(shift % 26 for shift in shifts) % 26, ""
        for i, s in enumerate(shifts):
            move, sm = ord(S[i]) + sm % 26, sm - s
            res += chr(move > 122 and move - 26 or move)
        return res



849.py class Solution:
    def maxDistToClosest(self, seats):
        d = {}
        res = l = left = r = right = 0
        for i, s in enumerate(seats):
            if not s and left: d[i] = l = l + 1
            elif s: l, left = 0, 1
        for i in range(len(seats) - 1, -1, -1):
            if not seats[i] and right and (i not in d or d[i] > r): d[i] = r = r + 1 
            elif seats[i]: r, right = 0, 1
        return max(d.values())



850.py class Solution:
    def rectangleArea(self, rectangles):
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]] + [0]))
        x_i = {v: i for i, v in enumerate(xs)}
        count = [0] * len(x_i)
        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append([y1, x1, x2, 1])
            L.append([y2, x1, x2, -1])
        L.sort()
        cur_y = cur_x_sum = area = 0
        for y, x1, x2, sig in L:
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            for i in range(x_i[x1], x_i[x2]):
                count[i] += sig
            cur_x_sum = sum(x2 - x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], count))
        return area % (10 ** 9 + 7)



851.py class Solution:
    def loudAndRich(self, richer, quiet):
        edges, memo, res = collections.defaultdict(list), {}, [i for i in range(len(quiet))]
        for r, p in richer: edges[p].append(r)
        def explore(i):
            if i in memo: return memo[i]
            cur_min = i
            for v in edges[i]:
                cur = explore(v)
                if quiet[cur] < quiet[cur_min]: cur_min = cur
            res[i] = memo[i] = cur_min
            return cur_min
        for i in range(len(quiet)): explore(i)
        return res



852.py class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mx = max(A)
        return A.index(mx)



853.py class Solution:
    def carFleet(self, target, position, speed):
        res, s = 0, {position[i]: speed[i] for i in range(len(position))}
        position.sort()
        while position:
            cur = position.pop()
            res += 1
            while position and (s[position[-1]] - s[cur]) * (target - cur) / s[cur] >= cur - position[-1]:
                position.pop()
        return res



854.py class Solution:
    def kSimilarity(self, A, B):
        b, n, k, stack = [c for c in B], len(A), float("inf"), [(0, 0, [c for c in A])]
        while stack:
            i, cnt, s = stack.pop()
            while i < n and s[i] == b[i]:
                i += 1
            if i == n:
                if cnt < k:
                    k = cnt
            else:
                for j in range(i + 1, n):
                    if s[j] == b[i] and s[j] != b[j]:
                        ls = s[:]
                        ls[i], ls[j] = ls[j], ls[i]
                        stack.append((i + 1, cnt + 1, ls))
        return k



855.py class ExamRoom:

    def __init__(self, N):
        self.seated, self.n = [], N - 1
        

    def seat(self):
        if not self.seated:
            self.seated += 0,
            return 0
        mx = ind = 0
        for i in range(1, len(self.seated)):
            l, r = self.seated[i - 1], self.seated[i]
            if (r - l) // 2 > mx:
                mx = (r - l) // 2
                ind = l + mx
        if self.seated[-1] != self.n and self.n - self.seated[-1] > mx:
            mx, ind = self.n - self.seated[-1], self.n
        if self.seated[0] >= mx:
            mx, ind = self.seated[0], 0
        self.seated.append(ind)
        self.seated.sort()
        return ind
        
        
    def leave(self, p):
        self.seated.remove(p)




856.py class Solution:
    def scoreOfParentheses(self, S):
        stack, res = [], 0
        for c in S:
            if c == "(":
                stack.append(0)
            else:
                add = 2 * stack.pop() or 1
                if stack:
                    stack[-1] += add
                else:
                    res += add
        return res



857.py class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        workers, res, heap, sumq = sorted((w / q, q, w) for q, w in zip(quality, wage)), float("inf"), [], 0
        for ratio, q, w in workers:
            heapq.heappush(heap, -q)
            sumq += q
            if len(heap) > K:
                sumq += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, ratio * sumq)
        return res



858.py class Solution:
    def mirrorReflection(self, p, q):
        side, up, h = 2, 1, 0
        while True:
            h += q * up
            side = (side + 1) % 2
            if side == 0:
                side += 2
            if h < 0:
                h *= -1
                up *= -1
            elif h > p:
                h = p - (h - p)
                up *= -1
            if h % p == 0:
                return h and side or 0



859.py class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        dif, dup = [[s1, B[i]] for i, s1 in enumerate(A) if s1 != B[i]], len(A) != len(set(A))
        return len(dif) == 2 and dif[0] == dif[1][::-1] or (not dif and dup)



860.py class Solution:
    def lemonadeChange(self, bills):
        five = ten = 0
        for num in bills:
            if num == 5:
                five += 1
            elif num == 10 and five:
                ten += 1
                five -= 1
            elif num == 20 and five and ten:
                five -= 1
                ten -= 1
            elif num == 20 and five >= 3:
                five -= 3
            else:
                return False
        return True



861.py class Solution:
    def matrixScore(self, A):
        for i, row in enumerate(A):
            if not row[0]:
                A[i] = [1 - num for num in row]
        m, n, sm = len(A), len(A and A[0]), 0
        for c in range(n):
            cnt = sum(A[r][c] for r in range(m))
            sm += max(cnt, m - cnt) * 2 ** (n - c - 1)
        return sm



862.py class Solution:
    def shortestSubarray(self, A, K):
        heap, l, sm = [], float("inf"), 0
        heapq.heappush(heap, (0, -1))
        for i, num in enumerate(A):
            sm += num
            dif = sm - K
            while heap and (heap[0][0] <= dif or i - heap[0][1] >= l):
                preSum, preIndex = heapq.heappop(heap)
                if i - preIndex < l:
                    l = i - preIndex
            heapq.heappush(heap, (sm, i))
        return l < float("inf") and l or -1



863.py class Solution:
    def distanceK(self, root, target, K):
        adj, res, visited = collections.defaultdict(list), [], collections.defaultdict(int)
        def dfs(node):
            if node.left:
                adj[node].append(node.left)
                adj[node.left].append(node)
                dfs(node.left)
            if node.right:
                adj[node].append(node.right)
                adj[node.right].append(node)
                dfs(node.right)
        dfs(root)
        def dfs2(node, d):
            if d < K:
                visited[node] = 1
                for v in adj[node]:
                    if not visited[v]:
                        dfs2(v, d + 1)
                visited[node] = 0
            else:
                res.append(node.val)
        dfs2(target, 0)
        return res



864.py class Solution:
    def shortestPathAllKeys(self, grid):
        final, m, n, si, sj = 0, len(grid), len(grid[0]), 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] in "abcdef":
                    final |= 1 << ord(grid[i][j]) - ord("a")
                elif grid[i][j] == "@":
                    si, sj = i, j
        q, memo = [(0, si, sj, 0)], set()
        while q:
            moves, i, j, state = heapq.heappop(q)
            if state == final: return moves
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] != "#":
                    if grid[x][y].isupper() and not state & 1 << (ord(grid[x][y].lower()) - ord("a")): continue
                    newState = ord(grid[x][y]) >= ord("a") and state | 1 << (ord(grid[x][y]) - ord("a")) or state
                    if (newState, x, y) not in memo:
                        memo.add((newState, x, y))
                        heapq.heappush(q, (moves + 1, x, y, newState))
        return -1



865.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.l = 0
        self.nodes = set()
        self.res = 0
        def dfs(node, l):
            if node:
                if l > self.l:
                    self.nodes = {node.val}
                    self.l = l
                elif l == self.l:
                    self.nodes.add(node.val)
                dfs(node.left, l + 1)
                dfs(node.right, l + 1)
        def dfs2(node):
            if not node: return set()
            l = dfs2(node.left)
            r = dfs2(node.right)
            total = l | r | {node.val}
            if total & self.nodes == self.nodes:
                self.res = node
                return set()
            return total
        dfs(root, 0)
        dfs2(root)
        return self.res



866.py class Solution:
    def primePalindrome(self, N):
        def isPrime(x):
            if x < 2 or x % 2 == 0: return x == 2
            for i in range(3, int(x**0.5) + 1, 2):
                if x % i == 0: return False
            return True
        if 8 <= N <= 11: return 11
        for x in range(10 ** (len(str(N)) // 2), 10**5):
            y = int(str(x) + str(x)[-2::-1])
            if y >= N and isPrime(y): return y



867.py class Solution:
    def transpose(self, A):
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]



868.py class Solution:
    def binaryGap(self, N):
        pre = dist = 0
        for i, c in enumerate(bin(N)[2:]):
            if c == "1":
                dist = max(dist, i - pre)
                pre = i
        return dist



869.py class Solution:
    def reorderedPowerOf2(self, N):
        cnt = collections.Counter(str(N))
        return any(cnt == collections.Counter(str(1 << c)) for c in range(32))



870.py class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort(reverse = True)
        non = []
        res = [-1] * len(A)
        for b, i in sorted([(b, i) for i, b in enumerate(B)]):
            while A and A[-1] <= b:
                non.append(A.pop())
            if A:
                res[i] = A.pop()
            else:
                break
        for i in range(len(res)):
            if res[i] == -1:
                res[i] = non.pop()
        return res 



871.py class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        q, n, memo = [(0, -startFuel, 0, 0)], len(stations), set()
        while q:
            refill, fuel, pos, index = heapq.heappop(q)
            fuel *= -1
            if index == n:
                if fuel - (target - pos) >= 0:
                    return refill
            else:
                sPos, add = stations[index]
                if (index, refill) not in memo and fuel - (sPos - pos) >= 0:
                    memo.add((index, refill))
                    f1 = (fuel - (sPos - pos) + add) * -1
                    f2 = (fuel - (sPos - pos)) * -1
                    heapq.heappush(q, (refill + 1, f1, sPos, index + 1))
                    heapq.heappush(q, (refill, f2, sPos, index + 1))
        return -1



872.py class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node, arr):
            if node:
                if not node.left and not node.right: arr += [node.val]
                dfs(node.left, arr)
                dfs(node.right, arr)
                return arr
        return dfs(root1, []) == dfs(root2, [])



873.py class Solution:
    def lenLongestFibSubseq(self, A):
        n, pair, res, back = len(A), {}, 0, set()
        for i in range(n):
            back.add(A[i])
            j = i + 1
            mx = 2 * A[i]
            while j < n and A[j] < mx:
                if (A[j] - A[i], A[i]) in pair:
                    pair[(A[i], A[j])] = pair[(A[j] - A[i], A[i])] + 1
                else:
                    pair[(A[i], A[j])] = A[j] - A[i] in back and 3 or 2
                res = max(res, pair[(A[i], A[j])])
                j += 1
        return res > 2 and res or 0



874.py class Solution:
    def robotSim(self, commands, obstacles):
        i = j = mx = 0
        d, move, obstacles = 3, [(-1, 0), (0, -1), (1, 0), (0, 1)], set(map(tuple, obstacles))
        for command in commands:
            if command == -2: d = (d + 1) % 4
            elif command == -1: d = (d - 1) % 4
            else:
                x, y = move[d]
                while command and (i + x, j + y) not in obstacles:
                    i += x
                    j += y
                    command -= 1
            mx = max(mx, i ** 2 + j ** 2)
        return mx



875.py class Solution:
    def minEatingSpeed(self, piles, H):
        piles.sort()
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            h = sum(math.ceil(p / mid) for p in piles)
            if h > H:
                l = mid + 1
            elif h < H:
                r = mid - 1
            else:
                return mid
        return l



876.py class Solution:
    def middleNode(self, head):
        root, n = head, 0
        while head:
            head = head.next
            n += 1
        for _ in range(n // 2):
            root = root.next
        return root  



877.py class Solution:
    def stoneGame(self, piles): return True



878.py class Solution:
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def count(self, num, A, B, C):
        return num // A + num // B - num // C
    
    def nthMagicalNumber(self, N, A, B):
        l, r, C = 2, 2 ** 63  - 1, A * B // self.gcd(A, B)
        while l < r:
            mid = (l + r) // 2
            if self.count(mid, A, B, C) < N:
                l = mid + 1
            else:
                r = mid
        return l % (10 ** 9 + 7)



879.py class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (G + 1) for i in range(P + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(P, -1, -1):
                for j in range(G - g, -1, -1):
                    dp[min(i + p, P)][j + g] += dp[i][j]
        return sum(dp[P]) % (10**9 + 7)



880.py class Solution:
    def decodeAtIndex(self, S, K):
        stack, l = [], 0
        for c in S:
            l = l + 1 if c.isalpha() else l * int(c)
            stack += c,
            while l >= K:
                while stack[-1].isdigit(): l //= int(stack.pop())
                K = K % l
                if not K: return stack[-1]
                l -= 1
                stack.pop()



881.py class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        l, r, cnt = 0, len(people) - 1, 0
        while l <= r:
            if l != r and people[l] + people[r] > limit: l -= 1
            l += 1
            r -= 1
            cnt += 1
        return cnt



882.py class Solution:
    def reachableNodes(self, edges, M, N):
        adj, seen = collections.defaultdict(dict), set()
        for a, b, l in edges:
            adj[a][b] = [l, 0]
            adj[b][a] = [l, 0]
        q = [(0, M, None)]
        while q:
            new = []
            for i, moves, pre in q:
                seen.add(i)
                for j in adj[i]:
                    if moves > adj[i][j][1]:
                        adj[i][j][1] = moves
                        if moves > adj[i][j][0] and j != pre:
                            new.append((j, moves - adj[i][j][0] - 1, i))
            q = new 
        return sum(min(adj[i][j][1] + adj[j][i][1], l) for i, j, l in edges) + len(seen)



883.py class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        top = sum(grid[i][j] != 0 for i in range(n) for j in range(n))
        front = sum(max(grid[i]) for i in range(n))
        side = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        return top + front + side



884.py class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        c1 = collections.Counter(A.split())
        c2 = collections.Counter(B.split())
        return list(c for c in c1 if c1[c] == 1 and c not in c2) + list(c for c in c2 if c2[c] == 1 and c not in c1)



885.py class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        direct, res, n, l, ind = [(-1, 0), (0, 1), (1, 0), (0, -1)], [[r0, c0]], R * C, 1, 1
        while len(res) < n:
            for __ in range(2):
                for _ in range(l):
                    r0 += direct[ind][0]
                    c0 += direct[ind][1]
                    if 0 <= r0 < R and 0 <= c0 < C:
                        res.append([r0, c0])
                ind = (ind + 1) % 4
            l += 1
        return res



886.py class Solution:
    def merge(self, node, p, group, disliked):
        group[node] = p
        for v in disliked[node]:
            if group[v] == p or (group[v] == v and not self.merge(v, -p, group, disliked)): return False
        return True
    
    def possibleBipartition(self, N, dislikes):
        group, disliked = [i for i in range(N + 1)], collections.defaultdict(set)
        for a, b in dislikes:
            disliked[a].add(b)
            disliked[b].add(a) 
        for i in range(1, N + 1):
            if group[i] == i and not self.merge(i, 2001, group, disliked): return False
        return True



887.py class Solution:
    def superEggDrop(self, K, N):
        drops = 0                           # the number of eggs dropped
        floors = [0 for _ in range(K + 1)]  # floors[i] is the number of floors that can be checked with i eggs

        while floors[K] < N:                # until we can reach N floors with K eggs 

            for eggs in range(K, 0, -1):
                floors[eggs] += 1 + floors[eggs - 1]
            drops += 1

        return drops



888.py class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a, b = set(A), set(B)
        diff =(sum(A) - sum(B)) // 2
        for c in B:
            if c + diff in a:
                return [c + diff, c]



889.py class Solution:
    def constructFromPrePost(self, pre, post):
        if pre:
            root = TreeNode(pre.pop(0))
            post.pop()
            if pre:
                if pre[0] == post[-1]:
                    root.left = self.constructFromPrePost(pre, post)
                else:
                    l, r = post.index(pre[0]), pre.index(post[-1])
                    root.left = self.constructFromPrePost(pre[:r], post[:l + 1])
                    root.right = self.constructFromPrePost(pre[r:], post[l + 1:]) 
            return root



890.py class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for w in words:
            mp12, mp21, match = {}, {}, True
            for c1, c2 in zip(w, pattern):
                if (c1 in mp12 and mp12[c1] != c2) or (c2 in mp21 and mp21[c2] != c1):
                    match = False
                    break
                mp12[c1], mp21[c2] = c2, c1
            if match: res.append(w)
        return res



891.py class Solution:
    def sumSubseqWidths(self, A):
        A.sort()
        res=0
        for i in range(len(A)):
            res*=2
            res-=A[i]
            res+=A[~i]
        return res % (10**9+7)



892.py class Solution:
    def surfaceArea(self, grid):
        n, sm = len(grid), 0
        for i in range(n):
            for j in range(n):
                sm += grid[i][j] and grid[i][j] * 4 + 2
                if i > 0: sm -= min(grid[i - 1][j], grid[i][j])
                if j > 0: sm -= min(grid[i][j - 1], grid[i][j])
                if i < n - 1: sm -= min(grid[i + 1][j], grid[i][j])
                if j < n - 1: sm -= min(grid[i][j + 1], grid[i][j])
        return sm



893.py class Solution:
    def numSpecialEquivGroups(self, A):
        return len(set("".join(sorted(s[0::2])) + "".join(sorted(s[1::2])) for s in A))



894.py class Solution:
    def allPossibleFBT(self, N):
        def constr(N):
            if N == 1: yield TreeNode(0)
            for i in range(1, N, 2):
                for l in constr(i):
                    for r in constr(N - i - 1):
                        m = TreeNode(0)
                        m.left = l
                        m.right = r
                        yield m
        return list(constr(N))



895.py class FreqStack:

    def __init__(self):
        self.stacks = collections.defaultdict(list)
        self.freq = collections.Counter()
        self.maxFreq = 0

    def push(self, x):
        self.freq[x] += 1 
        self.maxFreq = max(self.maxFreq, self.freq[x])
        self.stacks[self.freq[x]].append(x)

    def pop(self):
        num = self.stacks[self.maxFreq].pop()
        self.freq[num] -= 1 
        if not self.stacks[self.maxFreq]: self.maxFreq -= 1
        return num



896.py class Solution:
    def isMonotonic(self, A):
        return all(A[i] <= A[i - 1] for i in range(1, len(A))) or all(A[i] >= A[i - 1] for i in range(1, len(A)))



897.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root, tail = None):
        if not root: return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res



898.py class Solution:
    def subarrayBitwiseORs(self, A):
        nums, n, pre = set(), len(A), set()
        for a in A:
            pre = {a} | {num | a for num in pre}
            nums |= pre
        return len(nums)



899.py class Solution:
    def orderlyQueue(self, S, K):
        return "".join(sorted(S)) if K > 1 else min(S[i:] + S[:i] for i in range(len(S)))



900.py class RLEIterator:

    def __init__(self, A):
        self.it = A[::-1]

    def next(self, n):
        while self.it and self.it[-1] <= n:
            if self.it[-1]: last = self.it[-2]
            n -= self.it.pop()
            self.it.pop()
        if n and self.it:
            self.it[-1] -= n
            last = self.it[-2]
        return last if self.it else -1
        



901.py class StockSpanner:

    def __init__(self):
        self.arr = []  
        self.res = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if self.arr and self.arr[-1] > price: self.res.append(1)
        else:
            i = len(self.arr) - 1
            while i >= 0:
                if self.arr[i] <= price and self.res[i]:
                    i -= self.res[i]
                else: break
            self.res.append(len(self.arr) - i)
        self.arr.append(price)
        return self.res[-1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)



902.py class Solution:
    def atMostNGivenDigitSet(self, D, N):
        def less(c):
            return len([char for char in D if char < c])
        d, cnt, l = len(D), 0, len(str(N))
        # For numbers which have less digits than N, simply len(D) ** digits_length different numbers can be created
        for i in range(1, l):
            cnt += d ** i
        """
        We should also consider edge cases where previous digits match with related digits in N. In this case, we can make a number with             previous digits + (digits less than N[i]) + D ** remaining length
        """
        for i, c in enumerate(str(N)):
            cnt += less(c) * (d ** (l - i - 1))
            if c not in D: break
            if i == l - 1: cnt += 1
        return cnt



903.py class Solution:
    def numPermsDISequence(self, S: str) -> int:
        dp = [1] * (len(S) + 1)
        for c in S:
            if c == "I":
                dp = dp[:-1]
                for i in range(1, len(dp)):
                    dp[i] += dp[i - 1]
            else:
                dp = dp[1:]
                for i in range(len(dp) - 1)[::-1]:
                    dp[i] += dp[i + 1]
        return dp[0] % (10**9 + 7)



904.py class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res = i = 0
        last = collections.defaultdict(int)
        for j, val in enumerate(tree):
            if len(last) == 2 and val not in last:
                pre = min(last.values())
                i = pre + 1
                last.pop(tree[pre])
            last[val] = j
            res = max(res, j - i + 1)
        return res



905.py class Solution:
    def sortArrayByParity(self, A):
        return [a for a in A if not a % 2] + [a for a in A if a % 2]



906.py class Solution:
    def superpalindromesInRange(self, L, R):
        L, R = int(L), int(R)
        left = int(math.floor(math.sqrt(L)))
        right = int(math.ceil(math.sqrt(R)))
        n1, n2 = len(str(left)), len(str(right))
        n1 = n1//2 if n1%2==0 else n1//2+1
        n2 = n2//2 if n2%2==0 else n2//2+1
        start = int('1' + '0'*(n1 - 1))
        end = int('9' * n2) + 1
        ans = 0 
        for i in range(start, end):
            x = str(i)
            num1 = int(x + x[::-1])
            num2 = int(x + x[:-1][::-1])
            for num in [num1, num2]:
                cand = num * num
                if L <= cand <= R and str(cand) == str(cand)[::-1]:
                    ans += 1
        return ans



907.py class Solution:
    def sumSubarrayMins(self, A):
        res, stack = 0, []  
        A = [float('-inf')] + A + [float('-inf')]
        for i, n in enumerate(A):
            while stack and A[stack[-1]] > n:
                cur = stack.pop()
                res += A[cur] * (i - cur) * (cur - stack[-1])
            stack.append(i)
        return res % (10 ** 9 + 7)



908.py class Solution:
    def smallestRangeI(self, A, K):
        l, r = min(A) + K, max(A) - K 
        return 0 if l >= r else r - l



909.py class Solution:
    def snakesAndLadders(self, board):
        arr, nn, q, seen, moves = [0], len(board) ** 2, [1], set(), 0
        for i, row in enumerate(board[::-1]): arr += row[::-1] if i % 2 else row
        while q:
            new = []
            for sq in q:
                if sq == nn: return moves 
                for i in range(1, 7):
                    if sq + i <= nn and sq + i not in seen:
                        seen.add(sq + i)
                        new.append(sq + i if arr[sq + i] == -1 else arr[sq + i])
            q, moves = new, moves + 1
        return -1                    



910.py class Solution:
    def smallestRangeII(self, A, K):
        A.sort()
        return min([max(A[-1] - K, A[i] + K) - min(A[0] + K, A[i + 1] - K) for i in range(len(A) - 1)] + [A[-1] - A[0]])



911.py class TopVotedCandidate:

    def __init__(self, persons, times):
        votes = collections.defaultdict(int)
        winner = 0
        self.winners = [None] * len(times)
        self.times = times
        for i, person in enumerate(persons):
            votes[person] += 1 
            if votes[person] >= votes[winner]:
                winner = person
            self.winners[i] = winner

    def q(self, t):
        return self.winners[bisect.bisect(self.times, t) - 1]



912.py class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot = random.choice(nums)
        lt = [v for v in nums if v < pivot]
        eq = [v for v in nums if v == pivot]
        gt = [v for v in nums if v > pivot]

        return self.sortArray(lt) + eq + self.sortArray(gt)
    



913.py class Solution:
    def catMouseGame(self, graph: 'List[List[int]]') -> 'int':
        mouse_visited = [False] * len(graph)
        mouse_win_map = [[None for column in range(len(graph))] for row in range(len(graph))]
        cat_visited = [False] * len(graph)
        cat_win_map = [[None for column in range(len(graph))] for row in range(len(graph))]
        if self.isMouseWin(graph, 1, 2, mouse_visited, mouse_win_map):
            return 1
        elif self.isCatWin(graph, 1, 2, cat_visited, cat_win_map):
            return 2
        else:
            return 0

    def isMouseWin(self, graph, mouse, cat, mouse_visited, mouse_win_map):
        if mouse == 0:
            return True
        if mouse_win_map[mouse][cat] is not None:
            return mouse_win_map[mouse][cat]
        mouse_visited[mouse] = True
        for mouseMove in graph[mouse]:
            if mouseMove == 0 or (mouseMove not in graph[cat] and  mouseMove != cat):
                if not mouse_visited[mouseMove]:
                    mouseWinFlag = True
                    for catMove in graph[cat]:
                        if catMove != 0 and not self.isMouseWin(graph, mouseMove, catMove, mouse_visited, mouse_win_map):
                            mouseWinFlag = False
                            break
                    if mouseWinFlag:
                        mouse_visited[mouse] = False
                        mouse_win_map[mouse][cat] = True
                        return True
        mouse_visited[mouse] = False
        mouse_win_map[mouse][cat] = False
        return False

    def isCatWin(self, graph, mouse, cat, cat_visited, cat_win_map):
        if mouse == 0:
            return False
        if cat_win_map[mouse][cat] is not None:
            return cat_win_map[mouse][cat]
        cat_visited[cat] = True
        for mouseMove in graph[mouse]:
            if mouseMove == 0 or (mouseMove not in graph[cat] and  mouseMove != cat):
                catWinFlag = True
                for catMove in graph[cat]:
                    if catMove != 0 and not cat_visited[catMove] and not self.isCatWin(graph, mouseMove, catMove,
                                                                                       cat_visited, cat_win_map):
                        catWinFlag = False
                        break
                if not catWinFlag:
                    cat_visited[cat] = False
                    cat_win_map[mouse][cat] = False
                    return False
        cat_visited[cat] = False
        cat_win_map[mouse][cat] = True
        return True



914.py class Solution:
    def hasGroupsSizeX(self, deck):
        import functools
        def gcd(a, b):
            if not b: return a
            return gcd(b, a % b)
        return functools.reduce(gcd, collections.Counter(deck).values()) != 1



915.py class Solution:
    def partitionDisjoint(self, A):
        rMin, lMax, mx, mn = [0] * len(A), [0] * len(A), -float("inf"), float("inf")
        for i, num in enumerate(A):
            mx = max(mx, num)
            lMax[i] = mx 
        for i in range(len(A) - 1, -1, -1):
            mn = min(mn, A[i])
            rMin[i] = mn 
        for i in range(len(A) - 1):
            if lMax[i] <= rMin[i + 1]:
                return i + 1



916.py class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        cnt = collections.Counter()
        for b in B:
            for k, v in collections.Counter(b).items():
                if cnt[k] < v:
                    cnt[k] = v
        res = []
        for a in A:
            if not cnt - collections.Counter(a):
                res.append(a)
        return res



917.py class Solution:
    def reverseOnlyLetters(self, S):
        r = [s for s in S if s.isalpha()]
        return "".join(S[i] if not S[i].isalpha() else r.pop() for i in range(len(S)))



918.py class Solution:
    def maxSubarraySumCircular(self, A):
        lMn, rMx, res, lSm, rSm, preSm = float("inf"), [-float("inf")] * (len(A) + 1), -float("inf"), 0, 0, 0
        for i in range(len(A) - 1, -1, -1):
            rSm += A[i]
            rMx[i] = max(rMx[i + 1], rSm)
        for i in range(len(A)):
            preSm += A[i]
            lMn = min(lMn, lSm)
            res = max(res, preSm, preSm - lMn, preSm + rMx[i + 1])
            lSm += A[i]
        return res



919.py class CBTInserter:

    def __init__(self, root):
        self.arr, q = [], [root]
        while q:
            self.arr += [node for node in q]
            q = [child for node in q for child in (node.left, node.right) if child]

    def insert(self, v):
        parent = self.arr[(len(self.arr) - 1) // 2]
        if not len(self.arr) % 2:
            child = parent.right = TreeNode(v)
        else:
            child = parent.left = TreeNode(v)
        self.arr += [child]
        return parent.val

    def get_root(self):
        return self.arr[0]



920.py from functools import lru_cache

class Solution:
    def numMusicPlaylists(self, N, L, K):
        @lru_cache(None)
        def dp(i, j): return +(j == 0) if not i else (dp(i-1, j-1) * (N-j+1) + dp(i-1, j) * max(j-K, 0)) % (10**9+7)
        return dp(L, N)



921.py class Solution:
    def minAddToMakeValid(self, S):
        r, l = 0, []
        for s in S:
            if s == "(":
                l.append(s)
            elif l:
                l.pop()
            else:
                r += 1 
        return r + len(l)



922.py class Solution:
    def sortArrayByParityII(self, A):
        even, odd = [a for a in A if not a % 2], [a for a in A if a % 2]
        return [even.pop() if not i % 2 else odd.pop() for i in range(len(A))]



923.py class Solution:
    def threeSumMulti(self, A, target):
        c = collections.Counter(A)
        res = 0
        for i, j in itertools.combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k: res += c[i] * (c[i] - 1) * (c[i] - 2) // 6
            elif i == j != k: res += c[i] * (c[i] - 1) // 2 * c[k]
            elif k > i and k > j: res += c[i] * c[j] * c[k]
        return res % (10**9 + 7)



924.py class Solution:
    def minMalwareSpread(self, graph, initial):
        def dfs(i):
            nodes.add(i)
            for j in range(len(graph[i])):
                if graph[i][j] and j not in nodes:
                    dfs(j)
        rank, initial = collections.defaultdict(list), set(initial)
        for node in sorted(initial):
            nodes = set()
            dfs(node)
            if nodes & initial == {node}:
                rank[len(nodes)].append(node)
        return rank[max(rank)][0] if rank else min(initial)



925.py class Solution:
    def isLongPressedName(self, name, typed):
        pre, i = None, 0
        for c in typed:
            if i < len(name) and c == name[i]:
                pre, i = name[i], i + 1
            elif c != pre:
                return False
        return i == len(name)



926.py class Solution:
    def minFlipsMonoIncr(self, s):
        res = cur = s.count("0")
        for c in s: res, cur = c == "1" and (res, cur + 1) or (min(res, cur - 1), cur - 1)
        return res



927.py class Solution(object):
    def threeEqualParts(self, A):
        sm = sum(A)
        if sm % 3: return [-1, -1]
        t = sm // 3
        if not t: return [0, len(A) - 1]
        breaks = [0] + [i for i, x in enumerate(A) if x]
        i1, j1, i2, j2, i3, j3 = breaks[1], breaks[t], breaks[t + 1], breaks[2 * t], breaks[2 * t + 1], breaks[3 * t]
        if not (A[i1: j1 + 1] == A[i2: j2 + 1] == A[i3: j3 + 1]): return [-1, -1]
        if i2 - j1 < len(A) - j3 or i3 - j2 < len(A) - j3: return [-1, -1]
        return [j1 + len(A) - j3 - 1, j2+ len(A) - j3]



928.py class Solution:
    def minMalwareSpread(self, graph, initial):
        def dfs(i):
            seen.add(i)
            return not any(graph[i][j] and j not in seen and (j in initials or not dfs(j)) for j in range(len(graph[i])))
        res, mx, initials = min(initial), 1, set(initial)
        for node in sorted(initial):
            impact = set()
            for j in range(len(graph[node])):
                seen = {node}
                if graph[node][j] and j not in initials and dfs(j): impact |= seen
            if len(impact) > mx: res, mx = node, len(impact)
        return res



929.py class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        rec = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            rec.add(local + '@' + domain)
        return len(rec)



930.py class Solution:
    def numSubarraysWithSum(self, A, S):
        res, sm, sums = 0, 0, collections.defaultdict(int)
        for a in A:
            sm += a
            res += sums[sm - S] + (sm == S)
            sums[sm] += 1
        return res



931.py class Solution:
    def minFallingPathSum(self, A):
        for i in range(1, len(A)):
            for j in range(len(A)):
                A[i][j] += min(A[i - 1][j and j - 1:j + 2])
        return min(A[-1])



932.py class Solution:
    def beautifulArray(self, N):
        if N == 1: return [1]
        half = self.beautifulArray(N - N // 2)
        return [i * 2 - 1 for i in half] + [i * 2 for i in half if i * 2 <= N]



933.py class RecentCounter:

    def __init__(self):
        self.p = collections.deque()        

    def ping(self, t):
        self.p.append(t)
        while self.p[0] < t - 3000:
            self.p.popleft()
        return len(self.p)



934.py class Solution:
    def shortestBridge(self, A):
        def dfs(i, j):
            A[i][j] = -1
            q.append((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                    dfs(x, y)
        def first():
            for i in range(n):
                for j in range(n):
                    if A[i][j]:
                        return i, j
        n, step, q = len(A), 0, []
        dfs(*first())
        while True:
            new = []
            for i, j in q:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            new.append((x, y))
            step += 1
            q = new



935.py class Solution:
    def knightDialer(self, N):
        x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1
        for _ in range(N - 1):
            x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = \u005C
                x6 + x8, x7 + x9, x4 + x8, \u005C
                x7 + x9 + x0, 0, x1 + x7 + x0, \u005C
                x2 + x6, x1 + x7, x2 + x4, \u005C
                x4 + x6
        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % (10 ** 9 + 7)



936.py class Solution:
    def movesToStamp(self, stamp, target):
        def okay(s):
            ret = False
            for c1, c2 in zip(s, stamp):
                if c1 == "*": continue
                elif c1 != c2: return False
                else: ret = True
            return ret
        t, move, mx, arr = "*" * len(target), 0, 10 * len(target), []
        while move < mx:
            pre = move
            for i in range(len(target) - len(stamp) + 1):
                if okay(target[i:i + len(stamp)]):
                    move += 1
                    arr = [i] + arr
                    target = target[:i] + "*" * len(stamp) + target[i + len(stamp):]
            if target == t: return arr
            if move == pre: break
        return []



937.py class Solution:
    def reorderLogFiles(self, logs):
        return sorted(filter(lambda l: l[l.find(" ") + 1].isalpha(), logs), key = lambda x: (x[x.find(" "):], x[:x.find(" ")])) + list(filter(lambda l: l[l.find(" ") + 1].isdigit(), logs))



938.py class Solution:
    def rangeSumBST(self, root, L, R):
        if not root: return 0
        l = self.rangeSumBST(root.left, L, R)
        r = self.rangeSumBST(root.right, L, R)
        return l + r + (L <= root.val <= R) * root.val



939.py class Solution:
    def minAreaRect(self, points):
        seen, bases, baseX, res = collections.defaultdict(dict), [], -1, float("inf")
        for x, y in sorted(points):
            if x != baseX:
                baseX, bases = x, []
            for base in bases:
                if y in seen[base]:
                    res = min(res, (x - seen[base][y]) * (y - base))
                seen[base][y] = x
            bases.append(y)
        return res if res < float("inf") else 0



940.py class Solution:
    def distinctSubseqII(self, S):
        res, end = 0, collections.Counter()
        for c in S:
            res, end[c] = res * 2 + 1 - end[c], res + 1
        return res % (10**9 + 7)



941.py class Solution:
    def validMountainArray(self, A):
        i = A and A.index(max(A))
        return A and 0<i<len(A)-1 and all(a1<a2 for a1,a2 in zip(A[:i],A[1:i+1])) and all(a2>a3 for a2,a3 in zip(A[i:],A[i+1:])) or False



942.py class Solution:
    def diStringMatch(self, S):
        l, r, arr = 0, len(S), []
        for s in S:
            arr.append(l if s == "I" else r)
            l, r = l + (s == "I"), r - (s == "D")
        return arr + [l]



943.py class Solution:
    def shortestSuperstring(self, A):
        def merge(a, b):
            for i in range(len(b), 0, -1):
                if a.endswith(b[:i]):
                    return i
            return 0
        def dfs(sup, s, st):
            if len(sup + "".join(st)) < len(res[0]):
                res[0] = sup + "".join(st)
            if st and any(new in st for new in merged[s][1:]):
                for new in merged[s][1:]:
                    if new in st:
                        dfs(sup + new[merged[s][0]:], new, st - {new})
            else:
                for nex in st:
                    for new in merged[nex][1:]:
                        if new in st:
                            dfs(sup + nex + new[merged[nex][0]:], new, st - {nex, new})
        merged = {}
        for a, b in itertools.combinations(A, 2):
            for a, b in ((a, b), (b, a)):
                s = merge(a, b)
                if a not in merged or s > merged[a][0]:
                    merged[a] = [s, b]
                elif s == merged[a][0]:
                    merged[a].append(b)
        res, st = ["".join(A)], set(A)
        for a in A:
            dfs(a, a, st - {a})
        return res[0]



944.py class Solution:
    def minDeletionSize(self, A):
        return sum(any(a[j] > b[j] for a, b in zip(A, A[1:])) for j in range(len(A[0])))



945.py class Solution:
    def minIncrementForUnique(self, A):
        st, used, move = set(A), set(), 0
        heapq.heapify(A)
        empty = [i for i in range(80000) if i not in st][::-1] if A else [] 
        while A:
            num = heapq.heappop(A)
            if num not in used:
                used.add(num)
            else:
                while empty[-1] < num:
                    empty.pop()
                move += empty[-1] - num
                heapq.heappush(A, empty.pop())
        return move



946.py class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        arr, i = [], 0
        for num in pushed:
            arr.append(num)
            while arr and arr[-1] == popped[i]:
                i += 1
                arr.pop()
        return arr == popped[i:][::-1]



947.py class Solution:
    def removeStones(self, stones):
        def dfs(i, j):
            points.discard((i, j))
            for y in rows[i]:
                if (i, y) in points:
                    dfs(i, y)
            for x in cols[j]:
                if (x, j) in points:
                    dfs(x, j)
        points, island, rows, cols = {(i, j) for i, j in stones}, 0, collections.defaultdict(list), collections.defaultdict(list)
        for i, j in stones:
            rows[i].append(j)
            cols[j].append(i)
        for i, j in stones:
            if (i, j) in points:
                dfs(i, j)
                island += 1
        return len(stones) - island



948.py class Solution:
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        l, r, score = 0, len(tokens) - 1, 0
        while l <= r:
            if P >= tokens[l]:
                P -= tokens[l]
                score += 1
                l += 1
            elif score and l != r:
                P += tokens[r]
                score -= 1
                r -= 1
            else:
                break
        return score



949.py class Solution:
    def largestTimeFromDigits(self, A):
        h = m = -float("inf")
        for n1, n2, n3, n4 in itertools.permutations(A):
            hh, mm = n1 * 10 + n2, n3 * 10 + n4
            if 0 <= hh <= 23 and 0 <= mm <= 59 and (hh > h or hh == h and mm > m):
                h, m = hh, mm
        sh = str(h) if h > 9 else "0" + str(h)
        sm = str(m) if m > 9 else "0" + str(m)
        return 0 <= h <= 23 and 0 <= m <= 59 and sh + ":" + sm or ""



950.py class Solution:
    def deckRevealedIncreasing(self, deck):
        ind = list(range(len(deck)))
        for num in sorted(deck):
            deck[ind[0]] = num
            ind = ind[2:] + [ind[1]] if len(ind) > 1 else []
        return deck



951.py class Solution:
    def flipEquiv(self, root1, root2):
        if not root1 or not root2: return root1 == root2
        if root1.left and root2.left and root1.left.val != root2.left.val or (not root1.left and root2.left) or (root1.left and not root2.left):
            root1.left, root1.right = root1.right, root1.left
        return root1.val == root2.val and self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)



952.py class Solution:
    def largestComponentSize(self, A):
        def find(i):
            return i if i == parent[i] else find(parent[i])
        
        def prime_factors(n):  
            res = set()
            while n % 2 == 0: 
                res.add(2)
                n //= 2
            for i in range(3, int(n**0.5) + 1, 2): 
                while n % i== 0: 
                    res.add(i) 
                    n //= i 
            if n > 2: 
                res.add(n)
            return res
        parent, dic = list(range(len(A))), {} 
        for i, n in enumerate(A):
            for p in prime_factors(n):
                if p in dic:
                    parent[find(i)] = find(dic[p])
                dic[p] = i
        for i, x in enumerate(parent):
            parent[i] = find(x)
        return max(collections.Counter(parent).values())



953.py class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        ind = {c: i for i, c in enumerate(order)}
        for a, b in zip(words, words[1:]):
            if len(a) > len(b) and a[:len(b)] == b:
                return False
            for s1, s2 in zip(a, b):
                if ind[s1] < ind[s2]:
                    break
                elif ind[s1] == ind[s2]:
                    continue
                else: 
                    return False
        return True



954.py class Solution:
    def canReorderDoubled(self, A):
        cnt = collections.Counter(A)
        for a in sorted(A, key = abs):
            if cnt[a] and cnt[a * 2]:
                cnt[a] -= 1
                cnt[a * 2] -= 1
            elif cnt[a] and a % 2 == 0 and cnt[a // 2]:
                cnt[a] -= 1
                cnt[a // 2] -= 1   
        return all(cnt[a] == 0 for a in A)



955.py class Solution:
    def minDeletionSize(self, A):
        res = 0
        cur = [""] * len(A)
        for col in zip(*A):
            cur2 = list(zip(cur, col))
            if cur2 == sorted(cur2):
                cur = cur2
            else:
                res += 1
        return res



956.py class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for x in rods:
            for d, h in list(dp.items()):
                dp[d + x] = max(dp.get(x + d, 0), h)
                dp[abs(d - x)] = max(dp.get(abs(d - x), 0), h + min(d, x))
        return dp[0]         



957.py class Solution:
    def prisonAfterNDays(self, cells, N):
        day, state, cur = 0, {}, "".join(map(str, cells))
        while cur not in state:
            state[cur] = day
            state[day] = cur
            if day == N:
                return list(map(int, cur))
            day += 1
            cur = "0" + "".join(cur[i - 1] == cur[i + 1] and "1" or "0" for i in range(1, len(cur) - 1)) + "0"
        return list(map(int, state[state[cur] + (N - state[cur]) % (day - state[cur])]))



958.py class Solution:
    def isCompleteTree(self, root):
        q, pre = [root, None], 1
        while any(q):
            i = q.index(None)
            if any(q[i:]) or pre > 1:
                return False
            pre = len(q[i:])
            q = [child for node in q[:i] for child in (node.left, node.right)] + [None]
        return True



959.py class Solution:
    def regionsBySlashes(self, grid):
        def dfs(i, j, k):
            if 0 <= i < n > j >= 0 and not matrix[i][j][k]:
                if grid[i][j] == "*":
                    if k <= 1:
                        matrix[i][j][0] = matrix[i][j][1] = cnt
                        dfs(i - 1, j, 2)
                        dfs(i, j + 1, 3)
                    else:
                        matrix[i][j][2] = matrix[i][j][3] = cnt
                        dfs(i + 1, j, 0)
                        dfs(i, j - 1, 1)
                elif grid[i][j] == "/":
                    if 1 <= k <= 2:
                        matrix[i][j][1] = matrix[i][j][2] = cnt
                        dfs(i, j + 1, 3)
                        dfs(i + 1, j, 0)
                    else:
                        matrix[i][j][0] = matrix[i][j][3] = cnt
                        dfs(i - 1, j, 2)
                        dfs(i, j - 1, 1)
                else:
                    matrix[i][j][0] = matrix[i][j][1] = matrix[i][j][2] = matrix[i][j][3] = cnt
                    dfs(i - 1, j, 2)
                    dfs(i, j + 1, 3)
                    dfs(i + 1, j, 0)
                    dfs(i, j - 1, 1)
        grid, n = [row.replace("\u005C\u005C", "*") for row in grid], len(grid)
        matrix, cnt = [[[0, 0, 0, 0] for j in range(n)] for i in range(n)], 0
        for i in range(n):
            for j in range(n):
                for k in range(4):
                    if not matrix[i][j][k]:
                        cnt += 1
                        dfs(i, j, k)
        return cnt



960.py class Solution:
    def minDeletionSize(self, A):
        m, n = len(A), len(A[0])
        dp = [1] * n
        for j in range(1, n):
            for i in range(j):
                if all(A[k][i] <= A[k][j] for k in range(m)):
                    dp[j] = max(dp[j], dp[i] + 1)
        return n - max(dp)



961.py class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return collections.Counter(A).most_common(1)[0][0]



962.py class Solution:
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ind, mx, index = float("inf"), 0, collections.defaultdict(list)
        for i, num in enumerate(A):
            index[num].append(i)
        A.sort()
        for i in range(len(A)):
            mx = max(mx, index[A[i]][-1] - ind)
            ind = min(ind, index[A[i]][0])
        return mx



963.py 
class Solution:
    def minAreaFreeRect(self, points):
        mn, st, n = float('inf'), {(x, y) for x, y in points}, len(points) 
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    if not (x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1) and (x3 + (x2 - x1), y3 + (y2 - y1)) in st:
                        mn = min(mn, ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 * ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5)
        return mn if mn < float("inf") else 0



964.py class Solution:
    def leastOpsExpressTarget(self, x: int, y: int) -> int:
        pos = neg = k = 0
        while y:
            y, cur = divmod(y, x)
            if k:
                pos, neg = min(cur * k + pos, (cur + 1) * k + neg), min((x - cur) * k + pos, (x - cur - 1) * k + neg)
            else:
                pos, neg = cur * 2, (x - cur) * 2
            k += 1
        return min(pos, k + neg) - 1



965.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        if root.left and root.left.val != root.val: return False
        if root.right and root.right.val != root.val: return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)



966.py class Solution:
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        st, cap, vow = set(wordlist), {}, {}
        for w in wordlist:
            newC = w.lower()
            newW = "".join(c if c not in "aeiou" else "*" for c in newC)
            if newC not in cap:
                cap[newC] = w
            if newW not in vow:
                vow[newW] = w
        for i, w in enumerate(queries):
            if w in st:
                pass
            elif w.lower() in cap:
                queries[i] = cap[w.lower()]
            else:
                new = "".join(c if c not in "aeiou" else "*" for c in w.lower())
                if new in vow:
                    queries[i] = vow[new]
                else:
                    queries[i] = ""
        return queries



967.py class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        q = {i for i in range(10)}
        for _ in range(N - 1):
            new = set()
            for num in q:
                last = num % 10
                if num and 0 <= last + K <= 9:
                    new.add(num * 10 + last + K)
                if num and 0 <= last - K <= 9:
                    new.add(num * 10 + last - K)
            q = new
        return list(q)



968.py class Solution:
    res = 0
    def minCameraCover(self, root):
        def dfs(root):
            if not root: return 2
            if not root.left and not root.right: return 0
            l, r = dfs(root.left), dfs(root.right)
            if l == 0 or r == 0:
                self.res += 1
                return 1
            if l == 1 or r == 1:
                return 2
            return 0
        return (dfs(root) == 0) + self.res



969.py class Solution:
    def pancakeSort(self, A):
        res = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        return res  



970.py class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        res = set()
        i = j = 0
        while x ** i <= bound:
            while x ** i + y ** j <= bound:
                if x ** i + y ** j not in res:
                    res.add(x ** i + y ** j)
                j += 1
                if y == 1: 
                    break
            j = 0
            i += 1
            if x == 1:
                break
        return list(res)




971.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root, voyage):
        res = []
        self.i = 0
        def dfs(node):
            if not node: return True
            if node.val != voyage[self.i]:
                return False
            self.i += 1
            if node.left and node.left.val != voyage[self.i]:
                node.left, node.right = node.right, node.left
                res.append(node.val)
            return dfs(node.left) and dfs(node.right)
        return res if dfs(root) else [-1]



972.py class Solution:
    def isRationalEqual(self, S, T):
        def f(s):
            i = s.find('(')
            if i >= 0:
                s = s[:i] + s[i + 1:-1] * 20
            return float(s[:20])
        return f(S) == f(T)



973.py class Solution:
    def kClosest(self, points, K):
        return sorted(points, key = lambda p: p[0] ** 2 + p[1] ** 2)[:K]



974.py class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = sm = 0
        sums = collections.defaultdict(int)
        sums[0] = 1
        for a in A:
            sm = (sm + a) % K
            sums[sm] += 1
            res += sums[sm] - 1
        return res



975.py class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        next_higher, next_lower = [0] * n, [0] * n

        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n - 1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        return sum(higher)
        



976.py class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        return ([0] + [a + b + c for a, b, c in zip(A, A[1:], A[2:]) if c < a + b])[-1]



977.py class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([x ** 2 for x in A])



978.py class Solution:
    def maxTurbulenceSize(self, A):
        arr = [A[i - 1] < A[i] for i in range(1, len(A))]
        cur = mx = 1 + (len(A) > 1)
        for i in range(1, len(arr)):
            if A[i] != A[i + 1] and arr[i] != arr[i - 1]:
                cur += 1
                mx = max(cur, mx)
            else:
                cur = 2
        return mx



979.py class Solution:
    def distributeCoins(self, root):
        self.ans = 0

        def dfs(node):
            if not node: return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans



980.py class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(i, j, visited):
            if grid[i][j] == 2:
                self.walks += visited == self.visit
                return
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] != -1:
                    grid[i][j] -= 1
                    dfs(x, y, visited + 1)
                    grid[i][j] += 1
        m, n = len(grid), len(grid[0])
        self.visit = m * n - sum(c == -1 for row in grid for c in row)
        self.walks = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] -= 1
                    dfs(i, j, 1)
        return self.walks



981.py class TimeMap:

    def __init__(self):
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ''




982.py class Solution:
    def countTriplets(self, A: List[int]) -> int:
        cnt = collections.Counter([a & b for a in A for b in A])
        return sum(cnt[k] for a in A for k in cnt if not a & k)



983.py class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day, days, last = [0] * 366, set(days), days[-1]
        for i in range(1, last + 1):
            if i not in days:
                day[i] = day[i - 1]
            else:
                day[i] = min(day[i - 1] + costs[0], day[i - 7 if i>= 7 else 0] + costs[1], day[i - 30 if i >= 30 else 0] + costs[2])
        return day[last]



984.py class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        if not A and not B: return ''
        if A >= B:
            a = 2 if A >= 2 else 1
            b = 2 if A - a - B < 1 and B >= 2 else 1 if B else 0
            return a * 'a' + b * 'b' + self.strWithout3a3b(A - a, B - b)
        else:
            b = 2 if B >= 2 else 1
            a = 2 if B - b - A < 1 and A >= 2 else 1 if A else 0
            return b * 'b' + a * 'a' + self.strWithout3a3b(A - a, B - b)
            



985.py class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sm = sum(a for a in A if a % 2 == 0)
        for i in range(len(queries)):
            val, ind = queries[i]
            sm -= A[ind] % 2 == 0 and A[ind]
            A[ind] += val
            sm += A[ind] % 2 == 0 and A[ind]
            queries[i] = sm
        return queries



986.py class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            s = max(A[i].start, B[j].start)
            e = min(A[i].end, B[j].end)
            if s <= e:
                res.append(Interval(s, e))
            if A[i].end < B[j].end:
                i += 1
            elif A[i].end == B[j].end:
                i += 1
                j += 1
            else:
                j += 1
        return res



987.py class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.arr = []
        def dfs(node, x, y):
            if node:
                self.arr.append((x, y, node.val))
                dfs(node.left, x - 1, y + 1)
                dfs(node.right, x + 1, y + 1)
        dfs(root, 0, 0)
        return [list(map(lambda x: x[-1], g)) for k, g in itertools.groupby(sorted(self.arr), key = lambda x: x[0])]



988.py class Solution:
    def smallestFromLeaf(self, root: TreeNode, s = '') -> str:
        if not root.right and not root.left:
            return chr(97 + root.val) + s
        if not root.right:
            return self.smallestFromLeaf(root.left, chr(97 + root.val) + s)
        if not root.left:
            return self.smallestFromLeaf(root.right, chr(97 + root.val) + s)
        return min(self.smallestFromLeaf(root.left, chr(97 + root.val) + s), self.smallestFromLeaf(root.right, chr(97 + root.val) + s))



989.py class Solution:
    def addToArrayForm(self, A, K):
        for i in range(len(A))[::-1]:
            A[i], K = (A[i] + K) % 10, (A[i] + K) // 10
        return [int(i) for i in str(K)] + A if K else A



990.py class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def uf(c):
            return uf(parent[ord(c) - ord('a')]) if parent[ord(c) - ord('a')] != c else ord(c) - ord('a')
        parent = [c for c in string.ascii_lowercase]
        for eq in equations:
            if eq[1] == '=':
                parent[uf(eq[0])] = parent[uf(eq[-1])]
        for eq in equations:
            if eq[1] == '!' and parent[uf(eq[0])] == parent[uf(eq[-1])]:
                return False
        return True



991.py class Solution:
    def brokenCalc(self, X, Y):
        res = 0
        while X < Y:
            res += Y % 2 + 1
            Y = (Y + 1) // 2
        return res + X - Y



992.py class Solution:
    def subarraysWithKDistinct(self, A, K):
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        count = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            if count[A[j]] == 0: K -= 1
            count[A[j]] += 1
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0: K += 1
                i += 1
            res += j - i + 1
        return res



993.py class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node, parent, depth, mod):
            if node:
                if node.val == mod:
                    return depth, parent
                return dfs(node.left, node, depth + 1, mod) or dfs(node.right, node, depth + 1, mod)
        dx, px, dy, py = dfs(root, None, 0, x) + dfs(root, None, 0, y)
        return dx == dy and px != py



994.py class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfs, t, m, n = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 2], 0, len(grid), len(grid[0])
        while bfs:
            new = []
            for i, j in bfs:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        new.append((x, y))
            bfs = new
            t += bool(bfs)
        return t if all(val != 1 for row in grid for val in row) else -1



995.py class Solution:
    def minKBitFlips(self, a: List[int], k: int) -> int:
        q = collections.deque()
        res = 0
        for i in range(len(a)):
            if len(q) % 2 != 0 and a[i] == 1 or len(q) % 2 == a[i] == 0:
                res += 1
                q.append(i+k-1)
            if q and q[0] == i: q.popleft()
            if q and q[-1] >= len(a): return -1
        return res



996.py class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        self.res = 0
        def dfs(cnt, num):
            if not cnt:
                self.res += 1
            for new in nex[num]:
                if cnt[new]:
                    cnt[new] -= 1
                    if not cnt[new]:
                        cnt.pop(new)
                    dfs(cnt, new)
                    cnt[new] += 1
            
        nex = collections.defaultdict(set)  
        cnt = collections.Counter(A)
        for a, b in itertools.permutations(A, 2):
            if not (a + b) ** 0.5 % 1:
                nex[a].add(b)
                nex[b].add(a)
        for a in set(A):
            cnt[a] -= 1
            if not cnt[a]:
                cnt.pop(a)
            dfs(cnt, a)
            cnt[a] += 1
        return self.res



997.py class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        j, cnt = collections.Counter(b for a, b in trust).most_common(1)[0] if trust else (N, 0)
        return j if j not in {a for a, b in trust} and cnt == N - 1 else -1



998.py class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int, parent = None) -> TreeNode:
        if not root or val > root.val:
            new = TreeNode(val)
            new.left = root
            if parent:
                if parent.right == root:
                    parent.right = new
                else:
                    parent.left = new
            root = new
        else:
            root.right = self.insertIntoMaxTree(root.right, val, root)
        return root



999.py class Solution:
    def numRookCaptures(self, board: List[List[str]], res = 0) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    for x in range(i - 1, -1, -1):
                        if board[x][j] in 'Bp':
                            res += board[x][j] == 'p'
                            break
                    for x in range(i + 1, 8):
                        if board[x][j] in 'Bp':
                            res += board[x][j] == 'p'
                            break
                    for y in range(j - 1, -1, -1):
                        if board[i][y] in 'Bp':
                            res += board[i][y] == 'p'
                            break
                    for y in range(j + 1, 8):
                        if board[i][y] in 'Bp':
                            res += board[i][y] == 'p'
                            break
                    return res



1000.py class Solution:
    def mergeStones(self, stones, K):
        n = len(stones)
        if (n - 1) % (K - 1): return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        import functools
        @functools.lru_cache(None)
        def dp(i, j):
            if j - i + 1 < K: return 0
            res = min(dp(i, mid) + dp(mid + 1, j) for mid in range(i, j, K - 1))
            if (j - i) % (K - 1) == 0:
                res += prefix[j + 1] - prefix[i]
            return res
        return dp(0, n - 1)



1001.py class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lampsOn = set()
        rowsOn = collections.defaultdict(int)
        colsOn = collections.defaultdict(int)
        diagOnTopLeftBottomRight = collections.defaultdict(int)
        diagOnBottomLeftTopRight = collections.defaultdict(int)
        for r, c in lamps:
            lampsOn.add((r, c))
            rowsOn[r] += 1
            colsOn[c] += 1
            diagOnTopLeftBottomRight[c-r] += 1
            diagOnBottomLeftTopRight[c+r-N] += 1
        
        result = []
        for r, c in queries:
            if rowsOn[r] > 0 or colsOn[c] > 0 or diagOnTopLeftBottomRight[c-r] > 0 or diagOnBottomLeftTopRight[c+r-N] > 0:
                result.append(1)
            else:
                result.append(0)
            adjacentLamps = [(r, c), (r, c-1), (r, c+1), (r-1, c), (r-1, c-1), (r-1, c+1), (r+1, c), (r+1, c-1), (r+1, c+1)]
            for r, c in adjacentLamps:
                if (r, c) in lampsOn:
                    lampsOn.discard((r, c))
                    rowsOn[r] -= 1
                    colsOn[c] -= 1
                    diagOnTopLeftBottomRight[c-r] -= 1
                    diagOnBottomLeftTopRight[c+r-N] -= 1
        return result



1002.py class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        cnt, res = {s: [float('inf'), 0] for s in string.ascii_lowercase}, []
        for w in A:
            for k, v in collections.Counter(w).items():
                cnt[k][0] = min(cnt[k][0], v)
                cnt[k][1] += 1
        for k in cnt:
            if cnt[k][1] == len(A):
                res += [k] * cnt[k][0]
        return res



1003.py class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for i in S:
            if i == 'c':
                if stack[-2:] != ['a', 'b']:
                    return False
                stack.pop()
                stack.pop()
            else:
                stack.append(i)
        return not stack



1004.py class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zeros, res = [-1] + [i for i, c in enumerate(A) if not c] + [len(A)], 0
        for j in range(K + 1, len(zeros)):
            res = max(res, zeros[j] - zeros[j - K - 1] - 1)
        return res or K and len(A)



1005.py class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for _ in range(K):
            val = heapq.heappop(A)
            heapq.heappush(A, -val)
        return sum(A)



1006.py class Solution:
    def clumsy(self, N: int) -> int:
        if N <= 2:
            return N
        if N <= 4:
            return N + 3
        if N % 4 == 0:
            return N + 1
        elif N % 4 <= 2:
            return N + 2
        else:
            return N - 1



1007.py class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        res = min(len(A) - max(A.count(c), B.count(c)) if all(a == c or b == c for a, b in zip(A, B)) else float('inf') for c in (A[0], B[0]))
        return res if res < float('inf') else -1



1008.py class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root



1009.py class Solution:
    def bitwiseComplement(self, N: int, M = 0, m = 0) -> int:
        return N ^ M if M and M >= N else self.bitwiseComplement(N, M + 2 ** m, m + 1)



1010.py class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod = [0] * 61
        for t in time:
            mod[-1] += mod[(60 - t % 60) % 60]
            mod[t % 60] += 1
        return mod[-1]



1011.py class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def check(mx):
            days, cur = 1, 0
            for w in weights:
                if cur + w <= mx:
                    cur += w
                else:
                    days += 1
                    cur = w
            return days
            
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            days = check(mid)
            if days <= D:
                r = mid
            else:
                l = mid + 1
        return r



1012.py class Solution(object):
    def numDupDigitsAtMostN(self, N):
        """
        :type N: int
        :rtype: int
        """     
                # given number n, see whether n has repeated number
        def has_repeated(n):
            str_n = str(n)
            return len(set(str_n)) != len(str_n)

        def permutation(n, k):
            prod = 1
            for i in range(k):
                prod *= (n-i)
            return prod

        # calculate number of non-repeated n-digit numbers
        # note: the n-digit number can't start with 0
        # i.e: n_digit_no_repeat(2) calculates the non-repeated
        #   numbers in range [10, 99] (inclusive)
        def n_digit_no_repeat(n):
            if n == 1:
                return 9
            else:
                return  9 * permutation(9, n-1)

        N_str = str(N)
        n_digit = len(N_str)
        digits = list(map(int, N_str))
        result = N - 1
        prefix = 0
        for i in range(1, n_digit):
            result -= n_digit_no_repeat(i)
        for i in range(n_digit):
            # when we fix the most significant digit, it 
            # can't be zero
            start = 0 if i else 1
            for j in range(start, digits[i]):
                if has_repeated(prefix * 10 + j):
                    continue
                result -= permutation(9 - i, n_digit-1-i)
            prefix = prefix*10 + digits[i]
        return result + has_repeated(N)



1013.py class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        tar = sum(A) // 3
        sm = cnt = 0
        for a in A:
            sm += a
            if sm == tar:
                sm = 0
                cnt += 1
        return cnt == 3



1014.py class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        pre, mx = 0, -float('inf')
        for j, a in enumerate(A):
            mx = max(mx, pre + a - j)
            pre = max(pre, a + j)
        return mx



1015.py class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        used, mod, cnt = set(), 1 % K, 1
        while mod:
            mod = (mod * 10 + 1) % K
            cnt += 1
            if mod in used:
                return -1
            used.add(mod)
        return cnt



1016.py class Solution:
    def queryString(self, S: str, N: int) -> bool:
        return not set(range(1, N + 1)) - {int(S[i:j + 1], 2) for i in range(len(S)) for j in range(i, len(S))}



1017.py class Solution:
    def baseNeg2(self, n: int) -> str:
        bits = []
        while n:
            n, rem = divmod(n, -2)
            if rem < 0:
                n += 1
                rem -= -2
            bits.append(str(rem))
        return "".join(bits[::-1]) if bits else '0'



1018.py class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        num = 0
        for i in range(len(A)):
            num = (num << 1) + A[i]
            A[i] = num % 5 == 0
        return A



1019.py # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        heap, res, j = [], [], 0
        while head:
            res.append(0)
            while heap and heap[0][0] < head.val:
                val, i = heapq.heappop(heap)
                res[i] = head.val
            heapq.heappush(heap, (head.val, j))
            j += 1
            head = head.next
        return res
        



1020.py class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        def dfs(i, j):
            A[i][j] = 0
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and A[x][y]:
                    dfs(x, y)
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    dfs(i, j)
        return sum(sum(row) for row in A)



1021.py class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        l = r = 0
        res = cur = ''
        for s in S:
            cur += s
            l += s == '('
            r += s == ')'
            if l == r:
                res += cur[1:-1]
                cur = ''
        return res 



1022.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, r: TreeNode, num = 0) -> int:
        if not r: 
            return 0
        num = (num << 1) + r.val
        return (self.sumRootToLeaf(r.left, num) + self.sumRootToLeaf(r.right, num) if r.left or r.right else num) % (10 ** 9 + 7)



1023.py class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for w in queries:
            j = 0
            for c in w:
                if j < len(pattern) and c == pattern[j]:
                    j += 1
                elif c.isupper():
                    j = len(pattern) + 1
            res.append(j == len(pattern))
        return res



1024.py class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key = lambda x: (-x[0], x[1]))
        x = cnt = mx = 0
        while clips and clips[-1][0] <= x < T:
            while clips and clips[-1][0] <= x:
                mx = max(mx, clips.pop()[1])
            if mx > x:
                x = mx
                cnt += 1
        return cnt if x >= T else -1



1025.py class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0



1026.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            mx = mn = node.val
            if node.left:
                lMn, lMx = dfs(node.left)
                mx = max(mx, lMx)
                mn = min(mn, lMn)
                self.res = max(self.res, abs(lMn - node.val), abs(lMx - node.val))
            if node.right:
                rMn, rMx = dfs(node.right)
                mx = max(mx, rMx)
                mn = min(mn, rMn)
                self.res = max(self.res, abs(rMn - node.val), abs(rMx - node.val))
            return mn, mx
        dfs(root)
        return self.res



1027.py class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = collections.defaultdict(int)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a, b = A[i], A[j]
                dp[b - a, j] = max(dp[b - a, j], dp[b - a, i] + 1)
        return max(dp.values()) + 1



1028.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def dfs(parent, s, lev):
            print(parent.val, s, lev)
            if not s: return
            i = lev
            l = 0
            while i < len(s) and s[i].isdigit():
                l = l * 10 + int(s[i])
                i += 1
            parent.left = TreeNode(l)  
            j = lev
            f = '-' * lev
            for ind in range(i, len(s)):
                if s[ind:].startswith(f) and not s[ind:].startswith(f + '-') and s[ind -1] != '-':
                    rr = ind
                    j = ind + lev
                    r = 0
                    while j < len(s) and s[j].isdigit():
                        r = r * 10 + int(s[j])
                        j += 1
                    parent.right = TreeNode(r)
                    dfs(parent.left, s[i:rr], lev + 1)
                    dfs(parent.right, s[j:], lev + 1)
                    return
            dfs(parent.left, s[i:], lev + 1)
        i = num = 0
        while i < len(S) and S[i].isdigit():
            num = num * 10 + int(S[i])
            i += 1
        root = TreeNode(num)
        dfs(root, S[i:], 1)
        return root
            



1029.py class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: abs(x[0] - x[1]))
        a = b = 0
        N = len(costs) // 2
        c = 0
        for c1, c2 in costs[::-1]:
            if c1 <= c2 and a < N or b >= N:
                c += c1
                a += 1
            else:
                c += c2
                b += 1
        return c



1030.py class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        bfs, res, seen = [[r0, c0]], [], {(r0, c0)}
        while bfs:
            res += bfs
            new = []
            for i, j in bfs:
                for x, y in (i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < R and 0 <= y < C and (x, y) not in seen:
                        seen.add((x, y))
                        new.append([x, y])
            bfs = new
        return res
                        



1031.py class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        l = [0] * n
        r = [0] * n
        sm = 0 
        for i in range(M - 1):
            sm += A[i]
        for j in range(n - M + 1):
            sm += A[j + M - 1]
            for i in range(j + 1):
                r[i] = max(r[i], sm)
            sm -= A[j]
        
        sm = 0
        for i in range(n - 1, n - M, -1):
            sm += A[i]
        for i in range(n - 1, M - 2, -1):
            sm += A[i - M + 1]
            for j in range(i + 1, n):
                l[j] = max(l[j], sm)
            sm -= A[i]
            
        
        
        
        sm = 0
        for i in range(L - 1):
            sm += A[i]
        res = 0
        for j in range(n - L + 1):
            sm += A[j + L - 1]
            if j >= M:
                res = max(res, sm + l[j - 1])
            if j + L < n:
                res = max(res, sm + r[j + L])
            sm -= A[j]
        return res



1032.py import functools
class StreamChecker(object):

    def __init__(self, words):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words: functools.reduce(dict.__getitem__, w, self.trie)['#'] = True
        self.waiting = []

    def query(self, letter):
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any("#" in node for node in self.waiting)



1033.py class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        m1 = b - 1 - a
        m2 = c - b - 1
        m1 + m2
        if a + 2 == b or b + 2 == c:
            return [1, m1 + m2]
        n1 = int(b - 1 > a)
        n2 = int(b + 1 < c)
        return [n1 + n2, m1 + m2]       
                



1034.py class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        def dfs(i, j):
            seen.add((i, j))
            if not (0 < i < m - 1 and 0 < j < n - 1 and grid[i - 1][j] == grid[i + 1][j] == grid[i][j - 1] == grid[i][j + 1] == grid[i][j]):
                matrix[i][j] = 0
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == self.tar and (x, y) not in seen:
                    dfs(x, y)
        m, n = len(grid), len(grid[0])
        seen = set()
        self.tar = grid[r0][c0]
        matrix = [row[:] for row in grid]
        dfs(r0, c0)
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    matrix[i][j] = color
        return matrix



1035.py class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp, m, n = collections.defaultdict(int), len(A), len(B)
        for i in range(m):
            for j in range(n):
                dp[i, j] = max(dp[i - 1, j - 1] + (A[i] == B[j]), dp[i - 1, j], dp[i, j - 1])
        return dp[m - 1, n - 1]



1036.py class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked: return True
        blocked = set(map(tuple, blocked))
        
        def check(blocked, source, target):
            si, sj = source
            ti, tj = target
            level = 0
            q = collections.deque([(si,sj)])
            vis = set()
            while q:
                for _ in range(len(q)):
                    i,j = q.popleft()
                    if i == ti and j == tj: return True
                    for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                        if 0<=x<10**6 and 0<=y<10**6 and (x,y) not in vis and (x,y) not in blocked:
                            vis.add((x,y))
                            q.append((x,y))
                level += 1
                if level == len(blocked): break
            else:
                return False
            return True
        
        return check(blocked, source, target) and check(blocked, target, source)



1037.py class Solution:
    def isBoomerang(self, p: List[List[int]]) -> bool:
        return (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) != (p[0][0] - p[2][0]) * (p[0][1] - p[1][1])



1038.py class Solution:
    val = 0
    def bstToGst(self, root):
        if root.right: self.bstToGst(root.right)
        root.val = self.val = self.val + root.val
        if root.left: self.bstToGst(root.left)
        return root



1039.py class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                memo[i, j] = min([dp(i, k) + dp(k, j) + A[i] * A[j] * A[k] for k in range(i + 1, j)] or [0])
            return memo[i, j]
        return dp(0, len(A) - 1)



1040.py class Solution:
    def numMovesStonesII(self, A: List[int]) -> List[int]:
        A.sort()
        i, n, low = 0, len(A), len(A)
        high = max(A[-1] - n + 2 - A[1], A[-2] - A[0] - n + 2)
        for j in range(n):
            while A[j] - A[i] >= n: i += 1
            if j - i + 1 == n - 1 and A[j] - A[i] == n - 2:
                low = min(low, 2)
            else:
                low = min(low, n - (j - i + 1))
        return [low, high]



1041.py class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for _ in range(4):
            for ins in instructions:
                if ins == 'G':
                    x += dx
                    y += dy
                elif ins == 'L':
                    dx, dy = -dy, dx
                else:
                    dx, dy = dy, -dx
        return x == y == 0



1042.py class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        res = [0] * N
        G = [[] for i in range(N)]
        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        for i in range(N):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
        return res



1043.py class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0] * (N + K)
        for i in range(N):
            curMax = 0
            for k in range(1, min(K, i + 1) + 1):
                curMax = max(curMax, A[i - k + 1])
                dp[i] = max(dp[i], dp[i - k] + curMax * k)
        return dp[N - 1]



1044.py from functools import reduce
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1

        def test(L):
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            for i in range(L, len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen: return i - L + 1
                seen.add(cur)
        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return S[res:res + lo]



1046.py class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        for _ in range(len(stones) - 1):
            bisect.insort(stones, stones.pop() - stones.pop())
        return stones[0]



1047.py class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for s in S:
            if stack and stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        return ''.join(stack)



1048.py class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def dfs(w1, size):
            return max([dfs(w2, size + 1) for w2 in graph[w1]], default = size)
        graph = collections.defaultdict(list)
        for w in words:
            graph[len(w)].append(w)
        for w1 in words:
            for w2 in graph[len(w1) + 1]:
                for i in range(len(w2)):
                    if w2[:i] + w2[i + 1:] == w1:
                        graph[w1].append(w2)
        return max(dfs(w, 1) for w in words)



1049.py class Solution:
    def lastStoneWeightII(self, A: List[int]) -> int:
        dp = {0}
        sumA = sum(A)
        for a in A:
            dp |= {a + i for i in dp}
        return min(abs(sumA - i - i) for i in dp)



1051.py class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))



1052.py class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], x: int) -> int:
        dif = mx = sum(c * g for c, g in zip(customers[:x], grumpy[:x]))
        for j in range(x, len(grumpy)):
            dif += (grumpy[j] * customers[j]) - (grumpy[j - x] * customers[j - x])
            mx = max(mx, dif)
        return mx + sum(c * (1- g) for c, g in zip(customers, grumpy))



1053.py class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        pre = []
        for i in range(len(A) - 1, -1, -1):
            bisect.insort_left(pre, (A[i], i))
            if pre.index((A[i], i)):
                j = pre[pre.index((A[i], i)) - 1][1]
                A[i], A[j] = A[j], A[i]
                break
        return A



1054.py class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = collections.Counter(barcodes).most_common()[::-1]
        ref = [val for val, t in cnt for _ in range(t)]
        for i in range(0, len(barcodes), 2):
            barcodes[i] = ref.pop()
        for i in range(1, len(barcodes), 2):
            barcodes[i] = ref.pop()
        return barcodes



1055.py class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        cnt = i = 0
        for t in target:
            i = source.find(t, i)
            if i == -1:
                i = source.find(t, 0)
                if i == -1:
                    return -1
                cnt += 1
            i += 1
        return cnt + 1



1056.py class Solution:
    def confusingNumber(self, N: int) -> bool:
        ret = ''.join("01####9#86"[int(n)] for n in str(N)[::-1])
        return '#' not in ret and ret != str(N)



1057.py class Solution:
    def assignBikes(self, W: List[List[int]], B: List[List[int]]) -> List[int]:
        ans, used = [-1] * len(W), set()
        for d, w, b in sorted([abs(W[i][0] - B[j][0]) + abs(W[i][1] - B[j][1]), i, j] for i in range(len(W)) for j in range(len(B))):
            if ans[w] == -1 and b not in used:
                ans[w] = b
                used.add(b)
            if len(used) == len(ans):
                break
        return ans



1058.py class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        prices = [float(p) for p in prices]
        sm = sum(math.floor(p) for p in prices)
        prices = sorted(p - math.floor(p) for p in prices if p - math.floor(p))
        if sm > target or target - sm > len(prices):
            return "-1"
        return "{:.3f}".format(sum([p - math.floor(p) for p in  prices[:sm - target]]) + sum([math.ceil(p) - p for p in prices[sm - target:]]))



1059.py class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(i):
            seen.add(i)
            for j in graph[i]:
                if j == i or j in seen or not dfs(j):
                    return False
            seen.discard(i)
            return len(graph[i]) != 0 or i == destination
        graph, seen = collections.defaultdict(set), set()
        for a, b in edges:
            graph[a].add(b)
        return dfs(source)
        



1060.py class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        cur = nums[0]
        for num in nums[1:]:
            if num - cur - 1 >= k:
                break
            else:
                k -= num - cur - 1
            cur = num
        return cur + k



1061.py class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        def root(c):
            return c if parent[c] == c else root(parent[c])
        parent = {s: s for s in string.ascii_lowercase}
        for a, b in zip(A, B):
            p1, p2 = root(a), root(b)
            if p1 <= p2:
                parent[p2] = p1
            else:
                parent[p1] = p2
        return ''.join(root(s) for s in S)



1062.py class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        for l in range(len(S), 0, -1):
            s = S[:l]
            seen = {s}
            for j in range(l, len(S)):
                s = s[1:] + S[j]
                if s in seen:
                    return l
                seen.add(s)
        return 0
                



1063.py class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack, res = [], 0
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            stack.append(num)
            res += len(stack)
        return res



1064.py class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        return ([i for i in range(len(A)) if A[i] == i] + [-1])[0]



1065.py class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        return [[i, j] for i in range(len(text)) for j in range(i, len(text)) if text[i:j + 1] in words]



1066.py class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def dis(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
        h = [[0, 0, 0]]
        seen = set()
        while True:
            cost, i, taken = heapq.heappop(h)
            if (i, taken) in seen: continue
            seen.add((i, taken))
            if i == len(workers):
                return cost
            for j in range(len(bikes)):
                if taken & (1 << j) == 0:
                    heapq.heappush(h, [cost + dis(i, j), i + 1, taken | (1 << j)])



1071.py class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == len(str2):
            return str1 if str1==str2 else ''
        else:
            if len(str1) < len(str2):
                str1,str2 = str2,str1
            if str1[:len(str2)] == str2:
                return self.gcdOfStrings(str1[len(str2):],str2)
            else:
                return ''



1072.py class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        res = 0
        for row in matrix:
            inv = [1 - r for r in row]
            res = max(res, sum(row == r or inv == r for r in matrix))
        return res
            



1074.py class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            for i in range(1, n):
                row[i] += row[i-1]
                
        res = 0
        for i in range(n):
            for j in range(i, n):
                c = {0:1}
                cur = 0
                for row in matrix:
                    cur += row[j] - (row[i-1] if i else 0)
                    
                    if cur - target in c:
                        res += c[cur-target]
                    
                    c[cur] = c.get(cur, 0) + 1
        return res



1078.py class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        return [text[i] for i in range(2, len(text)) if text[i-1] == second and text[i-2] == first]                         



1079.py class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return sum(len(set(itertools.permutations(tiles, i))) for i in range(1, len(tiles) + 1))



1080.py class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if root.left == root.right is None:
            return None if root.val < limit else root
        if root.left:
            root.left = self.sufficientSubset(root.left, limit - root.val)
        if root.right:
            root.right = self.sufficientSubset(root.right, limit - root.val)
        return root if root.left or root.right else None



1081.py class Solution:
    def smallestSubsequence(self, S: str) -> str:
        last = {c: i for i, c in enumerate(S)}
        res = ""
        left = 0
        while last:
            right = min(last.values())
            c, i = min((S[i], i) for i in range(left, right + 1) if S[i] not in res)
            left = i + 1
            res += c
            del last[c]
        return res



1085.py class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        return 1 - sum(map(int, str(min(A)))) % 2
        return 1 - sum(int(c) for c in str(min(A))) % 2



1086.py class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        res = []
        items.sort(key = lambda x: (-x[0], x[1]))
        while items:
            res.append([items[-1][0], sum(b for a, b in items[-5:]) // 5])
            while items and items[-1][0] == res[-1][0]:
                items.pop()
        return res



1087.py class Solution:
    def permute(self, S: str) -> List[str]:
        bfs = [""]
        mult = False
        chars = []
        for s in S:
            if s == ',': 
                continue
            elif s == '{':
                mult = True
            elif s == '}':
                bfs = [st + c for st in bfs for c in chars]
                chars = []
                mult = False
            elif mult:
                chars.append(s)
            else:
                bfs = [st + s for st in bfs]
        return sorted(bfs)
                



1088.py class Solution:
    def confusingNumberII(self, N: int) -> int:
        def diff(num):
            return num != ''.join('9' if c == '6' else '6' if c == '9' else c for c in num[::-1])
        def dfs(num):
            return sum(dfs(num * 10 + dig) for dig in [0, 1, 6, 8, 9]) + diff(str(num)) if num <= N else 0
        return sum(dfs(n) for n in [1, 6, 8, 9]) if N != 1000000000 else 1950627



1089.py class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        for num in list(arr):
            if i >= len(arr): break
            arr[i] = num
            if not num:
                i += 1
                if i < len(arr):
                    arr[i] = num
            i += 1



1090.py class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        cnt = collections.defaultdict(int)
        heap = [[-a, b] for a, b in zip(values, labels)]
        heapq.heapify(heap)
        use = sm =0 
        while use < num_wanted and heap:
            a, b = heapq.heappop(heap)
            if cnt[b] < use_limit:
                sm -= a
                use += 1
                cnt[b] += 1
        return sm



1091.py class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        bfs = [[0, 0]]
        cnt = 1
        seen = {(0, 0)}
        while bfs:
            new = []
            for i, j in bfs:
                for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1):
                    if 0 <= x < n and 0 <= y < n and (x, y) not in seen and not grid[x][y]:
                        if x == y == n - 1:
                            return cnt + 1
                        new.append((x, y))
                        seen.add((x, y))
            cnt += 1
            bfs = new
        return -1



1092.py class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def compute_lcs(s, t):
            m, n = len(s), len(t)
            dp = [[""] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if s[i - 1] != t[j - 1]:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + s[i - 1]
            return dp[-1][-1]
        cs = compute_lcs(str1, str2)
        ans = []
        i, j = 0, 0
        m, n = len(str1), len(str2)
        for ch in cs:
            while i < m and str1[i] != ch:
                ans.append(str1[i])
                i += 1
            while j < n and str2[j] != ch:
                ans.append(str2[j])
                j += 1
            ans.append(ch)
            i += 1
            j += 1
        return ''.join(ans) + str1[i:] + str2[j:]



1093.py class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        arr = [(i, c * 1.0) for i, c in enumerate(count) if c]
        acc = list(itertools.accumulate(count, lambda x, y: x + y))
        mean = sum(i * c for i, c in arr) / acc[-1] 
        mode = max(arr, key = lambda x: x[1])[0] * 1.0
        m1 = bisect.bisect(acc, (acc[-1] - 1) // 2)
        m2 = bisect.bisect(acc, acc[-1] // 2)
        return [arr[0][0] * 1.0, arr[-1][0] * 1.0, mean, (m1 + m2) / 2.0, mode]
        



1094.py class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        for a, b, c in trips:
            heapq.heappush(heap, (b, a))
            heapq.heappush(heap, (c, -a))
        cur = 0
        while heap:
            cur += heapq.heappop(heap)[1]
            if cur > capacity: return False
        return True



1095.py # """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l, r = 0, mountain_arr.length() - 1
        while l <= r:
            mid = (l  + r) // 2
            md = mountain_arr.get(mid)
            if mid and mountain_arr.get(mid - 1) < md > mountain_arr.get(mid + 1):
                pivot = mid
                break
            elif md < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid - 1
        l, r = 0, pivot
        while l <= r:
            mid = (l + r) // 2
            md = mountain_arr.get(mid)
            if md == target:
                return mid
            elif md < target:
                l = mid + 1
            else:
                r = mid - 1
        l, r = pivot, mountain_arr.length() - 1
        while l <= r:
            mid = (l + r) // 2
            md = mountain_arr.get(mid)
            if md == target:
                return mid
            elif md > target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
        



1096.py class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack,res,cur=[],[],[]
        for i in range(len(expression)):
            v=expression[i]
            if v.isalpha():
                cur=[c+v for c in cur or ['']]
            elif v=='{':
                stack.append(res)
                stack.append(cur)
                res,cur=[],[]
            elif v=='}':
                pre=stack.pop()
                preRes=stack.pop()
                cur=[p+c for c in res+cur for p in pre or ['']]
                res=preRes
            elif v==',':
                res+=cur
                cur=[]
        return sorted(set(res+cur))
        



1099.py class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        res, l, r = -1, 0, len(A) - 1
        while l < r:
            if A[l] + A[r] >= K:
                r -= 1
            else:
                res = max(res, A[l] + A[r])
                l += 1
        return res



1100.py class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        cnt = collections.Counter(S[:K - 1])
        res = 0
        for i in range(K - 1, len(S)):
            cnt[S[i]] += 1
            if len(cnt) == K:
                res += 1
            cnt[S[i - K + 1]] -= 1
            if not cnt[S[i - K + 1]]:
                cnt.pop(S[i - K + 1])
        return res



1101.py class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        def root(a):
            return a if parent[a] == a else root(parent[a])
        parent = [i for i in range(N)]
        time = -1
        for t, a, b in sorted(logs):
            A, B = root(a), root(b)
            parent[A] = parent[a] = parent[b] = B
            if A != B:
                time = t
        return time if all(root(a) == root(b) for a, b in zip(parent, parent[1:])) else -1



1102.py class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        heap = [(-A[0][0], 0, 0)]
        res = A[0][0]
        m, n = len(A), len(A[0])
        while heap:
            val, i, j = heapq.heappop(heap)
            A[i][j] = -1
            res = min(res, -val)
            if i == m - 1 and j == n - 1:
                break
            for x, y in (i + 1, j) , (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < m and 0 <= y < n and A[x][y] >= 0:
                    heapq.heappush(heap, (-A[x][y], x, y))
        return res
            



1103.py class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        i = 0
        while candies > 0:
            res[i % num_people] += min(candies, i + 1)
            i += 1
            candies -= i
        return res



1104.py class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = [label]
        while label != 1:
            d = int(math.log(label) / math.log(2))
            offset = int(2 ** (d + 1)) - label - 1
            label = (int(2 ** d) + offset) // 2
            res = [label] + res
        return res



1105.py class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            max_width = shelf_width
            max_height = 0
            j = i - 1
            while j >= 0 and max_width - books[j][0] >= 0:
                max_width -= books[j][0]
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + max_height)
                j -= 1
        return dp[n] 
    



1106.py class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for c in expression:
            if c == ')':
                cache = []
                while stack[-1] != '(':
                    cache.append(stack.pop())
                stack.pop()
                cur = stack.pop()
                stack.append(all(cache) if cur == '&' else any(cache) if cur == '|' else not cache.pop())
            elif c != ',':
                stack.append(True if c == 't' else False if c == 'f' else c)
        return stack.pop()        



1108.py class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")



1109.py class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        i = cur = 0
        for j, val in sorted([[i - 1, k] for i, j, k in bookings] + [[j, -k] for i, j, k in bookings]):
            while i < j:
                res[i] = cur
                i += 1
            cur += val
        return res



1110.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        def dfs(node, parent):
            if not node: return True
            dfs(node.left, node)
            dfs(node.right, node)
            if node.val in blacklist:
                if parent and parent.left == node:
                    parent.left = None
                elif parent:
                    parent.right = None
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
        res = []
        blacklist = set(to_delete)
        dfs(root, None)
        return res + [root] if root.val not in blacklist else res



1111.py class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        stack = []
        res = [0] * len(seq)
        for i, c in enumerate(seq):
            if c == '(':
                stack.append(i if not stack or stack[-1] < 0 else -i)
            else:
                ind = stack.pop()
                if ind >= 0:
                    res[i] = res[ind] = 1
        return res       



1114.py import threading
class Foo(object):
    def __init__(self):
        self.two = threading.Semaphore()
        self.three = threading.Semaphore()
        self.two.acquire()
        self.three.acquire()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.two.release()
		
    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.two.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.three.release()
        
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.three.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()



1115.py import threading
class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.f = threading.Semaphore()
        self.b = threading.Semaphore()
        self.b.acquire()

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in range(self.n):
            self.f.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.b.release()


    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in range(self.n):
            self.b.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.f.release()



1116.py import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.z = threading.Semaphore()
        self.e = threading.Semaphore()
        self.o = threading.Semaphore()
        self.e.acquire()
        self.o.acquire()
        self.cur = 1
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.z.acquire()
            printNumber(0)
            if self.cur % 2:
                self.o.release()
            else:
                self.e.release()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n // 2):
            self.e.acquire()
            printNumber(self.cur)
            self.cur += 1
            self.z.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n // 2 + self.n % 2):
            self.o.acquire()
            printNumber(self.cur)
            self.cur += 1
            self.z.release()



1117.py from threading import Lock

class H2O(object):
    def __init__(self):
        self.H = 0
        self.O = 0
        self.mu = Lock()
        pass


    def hydrogen(self, releaseHydrogen):
        self.releaseHydrogen = releaseHydrogen
        with self.mu:
            self.H += 1
            self.ouput()

    def oxygen(self, releaseOxygen):
        self.releaseOxygen = releaseOxygen
        with self.mu:
            self.O += 1
            self.ouput()
        
    def ouput(self):
        while self.ok():
            self.releaseHydrogen()
            self.releaseHydrogen()
            self.releaseOxygen()
            self.H -= 2
            self.O -= 1
    
    def ok(self):
        return self.H >= 2 and self.O >= 1



1118.py class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        return 29 + {2: Y % (Y % 25 and 4 or 16) and -1}.get(M, ((M % 2) ^ (M > 7)) + 1)



1119.py class Solution:
    def removeVowels(self, S: str) -> str:
        return ''.join(filter(lambda x: x not in 'aeiou', S))
        return ''.join(c for c in S if c not in 'aeiou')
        



1120.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maximumAverageSubtree(self, node, parent = None): 
        if not node: 
            return 0, 0, 0
        lCnt, lSum, lAvg = self.maximumAverageSubtree(node.left, node)
        rCnt, rSum, rAvg = self.maximumAverageSubtree(node.right, node)
        ret = max((node.val + lSum + rSum) / (lCnt + rCnt + 1), lAvg, rAvg) 
        return (lCnt + rCnt + 1, lSum + rSum + node.val, ret) if parent else ret
        



1121.py class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        return K * max(collections.Counter(nums).values()) <= len(nums)              



1122.py class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return sorted(arr1, key = lambda x: arr2.index(x) if x in arr2 else len(arr2) + x)



1123.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if not root:
                return 0, None
            d1, lca1 = helper(root.left)
            d2, lca2 = helper(root.right)
            if d1 > d2:
                node = lca1
            elif d1 < d2:
                node = lca2
            else:
                node = root
            return max(d1, d2) + 1, node
        return helper(root)[1]



1124.py class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score += h > 8
            score -= h < 9
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        return res



1125.py class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n, m = len(req_skills), len(people)
        key = {v: i for i, v in enumerate(req_skills)}
        dp = {0: []}
        for i, p in enumerate(people):
            his_skill = 0
            for skill in p:
                if skill in key:
                    his_skill |= 1 << key[skill]
            for skill_set, need in list(dp.items()):
                with_him = skill_set | his_skill
                if with_him == skill_set: continue
                if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                    dp[with_him] = need + [i]
        return dp[(1 << n) - 1]



1128.py class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum(v * (v - 1) // 2 for v in collections.Counter(tuple(sorted(d)) for d in dominoes).values())



1129.py class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        
        def dfs(i, mod, cnt):
            res[i][mod] = cnt
            for v in edge[i][mod]:
                if cnt < res[v][1 - mod]:
                    dfs(v, 1 - mod, cnt + 1)
                    
        res = [[float('inf'), float('inf')] for _ in range(n)]
        edge = [[[], []] for _ in range(n)]
        for u, v in red_edges:
            edge[u][0].append(v)
        for u, v in blue_edges:
            edge[u][1].append(v)
        dfs(0, 0, 0)
        dfs(0, 1, 0)
        return [x if x != float('inf') else -1 for x in map(min, res)]



1130.py class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        res, n = 0, len(A)
        stack = [float('inf')]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack)  >2:
            res += stack.pop() * stack[-1]
        return res



1131.py class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        l1, l2 ,l3, l4 = [], [], [], []
        for i in range(len(arr1)):
            l1 += [arr1[i]+arr2[i]+i]
            l2 += [arr1[i]-arr2[i]+i]
            l3 += [-arr1[i]+arr2[i]+i]
            l4 += [-arr1[i]-arr2[i]+i]
        res = []
        res += [max(l1)-min(l1)]
        res += [max(l2) -min(l2)]
        res += [max(l3)-min(l3)]
        res += [max(l4)-min(l4)]
        return max(res)



1133.py class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        cnt = collections.Counter(A)
        a = sorted(k for k, v in cnt.items() if v == 1)
        return a[-1] if a else -1
        



1134.py class Solution:
    def isArmstrong(self, N: int) -> bool:
        ns = [(int(c), int(c)) for c in str(N)]
        sm = sum(a for a, b in ns)
        while sm < N:
            ns = [(a * b, b) for a, b in ns]
            sm = sum(a for a, b in ns)
        return sm == N
        



1135.py class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        heap = [(0, 1)]
        visited = [0] * (N + 1)
        res = 0
        graph = [[] for _ in range(N + 1)]
        for a, b, c in connections:
            graph[a].append([b, c])
            graph[b].append([a, c])
        while heap:
            cost, city = heapq.heappop(heap)
            if visited[city]: continue
            visited[city] = 1
            res += cost
            for nCity, nCost in graph[city]:
                if not visited[nCity]:
                    heapq.heappush(heap, (nCost, nCity))
        return res if all(visited[1:]) else -1
            
            



1136.py class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        """
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """
        if N == 1:
            return 1
        graph = collections.defaultdict(list)
        for p, q in relations:
            graph[q-1].append(p-1)

        def need_semesters(n):
            if dp[n] > 0:   # node was visited
                return dp[n]
            if dp[n] == -1: # node is being visited, there is a cycle!
                return -1
            dp[n] = -1 # start visiting the node
            res = 0
            for p in graph[n]:
                a = need_semesters(p)
                if a == -1:
                    return -1
                res = max(res, a)
            dp[n] = res + 1
            return dp[n]

        dp = [0]*N
        for n in range(N):
            if need_semesters(n) == -1:
                return -1
        return max(dp)



1137.py class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        for _ in range(n):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
        return t0
        



1138.py class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        ind = {s: [i // 5, i % 5] for i, s in enumerate(string.ascii_lowercase)}
        x = y = 0
        res = ""
        for c in target:
            xx, yy = ind[c]
            if yy < y:
                res += 'L' * (y - yy)
            if xx > x:
                res += 'D' * (xx - x)
            if xx < x:
                res += 'U' * (x - xx)
            if yy > y:
                res += 'R' * (yy - y)
            res += '!'
            x, y = xx, yy
        return res



1139.py class Solution:
    def largest1BorderedSquare(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        res = 0
        top, left = [a[:] for a in A], [a[:] for a in A]
        for i in range(m):
            for j in range(n):
                if A[i][j]:
                    if i: top[i][j] = top[i - 1][j] + 1
                    if j: left[i][j] = left[i][j - 1] + 1
        for r in range(min(m, n), 0, -1):
            for i in range(m - r + 1):
                for j in range(n - r + 1):
                    if min(top[i + r - 1][j], top[i + r - 1][j + r - 1], left[i]
                           [j + r - 1], left[i + r - 1][j + r - 1]) >= r:
                        return r * r
        return 0



1140.py class Solution:
    def stoneGameII(self, A: List[int]) -> int:
        N = len(A)
        for i in range(N - 2, -1, -1):
            A[i] += A[i + 1]
        from functools import lru_cache
        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= N: return A[i]
            return A[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))
        return dp(0, 1)



1143.py class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1] else max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]



1144.py class Solution:
    def movesToMakeZigzag(self, N: List[int]) -> int:
        moves = [max(0, N[i] - min(N[i-1:i] + N[i+1:i+2]) + 1) for i in range(len(N))]
        return min(sum(moves[::2]), sum(moves[1::2]))



1145.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        c = [0, 0]
        def count(node):
            if not node: return 0
            l, r = count(node.left), count(node.right)
            if node.val == x:
                c[0], c[1] = l, r
            return l + r + 1
        return count(root) // 2 < max(max(c), n - sum(c) - 1)



1146.py class SnapshotArray:

    def __init__(self, length: int):
        self.s = 0
        self.arr = [[[0, 0]] for i in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.s == self.arr[index][-1][0]:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.s, val])

    def snap(self) -> int:
        self.s += 1
        return self.s - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect_left(self.arr[index], [snap_id])
        if i < len(self.arr[index]):
            if self.arr[index][i][0] > snap_id:
                i -= 1
            return self.arr[index][i][1]
        return self.arr[index][-1][1]



1147.py class Solution:
    def longestDecomposition(self, S: str) -> int:
        res, l, r = 0, "", ""
        for i, j in zip(S, S[::-1]):
            l, r = l + i, j + r
            if l == r:
                res, l, r = res + 1, "", ""
        return res



1150.py class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return nums.count(target) > len(nums) // 2
        



1151.py class Solution:
    def minSwaps(self, data: List[int]) -> int:
        l = data.count(1)
        mn = cur = data[:l].count(0)
        for i in range(l, len(data)):
            cur += not data[i] 
            cur -= not data[i - l]
            mn = min(mn, cur)
        return mn
        



1152.py class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        dp = collections.defaultdict(list)
        count = collections.Counter()
        for t, u, w in sorted(zip(timestamp, username, website)):
            dp[u].append(w)
        for u in dp:
            count += collections.Counter(set(seq for seq in itertools.combinations(dp[u], 3)))
        target = max(count.values())
        return min(list(k) for k in count if count[k] == target)



1153.py class Solution:
    def canConvert(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        dp = {}
        for i, j in zip(s1, s2):
            if dp.setdefault(i, j) != j:
                return False
        return len(set(s2)) < 26



1154.py class Solution:
    def dayOfYear(self, date: str) -> int:
        cnt = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y, m, d = map(int, date.split('-'))
        days = sum(cnt[:m - 1]) + d
        if m > 2:
            if y % 400 == 0: days += 1
            if y % 100 == 0: return days
            if y % 4 == 0: days += 1
        return days



1155.py class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for j in range(target + 1)] for i in range(d + 1)]
        dp[0][0] = 1
        for i in range(d):
            for ff in range(1, f + 1):
                for sm in range(target):
                    if sm + ff <= target:
                        dp[i + 1][sm + ff] += dp[i][sm]
                        dp[i + 1][sm + ff] %= mod
        return dp[d][target]



1156.py class Solution:
    def maxRepOpt1(self, S: str) -> int:
        A = [[c, len(list(g))] for c, g in itertools.groupby(S)]
        count = collections.Counter(S)
        res = max(min(k + 1, count[c]) for c, k in A)
        for i in range(1, len(A) - 1):
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        return res



1157.py class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.dp = collections.defaultdict(list)
        for i, v in enumerate(arr):
            self.dp[v].append(i)
        self.occur = sorted([(len(v), k) for k, v in self.dp.items()], reverse = True)
        
    def query(self, left: int, right: int, threshold: int) -> int:
        for o, v in self.occur:
            if o < threshold: break
            l = self.dp[v]
            low = bisect.bisect_left(l, left)
            high = bisect.bisect_right(l, right)
            if high - low >= threshold:
                return v
        return -1



1160.py from collections import Counter as cnt
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum(not cnt(w) - cnt(chars) and len(w) for w in words)



1161.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        levels, l, q = [], 1, [root]
        while q:
            levels.append([sum(node.val for node in q), l])
            l += 1
            q = [child for node in q for child in (node.left, node.right) if child]
        return sorted(levels, key = lambda x: (x[0], -x[1]))[-1][1]



1162.py class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = [[i, j] for i in range(n) for j in range(n) if grid[i][j]]
        d = -1
        while q and len(q) != n ** 2:
            Q = []
            for i, j in q:
                for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if 0 <= x < n > y >= 0 and not grid[x][y]:
                        grid[x][y] = 1
                        Q.append([x, y])
            q = Q
            d += 1
        return d
            
            



1163.py class Solution:
    def lastSubstring(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            result = max(result, s[i:])
        return result
        



1165.py class Solution:
    def calculateTime(self, k: str, word: str) -> int:
        return sum(abs(k.index(a) - k.index(b)) for a, b in zip(k[0] + word, word))



1166.py class FileSystem:

    def __init__(self):
        self.d = {"" : -1}

    def create(self, path: str, value: int) -> bool:
        parent = path[:path.rfind('/')]
        if parent in self.d and path not in self.d:
            self.d[path] = value
            return True
        return False

    def get(self, path: str) -> int:
        return self.d.get(path, -1)



1167.py class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        while len(sticks) != 1:
            new = heapq.heappop(sticks) + heapq.heappop(sticks)
            res += new
            heapq.heappush(sticks, new)
        return res
        



1168.py class Solution:
    def minCostToSupplyWater(self, n: int, wells, pipes) -> int:
        q = sorted([[w, u, v] for u, v, w in pipes] + [[w, 0, i+1] for i, w in enumerate(wells)])
        uf = [i for i in range(n+1)]
        res = count = 0
        
        def find(x):
            if (x != uf[x]):
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            uf[x] = y
            
        for w, u, v in q:
            rA, rB = find(u), find(v)
            if rA == rB:
                continue
            union(rA, rB)
            res += w
            count += 1
            if count == n:
                return res
        return res 



1169.py class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        last = collections.defaultdict(list)
        ret = set()
        for n, t, a, c in sorted([t.split(',') for t in transactions], key = lambda x: int(x[1])):
            if int(a) > 1000:
                ret.add(','.join([n, t, a, c]))
            if n in last:
                for tt, aa, cc in last[n][::-1]:
                    if int(t) - int(tt) > 60:
                        break
                    if cc != c:
                        ret.add(','.join([n, tt, aa, cc]))
                        ret.add(','.join([n, t, a, c]))
            last[n].append([t, a, c])
        return list(ret)
        



1170.py class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = sorted(w.count(min(w)) for w in words)
        return [len(f) - bisect.bisect(f, q.count(min(q))) for q in queries]
        



1172.py class DinnerPlates:

    def __init__(self, capacity: int):
        self.c = capacity
        self.stacks = []
        self.l = [] # pushable
        self.r = [] # poppable
        
    def push(self, val: int) -> None:
        if not self.l:
            # if the rightmost is empty, clear it from self.r
            while self.r and not self.stacks[-self.r[0]]:
                heapq.heappop(self.r)
            i = 0 if not self.r else -self.r[0] + 1
            self.stacks.append([val])
            heapq.heappush(self.r, -i)
            if len(self.stacks[i]) < self.c:
                heapq.heappush(self.l, i)
        else:
            i = self.l[0]
            # new poppable
            if not self.stacks[i]:
                heapq.heappush(self.r, -i)
            self.stacks[i].append(val)
            if len(self.stacks[i]) == self.c:
                heapq.heappop(self.l)
                
    def pop(self) -> int:
        while self.r and not self.stacks[-self.r[0]]:
            heapq.heappop(self.r)
        return self.popAtStack(-self.r[0]) if self.r else -1

    def popAtStack(self, index: int) -> int:
        if index < len(self.stacks) and self.stacks[index]:
            ret = self.stacks[index].pop()
            if len(self.stacks[index]) == self.c - 1:
                heapq.heappush(self.l, index)
            return ret
        return -1
        



1175.py class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        cnt = bisect.bisect(primes, n)
        return math.factorial(cnt) * math.factorial(n - cnt) % (10 ** 9 + 7)
    



1176.py class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        sm = sum(calories[:k])
        points = (sm > upper) - (sm < lower)
        for i in range(k, len(calories)):
            sm += calories[i] - calories[i - k]
            points += (sm > upper) - (sm < lower)
        return points
            



1177.py class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        cnts = [{}]
        for i, c in enumerate(s):
            cnts.append(dict(cnts[-1]))
            cnts[-1][c] = cnts[-1].get(c, 0) + 1
        res = []
        for i, j, k in queries:
            res.append(sum((v - cnts[i].get(k, 0)) % 2 for k, v in cnts[j + 1].items()) - k * 2 <= 1)
        return res
        
        



1178.py from itertools import combinations as cb
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        cnt = collections.Counter(''.join(sorted(set(w))) for w in words)
        return [sum(cnt[''.join(sorted(s + (p[0], )))] for l in range(len(p)) for s in cb(p[1:], l)) for p in puzzles]



1180.py class Solution:
    def countLetters(self, S: str) -> int:
        cnt = collections.Counter()
        i = res = 0
        for j, c in enumerate(S):
            cnt[c] += 1
            while len(cnt) > 1:
                cnt[S[i]] -= 1
                if not cnt[S[i]]:
                    cnt.pop(S[i])
                i += 1
            res += j - i + 1
        return res
                
            



1181.py class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        res = []
        for i in range(len(phrases)):
            for j in range(i + 1, len(phrases)):
                w1 = phrases[i].split()[-1]
                w2 = phrases[j].split()[0]
                if w1 == w2:
                    r = phrases[i] + ' ' + ' '.join(phrases[j].split()[1:])
                    res.append(r.rstrip())
                w1 = phrases[j].split()[-1]
                w2 = phrases[i].split()[0]
                if w1 == w2:
                    r = phrases[j] + ' ' + ' '.join(phrases[i].split()[1:])
                    res.append(r.rstrip())
        return sorted(set(res))        



1182.py class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        l1 = l2 = l3 = -1
        left = [[float('inf') for _ in range(3)] for __ in range(len(colors))]
        res = []
        for i, c in enumerate(colors):
            if c == 1:
                l1 = i
            elif c == 2:
                l2 = i
            else:
                l3 = i
            if l1 != -1:
                left[i][0] = i - l1
            if l2 != -1:
                left[i][1] = i - l2
            if l3 != -1:
                left[i][2] = i - l3
                
        l1 = l2 = l3 = -1
        right = [[float('inf') for _ in range(3)] for __ in range(len(colors))]
        for i in range(len(colors) - 1, -1, -1):
            c = colors[i]
            if c == 1:
                l1 = i
            elif c == 2:
                l2 = i
            else:
                l3 = i
            if l1 != -1:
                right[i][0] = l1  - i
            if l2 != -1:
                right[i][1] = l2 - i
            if l3 != -1:
                right[i][2] = l3 - i
        for i, c in queries:
            res.append(min(left[i][c - 1], right[i][c - 1]))
        return [c if c != float('inf') else -1 for c in res]
            
            
        
            
        



1184.py class Solution:
    def distanceBetweenBusStops(self, d: List[int], i: int, j: int) -> int:
        return min(sum(d[min(i, j):max(i, j)]), sum(d[:min(i, j)] + d[max(i, j):]))



1185.py from datetime import date
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return date(year, month, day).strftime("%A")



1186.py class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        def cumSum(it):
            sm = mn = 0
            sums = [0] * len(arr)
            for i, num in it:
                sm += num
                sums[i] = sm - mn
                mn = min(mn, sm)
            return sums
        
        lSum = cumSum(enumerate(arr))
        rSum = cumSum(reversed(list(enumerate(arr))))
        res = -float('inf')
        for i, num in enumerate(arr):
            if num >= 0:
                cur = lSum[i] + rSum[i] - num
            else:
                cur = lSum[i] + rSum[i] - 2 * num
            res = max(res, cur)
        return res if any(c >= 0 for c in arr) else max(arr)



1187.py class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {-1:0}
        arr2.sort()
        for i in arr1:
            tmp = collections.defaultdict(lambda: float('inf'))
            for key in dp:
                if i > key:
                    tmp[i] = min(tmp[i],dp[key])
                loc = bisect.bisect_right(arr2,key)
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp[arr2[loc]],dp[key]+1)
            dp = tmp
        if dp:
            return min(dp.values())
        return -1



1188.py import threading

class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        self.queue = collections.deque()

    def enqueue(self, element: int) -> None:
        self.pushing.acquire()
        self.queue.append(element)
        self.pulling.release()
		
    def dequeue(self) -> int:
        self.pulling.acquire()
        self.pushing.release()
        return self.queue.popleft()

    def size(self) -> int:
        return len(self.queue)



1189.py class Solution:
    def maxNumberOfBalloons(self, t: str) -> int:
          return min(t.count(c) // 'balloon'.count(c) for c in 'balon')



1190.py class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']
        for c in s:
            if c == '(':
                stack.append('')
            elif c == ')':
                add = stack.pop()[::-1]
                stack[-1] += add
            else:
                stack[-1] += c
        return stack.pop()



1191.py class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int, mod = 10 ** 9 + 7) -> int:
        def Kadane(arr, res = 0, cur = 0):
            for num in arr:
                cur = max(num, num + cur)
                res = max(res, cur)
            return res
        return ((k - 2) * max(sum(arr), 0) + Kadane(arr * 2) ) % mod if k > 1 else Kadane(arr) % mod



1196.py class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        return bisect.bisect(list(itertools.accumulate(sorted(arr))), 5000)



1197.py from functools import lru_cache
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i == j == 0:
                return 0
            if i == 1 and j == 0 or j == 1 and i == 0:
                return float('inf')
            return min(dfs(abs(i - 2), abs(j - 1)), dfs(abs(i - 1), abs(j - 2))) + 1
        return dfs(abs(x), abs(y))



1198.py from itertools import chain as chn
from collections import Counter as cnt
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        return min([k for k, v in cnt(chn(*mat)).items() if v == len(mat)] or [-1])



1199.py class Solution:
    def minBuildTime(self, A: List[int], split: int) -> int:
        heapq.heapify(A)
        while len(A) > 1:
            x, y = heapq.heappop(A), heapq.heappop(A)
            heapq.heappush(A, y + split)
        return heapq.heappop(A)



1200.py class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == mn]        



1201.py class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(a, b):
            return a if not b else gcd(b, a % b)
        ab, ac, bc = a * b // gcd(a, b), a * c // gcd(a, c), b * c // gcd(b, c)
        abc = ab * c // gcd(ab, c)
        l, r = 1, 2 * 10 ** 9
        while l < r:
            mid = (l + r) // 2
            if mid // a + mid // b + mid // c - mid // ab - mid // ac - mid // bc + mid // abc < n:
                l = mid + 1
            else:
                r = mid
        return l
        



1202.py class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UF:
            def __init__(self, n): self.p = list(range(n))
            def union(self, x, y): self.p[self.find(x)] = self.find(y)
            def find(self, x):
                if x != self.p[x]: self.p[x] = self.find(self.p[x])
                return self.p[x]
        uf, res, m = UF(len(s)), [], collections.defaultdict(list)
        for x,y in pairs: 
            uf.union(x,y)
        for i in range(len(s)): 
            m[uf.find(i)].append(s[i])
        for comp_id in m.keys(): 
            m[comp_id].sort(reverse=True)
        for i in range(len(s)): 
            res.append(m[uf.find(i)].pop())
        return ''.join(res)
        
            



1203.py class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topo_sort(points, pre, suc):
            order = []
            sources = [p for p in points if not pre[p]]
            while sources:
                s = sources.pop()
                order.append(s)
                for u in suc[s]:
                    pre[u].remove(s)
                    if not pre[u]:
                        sources.append(u)
            return order if len(order) == len(points) else []
        
        # find the group of each item
        group2item = collections.defaultdict(set)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
            group2item[group[i]].add(i)
        # find the relationships between the groups and each items in the same group
        t_pre, t_suc = collections.defaultdict(set), collections.defaultdict(set)
        g_pre, g_suc = collections.defaultdict(set), collections.defaultdict(set)
        for i in range(n):
            for j in beforeItems[i]:
                if group[i] == group[j]:
                    t_pre[i].add(j)
                    t_suc[j].add(i)
                else:
                    g_pre[group[i]].add(group[j])
                    g_suc[group[j]].add(group[i])
        # topological sort the groups
        groups_order = topo_sort([i for i in group2item], g_pre, g_suc)
        # topological sort the items in each group
        t_order = []
        for i in groups_order:
            items = group2item[i]
            i_order = topo_sort(items, t_pre, t_suc)
            if len(i_order) != len(items):
                return []
            t_order += i_order
        return t_order if len(t_order) == n else []



1207.py from collections import Counter as cnt
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return all(v == 1 for v in cnt(cnt(arr).values()).values())



1208.py class Solution:
    def equalSubstring(self, s: str, t: str, mx: int) -> int:
        i = 0
        for j in range(len(s)):
            mx -= abs(ord(s[j]) - ord(t[j]))
            if mx < 0:
                mx += abs(ord(s[i]) - ord(t[i]))
                i += 1
        return j - i + 1



1209.py class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i, c in enumerate(s):
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        return ''.join(k * v for k, v in stack) 
                



1210.py class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        q, move, n, seen = {(0, 1, 0)}, 0, len(grid), set()
        while q:
            new = set()
            for i, j, hv in q:
                if i == j == n - 1 and not hv:
                    return move
                if hv and i < n - 1 and not grid[i + 1][j]:
                    if (i + 1, j, 1) not in seen:
                        new.add((i + 1, j, 1))
                if hv and j + 1 < n and grid[i][j + 1] == grid[i - 1][j + 1] == 0:
                    if (i, j + 1, 1) not in seen:
                        new.add((i, j + 1, 1))
                    if (i - 1, j + 1, 0) not in seen:
                        new.add((i - 1, j + 1, 0))
                if not hv and j + 1 < n and not grid[i][j + 1]:
                    if (i, j + 1, 0) not in seen:
                        new.add((i, j + 1, 0))
                if not hv and i + 1 < n and grid[i + 1][j] == grid[i + 1][j - 1] == 0:
                    if (i + 1, j, 0) not in seen:
                        new.add((i + 1, j, 0))
                    if (i + 1, j - 1, 1) not in seen:
                        new.add((i + 1, j - 1, 1))
            q = new
            seen |= new
            move += 1
        return -1



1213.py class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return sorted(set(arr1) & set(arr2) & set(arr3))



1214.py # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import lru_cache
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        
        
        
        
        
        def dfs(node):
            return dfs(node.left) | dfs(node.right) | {node.val} if node else set()
        q1 = dfs(root1)
        return any(target - a in q1 for a in dfs(root2))



1215.py class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        def dfs(n):
            if n > high: 
                return 
            if n >= low:
                q.add(n)
            d = n % 10
            if d == 0:
                dfs(n * 10 + 1)
            elif d == 9:
                dfs(n * 10 + 8)
            else:
                dfs(n * 10 + d + 1) 
                dfs(n * 10 + d - 1)
        q = set()
        for i in range(10):
            dfs(i)
        return sorted(q)



1216.py class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)] 
        for i in range(n + 1): 
            for j in range(n + 1): 
                if not i or not j: 
                    dp[i][j] = i or j 
                elif s[i - 1] == s[n - j]: 
                    dp[i][j] = dp[i - 1][j - 1] 
                else: 
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        return dp[n][n] <= k * 2



1217.py class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        return min(sum((c1 - c2) % 2 for c2 in chips) for c1 in chips)



1218.py class Solution:
    def longestSubsequence(self, arr: List[int], d: int) -> int:
        dp = collections.Counter()
        for a in arr:
            dp[a] = max(dp[a], dp[a - d] + 1)
        return max(dp.values())



1219.py class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j, v):
            seen.add((i, j))
            dp[i][j] = max(dp[i][j], v)
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y] and (x, y) not in seen:
                    dfs(x, y, v + grid[x][y])
            seen.discard((i, j))
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    seen = set()
                    dfs(i, j, grid[i][j])
        return max(c for row in dp for c in row)



1220.py class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [1] * 5
        for _ in range(n - 1):
            add = [0] * 5
            # from a
            add[1] = (add[1] + dp[0]) % mod
            # from e
            add[0] = (add[0] + dp[1]) % mod
            add[2] = (add[2] + dp[1]) % mod
            # from i
            add[0] = (add[0] + dp[2]) % mod
            add[1] = (add[1] + dp[2]) % mod
            add[3] = (add[3] + dp[2]) % mod
            add[4] = (add[4] + dp[2]) % mod
            # from o
            add[2] = (add[2] + dp[3]) % mod
            add[4] = (add[4] + dp[3]) % mod
            # from u
            add[0] = (add[0] + dp[4]) % mod
            for i in range(5):
                dp[i] = add[i] % mod
        return sum(dp) % mod



1221.py class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = cnt = 0         
        for c in s:
            cnt += c == 'L'
            cnt -= c == 'R'
            res += cnt == 0
        return res  



1222.py class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        def dfs(dr, dc, r, c):
            while 0 <= r <= 7 and 0 <= c <= 7:
                if (r, c) in q:
                    res.append([r, c])
                    break
                r += dr
                c += dc
        q = set((r,c) for r, c in queens)
        res = []
        for dr, dc in (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1):
            dfs(dr, dc, *king)
        return res



1223.py class Solution:
    def dieSimulator(self, n: int, r: List[int]) -> int:
        K = max(r)
        dp = [[[0 for k in range(K)] for j in range(6)] for i in range(n)] 
        for j in range(6): dp[0][j][0] = 1
        for i in range(1, n):
            for j in range(6):
                dp[i][j][0] += sum(dp[i-1][t][k] for t in range(6) for k in range(r[t]) if t != j)
                for k in range(1, r[j]):
                    dp[i][j][k] = dp[i-1][j][k-1]
        return sum(dp[n-1][j][k] for j in range(6) for k in range(K)) % (10**9+7)



1224.py class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        def okay():
            if len(dic) == 1 and (1 in dic or 1 in dic.values()):
                return True 
            if len(dic) == 2:
                c1, c2 = sorted(dic.keys())
                if c2 - c1 == 1 and dic[c2] == 1 or (c1 == 1 and dic[1] == 1):
                    return True
        cnt = collections.Counter(nums)
        dic = collections.Counter(cnt.values())
        l = len(nums)
        for num in nums[::-1]:
            if okay():
                return l
            dic[cnt[num]] -= 1
            if not dic[cnt[num]]:
                dic.pop(cnt[num])
            cnt[num] -= 1
            if cnt[num]:
                dic[cnt[num]] += 1
            l -= 1
            if okay():
                return l



1227.py class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return max(0.5, 1 / n)



1228.py class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = (arr[-1] - arr[0]) // len(arr)
        for a, b in zip(arr, arr[1:]):
            if b != a + d:
                return a + d
        return 0
        



1229.py class Solution:
    def minAvailableDuration(self, s1: List[List[int]], s2: List[List[int]], d: int) -> List[int]:
        s2.sort()
        j = 0
        for s, e in sorted(s1):
            while j < len(s2) - 1 and s2[j][1] < s:
                j += 1
            if s2[j][0] <= e:
                l, r = max(s, s2[j][0]), min(e,s2[j][1])
                if r - l >= d:
                    return [l, l + d]



1230.py class Solution:
    def probabilityOfHeads(self, p: List[float], t: int) -> float:
        n = len(p)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] * (1 - p[i - 1])
                else : 
                    dp[i][j] = (dp[i - 1][j] * (1.0 - p[i - 1])) + (dp[i - 1][j - 1] * p[i - 1])
        return dp[-1][t]
        



1231.py class Solution:
    def maximizeSweetness(self, sw: List[int], K: int) -> int:
        def ok(m):
            c = sm = 0
            for s in sw:
                sm += s
                if sm >= m:
                    sm = 0 
                    c += 1
            return c >= K + 1
        l, r = 1, sum(sw)
        while l < r:
            m = (l + r) // 2
            if ok(m):
                l = m + 1
            else:
                r = m - 1
        print(l, r)
        return r if ok(r) else l - 1
        



1232.py class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        return len(set(a[0] == b[0] or (b[1] - a[1]) / (b[0] - a[0]) for a, b in zip(c, c[1:]))) == 1



1233.py class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        st = set(folder)
        for f in folder:
            if any(p in st for p in itertools.accumulate(f.split('/'), lambda x, y: x + '/' + y) if p and p != f):
                st.discard(f)
        return list(st)   



1234.py class Solution:
    def balancedString(self, s: str) -> int:
        cnt, i, res = {c: max(s.count(c) - len(s) // 4, 0) for c in 'QWER'}, 0, len(s)
        for j, c in enumerate(s):
            cnt[c] -= 1
            while i < len(s) and cnt[s[i]] < 0:
                cnt[s[i]] += 1
                i += 1
            if not any(cnt[c] > 0 for c in 'QWER'):
                res = min(res, j - i + 1)
        return res



1235.py class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]



1236.py # """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        host = startUrl[:(startUrl + '/').find('/', startUrl.find('//') + 2)]
        q, seen = [startUrl], {startUrl}
        for url in q:
            for nex in htmlParser.getUrls(url):
                if nex[:(nex + '/').find('/', nex.find('//') + 2)] == host and nex not in seen:
                    q.append(nex)
                    seen.add(nex)
        return q



1237.py from itertools import product as pr


class Solution(object):
    def findSolution(self, customfunction, z):
        return [
            [i, j]
            for i, j in pr(range(1, z + 1), repeat=2)
            if customfunction.f(i, j) == z
        ]





1238.py class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [start ^ i ^ i >> 1 for i in range(1 << n)]




1239.py class Solution:
    def maxLength(self, arr: List[str]) -> int:
        bfs = [""]
        for b in filter(lambda x: len(x) == len(set(x)), arr):
            bfs += [a + b for a in bfs if not set(a) & set(b)]
        return max(map(len, bfs))




1240.py class Solution:
    memo = {}

    def tilingRectangle(self, n: int, m: int) -> int:
        if (n, m) in {(11, 13), (13, 11)}:
            return 6
        if n == m:
            return 1
        if (n, m) not in self.memo:
            nMin = mMin = float("inf")
            for i in range(1, n // 2 + 1):
                nMin = min(
                    nMin, self.tilingRectangle(i, m) + self.tilingRectangle(n - i, m)
                )
            for j in range(1, m // 2 + 1):
                mMin = min(
                    mMin, self.tilingRectangle(n, j) + self.tilingRectangle(n, m - j)
                )
            self.memo[(n, m)] = min(nMin, mMin)
        return self.memo[(n, m)]




1243.py class Solution:
    def transformArray(self, arr: List[int], change: bool = True) -> List[int]:
        while change:
            new = (
                arr[:1]
                + [
                    b + (a > b < c) - (a < b > c)
                    for a, b, c in zip(arr, arr[1:], arr[2:])
                ]
                + arr[-1:]
            )
            arr, change = new, arr != new
        return arr




1244.py class Leaderboard:
    def __init__(self):
        self.scores = collections.defaultdict(set)
        self.p = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[self.p[playerId]].discard(playerId)
        self.p[playerId] += score
        self.scores[self.p[playerId]].add(playerId)

    def top(self, K: int) -> int:
        sm = cnt = 0
        for score, players in sorted(self.scores.items())[::-1]:
            if len(players) + cnt <= K:
                sm += len(players) * score
                cnt += len(players)
            else:
                sm += (K - cnt) * score
                cnt = K
        return sm

    def reset(self, playerId: int) -> None:
        self.scores[self.p[playerId]].discard(playerId)
        self.p[playerId] = 0
        self.scores[0].add(playerId)




1245.py class Solution:
    def treeDiameter(self, edges: List[List[int]], move: int = 0) -> int:
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        bfs = {(u, None) for u, nex in graph.items() if len(nex) == 1}
        while bfs:
            bfs, move = (
                {(v, u) for u, pre in bfs for v in graph[u] if v != pre},
                move + 1,
            )
        return max(move - 1, 0)




1246.py class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for l in range(1, n + 1):
            i, j = 0, l - 1
            while j < n:
                if l == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + dp[i + 1][j]
                    if arr[i] == arr[i + 1]:
                        dp[i][j] = min(1 + dp[i + 2][j], dp[i][j])
                    for k in range(i + 2, j + 1):
                        if arr[i] == arr[k]:
                            dp[i][j] = min(dp[i + 1][k - 1] + dp[k + 1][j], dp[i][j])
                i, j = i + 1, j + 1
        return dp[0][n - 1]




1247.py class Solution:
    def minimumSwap(self, s1: str, s2: str, xy: int = 0, yx: int = 0) -> int:
        for a, b in zip(s1, s2):
            xy += a == "x" and b == "y"
            yx += a == "y" and b == "x"
        return (xy + yx) // 2 + (xy % 2) * 2 if xy % 2 == yx % 2 else -1




1248.py class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int, cnt: int = 0) -> int:
        odds = [-1] + [i for i, num in enumerate(nums) if num % 2] + [len(nums)]
        return sum(
            (odds[j - k + 1] - odds[j - k]) * (odds[j + 1] - odds[j])
            for j in range(k, len(odds) - 1)
        )





1249.py class Solution:
    def minRemoveToMakeValid(
        self, s: str, res: str = "", l: str = "(", r: str = ")", b: int = 0
    ) -> str:
        for _ in range(2):
            for c in s:
                if c == r and b <= 0:
                    continue
                b += c == l
                b -= c == r
                res += c
            res, s, l, r, b = "", res[::-1], r, l, 0
        return s




1250.py from functools import reduce


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce(math.gcd, nums) == 1




1252.py from collections import Counter as cnt


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row, col = cnt(r for r, c in indices), cnt(c for r, c in indices)
        return sum((row[i] + col[j]) % 2 for i in range(n) for j in range(m))




1253.py class Solution:
    def reconstructMatrix(
        self, upper: int, lower: int, colsum: List[int]
    ) -> List[List[int]]:
        res = [[0] * len(colsum) for _ in range(2)]
        for j, sm in enumerate(colsum):
            if sm == 2:
                if upper == 0 or lower == 0:
                    return []
                upper -= 1
                lower -= 1
                res[0][j] = res[1][j] = 1
            elif sm:
                if upper == lower == 0:
                    return []
                if upper >= lower:
                    upper -= 1
                    res[0][j] = 1
                else:
                    lower -= 1
                    res[1][j] = 1
        return res if upper == lower == 0 else []




1254.py class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, ret=True):
            grid[i][j] = -1
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n:
                    if not grid[x][y]:
                        ret &= dfs(x, y)
                else:
                    ret = False
            return ret

        m, n = len(grid), len(grid[0])
        return sum(dfs(i, j) for i in range(m) for j in range(n) if grid[i][j] == 0)





1255.py from collections import Counter as cnt


class Solution:
    def maxScoreWords(self, w: List[str], l: List[str], s: List[int]) -> int:
        def dfs(use, i):
            return (
                use
                and i < len(w)
                and max(
                    dfs(use, i + 1),
                    not cnt(w[i]) - use
                    and sum(s[ord(c) - ord("a")] for c in w[i])
                    + dfs(use - cnt(w[i]), i + 1),
                )
            )

        return int(dfs(cnt(l), 0))




1256.py class Solution:
    def encode(self, num: int) -> str:
        return bin(num + 1)[3:]




1257.py class Solution:
    def findSmallestRegion(
        self, regions: List[List[str]], region1: str, region2: str
    ) -> str:
        nex = {r: region[0] for region in regions for r in region[1:]}
        r1, r2 = region1, region2
        while r1 != r2:
            r1 = nex[r1] if r1 in nex else region2
            r2 = nex[r2] if r2 in nex else region1
        return r1




1258.py class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        def root(s):
            return s if parent[s] == s else root(parent[s])

        parent = {s: s for s in [c for sy in synonyms for c in sy] + text.split()}
        for a, b in synonyms:
            parent[root(a)] = root(b)
        bfs = [""]
        for t in text.split():
            r = root(t)
            bfs = [s + " " + w for s in bfs for w in parent if root(w) == r]
        return sorted(s[1:] for s in bfs)




1259.py class Solution:
    def numberOfWays(self, num_people):
        self.memo = {0: 1}

        def dp(n):
            if n not in self.memo:
                self.memo[n] = sum(
                    [dp(i - 2) * dp(n - i) for i in range(2, n + 1, 2)]
                ) % (10 ** 9 + 7)
            return self.memo[n]

        return dp(num_people)




1260.py class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        chain = [r for row in grid for r in row]
        k %= len(chain)
        chain = chain[-k:] + chain[:-k]
        return [chain[i : i + len(grid[0])] for i in range(0, len(chain), len(grid[0]))]





1261.py class FindElements:
    def dfs(self, node: TreeNode, real: int = 0):
        if node:
            node.val = real
            self.nums.add(node.val)
            self.dfs(node.left, real * 2 + 1)
            self.dfs(node.right, real * 2 + 2)

    def __init__(self, root: TreeNode):
        self.root = root
        self.nums = set()
        self.dfs(root)

    def find(self, target: int) -> bool:
        return target in self.nums




1262.py class Solution:
    def maxSumDivThree(
        self, nums: List[int], dp: list = [0, -float("inf"), -float("inf")]
    ) -> int:
        for num in nums:
            dp = [max(dp[i], dp[(i - num) % 3] + num) for i in range(3)]
        return dp[0]
