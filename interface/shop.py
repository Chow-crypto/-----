# @Author : 大海
# @File : shop.py

from interface import bank
from interface import user
from db.db_handle import db_serialization

from lib import common
# 三十一
def shopping_interface(name, shopping_cart, cost_money):
    '''
        购物接口
        :param name:
        :param shopping_cart:
        :param cost_money:
        :return:
        '''
    # 三十二
    # 需要消费进行扣款，那么这个应该和银行打交道 调用 bank 接口去做这件事情
    # 这个银行的接口要判断我的钱是否大于花费的钱
    if bank.consum_interface(name, cost_money):
        # 保存购物车
        # 查询用户json字典
        user_dic = user.get_userinfo_by_name(name)
        user_dic['shopping_cart'] = shopping_cart
        # 更新用户json字典
        db_serialization.update(user_dic)
        common.log('%s 花费 %s 购买了 %s' % (name, cost_money, shopping_cart))
        print('%s 花费 %s 购买了 %s' % (name, cost_money, shopping_cart))
        return True


    else:
        return False

def check_shoppingcart(name):
    '''
        查看购物车
        :param name:
        :return:
        '''
    # 查询用户json字典
    user_dic = user.get_userinfo_by_name(name)
    print('%s 查看了购物车' % name)
    common.log('%s 查看了购物车' % name)
    return user_dic['shopping_cart']





