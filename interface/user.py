# @Author : 大海
# @File : user.py

from db.db_handle import db_serialization
from lib import common
# 五
# 写一个查询用户信息的接口
def get_userinfo_by_name(name):
    '''
        写一个查询用户信息的接口
        :param name:
        :return:
        '''
    # 这里需要用到一个db 下面的 db_handle 数据管理的方法在这个文件夹下
    # 这里需要返回用户信息   ？？？
    return db_serialization.select(name)

# 九
def register_user(name,password,balance=15000):
    '''
        注册用户接口
        :param name:
        :param password:
        :param balance:
        :return:
        '''
    # 信息传入定义的字典
    user_dic = {'name': name, 'password': password, 'locked': False, 'account': balance, 'shopping_cart': {},
                'bankflow': []}
    # 这个字典到时候会存储成json文件
    # 需要通过谁写入    ？？？
    # db包  db_handle模块 的 db_serialization 对象的方法
    # db_serialization
    db_serialization.update(user_dic)
    print('%s 注册了' % name)
    # 十一
    # 存储一个日志
    # 日志是公用的 在lib 文件夹 commin 写方法 数据存储到 log 文件夹里面
    # 需要添加log 下面日志文件的路径到 setting 里面
    common.log('%s注册了' % name)

def lock_user(name):
    '''
    锁定用户接口
    :param name:
    :return:
    '''
    # 拿到注册用户的字典信息
    user_dic=db_serialization.select(name)
    # 锁定改成True
    user_dic['locked'] = True
    # 重新写入字典信息
    db_serialization.update(user_dic)
    print('密码输入错误3次锁定5秒,请5秒后再登录')
    print('已被锁定')
    # 记录日志
    common.log('已被锁定')

def unlock_user(name):
    '''
        解锁用户接口
        :param name:
        :return:
        '''
    # 拿到注册用户的字典信息
    user_dic = db_serialization.select(name)
    # 锁定改成True
    user_dic['locked'] = False
    # 重新写入字典信息
    db_serialization.update(user_dic)
    print('已经解锁')
    # 记录日志
    common.log('已经解锁')



