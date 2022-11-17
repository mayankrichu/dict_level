'''
example
'''
dict1 = { 
         "a3": 
            {"b1" : "b2", 
             "b3" : "b4", 
             "b5" : { "c1" : "c2" , "c3" : {"d4" : "d5", "d6" : {"e7" : "e8"}}}}, "a1": "a2"}

d = {1:
     {'name':'x', 'age':24, 
      'address':{'country':'zzz', 'zip':12345}}, 
     2:{'name':'y', 'age':21, 'address':{'country':'yyy', 'zip':54321}}, 3:{'name':'z', 'age':25}}

def dictionary_loop(dict1, level = 1):
  global level1 
  level1 = level
  print(dict1)
  for i in dict1:
    if isinstance(dict1[i], dict):
      level+=1
      dictionary_loop(dict1[i], level)
      

  #print(level)
  return level1
      
      
level1 = dictionary_loop(dict1)
print(level1)
