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




## data structure


