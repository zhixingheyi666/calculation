#_*_coding:utf-8_*_

__author__ = 'Master Wang'

import sys

sysFc = 'D:\\python_learn\\sysFc'
sys.path.append(sysFc)

from logSf10 import crLog

logger = crLog(fname='D:\桌面\isbn.log')
# logger = crLog(fname = 'D:\桌面\handlers.log')
logger.info('Succeed')

# 引入数据库连接
from connSql import mkcon

cursor, mkconn = mkcon('my', database='temp')


if __name__ == '__main__':
    print('Test')


