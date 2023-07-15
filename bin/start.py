# @Author : 大海
# @File : start.py

#   python   90%编程能力     40分钟 敲出来  反应能力 逻辑思维
#   不分屏    盲拧魔方
#   脑袋里面 有一个个格子
#   一个个分解      思考   一个个攻破
#   恶性循环     失眠   》》》   太疲劳   》》》 喝咖啡
#            负面    》》》   疲劳心累   》》》   打牌 喝酒
#   良性循环     早起   》》》   锻炼    》》》  效率高
#            被老师表扬  》》》 更加认真学习  》》》 考上好学校
#             成就感   》》》  敲代码   》》》  专研
#    一下   砖石   》》》  打游戏   》》》  又升级了   短期 一下看到效果
#    学习一门技术      滞后的效果     脱胎换骨   7年   所有的细胞更新一遍
#    早起     7年后身体健康
#    分开  好简单
#    板砖思维     一个事情   直接一定可以搞定
#    风控思维     老板       知道行业的风向
#    分解开
#    仪式主义   打开电脑
#    一上来     英雄联盟   5小时
#    pycharm    2小时     研究
#    去了健身房
# https://www.processon.com/diagrams
# 流程图
import sys
import os
print(os.path.dirname(__file__))
Source_path = os.path.dirname(os.path.dirname(__file__))
# D:/shoping_cart_A7
print(Source_path)

sys.path.append(Source_path)
print(sys.path)

from core import src
# 设置成主程序run
if __name__ == '__main__':
    src.run()

