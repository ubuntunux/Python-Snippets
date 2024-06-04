[CONTENTS](README.md)
## 코드 추적하기 ( TraceCallStack )
현재 실행중인 소스코드의 파일이름, 라인넘버등을 출력하는 방법입니다.

    import os
    import re
    import traceback    
    
    
    #
    # UTIL : call stack function for log
    #
    reTraceStack = re.compile("File \"(.+?)\", line (\d+?), .+")  # [0] filename, [1] line number
    
    
    def getTraceCallStack():
        for line in traceback.format_stack()[::-1]:
            m = re.match(reTraceStack, line.strip())
            if m:
                filename = m.groups()[0]
                # ignore case
                if filename == __file__:
                    continue
                filename = os.path.split(filename)[1]
                lineNumber = m.groups()[1]
                return "[%s:%s]" % (filename, lineNumber)
        return ""