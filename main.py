dict1 = {"a1": "a2", 
         "a3": 
            {"b1" : "b2", 
             "b3" : "b4", 
             "b5" : { "c1" : "c2" 
                     , "c3" : {"d4" : "d5"}}}}

def dictionary_loop(dict1, level = 1):
 
  for i in dict1:
    if isinstance(dict1[i], dict):
      level+=1
      dictionary_loop(dict1[i], level )

  return level
      
      


level = dictionary_loop(dict1, 0)

