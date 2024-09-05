# 괄호 선택 함수
def selectBracket(idx):
    # 길이만큼 고르면
    if idx >= len(visited):
        # 계산
        calculate()
        return
    # 괄호 쳤다면 --> 두번 연속 괄호를 칠 수 없기 때문에 두칸 뒤를 확인함
    visited[idx] = True
    selectBracket(idx + 2)
    # 괄호 치지 않았다면 --> 다음 연산자에 대해서 괄호를 칠지 확인함
    visited[idx] = False
    selectBracket(idx + 1)


# 연산 함수
def calc(a, b, opr):
    if opr == '+':
        return a + b
    elif opr == '-':
        return a - b
    elif opr == '*':
        return a * b
    else:
        return 0


# 계산 함수
def calculate():
    global maxResult
    # 숫자 계산용으로 복사해옴
    tmp = numbers[:]

    # 괄호 계산해서 숫자 반영
    for idx in range(len(visited)):
        # 괄호를 계산
        if visited[idx]:
            # 숫자를 변경해줌, tmp == 숫자, operators == 연산자
            tmp[idx] = calc(tmp[idx], tmp[idx + 1], operators[idx])

    # 인덱스와 연산자에 대해서
    for idx, opr in enumerate(operators):
        # 괄호 True라면
        if visited[idx]:
            # 다음 값은 이전에 괄호 내부 연산한 값임
            tmp[idx + 1] = tmp[idx]
        # 그렇지 않다면
        else:
            # 다음 값은 계산을 해야함
            tmp[idx + 1] = calc(tmp[idx], tmp[idx + 1], opr)
    # 마지막 값이 최대값임
    maxResult = max(maxResult, tmp[-1])


n = int(input())
# 숫자
numbers = []
# 연산자
operators = []
# 최댓값 저장용
maxResult = -(2**13)

# 입력을 받아 숫자와 연산자 분리
arr = list(input())
for char in arr:
    if char.isdigit():
        numbers.append(int(char))
    else:
        operators.append(char)

visited = [False] * len(operators)
# 괄호 선택 시작
selectBracket(0)
print(maxResult)
