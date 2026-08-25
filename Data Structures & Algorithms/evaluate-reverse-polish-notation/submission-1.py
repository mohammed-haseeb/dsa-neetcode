class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for ch in tokens:
            if ch not in ['+', '-', '*', '/']:
                st.append(int(ch))
            elif ch == '+':
                second_num = st.pop()
                first_num = st.pop()
                res = first_num + second_num
                st.append(res)
            elif ch == '-':
                second_num = st.pop()
                first_num = st.pop()
                res = first_num - second_num
                st.append(res)
            elif ch == '*':
                second_num = st.pop()
                first_num = st.pop()
                res = first_num * second_num
                st.append(res)
            elif ch == '/':
                second_num = st.pop()
                first_num = st.pop()
                res = int(first_num / second_num)
                st.append(res)

        return st[0]