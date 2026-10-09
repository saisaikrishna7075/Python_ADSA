'''
Stock Span :(Previous Greater Elem)
for 
Ev
'''

def Stock_Span1(prices1):
    n = len(prices1)
    span = [1] * n
    for i in range(n):
        j = i-1
        while j>=0 and prices1[j] <= prices1[i]:
            span[i] +=1
            j -= 1
    return span
prices1 = [100,80,60,70,75,85]
print(Stock_Span1(prices1))




def Stock_Span2(prices2):
    stack = []
    span =[]
    for i in range(len(prices2)):
        while stack and prices2[stack[-1]] <= prices2[i]:
            stack.pop()
        if not stack:
            span.append(i+1)
        else:
            span.append(i - stack[-1])
        stack.append(i)
    return span
prices2 = [100,80,60,70,75,85]
print(Stock_Span2(prices2))