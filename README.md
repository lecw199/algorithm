# algorithm
learning algorithm program

## 数学

### 二进制计算


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

#### 29 两数相除  
1、异或判断两个数正负;      
2、推导式：dividend/2**x > divisor ==> dividend > 2**x ** divisor;    
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

## 动态规划


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

## 排序





