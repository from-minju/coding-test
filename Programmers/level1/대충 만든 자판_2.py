
def solution(keymap, targets):
    answer = []
    dic = {}
    for k in keymap:
        for i, ch in enumerate(k):
            dic[ch] = min(i + 1, dic[ch]) if ch in dic else i + 1

    for target in targets:
        sum = 0
        for ch in target:
            if ch not in dic:
                sum = - 1
                break
            sum += dic[ch]
        answer.append(sum)

    return answer