
fav_icecream = ['chocolate', 'vanilla', 'mint', 'strawberry']
flavor_rank = [1, 4, 2, 3]

for ind in range(4):
    print(fav_icecream[ind], ":", flavor_rank[ind])

for flavor, rank in zip(fav_icecream, flavor_rank):
    print(flavor, ":", rank)


