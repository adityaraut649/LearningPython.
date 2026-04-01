def cheak(p1 , p2):
    if p1 == p2:
        return "Draw"
    elif p1 == "rock" and p2 == "paper":
        return "p1 wins!"
    else:
        return "p2 wins!"

print(cheak("rock", "paper"))
print(cheak("paper", "rock"))