```
# person dictionary 만드는 방법 1
>>> person = {'name': 'smith', 'age': 23}

# person dictionary 만드는 방법 2. 이 방법이 더 직관적일때도 있다.
>>> person = dict( name='smith', age=23 )

# person dictionary에서 데이터 읽어오기
>>> person['name'] 
'smith'

# 'gender'라는 key가 등록되어 있지 않으므로 에러가 발생한다. 
>>> person['gender']
KetError : 'gender'

# key가 있는지 없는지 모를 경우 if문을 사용하여 에러는 발생하지 않도록 할수 있다.
>>> person['gender'] if 'gender' in person else "I don't know."
'I don't know.'

# 위와 같은 동작을 더 간단하게 해보자. 'gender'라는 key가 없으면 지정해준 'I don't know.'를 출력한다.
>>> person.get('gender', 'I don't know.')
'I don't know.'
```
