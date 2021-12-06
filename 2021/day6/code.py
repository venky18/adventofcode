from collections import defaultdict

with open('in.txt') as f:
    fish = list(map(int, f.read().strip().split(',')))



def simulate_dic(dic):
    print(sorted(dic.items()))
    new_born = dic[0]
    for i in range(0,8):
        dic[i] = dic[i+1]
    dic[8] = new_born
    dic[6] += new_born
    return dic

days = 256
dic = defaultdict(int)
for ele in fish:
    dic[ele]+=1

for i in range(days):
    dic = simulate_dic(dic)

print(sum([v for k,v in dic.items()]))

# def simulate(fish):
#     new_fish = []
#     for idx, ele in enumerate(fish):
#         if ele-1 == -1:
#             fish[idx] = 6
#             new_fish.append(8)
#         else:
#             fish[idx] = ele-1
#     return fish+new_fish  


# for i in range(days):
#     fish = simulate(fish)

# print(len(fish))