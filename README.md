# algorithm
learning algorithm program

## 数学

### 二进制计算
#### 477 汉明距离总和
* 解法一   
统计所有数&2的零次方到2的32次方出现1，0的次数, 例如:   
nums = [2, 5, 6]
[2, 5, 6] 到 2^0  0，1，0 那在2的0次这个层面，汉明距离就是 count(0)*count(1) = 2；   
[2, 5, 6] 到 2^1  1，0，1 那在2的0次这个层面，汉明距离就是 count(0)*count(1) = 2；   
[2, 5, 6] 到 2^2  0，1，1 那在2的0次这个层面，汉明距离就是 count(0)*count(1) = 2； 
得出总距离就为6.   
注意到count(0)+count(1)为数组nums的长度，所以只要统计0的次数或者1的次数，剩余的用nums的长度去减统计的0的次数或者1的次数即可。
```
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        
        t = [1]*32
        for i in range(1,32):
            t[i] = t[i-1] << 1
            
        count = 0
        length = len(nums) 
        for i in t:
            one = 0
            for j in nums:
                one += (i&j) // i
            count += one*(length-one)
            
        return count
                    
```

#### 136 只出现一次的数字
* 解法一   
异或的应用   x ^ 0 = x; x ^ x =0   
```
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums[1:]:
            nums[0] ^= i
        return nums[0]
```

#### 389  找不同   
异或的应用   x ^ 0 = x; x ^ x =0     
```
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ret = 0
        for i in s:
            ret ^= ord(i)
        for j in t:
            ret ^= ord(j)
                
        return chr(ret)
```

260 只出现一次的数字 III
* 解法一 异或的应用   
```
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        t = 0
        for i in nums:
            t ^= i
            
        n = len(bin(t))-3  #取高位
        a, b = 0, 0
        for i in nums:
            if i>>n&1: # a高位为1， 相同的会消掉
                a ^= i
            else: # b高位必为0，相同的会消掉
                b ^= i
                
        return b, a
```


#### 371 两整数之和   
位运算求和，先异或不进位，与进位   
```
class Solution(object):
    
    def getSum(self, a, b):
        sum = a ^ b
        carry = (a & b) << 1
        if carry != 0:
            return self.getSum(sum, carry)
        return sum
```

#### 78 子集
* 解法一   
序列[1,2,3]的子集对应的排列就是000-111  
通过&计算1的顺序  
```
class Solution(object):
    def subsets(self, nums):
        length = 2**len(nums)
        result = [0] * length
        for i in range(length):
            t = i
            tmp = []
            j = 0
            while t:
                if t&1:
                    tmp.append(nums[j])
                j += 1
                t = t >> 1
                
            result[i] = tmp
            
        return result
```
* 解法二   
方法同一， 法一是&1后做偏移运算
这里是& 1，2，4...判断对应的位置是否为1   
```
class Solution(object):
    def subsets(self, nums):
        length = len(nums)
        size = 2 ** length
        i = 1

        result = [[]]
        while i < size:
            tmp = []
            for j in range(length):
                t = 1<<j
                if i&t:
                    tmp.append(nums[j])
            result.append(tmp)
            i += 1

        return result
```

#### 22 括号生成
* 解法一 用二进制进行位判断     
```
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        length = 2*n
        result = []
        
        binary = [ 1<<i for i in range(length-1, -1, -1)]
        mn = sum(binary[0::2])
        for i in range(2**length-1, mn-1, -1):
            tmp = ['(']
            left = 1
            right = 0
            for j in binary[1:]:
                if right > left or left >n or right > n:
                    break
                if i&j:
                    tmp.append('(')
                    left += 1
                else:
                    tmp.append(')')
                    right += 1
                    
            if len(tmp) == length and left == right:
                result.append(''.join(tmp))
                
        return result
```

#### 201 数字范围按位与

* 解法一 统计各个位置上的0 
```
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
        if m == 0 and n-m < 2:
            return n&m
        
        nlength = len(bin(n))
        mlength = len(bin(m))
        
        t = [1]*32
        for i in range(1,32):
            t[i] = t[i-1] << 1
            
        if nlength == mlength:
            rec = [1]*(nlength-2)
            d = m
            while True:
                if sum(rec) == 1 or d > n:
                    break
                for i in range(nlength-2): # 记录各个位置上的0
                    if t[i]&d == 0:
                        rec[i] =0
                d += 1
                   
            ret = 0
            for i in range(nlength-2):
                ret += rec[i]*t[i]
            return ret
            
        elif nlength > mlength:
            return 0
```

* 解法二  计算n与m的二进制高位  

