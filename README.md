open-government
===============

Open source algorithmic government with voluntary participation



Background
----------

What anarchists understand as a "government" in it's current state is an organization with a monopoly on force or voilence. 

![alt text](http://i.imgur.com/9qjlo93.png "Government life cycle MC")

```python
>>> import numpy as np
>>> a = np.matrix('0.2 0.8 0 0 0; 0 0.9 0.1 0 0; 0 0.1 0.8 0.1 0; 0 0 0.1 0.6 0.3; 0.5 0 0 0 0.5')
>>> print a
[[ 0.2  0.8  0.   0.   0. ]
 [ 0.   0.9  0.1  0.   0. ]
 [ 0.   0.1  0.8  0.1  0. ]
 [ 0.   0.   0.1  0.7  0.2]
 [ 0.5  0.   0.   0.   0.5]]
>>> np.linalg.matrix_power(a,100)[0]
matrix([[ 0.02890173,  0.53949904,  0.30828516,  0.07707129,  0.04624277]])
```


