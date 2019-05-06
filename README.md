# algorithm
learning algorithm program

## 数学

### 213 2的冥
*  解法一   
考虑2的特性，转换成二进制数，统计1的数量
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
二进制运算
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

### 326 3的冥
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







