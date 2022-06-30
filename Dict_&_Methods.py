'''Dictonary is the combination of keys and value parirs,it represents with {},
in dict we have to continue the key:values in dict using (,) at the end of the dict that's optional to use (,)  '''

# a={1:'hii',2:'hello',3:'python'}
# print(a[1]) # 'hii'
# print(a[2]) # 'hello'
# print(a[3]) # 'python'
# print(a[4]) # KeyError (if the value is not there it will show the keyerror)

'''in dictonary all data types are included,wecan add one more dict inside it '''
# a={1:1,2:5.6,3:'ef',4:[3,4],5:(1,2),6:{1,2},7:{4:5}}
# print(a[1],type(a[1])) # 1 int
# print(a[2],type(a[2])) # 5.6 float
# print(a[3],type(a[3])) # ef str
# print(a[4],type(a[4])) # [3,4] list


'''Dictonary methods-11'''
# a={1:'abc',2:'def',3:'efg'}
# a.clear()
# print(a) # {} (if the dictonary will be clear it will show the value as {})

# a={1:'xyz',2:'abc'}
# a.copy()
# print(a) # {1: 'xyz', 2: 'abc'}

# a={10,20,30,40}
# print(dict.fromkeys(a,5)) # {40: 5, 10: 5, 20: 5, 30: 5} ( it will give the values to every key)

# a={1:'ab',2:'cd',3:'ef',4:'gh',}
# print(a.get(3)) # ef 
# print(a.get(5)) # none

# a={1:'ab',2:'cd',3:'ef',4:'gh',}
# print(a.items()) # ([(1, 'ab'), (2, 'cd'), (3, 'ef'), (4, 'gh')])

# a={1: 'hii',2:4.3,3:[1,2]}
# print(a.keys()) # ([1, 2, 3])

'''it will not take the empty pop(),we have to give the value which we want to poped out '''
# a={1:'ab',2:'cd',3:'ef'}
# a.pop(2) 
# # print(a) # # {1:'ab',3:'ef'}
# a.pop(4)
# print(a) # keyerror (if the value is not there indict it will shoe the keyerror)
# a.popitem()
# print(a) # {1: 'ab', 2: 'cd'} (in popitems it will poped out the last key:value)

'''we can update and add the value'''
# a={1:'niha',2:'rika',3:'abc'}
# a.update({2:'hii'})
# print(a) # {1: 'niha', 2: 'hii', 3: 'abc'}
# a.update({5:'abc'})
# print(a) # {1: 'niha', 2: 'rika', 3: 'abc', 5: 'abc'}

'''in setdefault we can not update the value but we can add thevalue to dict'''
# a={1:'niharika',2:'pravalika',3:'python'}
# a.setdefault(2,'hello')
# print(a) # {1:'niharika',2:'pravalika',3:'python'}
# a.setdefault(4,'hii')
# print(a) # {1:'niharika',2:'pravalika',3:'python,4:'hii'}

# a={1:'xyz',2:'abc',3:'efg'}
# print(a.values()) # (['xyz', 'abc', 'efg'])