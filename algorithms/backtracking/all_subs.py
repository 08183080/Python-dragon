"""
获取字符串的所有子字符串
"""
from __future__ import annotations

from typing import Any


def generate_all_subsequences(sequence: list[Any]) -> None:
    create_state_space_tree(sequence, [], 0)


def create_state_space_tree(
    sequence: list[Any], current_subsequence: list[Any], index: int
) -> None:
    """
    Creates a state space tree to iterate through each branch using DFS.
    We know that each state has exactly two children.
    It terminates when it reaches the end of the given sequence.
    使用DFS迭代每一个分支, 创建一个状态空间树
    对于每一个状态都有两个儿子
    """
    if index == len(sequence):
        print(current_subsequence)
        return

    """
              1o
            //  \\
           2o     3o
        回溯过程:
        (1) 1o -> 2o, 添加下一层的左节点, 递归
        (2) 2o -> 1o, 回溯
        (3) 1o -> 3o, 添加下一层的右节点, 递归
    """
    current_subsequence.append(sequence[index]) # 增加下一层的结点      ->      1
    create_state_space_tree(sequence, current_subsequence, index + 1) # 访问下一层
    current_subsequence.pop() # 切换下一层的空节点
    create_state_space_tree(sequence, current_subsequence, index + 1)  # 再访问下一层   ->  0
    

if __name__ == "__main__":
    seq: list[Any] = [3, 1, 2, 4]
    generate_all_subsequences(seq)

    # seq.clear()
    # seq.extend(["A", "B", "C"])
    # generate_all_subsequences(seq)