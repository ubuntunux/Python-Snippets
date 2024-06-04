> [Python Snippets](../README.md) / [알고리즘](README.md) / Quine - 자신의 소스코드를 출력하는 프로그램.md
## Quine - 자신의 소스코드를 출력하는 프로그램

    >>> s = 's = %r;print(s%%s)';print(s%s)
    s = 's = %r;print(s%%s)';print(s%s)