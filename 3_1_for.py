a = [{'school_class': "4a", 'scores': [3,4,4,5,2,3,4,4]},\
   {'school_class': '4б', 'scores': [4,5,4,4,3,3,4,5]},\
     {'school_class': '4в', 'scores': [3,4,4,5,3,2,5]}]

  
for s in a:
    avg = 0
    z1 = 0
    q = 0
    def main(a):
        
        z += sum(s.get('scores'))
        l += len(s.get('scores'))
        avg = z / l
        z1 = s.get('school_class')
        q = sum(s.get('scores'))/len(s.get('scores'))
        return z1, q ,avg
    print(z1, q)
    print(avg)