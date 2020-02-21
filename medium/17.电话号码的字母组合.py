#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (52.34%)
# Likes:    586
# Dislikes: 0
# Total Accepted:    79.3K
# Total Submissions: 150.9K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
#
#

# @lc code=start


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        answer = [""]
        for i in range(len(digits)):
            if digits[i] == "2":
                answer *= 3
                for j in range(0, len(answer) // 3):
                    answer[j] += "a"
                for j in range(len(answer)//3, len(answer)//3*2):
                    answer[j] += "b"
                for j in range(len(answer)//3*2, len(answer)):
                    answer[j] += "c"
            elif digits[i] == "3":
                answer *= 3
                for j in range(0, len(answer)//3):
                    answer[j] += "d"
                for j in range(len(answer)//3, len(answer)//3*2):
                    answer[j] += "e"
                for j in range(len(answer)//3*2, len(answer)):
                    answer[j] += "f"
            elif digits[i] == "4":
                answer *= 3
                for j in range(0, len(answer)//3):
                    answer[j] += "g"
                for j in range(len(answer)//3, len(answer)//3*2):
                    answer[j] += "h"
                for j in range(len(answer)//3*2, len(answer)):
                    answer[j] += "i"
            elif digits[i] == "5":
                answer *= 3
                for j in range(0, len(answer)//3):
                    answer[j] += "j"
                for j in range(len(answer)//3, len(answer)//3*2):
                    answer[j] += "k"
                for j in range(len(answer)//3*2, len(answer)):
                    answer[j] += "l"
            elif digits[i] == "6":
                answer *= 3
                for j in range(0, len(answer)//3):
                    answer[j] += "m"
                for j in range(len(answer)//3, len(answer)//3*2):
                    answer[j] += "n"
                for j in range(len(answer)//3*2, len(answer)):
                    answer[j] += "o"
            elif digits[i] == "7":
                answer *= 4
                for j in range(0, len(answer)//4):
                    answer[j] += "p"
                for j in range(len(answer)//4, len(answer)//4*2):
                    answer[j] += "q"
                for j in range(len(answer)//4*2, len(answer)//4*3):
                    answer[j] += "r"
                for j in range(len(answer)//4*3, len(answer)):
                    answer[j] += "s"
            elif digits[i] == "8":
                answer *= 3
                for j in range(0, len(answer)//3):
                    answer[j] += "t"
                for j in range(len(answer)//3, len(answer)//3*2):
                    answer[j] += "u"
                for j in range(len(answer)//3*2, len(answer)):
                    answer[j] += "v"
            elif digits[i] == "9":
                answer *= 4
                for j in range(0, len(answer)//4):
                    answer[j] += "w"
                for j in range(len(answer)//4, len(answer)//4*2):
                    answer[j] += "x"
                for j in range(len(answer)//4*2, len(answer)//4*3):
                    answer[j] += "y"
                for j in range(len(answer)//4*3, len(answer)):
                    answer[j] += "z"
        return answer
        # @lc code=end
