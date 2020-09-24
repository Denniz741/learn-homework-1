"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
list_scores = [{'school_class': "4a", 'scores': [3,4,4,5,2,3,4,4]},\
      {'school_class': '4б', 'scores': [4,5,4,4,3,3,4,5]},\
            {'school_class': '4в', 'scores': [3,4,4,5,3,2,5]}]  

def main(list_scores):
      sum_scores_sch = 0  #сумма баллов по школе  
      n_rat_class = 0     # количество баллов по школе  
      sch_avg = 0          # средний балл по школе  
      class_name = 0
         
      
      for s in list_scores:
              
              sum_scores_sch += sum(s.get('scores'))
              n_rat_class  += len(s.get('scores'))
              sch_avg = round((sum_scores_sch / n_rat_class),2) 
              class_name = s.get('school_class')
              class_avg = sum(s.get('scores'))/len(s.get('scores'))
              print(f'Класс {class_name} средний балл {round(class_avg, 2)}')
      print(f'Средний балл по школе равен {sch_avg}')
      return round(sch_avg, 2)
  
     
if __name__ == "__main__":
     main(list_scores)




    #"""
    #Эта функция вызывается автоматически при запуске скрипта в консоли
    #В ней надо заменить pass на ваш код
   # """
   
    

 
