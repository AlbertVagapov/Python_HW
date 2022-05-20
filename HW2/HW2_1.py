# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

Text = "арбуз крокодил канат абвешка обруч абв"
Text = Text.split(' ')
print(Text)

T = ''
for word in Text:
    if word.find('абв') == -1:
        T += word + ' '
print(T)