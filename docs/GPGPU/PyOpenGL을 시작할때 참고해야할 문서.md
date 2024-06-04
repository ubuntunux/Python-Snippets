[Previous](..)
## PyOpenGL을 시작할때 참고해야할 문서
PyOpenGL을 시작할때 참고해야할 문서

원문 : [http://www.siafoo.net/article/58](http://www.siafoo.net/article/58)

```

1   Introduction

If you have never encountered OpenGL, then you might not be aware of the fact that it is an excellent 3D graphics API and an absolute pleasure to work with. One caveat however is that setting up your application to use OpenGL can be... kind of painful. The struggle comes from the fact that each GUI library handles the OpenGL rendering context slightly differently and some GUIs require various tricks [1]. Also initializing the viewport can be done in several different ways and getting it right (while trying to hack some code together) can also be painful, especially if you have to recompile every time you change something.

2   PyOpenGL

PyOpenGL, as the name implies, is the Pythonic OpenGL API. If you have OpenGL experience but have never used PyOpenGL you should take the time to read the PyOpenGL for OpenGL Programmers tutorial. Although you can pretty much write C OpenGL in Python the PyOpenGL package also provides a nicer more python oriented interface for the OGL API.

2.1   Advantages of PyOpenGL

NumPy arrays are natively supported [2], making manipulation of large data sets easy and fast.
OpenGL calls are wrapped with glGetError so you automatically get exceptions when things go wrong.
You can copy/paste code to and from C/C++ since most of the OpenGL API is the same, or a slightly pythonified version, as the C API. This makes porting code a breeze.
It's Python so No need to compile which means faster changes.
It's Open Source so it's getting better every day.
Contributing is easy since the APIs calls are not very tightly coupled and once you understand the basics of how PyOpenGL and ctypes work you can easily contribute to the project by providing wrappers and pythonifications [3] for OpenGL calls.
2.2   Disadvantages of PyOpenGL

The PyOpenGL API consists of auto generated wrapper code with hand written pythonifications, this makes some errors harder to understand.
Lesser used / known APIs are not wrapped as nicely making your code ugly (see Using GLSL with PyOpenGL).
If you don't initialize your buffers correctly python will segfault, but that's what would happen in C/C++ so I guess it's not a disadvantage.
It's easier to write slow applications in PyOpenGL. The reason being that Python is obviously slower then C when running loops and calling methods, so drawing using immediate mode (glBegin/glEnd) tends to be much slower than C (in my superficial tests). However using vertex arrays and being smart about your code will ensure that your performance is close to C/C++ code.
3   Tips

3.1   Use the Pythonic functions

A large portion of the PyOpenGL API has pythonic wrappers, try to use those functions instead of the ones you are used to in C, this will make your code cleaner and therefore easier to understand and debug. Look at PyOpenGL for OpenGL Programmers and the PyOpenGL doc pages to see exactly which calls are pythonic.

For example you can call glGenTexture with one argument, the number of texture IDs you want, and it will return either a single integer based texture id or a list of texture IDs. You can also call it the standard way, initializing an ID and providing it to the function.

Another example is you can call glVertexPointer the C way providing the necessary arguments or use the pythonic glVertexPointer[f|b|i|] set and only providing an array of the given type.

3.2   Zero is not NULL

Some OpenGL calls require a pointer to a data buffer, and sometimes you must call these functions with a NULL pointer. In C/C++ it is perfectly legal to do the following:

# 's
1glBindBuffer(GL_ARRAY_BUFFER, buffer)
2glVertexPointer(3, GL_FLOAT, 0, 0)
but in Python you have to do this:

# 's
1glBindBuffer(GL_ARRAY_BUFFER, buffer)
2glVertexPointer(3, GL_FLOAT, 0, None)
3.3   NumPy array data type

When creating NumPy arrays you don't normally have to specify the data type, it will automatically be inferred from the content. However on a 64bit machine NumPy seems to automatically make floats into float64s which are actually doubles. Surely you can already see the problem with this, you are telling OGL that you are giving it an array of 256 floats, but instead it gets 128 doubles... the result is something like this:

http://www.siafoo.net/image/37?w=300
That is supposed to be a solid cube, surrounded with a wireframe cube

Specifying the data type for a numpy array can be done using the dtype parameter to the array function:

# 's
1a = array([0.0, 0.5, 1.0], dtype=float32)
3.4   Generating Buffers

Sometimes you would need to generate some buffers, for example using the glGenBuffers VBO call or the old version of the glGenTextures [4] texture generation call.

In this case you must define the variable beforehand and initialize it to the correct type:

# 's
1buffer = 0
2glGenTextures(1, buffer)
3
4# Sometimes you need the exact data type like above:
5from OpenGL.raw import GL
6buffer = GL.GLuint(0)
7glGenBuffers(1, buffer)
3.5   Loading Image Textures

Although there are plenty of good imaging libraries for C/C++ I doubt that any of them are as easy to use as the Python Image Library (PIL). Although PIL's commercially licensed version has an OpenGL Image interface, with the free version in order to load an image as a texture you can do something like:

# 's
 1import Image
 2img = Image.open('some_img.png') # .jpg, .bmp, etc. also work
 3img_data = numpy.array(list(img.getdata()), numpy.int8)
 4
 5texture = glGenTextures(1)
 6glPixelStorei(GL_UNPACK_ALIGNMENT,1)
 7glBindTexture(GL_TEXTURE_2D, texture)
 8glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
 9glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
10glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
11glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
12glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
3.6   Geometry Rendering Performance

In general the fewer OpenGL calls you make, the better, true in C but even more so in Python. The performance hierarchy for drawing geometry in OpenGL is as follows (from slowest to fastest):

Immediate mode (glBegin/glEnd) - One of the strengths of OpenGL and one of the main reason OGL is so easy to learn, but it's also the slowest way of drawing primitives.
# 's
1# Somewhere before the drawing code
2circle = [[radius*math.sin(math.radians(deg)), radius*math.cos(math.radians(deg)), 0.0] for deg in xrange(360)]
3
4# In the drawing code
5glBegin(GL_LINE_STRIP)
6for pt in circle:
7    glVertex(pt)
8glEnd()
Vertex arrays - By precalculating vertex coordinates, color, normals and texture values and loading them into buffers you not only reduce the number of calls you make but you also allow the hardware to more efficiently transfer the data to the video card. The buffer data is still sent to the video card on every frame but this time in one giant block.
# 's
1glVertexPointerf(circle)
2glDrawArrays(GL_LINE_STRIP, 0, len(circle))
Interleaved Vertex Arrays - Same as vertex arrays, except that you can place multiple types of data inside one giant buffer and then render it all using the same glDrawArrays/glDrawElements calls as before. Create a buffer with the data then use glInterleavedArrays to prepare it for rendering.
Vertex Buffer Objects (VBOs) - The geometry equivalent of the texture objects, VBOs allow you to move the vertex, color, normal, texture data to the video card and render it when needed, without moving the data to the card on every render call. Depending on your application, VBOs can provide a huge performance boost... although their support in PyOpenGL is a bit rough. Making things a lot easier is Nathan Ostgard's VBO class
# 's
 1# Generate Buffers (inside Init method)
 2circle = array(circle, dtype=float32)
 3vertex_vbo = GL.GLuint(0)
 4glGenBuffers(1, vertex_vbo)
 5glBindBuffer(GL_ARRAY_BUFFER, circle)
 6glBufferData(GL_ARRAY_BUFFER, ADT.arrayByteCount(circle), ADT.voidDataPointer(circle), GL_STATIC_DRAW_ARB)
 7
 8# Draw buffers (inside Render method)
 9glBindBuffer(GL_ARRAY_BUFFER, vertex_vbo)
10glVertexPointer(3, GL_FLOAT, 0, None)
11glDrawArrays(GL_LINE_STRIP, 0, circle.shape[0])
3.7   row/column-major

NumPy by default uses row-major array order, just like C. OpenGL sort of expects/returns column-major arrays which means that you need to use the transpose of the modelview or whatever other matrices you are using. In fact when setting matrices for use by shader code using one of the glUniformMatrix* calls the third argument is whether the matrix should be transposed or not.

Example:

# 's
1# Get the modelview matrix and transform some vertices
2model_view = matrix(glGetFloatv(GL_MODELVIEW_MATRIX))
3vs = model_view.T*vertices
4
5# Save the 'old' model_view inside for use by a vertex/fragment shader
6glUniformMatrix4fv(glGetUniformLocation(program, "oldModelView"), 1, True, model_view)
Note

I am not too clear on this point but don't have the time right now to totally figure it out.

4   Random Errors

4.1   Type Errors

If you ever get strange errors about wrong types, try to manually coerce your data type into whatever type the API expects. Look in the OpenGL.raw package, there you will find all the proper OpenGL typedefs such as GLuint and GLfloat You can create a new variable with the correct type using something like this:

# 's
1from OpenGL.raw import GL as simple
2foo = simple.GLuint( 0 )
4.2   Random Exceptions

The PyOpenGL wrappers call glGetError automatically and throw exceptions when needed. However if you have defined some custom wrappers (see Using GLSL with PyOpenGL) you won't get automatic exception handling. The effect is that if one of your APIs generates an error you will get an exception the first time a proper PyOpenGL API is called. This should remind you of compiler errors from "back in the day" when the actual error is a hundred lines above the error message.

5   GUI Notes

Misc notes about building graphical user interfaces with Python that can use OpenGL

5.1   wxPython

wxPython is the Python API for the wxWidgets cross-platform GUI toolkit.

To use OpenGL in a wxPython application you can either subclass wx.glcanvas.GLCanvas or simply create an instance of the class and then bind the wx.EVT_PAINT to your drawing function.

Warning

By default double buffering is not enabled, which will most likely cause flicker. To enable double buffering pass attribList=[wx.glcanvas.WX_GL_DOUBLEBUFFER] to the GLCanvas constructor.

To further prevent flickering you can bind the erase background event to nothing, like: wx.EVT_ERASE_BACKGROUND(self, lambda e : None).

See Using OpenGL with wxPython for a rudimentary example of wxPython + PyOpenGL

5.2   PyGTK

?

5.3   PyQT

http://wiki.python.org/moin/PyQt

5.4   GLUT

The OpenGL Utility Toolkit is probably the easiest GUI framework to learn and setup, resulting in fastest application development time. However it is also very simple and is not suitable for building large scale GUIs.

Note

If you plan on developing serious GUI based applications, with or without OpenGL, you should invest some time in learning a proper GUI toolkit.

PyOpenGL seems to provide GLUT bindings in the OpenGL.GLUT package.

6   Conclusion

PyOpenGL is not perfect but it's nonetheless a fantastic framework for developing 3D applications, prototyping OpenGL code, or playing with shaders (or other OGL features). Vastly increasing it's RAD capabilities is the fact that PyOpenGL integrates well with the SciPy/NumPy numerical processing library allowing you to develop algorithms and process data with much less code than C or FORTRAN but with very similar performance [5] and then render the data in OpenGL.

Although the title of this article implies that all PyOpenGL is good for is prototyping, that is not true. You can write full blown applications with PyOpenGL combined with pretty much any GUI toolkit you choose.

As a side note, feel free to add more tips, tricks and hacks pertaining to PyOpenGL to this article.

7   Footnotes

[1]	For example the wxGLCanvas object from wxWidgets should have it's erase background background event overriden with an empty body to prevent flickering. I am fairly certain this is true for the Win32 API as well.
[2]	NumPy is supported in most of the API, but if you run into problems you can always use the numpy.array.ctypes.data method or the OpenGL.arrays.ArrayDatatype class in order to extract the data and manually pass it to the call.
[3]	Yes, I am making up words.
[4]	glGenTextures is actually pythonic, you only need to provide one argument specifying how many textures you want and either an integer id or a list of texture ids will be returned
[5]	NumPy is a set of FORTRAN and C libraries with Python wrappers. If you use the library correctly and avoid Python loops (which you can in most cases) your NumPy code performs most of it's heavy computation inside the Fortran or C libraries resulting in lighting fast speed.
```
