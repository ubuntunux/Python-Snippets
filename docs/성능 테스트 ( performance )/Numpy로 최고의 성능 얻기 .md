[http://ipython-books.github.io/featured-01/](http://ipython-books.github.io/featured-01/)

```
NumPy is the cornerstone of the scientific Python software stack. It provides a special data type optimized for vector computations, the ndarray. This object is at the core of most algorithms in scientific numerical computing.

With NumPy arrays, you can achieve significant performance speedups over native Python, particularly when your computations follow the Single Instruction, Multiple Data (SIMD) paradigm. However, it is also possible to unintentionally write non-optimized code with NumPy.

In this featured recipe, we will see some tricks that can help you write optimized NumPy code. We will start by looking at ways to avoid unnecessary array copies in order to save time and memory. In that respect, we will need to dig into the internals of NumPy.

Learning to avoid unnecessary array copies
Computations with NumPy arrays may involve internal copies between blocks of memory. These copies are not always necessary, in which case they should be avoided. Here are a few tips that can help you optimize your code accordingly.

import numpy as np
Inspect the memory address of arrays

The first step when looking for silent array copies is to find out the location of arrays in memory. The following function does just that:
def id(x):
    # This function returns the memory
    # block address of an array.
    return x.__array_interface__['data'][0]
You may sometimes need to make a copy of an array, for instance if you need to manipulate an array while keeping an original copy in memory.
a = np.zeros(10); aid = id(a); aid
71211328
b = a.copy(); id(b) == aid
False
Two arrays with the same data location (as returned by id) share the underlying data buffer. However, the opposite is only true if the arrays have the same offset (meaning that they have the same first element). Two shared arrays with different offsets will have slightly different memory locations, as shown in the following example:

id(a), id(a[1:])
(71211328, 71211336)
In this recipe, we'll make sure to use this method with arrays that have the same offset. Here is a more reliable solution for finding out if two arrays share the same data:

def get_data_base(arr):
    """For a given Numpy array, finds the
    base array that "owns" the actual data."""
    base = arr
    while isinstance(base.base, np.ndarray):
        base = base.base
    return base

def arrays_share_data(x, y):
    return get_data_base(x) is get_data_base(y)
print(arrays_share_data(a,a.copy()),
      arrays_share_data(a,a[1:]))
False True
Thanks to Michael Droettboom for pointing out this precision and proposing this alternative solution.

In-place and implicit copy operations

Array computations can involve in-place operations (first example below: the array is modified) or implicit-copy operations (second example: a new array is created).
a *= 2; id(a) == aid
True
c = a * 2; id(c) == aid
False
Be sure to choose the type of operation you actually need. Implicit-copy operations are significantly slower, as shown here:

%%timeit a = np.zeros(10000000)
a *= 2
10 loops, best of 3: 19.2 ms per loop
%%timeit a = np.zeros(10000000)
b = a * 2
10 loops, best of 3: 42.6 ms per loop
Reshaping an array may or may not involve a copy. The reasons will be explained below. For instance, reshaping a 2D matrix does not involve a copy, unless it is transposed (or more generally non-contiguous):
a = np.zeros((10, 10)); aid = id(a); aid
53423728
Reshaping an array while preserving its order does not trigger a copy.

b = a.reshape((1, -1)); id(b) == aid
True
Transposing an array changes its order so that a reshape triggers a copy.

c = a.T.reshape((1, -1)); id(c) == aid
False
Therefore, the latter instruction will be significantly slower than the former.

The flatten and ravel methods of an array reshape it into a 1D vector (flattened array). The former method always returns a copy, whereas the latter returns a copy only if necessary (so it's significantly faster too, especially with large arrays).
d = a.flatten(); id(d) == aid
False
e = a.ravel(); id(e) == aid
True
%timeit a.flatten()
1000000 loops, best of 3: 881 ns per loop
%timeit a.ravel()
1000000 loops, best of 3: 294 ns per loop
Broadcasting rules

Broadcasting rules allow you to make computations on arrays with different but compatible shapes. In other words, you don't always need to reshape or tile your arrays to make their shapes match. The following example illustrates two ways of doing an outer product between two vectors: the first method involves array tiling, the second one involves broadcasting. The last method is significantly faster.
n = 1000
a = np.arange(n)
ac = a[:, np.newaxis]
ar = a[np.newaxis, :]
%timeit np.tile(ac, (1, n)) * np.tile(ar, (n, 1))
100 loops, best of 3: 10 ms per loop
%timeit ar * ac
100 loops, best of 3: 2.36 ms per loop
Making efficient selections in arrays with NumPy
NumPy offers multiple ways of selecting slices of arrays. Array views refer to the original data buffer of an array, but with different offsets, shapes and strides. They only permit strided selections (i.e. with linearly spaced indices). NumPy also offers specific functions to make arbitrary selections along one axis. Finally, fancy indexing is the most general selection method, but it is also the slowest as we will see in this recipe. Faster alternatives should be chosen when possible.

Let's create an array with a large number of rows. We will select slices of this array along the first dimension.
n, d = 100000, 100
a = np.random.random_sample((n, d)); aid = id(a)
Array views and fancy indexing

Let's select one every ten rows, using two different methods (array view and fancy indexing).
b1 = a[::10]
b2 = a[np.arange(0, n, 10)]
np.array_equal(b1, b2)
True
The view refers to the original data buffer, whereas fancy indexing yields a copy.
id(b1) == aid, id(b2) == aid
(True, False)
Let's compare the performance of both methods.
%timeit a[::10]
1000000 loops, best of 3: 804 ns per loop
%timeit a[np.arange(0, n, 10)]
100 loops, best of 3: 14.1 ms per loop
Fancy indexing is several orders of magnitude slower as it involves copying a large array.

Alternatives to fancy indexing: list of indices

When non-strided selections need to be done along one dimension, array views are not an option. However, alternatives to fancy indexing still exist in this case. Given a list of indices, NumPy's function take performs a selection along one axis.
i = np.arange(0, n, 10)
b1 = a[i]
b2 = np.take(a, i, axis=0)
np.array_equal(b1, b2)
True
The second method is faster:

%timeit a[i]
100 loops, best of 3: 13 ms per loop
%timeit np.take(a, i, axis=0)
100 loops, best of 3: 4.87 ms per loop
Alternatives to fancy indexing: mask of booleans

When the indices to select along one axis are specified by a vector of boolean masks, the function compress is an alternative to fancy indexing.
i = np.random.random_sample(n) < .5
The selection can be made using fancy indexing or the np.compress function.

b1 = a[i]
b2 = np.compress(i, a, axis=0)
np.array_equal(b1, b2)
True
%timeit a[i]
10 loops, best of 3: 59.8 ms per loop
%timeit np.compress(i, a, axis=0)
10 loops, best of 3: 24.1 ms per loop
The second method is also significantly faster than fancy indexing.

Fancy indexing is the most general way of making completely arbitrary selections of an array. However, more specific and faster methods often exist and should be preferred when possible.

Array views should be used whenever strided selections have to be done, but one needs to be careful about the fact that views refer to the original data buffer.

How it works?
In this section, we will see what happens under the hood when using NumPy, and how this knowledge allows us to understand the tricks given in this recipe.

Why are NumPy arrays efficient?

A NumPy array is basically described by metadata (number of dimensions, shape, data type, and so on) and the actual data. The data is stored in a homogeneous and contiguous block of memory, at a particular address in system memory (Random Access Memory, or RAM). This block of memory is called the data buffer. This is the main difference with a pure Python structure, like a list, where the items are scattered across the system memory. This aspect is the critical feature that makes NumPy arrays so efficient.

Why is this so important? Here are the main reasons:

Array computations can be written very efficiently in a low-level language like C (and a large part of NumPy is actually written in C). Knowing the address of the memory block and the data type, it is just simple arithmetic to loop over all items, for example. There would be a significant overhead to do that in Python with a list.

Spatial locality in memory access patterns results in significant performance gains, notably thanks to the CPU cache. Indeed, the cache loads bytes in chunks from RAM to the CPU registers. Adjacent items are then loaded very efficiently (sequential locality, or locality of reference).

Data elements are stored contiguously in memory, so that NumPy can take advantage of vectorized instructions on modern CPUs, like Intel's SSE and AVX, AMD's XOP, and so on. For example, multiple consecutive floating point numbers can be loaded in 128, 256 or 512 bits registers for vectorized arithmetical computations implemented as CPU instructions.

Additionally, let's mention the fact that NumPy can be linked to highly optimized linear algebra libraries like BLAS and LAPACK, for example through the Intel Math Kernel Library (MKL). A few specific matrix computations may also be multithreaded, taking advantage of the power of modern multicore processors.

In conclusion, storing data in a contiguous block of memory ensures that the architecture of modern CPUs is used optimally, in terms of memory access patterns, CPU cache, and vectorized instructions.

What is the difference between in-place and implicit-copy operations?

Let's explain trick 3. An expression like a *= 2 corresponds to an in-place operation, where all values of the array are multiplied by two. By contrast, a = a * 2 means that a new array containing the values of a * 2 is created, and the variable a now points to this new array. The old array becomes unreferenced and will be deleted by the garbage collector. No memory allocation happens in the first case, contrary to the second case.

More generally, expressions like a[i:j] are views to parts of an array: they point to the memory buffer containing the data. Modifying them with in-place operations changes the original array. Hence, a[:] = a * 2 results in an in-place operation, unlike a = a * 2.

Knowing this subtlety of NumPy can help you fix some bugs (where an array is implicitly and unintentionally modified because of an operation on a view), and optimize the speed and memory consumption of your code by reducing the number of unnecessary copies.

Why cannot some arrays be reshaped without a copy?

We explain here trick 4, where a transposed 2D matrix cannot be flattened without a copy. A 2D matrix contains items indexed by two numbers (row and column), but it is stored internally as a 1D contiguous block of memory, accessible with a single number. There is more than one way of storing matrix items in a 1D block of memory: we can put the elements of the first row first, the second row then, and so on, or the elements of the first column first, the second column then, and so on. The first method is called row-major order, whereas the latter is called column-major order. Choosing between the two methods is only a matter of internal convention: NumPy uses the row-major order, like C, but unlike FORTRAN.

Array layout

More generally, NumPy uses the notion of strides to convert between a multidimensional index and the memory location of the underlying (1D) sequence of elements. The specific mapping between array[i1, i2] and the relevant byte address of the internal data is given by

offset = array.strides[0] * i1 + array.strides[1] * i2

When reshaping an array, NumPy avoids copies when possible by modifying the strides attribute. For example, when transposing a matrix, the order of strides is reversed, but the underlying data remains identical. However, flattening a transposed array cannot be accomplished simply by modifying strides (try it!), so a copy is needed (thanks to Chris Beaumont from Harvard for clarifying an earlier version of this paragraph).

Recipe 4.6 (Using stride tricks with NumPy) contains a more extensive discussion on strides. Also, recipe 4.7 (Implementing an efficient rolling average algorithm with stride tricks) shows how one can use strides to accelerate particular array computations.

Internal array layout can also explain some unexpected performance discrepancies between very similar NumPy operations. As a small exercise, can you explain the following benchmarks?

a = np.random.rand(5000, 5000)
%timeit a[0,:].sum()
%timeit a[:,0].sum()
100000 loops, best of 3: 9.57 µs per loop
10000 loops, best of 3: 68.3 µs per loop
What are NumPy broadcasting rules?

Broadcasting rules describe how arrays with different dimensions and/or shapes can still be used for computations. The general rule is that two dimensions are compatible when they are equal, or when one of them is 1. NumPy uses this rule to compare the shapes of the two arrays element-wise, starting with the trailing dimensions and working its way forward. The smallest dimension is internally stretched to match the other dimension, but this operation does not involve any memory copy.

References
Here are a few references:

NumPy performance tricks.
Locality of reference.
Internals of NumPy in the SciPy lectures notes.
100 NumPy exercices.
Broadcasting rules and examples.
Array interface in NumPy.
The complete list of NumPy routines is available on the NumPy Reference Guide.
List of indexing routines.
You will find related recipes on the book's repository.

You'll find the rest of the chapter in the full version of the IPython Cookbook, by Cyrille Rossant, Packt Publishing, 2014.

 
Two books on Python for data science, by Cyrille Rossant.
beginner-level
   code    data    updates
advanced-level
   code    data    updates

```