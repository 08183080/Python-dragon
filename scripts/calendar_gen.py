""""
我一开始文件命名为calendar.py
结果报错 
https://stackoverflow.com/questions/67472180/an-error-appears-while-writing-a-calendar-programtypeerror-int-object-is-not

you cant have your python file have the same name as any module!
"""


import calendar

year = int(input("请输入当前年份: "))
month = int(input("请输入当前月份: "))

print(calendar.month(year, month))
input("请按任意键结束...")