import itertools

num_of_piles = int(input("What is the number of piles in the game? "))
min = int(input("What is the minimum amount of coins possible in each pile? "))
max = int(input("What is the maximum amount of coins possible in each pile? "))

combinations = []
total = 0
nim_sums = 0 

def XOR(num1, num2):
    num = ""

    while len(num1) < len(num2):
        num1 = "0" + num1
    while len(num1) > len(num2):
        num2 = "0" + num2

    for i in range(0, len(num1)):
        if int(num1[i]) + int(num2[i]) == 2:
            num = num + "0"
        else:
            num = num + str(int(num1[i]) + int(num2[i]))
        
    return num

def nimSum(piles):
    bin_piles = []
    for i in range(0, len(piles)):
        bin_piles.append(int(str(bin(piles[i])[2:])))
    nim_sum = str(bin_piles[0])
    for i in range(1, len(bin_piles)):
        nim_sum = XOR(nim_sum, str(bin_piles[i]))
    return int(nim_sum)

for a in range(min, max+1):
    if num_of_piles > 1:
        for b in range(min, max+1):
            if num_of_piles > 2:
                for c in range(min, max+1):
                    if num_of_piles > 3:
                        for d in range(min, max+1):
                            if num_of_piles > 4:
                                for e in range(min, max+1):
                                    if num_of_piles > 5:
                                        for f in range(min, max+1):
                                            if num_of_piles > 6:
                                                for g in range(min, max+1):
                                                    if num_of_piles > 7:
                                                        for h in range(min, max+1):
                                                            if num_of_piles > 8:
                                                                for i in range(min, max+1):
                                                                    if num_of_piles > 9:
                                                                        for j in range(min, max+1):
                                                                            if num_of_piles > 10:
                                                                                for k in range(min, max+1):
                                                                                    if num_of_piles > 11:
                                                                                        for l in range(min, max+1):
                                                                                            if num_of_piles > 12:
                                                                                                for m in range(min, max+1):
                                                                                                    if num_of_piles > 13:
                                                                                                        for n in range(min, max+1):
                                                                                                            if num_of_piles > 14:
                                                                                                                for o in range(min, max+1):
                                                                                                                    if num_of_piles > 15:
                                                                                                                        for p in range(min, max+1):
                                                                                                                            if num_of_piles > 16:
                                                                                                                                for q in range(min, max+1):
                                                                                                                                    if num_of_piles > 17:
                                                                                                                                        for r in range(min, max+1):
                                                                                                                                            if num_of_piles > 18:
                                                                                                                                                for s in range(min, max+1):
                                                                                                                                                    if num_of_piles > 19:
                                                                                                                                                        for t in range(min, max+1):
                                                                                                                                                            combinations.append([t, s, r, q, p, o, n, m, l, k, j, i, h, g, f, e, d, c, b, a])
                                                                                                                                                            print(str(a/max))
                                                                                                                                                    else:
                                                                                                                                                        combinations.append([s, r, q, p, o, n, m, l, k, j, i, h, g, f, e, d, c, b, a])
                                                                                                                                                        print(str(a/max))
                                                                                                                                            else:
                                                                                                                                                combinations.append([r, q, p, o, n, m, l, k, j, i, h, g, f, e, d, c, b, a])
                                                                                                                                                print(str(a/max))
                                                                                                                                    else:
                                                                                                                                        combinations.append([q, p, o, n, m, l, k, j, i, h, g, f, e, d, c, b, a])
                                                                                                                                        print(str(a/max))
                                                                                                                            else:
                                                                                                                                combinations.append([p, o, n, m, l, k, j, i, h, g, f, e, d, c, b, a])
                                                                                                                                print(str(a/max))
                                                                                                                    else:
                                                                                                                        combinations.append([o, n, m, l, k, j, i, h, g, f, e, d, c, b, a])
                                                                                                                        print(str(a/max))
                                                                                                            else:
                                                                                                                combinations.append([n, m, l, k, j, i, h, g, f, e, d, c, b, a])
                                                                                                                print(str(a/max))
                                                                                                    else:
                                                                                                        combinations.append([m, l, k, j, i, h, g, f, e, d, c, b, a])
                                                                                                        print(str(a/max))
                                                                                            else:
                                                                                                combinations.append([l, k, j, i, h, g, f, e, d, c, b, a])
                                                                                                print(str(a/max))
                                                                                    else:
                                                                                        combinations.append([k, j, i, h, g, f, e, d, c, b, a])
                                                                                        print(str(a/max))
                                                                            else:
                                                                                combinations.append([j, i, h, g, f, e, d, c, b, a])
                                                                                print(str(a/max))
                                                                    else:
                                                                        combinations.append([i, h, g, f, e, d, c, b, a])
                                                                        print(str(a/max))
                                                            else:
                                                                combinations.append([h, g, f, e, d, c, b, a])
                                                                print(str(a/max))
                                                    else:
                                                        combinations.append([g, f, e, d, c, b, a])
                                                        print(str(a/max))
                                            else:
                                                combinations.append([f, e, d, c, b, a])
                                                print(str(a/max))
                                    else:
                                        combinations.append([e, d, c, b, a])
                                        print(str(a/max))
                            else:
                                combinations.append([d, c, b, a])
                                print(str(a/max))
                    else:
                        combinations.append([c, b, a])
                        print(str(a/max))
            else:
                combinations.append([b, a])
                print(str(a/max))
    else:
        combinations.append([a])
        print(str(a/num_of_piles))

for i in range(0, len(combinations)):
    combinations[i] = combinations[i][:num_of_piles]

combinations = list(combinations for combinations,_ in itertools.groupby(combinations))

for combination in combinations:
    pick = []
    for i in range(0, len(combination)):
        pick.append(combination[i])

    if nimSum(pick) == 0:
        nim_sums += 1
    total += 1

print("The propability of the player beginning winning is " + str(((1-nim_sums/total))*100) + "%")
