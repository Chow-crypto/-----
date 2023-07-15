# @Author : 大海
# @File : db_handle.py

# 六.注册的用户信息保存成序列化json文件
# 思路
# 1.路径
# 2.有json模块,存储成序列化文件

import os
import json
from conf import setting
class Serialization:
    def select(self,name):
        # 读取一个文件信息，我们需要什么？
        # 1.需要文件路径
        # 思路
        # 我们可以通过json文件名进行查询，
        # 如果查到文件存在，说明已经注册了，
        # 不存在，代表没注册
        # 路径写道setting里面  ？？？
        # D:/shoping_cart_A7\db/李老师.json
        path = r'%s/%s.json'%(setting.DB_path,name)
        # 有李老师.json这个json文件就返回，没有就返回False
        # 返回给谁  bank shop user 这个三个接口 都可能用的上
        if os.path.isfile(path):
            with open(path,'r',encoding='utf-8')as f:
                # 对序列化json文件操作load
                return json.load(f)
        else:
            return False

        # 十
    def update(self, user_dic):
        # D:\shoping_cart_A7    db
        path_file = os.path.join(setting.Source_path,'db','%s.json'%user_dic['name'])
        # 注册是利用json文件名注册  数据写入文件
        with open(path_file,'w',encoding='utf-8')as f:
            json.dump(user_dic,f)
            f.flush()

db_serialization=Serialization()


