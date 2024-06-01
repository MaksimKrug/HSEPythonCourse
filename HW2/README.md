# Домашка 2

## Что хотим
Необходимо сделать ноутбук (collab норм) с анализом данных и предсказанием какого-то таргета (опционально). Вам необходимо поделиться на группы по 1-2 человека, найти какой-то датасет (я бы искал на [kaggle](https://www.kaggle.com/datasets)) и провести его анализ. Если хотите балл повыше, то надо будет еще предсказать какой-то таргет. Результаты надо будет представить лично или в дискорде (или еще как-то, это обсуждаемо).

### Где записаться
[Вот тут лежит табличка](https://docs.google.com/spreadsheets/d/1mnt6ZVVhUmW9LSc3U5JZ4_HFV3iVxXSmMh9hpRG8fI8/edit?pli=1#gid=60225690), в которую записываться. Указывается свои данные, ссылку на датасет. Если делайте вдвоем, то второй человек может не указывать ссылку на дасете а написать с кем он делает, так будет проще понять кому надо датасет подтвердить, а кому нет. Если берет какие-то свои данные, то скиньте мне их или как-то покажите, чтобы я могу понять что они подходят. Если с датасетом все ок, я напишу это в колонке `Датасет чек`, если есть какие-то проблемы, то тоже отпишу.

### Требования к датасету
В целом, вы можете брать любой датасет, который захотите, но к нему есть требования:
1. Табличные данные - если хотите делать семантический анализ текста или предсказывать где на картинке котик, это хорошо, но не для нашего курса. Данные должны представлять собой табличку, в которой есть какие-то признаки, которые вы можете выразить числом. Если в данных есть, например, имена - это ок, просто вы не должны пытаться по ним предсказать выжил пассажир или нет.
2. Признаки - должно быть хотя бы 5, и они не должны все относиться к одной категории, т.е. взять датасет где одни `float` нельзя. В целом, если признаки только категориальные, может и ок - скиньте датасет и я посмотрю.
3. Таргет - напишите что вы хоите предсказывать и зачем вообще вам этот датасет. Например, в датасете `titanic`, мы хотим предсказать выжил ли пассажир, а может класс каюты или возраст, т.е. можете выбрать что хотите, главное обоснуйте почему.
4. Описание признаков - не забудьте его добавить, иначе если я спрошу что это за колонка, а вы не сможете ответить, будет не очень комфортненько.

## Система оценивания
Основной критерий - вам надо рассказать о датасете и что вы делали с признаками. Вам надо эти признаки визуализировать и расписать какие-то выводы, т.е. просто гора графиков - не очень, гора графиков без подписей - совсем не очень.
Примерные критерии такие:
4-5 баллов - что-то сделали, но совсем грустно, выводы невнятные, графики не подписаны;
6-7 баллов - все ок, но есть косяки в логике;
8 баллов - все хорошо, с EDA вы справились;
9-10 баллов - еще и моделек накинули, правильно для них данные подготовили и т.д., здесь буду чуть сильнее придираться.

Критерии совсем примерные, на месте посмотрим что вы сделайте, но ориентируетесь на референс, который я покажу на паре (ноутбук есть в `Lectures`). Если есть какие-то вопросы - спросите, только что-то конкретное (типо надо ли нормализовать бинарный признак).

## Сроки
Крайний срок - последняя пара, дальше можно будет донести, но уже онлайн и не факт, так что постарайтесь не затягивать. На защите домашки может приходить один человек, оценка все равно будет у обоих одинаковой. Постарайтесь сохранить все аутпуты вашего ноутбука, т.к. на паре мы скорее всего не будем его запускать, т.е. приносить с собой данные не надо.