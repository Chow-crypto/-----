# @Author : 大海
# @File : common.py
from conf import setting
from core import src
import time
# 十二
# 日志写入数据方法
def log(msg):
    current_time = time.strftime('%Y-%m-%d %X')
    with open(setting.LOG1_path,'a',encoding='utf-8')as f:
        f.write(current_time+ '-'*5 + msg+'\n')


def login_intter(func):
    '''
    func就是它们
    '3':check_balance,
    '4':transfer,
    '5':repay,
    '6':withdraw,
    '7':check_record,
    '8':shopping,
    '9':look_shoppingcart,
    '10':loginout,
    都要在登录的情况下才能执行
    全部都写一个登录装饰器
    公用的在commin里面写
    '''
    def wrapper():
        if not src.user_data['is_auth']:
            src.login()
        else:
            # 这里的func指的是被装饰的函数
            func()
    return wrapper