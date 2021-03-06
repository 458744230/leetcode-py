from typing import *
import time


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k = k % (m * n)
        if k == 0:
            return grid
        reshaped = []
        for row in grid:
            for item in row:
                reshaped.append(item)
        pos = m * n - k
        r = reshaped[pos:] + reshaped[:pos]
        for i in range(m):
            for j in range(n):
                grid[i][j] = r[i * n + j]
        return grid

    def maxSumDivThree(self, nums: List[int]) -> int:
        grouped = [[], [], []]
        for item in nums:
            grouped[item % 3].append(item)
        l1 = len(grouped[1])
        l2 = len(grouped[2])
        total = sum(nums)
        if total % 3 == 0:
            return total
        grouped[1].sort()
        grouped[2].sort()
        if total % 3 == 1:
            if l1 > 0:
                s1 = grouped[1][0]
            else:
                s1 = 100000
            if l2 > 1:
                s2 = grouped[2][0] + grouped[2][1]
            else:
                s2 = 100000
            return total - min(s1, s2)
        else:
            if l1 > 1:
                s1 = grouped[1][0] + grouped[1][1]
            else:
                s1 = 100000
            if l2 > 0:
                s2 = grouped[2][0]
            else:
                s2 = 100000
            if l1 > 0 and l2 > 1:
                s3 = grouped[1][0] + grouped[2][0] + grouped[2][1]
            else:
                s3 = 100000
            return total - min(s1, s2, s3)

    def minPushBox(self, grid: List[List[str]]) -> int:
        import queue
        m = len(grid)
        n = len(grid[0])
        S = (-1, -1)
        B = (-1, -1)
        T = (-1, -1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S':
                    S = (i, j)
                    grid[i][j] = '.'
                if grid[i][j] == 'B':
                    B = (i, j)
                    grid[i][j] = '.'
                if grid[i][j] == 'T':
                    T = (i, j)
                    grid[i][j] = '.'
        if B == T:
            return 0

        dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]

        def dfs(src, dst, b, v: set):
            if src == dst:
                return True
            v.add(src)
            for d in dirs:
                nd = (src[0] + d[0], src[1] + d[1])
                if 0 <= nd[0] < m and 0 <= nd[1] < n and grid[nd[0]][nd[1]] != '#' and nd != b and nd not in v:
                    if dfs(nd, dst, b, v):
                        return True
            return False

        visited = set()
        q = queue.Queue()
        q.put_nowait([B, S])
        step = 0
        while not q.empty():
            step += 1
            for _ in range(q.qsize()):
                b_, s_ = q.get_nowait()
                for i, d in enumerate(dirs):
                    nd = (b_[0] + d[0], b_[1] + d[1])  # next
                    ls = (b_[0] - d[0], b_[1] - d[1])  # last
                    if 0 <= nd[0] < m and 0 <= nd[1] < n \
                            and 0 <= ls[0] < m and 0 <= ls[1] < n \
                            and grid[nd[0]][nd[1]] != '#' \
                            and grid[ls[0]][ls[1]] != '#':  # 前后都是空地才有可能推动
                        state = (b_[0], b_[1], i)
                        if state in visited or (not dfs(s_, ls, b_, set())):
                            continue
                        if nd == T:
                            return step
                        visited.add(state)
                        q.put_nowait((nd, b_))

        return -1


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0

        def go(node: TreeNode, val):
            if node is None:
                return
            node.val = val
            go(node.left, 2 * val + 1)
            go(node.right, 2 * val + 2)

        go(root, 0)
        self.root = root

    def find(self, target: int) -> bool:
        path = [target]
        while target > 0:
            target = (target - 1) // 2
            path.append(target)
        node = self.root
        for p in path[:0:-1]:
            if p % 2 == 0:
                node = node.right
            else:
                node = node.left
            if node is None:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    # print(s.maxSumDivThree([3, 6, 5, 1, 8]))
    # print(s.maxSumDivThree([4]))
    # print(s.maxSumDivThree(
    #     [366, 809, 6, 792, 822, 181, 210, 588, 344, 618, 341, 410, 121, 864, 191, 749, 637, 169, 123, 472, 358, 908,
    #      235, 914, 322, 946, 738, 754, 908, 272, 267, 326, 587, 267, 803, 281, 586, 707, 94, 627, 724, 469, 568, 57,
    #      103, 984, 787, 552, 14, 545, 866, 494, 263, 157, 479, 823, 835, 100, 495, 773, 729, 921, 348, 871, 91, 386,
    #      183, 979, 716, 806, 639, 290, 612, 322, 289, 910, 484, 300, 195, 546, 499, 213, 8, 623, 490, 473, 603, 721,
    #      793, 418, 551, 331, 598, 670, 960, 483, 154, 317, 834, 352]))
    # print(s.minPushBox([["#", "#", "#", "#", "#", "#"],
    #                     ["#", "T", "#", "#", "#", "#"],
    #                     ["#", ".", ".", "B", ".", "#"],
    #                     ["#", ".", "#", "#", ".", "#"],
    #                     ["#", ".", ".", ".", "S", "#"],
    #                     ["#", "#", "#", "#", "#", "#"]]))
    # print(s.minPushBox(grid=[["#", "#", "#", "#", "#", "#"],
    #                          ["#", "T", "#", "#", "#", "#"],
    #                          ["#", ".", ".", "B", ".", "#"],
    #                          ["#", "#", "#", "#", ".", "#"],
    #                          ["#", ".", ".", ".", "S", "#"],
    #                          ["#", "#", "#", "#", "#", "#"]]))
    # print(s.minPushBox(grid=[["#", "#", "#", "#", "#", "#"],
    #                          ["#", "T", ".", ".", "#", "#"],
    #                          ["#", ".", "#", "B", ".", "#"],
    #                          ["#", ".", ".", ".", ".", "#"],
    #                          ["#", ".", ".", ".", "S", "#"],
    #                          ["#", "#", "#", "#", "#", "#"]]))
    # print(s.minPushBox(grid=[["#", "#", "#", "#", "#", "#", "#"],
    #                          ["#", "S", "#", ".", "B", "T", "#"],
    #                          ["#", "#", "#", "#", "#", "#", "#"]]))
    print(s.minPushBox([["#", ".", ".", "#", "#", "#", "#", "#"], ["#", ".", ".", "T", "#", ".", ".", "#"],
                        ["#", ".", ".", ".", "#", "B", ".", "#"], ["#", ".", ".", ".", ".", ".", ".", "#"],
                        ["#", ".", ".", ".", "#", ".", "S", "#"], ["#", ".", ".", "#", "#", "#", "#", "#"]]))
