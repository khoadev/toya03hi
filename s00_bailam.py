#region debai
"""
--- ma debai / id
hi(name)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/toya03hi

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/uYheiLdfy6K8LVQj6

--- debai / problem
Khi chay voi input           | Ketqua output
---------------------------- | -----------------
hi(name='Mom')               | Hi Mom!
hi('Mom')                    | Hi Mom!
hi('')                       | Hi!
hi()                         | Hi!
hi(None)                     | Hi!

------------------- mucdo: kho -----------------
hi('Mom', 'Dad')             | Hi Mom, and Dad!
hi('A', 'B', 'C')            | Hi A, B, and C!
hi('1', '22', '333', '4444') | Hi 1, 22, 333 and 4444!
"""
#endregion debai

#region bailam
def hi(name=None,*args):

  if name == None or name == '':
    return f'Hi!'
  if len(args) == 0:
    return f'Hi {name}!'
  else:
    strname = f'{name}, '
    for i,n in enumerate(args):
      if i == len(args)-1:
        strname += f'and {n}'
      else:
        strname += f'{n}, '
    return f'Hi {strname}!'


print(hi(name='Mom'))
print(hi('Mom'))
print(hi(''))
print(hi())
print(hi(None))
print(hi('Mom', 'Dad'))
print(hi('A', 'B', 'C'))
print(hi('1', '22', '333', '4444'))
#endregion bailam

