# @Author : 大海
# @File : setting.py

import os
print(os.path.dirname(__file__))
Source_path = os.path.dirname(os.path.dirname(__file__))
# D:/shoping_cart_A7
print(Source_path)

DB_path = os.path.join(Source_path,'db')
print(DB_path)

# D:/shoping_cart_A7\db

LOG1_path = os.path.join(Source_path,'log','user1.log')

print(LOG1_path)

# D:/shoping_cart_A7\log\user1.log
