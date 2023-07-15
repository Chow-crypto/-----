# @Author : 大海
# @File : bank.py
from  lib import common
from  interface import user

from db.db_handle import db_serialization
def check_balance_interface(name):
    '''
        查看余额接口
        :param name:
        :return:
        '''
    print('%s 查看了余额' % (name))
    common.log('%s 查看了余额' % name)
    # 思考逻辑 ， 后面代码不用管了 一条龙服务
    user_dic = user.get_userinfo_by_name(name)
    return user_dic['account']

def transfer_interface(from_name, to_name, account):
    '''
        转账接口输入自己name,别人name,和钱
        :param from_name:
        :param to_name:
        :param account:
        :return:
        '''
    from_user_dic = user.get_userinfo_by_name(from_name)
    to_user_dic = user.get_userinfo_by_name(to_name)
    if from_user_dic['account'] >= account:  # 比较自己的钱和需要转入的钱
        from_user_dic['account'] -= account  # 自己的钱减
        to_user_dic['account'] += account  # 别人的钱加
        # 记录
        from_user_dic['bankflow'].extend(['%s 转账 %s 元 给  %s'%(from_name, account, to_name)])
        to_user_dic['bankflow'].extend(['%s 收到 %s 转账 %s'%(to_name, account, from_name)])
        # 写入json 更新用户转账数据
        # 十九
        db_serialization.update(from_user_dic)
        db_serialization.update(to_user_dic)
        common.log('%s 收到 %s 转账 %s' % (to_name, account, to_name))
        print('%s 向 %s 转账 %s' % (from_name, to_name, account))
    else:
        print('转账钱不够')


def repay_interface(name, account):
    '''
        存款接口
        :param name:
        :param account:
        :return:
        '''
    # # 查询json用户获取用户字典
    user_dic=db_serialization.select(name)
    # 用户字典余额减去存款金额
    user_dic['account'] += account
    user_dic['bankflow'].append('%s 转入 %s 元' % (name, account))
    # # 写入json 更新用户存款数据
    db_serialization.update(user_dic)
    print('%s存款了%s' % (name, account))
    common.log('%s存款了%s' % (name, account))

# 二十五
def withdraw_interface(name, account):
    '''
    取款接口
    :param name:
    :param account:
    :return:
    '''
    # # 查询json用户获取用户字典
    user_dic = db_serialization.select(name)
    # 用户字典余额减去取款金额
    user_dic['account'] -= account
    user_dic['bankflow'].append('%s 取出 %s 元' % (name, account))
    # # 写入json 更新用户还款数据
    db_serialization.update(user_dic)
    print('%s取了%s' % (name, account))
    common.log('%s取了%s' % (name, account))


def check_bankflow_interface(name):
    '''
        银行流水接口
        :param name:
        :return:
        '''
    user_dic = db_serialization.select(name)
    common.log('%s 查看银行流水' % name)
    return user_dic['bankflow']

# 三十三
def consum_interface(name, account):
    '''
    消费接口
    :param name:
    :param account:
    :return:
    '''
    # 查询用户json字典
    user_dic = user.get_userinfo_by_name(name)
    if user_dic['account'] >= account:
        user_dic['account'] -= account
        # 添加到bankflow列表里面记录流水
        user_dic['bankflow'].extend(['%s 消费了 %s 元钱' % (name, account)])
        db_serialization.update(user_dic)
        common.log('%s 消费了 %s 元钱' % (name, account))
        print(('%s 消费 %s 元' % (name, account)))
        return True
    else:
        return False













