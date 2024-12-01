ans = 0
# ALLOWED = {
#     "red": 12,
#     "green": 13,
#     "blue": 14,
# }


# part 1, 2
with open("input.txt", "r") as fp:
    for i, line in enumerate(fp.readlines()):
        rounds = line[line.find(":") + 1:].split(";")
        mp = {
            "red": 0, 
            "green": 0,
            "blue": 0,
        }
        # flag = True
        for round in rounds:
            values = round.strip().split(", ")
            for val in values:
                # if not flag:
                #     break 
                val = val.strip().split()
                mp[val[-1]] = max(mp[val[-1]], int(val[0]))
                # if int(val[0]) > ALLOWED[val[-1]]:
                #     flag = False 

        ans += mp["red"] * mp["blue"] * mp["green"]
        # if flag:
        #     ans += i + 1
        
print(ans)

# part 2
