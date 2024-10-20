class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st=[]
        for i in expression:
            if i==")":
                re=[]
                while st[-1]!="(":
                    re.append(st.pop())
                st.pop()
                op = st.pop()
                if op =="!":
                    bo = not re[0] 
                elif op == "&":
                    bo = all(re)
                else:
                    bo=any(re)
                st.append(bo)
            elif i!=",":
                if i=='f':
                    st.append(False)
                elif i=='t':
                    st.append(True)
                else:
                    st.append(i)
        return st.pop()