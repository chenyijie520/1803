id_card = {'name':'陈怡杰','age':17,'sex':'女','group':'汉'}

print(id_card)

id_card['address'] = '北京市'
id_card['merry'] = '是'
id_card.setdefault('age',17)
id_card.setdefault('height',156)
print(id_card)

id_card.pop('merry')
id_card.popitem()



id_card['name']7

