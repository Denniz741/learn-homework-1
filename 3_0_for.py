a = [{'school_class': "4a", 'scores': [3,4,4,5,2,3,4,4]},\
   {'school_class': '4б', 'scores': [4,5,4,4,3,3,4,5]},\
     {'school_class': '4в', 'scores': [3,4,4,5,3,2,5]}]  

l = 0
z = 0
avg = 0
for s in a:
      z += sum(s.get('scores'))
      l += len(s.get('scores'))
      avg = z / l
      z1 = s.get('school_class')
      q = sum(s.get('scores'))/len(s.get('scores')) 
      print(z1, round(q, 2))
print('Средний балл по школе ',round(avg,2))  





       

    
