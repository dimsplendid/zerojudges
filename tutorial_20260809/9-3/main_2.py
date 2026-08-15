noise = "()-[]{};:<>?@#$%^&*"

#start
import sys
for s in sys.stdin:
    words = s

    correct = ''

    for w in words:
        if w not in noise:
            correct += w

    print(correct)
