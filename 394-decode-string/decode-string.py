class Solution:
    def decodeString(self, s: str) -> str:
        num_st = []
        str_st = []
        cur_num = 0
        cur_str = ""
        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == "[":
                num_st.append(cur_num)
                str_st.append(cur_str)
                cur_num = 0
                cur_str = ""
            elif c == "]":
                prev_num = num_st.pop()
                prev_str = str_st.pop()
                cur_str = prev_str + cur_str * prev_num
            else:
                cur_str+=c

        return cur_str

        