#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family.append('отец')
my_family.append('мать')
my_family.append('сын')

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
]
my_family_height.append(['отец',176])
my_family_height.append(['мать',156])
my_family_height.append(['сын',175])
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print(my_family_height)
print("Рост отца -",my_family_height[0][1],'см')