```
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
        if m == 0 and n-m < 2: # 边界条件
            return n&m
        
        nlength = len(bin(n))  # 计算二进制长度，这里还有'0b'未去掉
        mlength = len(bin(m))
        
        # 可以将该段代码，放到类初始化函数中，也可以修改32-->nlength-2
        t = [1]*32   # 保存2的次方用以判断数字该位置上是否为1
        for i in range(1,32):
            t[i] = t[i-1] << 1  # 位移加快处理
            
        if nlength > mlength:
            return 0

        elif nlength == mlength:
            total = 0
            for i in range(nlength-3, -1, -1): 
                d = n & t[i]
                if d ==  m & t[i] : # 将m与n的高位依次取出
                    total +=  d
                else:
                    break
                
            return total              
```

#### 401 二进制手表   
* 解法一 用二进制位来标记选中该时间   
```
class Solution:
    def readBinaryWatch(self, num: int) :
        
        if num == 0:
            return ['0:00']
        elif num > 8:
            return []
            
        hour = [1, 2, 4, 8]
        minute = [1, 2, 4,  8, 16, 32]
        h_mx = 3
        m_mx = 5
        
        def compute(t, lst, mx):
            if t == 0:
                return [0]
            s = []
            length = len(lst)
            for i in range(1, sum(lst[length-t:])+1):
                zero_list = [0]*length
                count = 0
                for j in range(length):
                    if i&lst[j]:   # 标记二进制位置
                        zero_list[j] = 1
                        count += 1  # 统计二进制位为1的数量
                if count == t:  
                    string = 0
                    for k in range(length):
                        string += zero_list[k]*lst[k]
                    if string < mx:
                        s.append(string)
            return s
        
        ret = []
        for i in range(min(h_mx,num)+1):

            j = num - i
            if j > m_mx:
                continue
            
            s_hour = compute(i, hour, 12)
            s_minute = compute(j, minute, 60)
                
            for p in s_hour:
                for q in s_minute:
                    ret.append('%s:%02d'% (p,q))
                
        return ret
```

#### 397 整数替换   
* 解法一  当加1可以抵消2位时，加1，否则减1   
```
class Solution:
    def integerReplacement(self, num: int) :
        count = 0
        while num > 1:
            if num == 3: #  边界条件3
                count += 2
                break
                
            if num & 0b1 == 0: # 偶数时，除以2
                num //=  2
                count += 1
            else:
                if (num+1) & 0b11 == 0: # 当加1可以抵消2位时，加1，否则减1
                    num += 1
                else:
                    num -= 1
                count += 1
        return count
```

#### 29 两数相除  
1、异或判断两个数正负;      
2、推导式：dividend/2\*\*x > divisor ==> dividend > 2\*\*x * divisor;    
3、边界点 -2**31 / -1;   
```
class Solution:
    
    def __init__(self):
        self.mn = -2**31
        
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == 0:
            return 0
        
        if divisor == -1:
            if dividend == self.mn:
                return -self.mn-1
            return  -dividend
        
        if divisor == 1:
            return dividend
        
        isNegative = (dividend ^ divisor) < 0
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                result += (1 << i)
                dividend -= (divisor << i)
                
        return -result if isNegative else result     
```

#### 213 2的冥
*  解法一   
内置函数的应用
```
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <  1:
            return False
        elif n < 3:
            return True
        
        return bin(n).count('1') == 1 
```

* 解法二   
n&(n-1)的应用
```
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <  1:
            return False
        
        return n & (n-1) == 0
```

简写   
```
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0
```

####  318 最大单词长度乘积  
将26个字母对应到2\*\*1-2\*\*26次, 然后用&计算即可。   
* 解法一
```
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        b = [1] * 26
        for i in range(1,26):
            b[i] = 2*b[i-1]
            
        length = len(words)
        res = [0]*length
        for i in range(length):
            for j in set(words[i]):
                res[i] += b[ord(j) - 97]
                
        mx = 0
        for i in range(length-1):
            for j in range(i, length):
                if res[i]&res[j] == 0:
                    t = len(words[i]) * len(words[j])
                    if t > mx:
                        mx = t
                        
        return mx
```   


#### 326 3的冥
* 解法一   
log(n,3) = log10(n)/log10(3)
```
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        if n == 1:
            return True
        
        from math import log10
        
        return  n == 3 ** int(log10(n)/log10(3)) 
```

* 解法二   
暴力解决   
```  
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        
        while n%3 == 0:
            n //= 3
        
        return n == 1
```

* 解法三
取最大的3的冥   
```
class Solution:
    def __init__(self):
        from math import log10
        self.mx = 3**(log10(0xffffffff)//log10(3))
    
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        
        return self.mx%n == 0
```

 
#### 954 二倍数对数组  array-of-doubled-pairs

这个题，题意很简单，判断一个列表，通过更换位置，使偶数位置上的数是奇数位置上的两倍。


#### 1442 形成两个异或相等数组的三元组数目 count-triplets-that-can-form-two-arrays-of-equal-xor

