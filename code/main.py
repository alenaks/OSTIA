from ostia import *


# a -> 0, b -> 1

S1 = [("ab", "01"), ("aba", "010"), ("aaa", "000"), ("bb", "11"), ("babb", "1011"), ("bbaa", "1100"), ("aa", "00"),
     ("baab", "1001"), ("ba", "10"), ("bba", "110"), ("baa", "100"), ("bab", "101")]
Sigma = ["a", "b"]
Gamma = ["0", "1"]

T1 = ostia(S1, Sigma, Gamma)
print("States:", T1.Q)
print("Transitions:", T1.E)
print("State outputs:", T1.stout)

test = ["aba", "bbb", "ababa", "abbaba"]
for w in test:
    print(w, "--->", T1.rewrite(w))

print("------------------------------------------------")


# a -> 0 unless final, then it's 1; b -> 1
# pattern from Colin de la Higuera (2010)

S2 = [("b", "1"), ("a", "1"), ("ab", "01"), ("abb", "011"), ("bb", "11"), ("aa", "01"), 
     ("aaa", "001"), ("aabaab", "001001"), ("aab", "001"), ("aaba", "0011"), ("aabaa", "00101")]
Sigma = ["a", "b"]
Gamma = ["0", "1"]

T2 = ostia(S2, Sigma, Gamma)
print("States:", T2.Q)
print("Transitions:", T2.E)
print("State outputs:", T2.stout)

test = ["aba", "bbb", "ababa", "abbaba"]
for w in test:
    print(w, "--->", T2.rewrite(w))
