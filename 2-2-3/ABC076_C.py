S = input()
T = input()
t = len(T)

for i in range(len(S)-t, -1, -1):
    for j in range(t):
        k = S[i+j]
        if k != T[j] and k != "?":
            break
    else:
        print((S[:i]+T+S[i+t:]).replace("?", "a"))
        exit()
print("UNRESTORABLE")


# Sd = input()
# T = input()

# def check(A, B):
#     for a, b in zip(A, B):
#         if a != '?' and a != b:
#             return False

#     return True


# for i in range(len(Sd) - len(T) + 1)[::-1]:
#     if check(Sd[i:i + len(T)], T):
#         print((Sd[:i] + T + Sd[i + len(T):]).replace('?', 'a'))
#         break
# else:
#     print('UNRESTORABLE')