这个题目完全考察了对异或的应用


#### 762 二进制表示中质数个计算置位
* 解法一   
```
class Solution:
    def __init__(self):
        self.prime = dict.fromkeys([2,3,5,7,11,13,17,19,23,29,31])

    def countPrimeSetBits(self, L: int, R: int) -> int:
        sm = 0
        for i in range(L, R+1):
            count = 0
            while i != 0:
                i &= i-1
                count += 1
                
            if count in self.prime:
                sm += 1
                
        return sm
```

* 解法二   
转为二进制直接统计1的数量
``` 
class Solution:
    def __init__(self):
        self.prime = dict.fromkeys([2,3,5,7,11,13,17,19,23])

    def countPrimeSetBits(self, L: int, R: int) -> int:
        sm = 0
        for i in range(L, R+1):
            if bin(i).count('1') in self.prime:
                sm += 1
                
        return sm
```

* 解法三  
二进制取最低位计算
```
class Solution:
    def __init__(self):
        self.prime = dict.fromkeys([2,3,5,7,11,13,17,19,23])

    def countPrimeSetBits(self, L: int, R: int) -> int:
        sm = 0
        for i in range(L, R+1):
            count = 0
            while i > 0:
                if i&1 == 1:
                    count += 1
                i = i >> 1
                    
            if count in self.prime:
                sm += 1
                
        return sm
```

#### 633 平方之和

* 解法一 暴力法   
``` 
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        if c < 2:
            return True
        
        i, j = 0, int(c ** 0.5)
        
        while i <= j:
            left = (i+j)**2
            right = c + 2*i*j
            if  left == right:
                return True
            elif left < right:
                i += 1
            elif left > right:
                j -=1
                
        return False
```
*  解法二  
```
```

#### 367 有效的完全平方数

*


#### 50 Power(x, n)
* 解法一 简单分治
```
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return x/x

        flag = True
        if n < 0:
            n, flag = -n, False
        
        cnt, x2 = 1, x
        while True:
            if n%2 == 0:
                x2 = x2*x2
                n /= 2
                if n == 1:
                    break
            else:
                n -= 1
                if n == 0:
                    break
                cnt *= x2
                
        if flag:
            return cnt*x2

        return 1/(cnt*x2)
```

### 平面计算



### 矩阵计算


### 素数


## 分治法
二分法： 是分治法的一种特殊情况，会缩小问题的规模，时间复杂度为logN   


## 链表

### 快慢指针

## 贪心算法

## 堆

## 树

#### 421 数组中两个数的最大异或值

## 动态规划

#### 898 子数组按位或操作   
* 解法一 中级难度dp    
1、转移方程式dp[i] = {b ^ A[i] for b in dp[i - 1]} + {A[i]}，即以A[i]结尾的所有子数组异或结果等于以A[i-1]结尾的所有子数组异或结果，与当前的A[i]异或的结果集合，再并上{A[i]}     
2、 t = { a|n for n in cur}  ==> len(t) < 32  
```
class Solution(object):
    def subarrayBitwiseORs(self, A):
        res = set()
        cur = set()
        for a in A:
            cur = {n | a for n in cur} | {a}
            res |= cur   # 取并集
        return len(res)
```

####  97 交错字符串  interleaving-string

这道题挺有意思的一道dp题， 一般的dp都是提供正向，这道题提供x轴和y轴，来拼凑，一般人很难想到都为认为是搜索题，而走偏；


## 搜索

### dfs 深度优先搜索

#### 78 子集   
递归，注意数组在递归中的影响，递归的出口
```
class Solution(object):
    def subsets(self, nums):
        length = len(nums)
        result = []
        
        def dfs(t, tmp=None):
            if tmp == None:
                tmp = []
                
            if t == length:
                result.append(tmp)
                return
            
            dfs(t+1, tmp.copy())
            tmp.append(nums[t])
            dfs(t+1, tmp.copy())
        dfs(0)
        
        return result
        
```

#### 22 括号生成
* 解法一 dfs  
```
class Solution(object):
    def generateParenthesis(self, n):
        
        length = 2*n
        result = []
        def dfs(left, right, string):
            
            if left < right or left > n or right > n:
                return
            
            if left == n and left == right:
                result.append(string)
                return
            
            dfs(left, right+1, string+')')
                
            dfs(left+1, right,  string+'(')
            
        dfs(1, 0, '(')
        return result
```

## 排序


## 特殊的算法

### Rabin-Karp

假设子串的长度为M,目标字符串的长度为N
计算子串的hash值
计算目标字符串中每个长度为M的子串的hash值（共需要计算N-M+1次）
比较hash值
如果hash值不同，字符串必然不匹配，如果hash值相同，还需要使用朴素算法再次判断


