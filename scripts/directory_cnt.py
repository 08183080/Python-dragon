"""
2023/9/22
统计文件夹中的所有文件大小
并按照各种条件排序
"""
import os

"""
打印输出所有文件
"""
def get_all(path):
    files = os.listdir(path)
    for file in files:
        print(file)
        
"""
获取文件夹的大小
"""
def get_size(path):
    cnt = 0
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            cnt += os.path.getsize(file_path)
        # 若里面有子文件夹则递归子文件夹进行统计
        elif os.path.isdir(file_path):
            cnt += get_size(file_path)
    return cnt

"""
文件排序有哪些?
1. 文件大小
2. 文件创建时间
3. 文件修改时间
4. 文件名

"""


"""
按照文件名进行排序(字符串排序)
"""
def sort_by_name(path):
    files = os.listdir(path)
    sorted(files)
    # print(files)
    for file in files:
        print(file)

"""
按照数字排序
针对于img_xxx这样的情况
"""


# path = "."
# get_all(path)
# print(get_size(path))
# sort_by_name(path)

path = input("请输入你想要查询的文件夹:")
# print("文件夹下的所有数据如下:")
# get_all(path)
print("文件夹内所有文件按照字典序排序:")
sort_by_name(path)
print(f"文件夹内所有文件以及子文件的大小总和: {get_size(path)}字节")
input("后续支持其他排序方式,请按任意键退出...")