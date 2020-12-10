def count_func(numbers):
    global maxx

    idx = 0
    summ = int(numbers[idx])
    while idx < len(numbers)-2:

        idx += 1

        if numbers[idx] == '+':
            summ += int(numbers[idx+1])
            idx += 1
        elif numbers[idx] == '-':
            summ -= int(numbers[idx+1])
            idx += 1

        elif numbers[idx] == '*':
            summ *= int(numbers[idx+1])
            idx += 1

    if maxx < summ:
        maxx = summ

def func(tmp, used, cnt):

    if cnt == N//2+1:
        count_func(tmp)
        return
    cntt = (cnt-1)*2

    if not used[cnt-1]:
        tmp2 = tmp[::]
        if tmp:
            tmp.pop()

        if sentence[cntt + 1] == '*':
            tmp.append(int(sentence[cntt]) * int(sentence[cntt + 2]))
        elif sentence[cntt + 1] == '+':
            tmp.append(int(sentence[cntt]) + int(sentence[cntt + 2]))
        elif sentence[cntt + 1] == '-':
            tmp.append(int(sentence[cntt]) - int(sentence[cntt + 2]))
        used[cnt] = 1
        func(tmp, used, cnt+1)
        used[cnt] = 0
        if not tmp2:
            tmp2.append(sentence[cntt])
        tmp2.append(sentence[cntt + 1])
        tmp2.append(sentence[cntt + 2])
        func(tmp2,used,cnt+1)
    else:
        tmp.append(sentence[cntt+1])
        tmp.append(sentence[cntt+2])
        func(tmp,used,cnt+1)



N = int(input())

sentence = list(input())

if '0' in sentence:
    if sentence[sentence.index('0') - 1] == '*':
        sentence = sentence[sentence.index('0')::]
        N = len(sentence)

if N == 1:
    print(sentence[0])
else:
    used = [0] * (N//2+1)

    maxx = -(2**31)

    func([], used, 1)

    print(maxx)