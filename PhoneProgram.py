
import Cellphone_Class as cc


manufact = 'Apple'
model = 'iPhone X'
price = 1000

phone = cc.Phone(manufact,model,price)

print('The phone manufacturer is', phone.get_manufact())
print("The phone's model is", phone.get_model())
print("The phone's retail price is", phone.get_price())

manufact = input('Enter phone manfacturer: ')
model = input('Enter phone model number: ')
price = input('Enter phone retail price: ')

phone.set_manufact(manufact)
phone.set_model(model)
phone.set_retail_price(price)

print('The phone manufacturer is', phone.get_manufact())
print("The phone's model is", phone.get_model())
print("The phone's retail price is", phone.get_price())

   