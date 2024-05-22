## За что не снимал баллы
1. Качество кода
2. Скорость работы
3. Какие-то странные штуки: решение не в функции, а просто само по себе; кто-то в функциях возвращает print.


## Комментарии по задачам
Task1&2: Кто решил через сортировку и одно сравнение - молодцы. Кто решил через вложенные циклы - тоже молодцы, но чуть меньше.

Task3: функция должна возвращать `bool`, в одной работе увидел, что зачем-то стоит `return print(True)`, не очень корректно, но ок, балы за это не снизил.

Task4: задача не очень хорошо сформулирована, я указал конкретный список гласных, но не указал что делать с `А` и `а`. Так что все кто привел в `lowercase` это правильно, и те кто не привел, тоже правильно, даже если искали только маленькие буквы.

Task5: много кто зачем-то удалял пробелы, если честно я не очень понял зачем... У меня есть два вопроса: 1) Зачем удалять пробелы, чем они вас так сильно смущают, я не очень понял. Любой символ здесь ок, пробелы цифры, знаки препинания тоже могут быть частью строки. Из Википедии: `Палиндро́м (от др.-греч. πάλιν — «назад, снова» и др.-греч. δρóμος — «бег, движение»), пе́ревертень[1] — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях.` 2) Задач на палиндромы три и если правильно убирать пробелы в первой, то в последующих вы их обычно не убирали, т.е. если правильно решение Task5, то тогда Task6 и Task7 (если в них не убирали пробелы) - не очень корректное.

Task6: видел косяк, где все же вызывается функция от Task5, но опять же некорректно считает пробелы, т.е. для `aa a` выдает 4.

Task8: косяк в расчете моды, в условии было указано, что `в случае если два и более объекта встречаются одинаковое количество раз модой будет наибольший из них`, т.е. для `[1,1,2,2]` ответ - 2, а не 1. Снял за это пол балла, хотя по факту это единственное условие в задаче.