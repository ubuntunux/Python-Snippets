[https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.ctypes.html](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.ctypes.html)

```
import ctypes
import numpy as np
data = np.array([0, ], dtype=np.uint32)
value_ptr = data.ctypes.data_as(ctypes.c_void_p)
```

another example)

[https://stackoverflow.com/questions/3195660/how-to-use-numpy-array-with-ctypes](https://stackoverflow.com/questions/3195660/how-to-use-numpy-array-with-ctypes)

```
import ctypes
import numpy
c_float_p = ctypes.POINTER(ctypes.c_float)
data = numpy.array([[0.1, 0.1], [0.2, 0.2], [0.3, 0.3]])
data = data.astype(numpy.float32)
data_p = data.ctypes.data_as(c_float_p)
```