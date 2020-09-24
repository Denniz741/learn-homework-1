"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


q = {'Как дела?': 'Хорошо','Что делаешь?': \
  "Программирую", "Как пройти в библиотеку?": \
    "В какую библиотеку ?", "Где ты живёшь?":"В Омске."} 
while True:
  try:
    a = input('Задайте мне вопрос.   ')
    
    def ask_user(q,a):
        while True:
              a == q.keys()
              for s in q:
                  if a == s:
                      return(q[s])
                  
                        
    print(ask_user(q,a))
          
  except KeyboardInterrupt:
                  print('Пока!')
                  break
                                                

if __name__ == "__main__":
  ask_user(q,a)