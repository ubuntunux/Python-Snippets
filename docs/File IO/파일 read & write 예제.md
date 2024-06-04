[CONTENTS](README.md)
## 파일 read & write 예제

파일 불러오기

    f = open("filename.txt", "r")
    text = f.read()
    f.close()
    
파일 저장하기

    f = open("filename.txt", "w")
    f.write("Hello world.")
    f.close()
    
binary 파일 불러오기 ( https://docs.python.org/3/library/struct.html )

    import struct

    f = open("filename.txt", "rb")
    text = f.read(4)  # read 4 bytes
    data = struct.unpack("i", text)  # cover to 4 byte int
    f.close()