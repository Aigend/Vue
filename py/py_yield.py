# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : leetcode
# @File    : py_yield.py
# @Date    : 2022/09/18:21:06
# @Author  : jinwenlong@oppo.com
# deom4
import time
import asyncio


async def add_clothes():
    print('往洗衣机添加衣服....')
    await asyncio.sleep(2)       # 模拟这个任务耗时2秒


async def washing1():
    print('洗衣机工作之前，需加衣服进去')
    await add_clothes()  # 等待这个事情完成
    print('衣服加进去，可以开始工作了。。。。')
    await asyncio.sleep(3)  # 模拟洗衣机工作的耗时
    print('washer1 finished')  # 洗完了

# 2. 将异步函数加入事件队列
tasks = [
    washing1(),
    # washing1()
]


if __name__ == '__main__':
    # 1. 创建一个事件循环
    loop = asyncio.get_event_loop()
    startTime = time.time()
    # 3.执行队列实践，直到最晚的一个事件被处理完毕后结束
    loop.run_until_complete(asyncio.wait(tasks))
    # 4.如果不在使用loop，建议使用关闭，类似操作文件的close()函数
    loop.close()
    endTime = time.time()
    print("洗完三批衣服共耗时: ",endTime-startTime)





