#Count the no of valid parenthesis
"""
Input:
str = "((())"

Output:
4
"""

str = input()
st = []
count = 0
for i in str:
    if i == '(':
        st.append(i)
    
    else:
        st.pop()
        count += 2
        
print(count)
        
    