from cluster import HierarchicalClustering


def distance(a, b):
    if len(a) == 0:
        return len(b)
    elif len(b) == 0:
        return len(a)
    elif a[0] == b[0]:
        return distance(a[1:], b[1:])
    else:
        return 1 + min(
            distance(a[1:], b),
            distance(a, b[1:]),
            distance(a[1:], b[1:])
        )


if distance("aa", "ab") != 1:
    raise Exception("incorrect distance")
if distance("aaaa", "abcd")!= 3:
    raise Exception("incorrect distance")

cl = HierarchicalClustering([
    "aa","bca","cbb","aac"
    
   # "China's panda and Australia's koala are two animals that aren't predator, pandas eat bamboo and koala's eat eucalyptus leaves.They are both different from pythons because pythons are potentially dangerous.",
    #"Pandas in China only eat bamboo and Koalas in Australia eat exclusively eucalyptus leaves. They are both restricted to one food while pythons eat a variety of foods.", 
    #"Pandas in China and Koalas in Australia are similar because they both only feed on one thing. Pandas eat bamboo and Koalas eucalyptus leaves. Unlike pythons which eat just about everything including Alligators.",
    #"Pandas and koalas are similar because they eat mainly one type of food for them. Pandas eat bamboo and koalas eat eucalyptus leaves. They differ from a python because pythons can eat just about anything.",
    # "Panda's only eat bamboo and koalas exclusively eat eucalyptus leaves",
    # "A China panda eats almost nothing, but bamboo koalas bear eat eucalyptus leaves, those two animals are similar because they both eat a food amount of leaves or something that is green.",
    # "China's panda is similar to Australia's Koala because in the article it states that the panda only eats bamboo and the koala eats eucalyptus leaves constantly. they both only eat one thing and are different from pythons because they eat multiple things.",
    # "Pandas in China and koalas in Australia are similar because they both are exclusively eating one food. China's panda eats almost nothing but bamboo, and Australia's koala bear, eats eucalyptus leaves almost exclusively . 'But they are different from pythons because pythons eat a much more vast assortment.",
    # "They both only practically eat one thing. For the panda its bamboo and the koala eats eucalyptus leaves both these two animals are very different than a python that has no legs and eats anything.",
    # "Pandas and koalas are similar to each other because they both only eat one type of food, while pythons try to eat anything that moves and fit in their mouth. This means that the koalas and pandas are much more likely to go about alike because of their food sources than the pythons.",
    # "Pandas and koalas are similar because they both almost exclusively eat just one food, pandas eat bamboo, and koalas eat eucalyptus leaves. Both animals are different from the python because pythons can adapt to different food sources while pandas and koalas can not.",
    # "They both are different from pythons because pythons eat other animals, example 'A Python swallowed an alligator.'The Pandas and Koalas only eat bamboo and eucalyptus leaves.",
    # "Panda in China only eat bamboo the Koala in Australia eat eucalyptus leaves exclusively.",
    # "Pandas and koalas are similar because they are both part of the specialist species and they both mostly eat one food source with pandas its bamboo and with koalas its eucalyptus leaves. They are both a total different species from pythons.",
    # "Pandas in China and koalas in Australia are similar because they only eat one thing. Pandas eat bamboo and koalas eat eucalyptus leaves. Pythons on the other are completely different because they have a large variety of what they eat.", 
    # "Pandas in China are similar to koalas i Australia because they both prosper off mainly one food source and live in one part of the world unless they are taken away or raised somewhere else. A python differs from these animals because it can be found living in many places and eating many things.",
    # "Pandas and koalas are similar because they only eat about one thing like pandas eat almost nothing but bamboo and the koalas eats only eucalyptus leaves only. The python eats anything it can get like an alligator.",
    # "China's panda eats almost nothing but bamboo that is why China's panda and Australia's koala are similar because Australia's koala they eat eucalyptus leaves almost exclusively. and China's panda and Australia's koalas are both different from pythons because pythons don't eat the same.",
    # "Chinas pandas and Australia's koala bears are similar because they each only eat one kind of food that it. The python can eat anything pretty much. Thats how the python is different from the pandas and koala. The koala eats eucalyptus leaves and pandas eat only bamboo.",
    # "Pandas in China are similar to koalas in Australia since they eat a certain type of food almost exclusively. They are different from pythons because pythons can live anywhere and are most abundant in or around humans.",
    # "Pandas and koalas eat almost one food exclusively while pythons will just about anything to get nutrition.",
    # "Both pandas in China and koalas in Australia are similar by the way that they both eat naturally growth vegetables like bamboo or eucalyptus plants; Yet they both differ from pythons because while they eat plants, the pythons consumes animals like pond rats- even alligators.",
    # "Pandas in China and koalas in Australia are similar because they both eat food from nature, for example pandas eat bamboo, and koalas eat eucalyptus leaves.",
    # "Panda's and koala's are similar in the way that they only like to eat one specific food, and nothing else. They are different from the python because they are not invasive to where they live. their population is extremely low and they are not being damaging to their home environment.",
    # "The pandas and koalas are alike because they both only eat one thing. As with the pythons they eat a few different things. They are different types of animals so they need different things.",
    # "Pandas and koala's are similar in they're eating habits: China's panda which eats almost nothing but bamboo or Australia's koala bear which eat leaves almost exclusively. They differ from pythons because the article explains how pythons eat almost anything.",
    # "Panda's are similar to koala bears because they both eat only one thing and those things which are bamboo, and eucalyptus leaves. These two bears on aren't harming anything by eating the foods. But pythons eat almost anything that moves and they are harming the environment.",
    # "The pandas in China are similar to koala bear in Australia because they only eat plants. There different because the one in China eat only bamboo and the one from Australia eats eucalyptus leaves almost exclusively.",
    # "Panda's and koalas are the same because they both eat the same thing everyday all day. Panda's eat bamboo and koala eat eucalyptus leaves.",
    # "Pandas and koalas are similar because they only eat 1 food source and can't adapt anywhere else like pythons can.",
    # "China's panda is like Australia's koala bear, because they both eat mostly one thing, bamboo and eucalyptus leaves. Also both of these things are vegetarian leafs and trees. Unlike a python which pretty much eats anything it can fit into its mouth even a alligator.",
    # "Pandas in China are similar to koalas in Australia, because they are animals that only eat bamboo and eucalyptus. They both differ from a python because the python eats animals.",
    # "Panda's and koala bears stay in rain forests, pythons you will mostly catch them in an hot environment.",
    # "Pandas and koalas are similar because they need special environment and food to live, while pythons don't.",
    # "The difference between the two koala and panda from a python is the different environments they live in . For example, the pythons lives along the canals of Cape Coral, pandas and koalas live near forest.",
    # "Just like pythons, koalas and pandas need their space. They live in a certain environment, that they can adapt to. Every animal must adapt to its place at where it lives. They can't just get up and move its not that easy.",
    # "Pandas and koalas are both mammals. They are different from pythons is that they of warm and fluffy and furry and snake are scale and unappealing to the eye.",
    # "Pandas and koalas are similar because they are both described as specialist animals The panda and koala bears a different from the pythons because because pythons are generalist animals",
    # "Pandas in China and koalas from Australia are similar because they are both specialist. They both are different from a python because a python is a generalist.",
    # "Panda's are similar to koala's because they are both specialists and a python is a generalist.",
    # "Panda's are similar to Koala's by they are both specialist species.Also a python is a generalist specie and can easily adapt to change. They eat a variety of foods, and accept change.",
    # "A panda from china and a koala from Australia are very similar because they are both specialists. This shows that they are unable to adopt , unlike pythons who are generalists.",
    # "Panda's and koalas are both similar because they are specialist. Pythons differ from these two animals because pythons are generalist. Pythons have a much broader range that they can survive in.",
    # "Koala's and panda's are both specialists, which means that their is only 1 food that is essential to their diets and can't be found much of anywhere else. While a python is a generalists and can survive in other places because it's food source is not limited.",
    # "Pandas in China are similar to koalas in Australia because they are both specialist who are not favored at this age.",
    # "Pandas in China are similar to koalas in Australia because they are both a specialists who need very specific environments to survive. They are different from pythons because pythons are generalists that can live close to almost anywhere.",
    # "Pandas in China are similar to koalas in Australia because they are both specialists. Pandas and koalas are different than pythons because a python is a generalist.",
    # "The China's panda and the Australia's koala are both specialist because they eat the same most of the time. Pythons are generalist which can eat different types of animals.",
    # "China's panda and Australia's koala are similar because they are both specialists. This means that they only eat specific items, such as bamboo and eucalyptus leaves. The python, on the other hand, is a generalist carnivore that will eat any meat.",
    # "Pandas in China are similar to koalas in Australia because they are both specialists. Both koalas and pandas are different from pythons in that pythons are generalists.",
    # "Panda  and koalas are similar because they're both specialists. They are both different from pythons because pythons are generalists, so they will eat almost anything; also pythons are invasive and pandas are koalas are not.",
    # "Pandas in China, and koalas in Australia are similar because they both are specialists. So they have to stay in specific habitats to survive. Pythons are generalists, they can move anywhere and adapt to their surroundings to survive.",
    # "The China's panda and Australia's koalas are similar because are specialist and they are different of pythons because are generalist so can live in many places but the specialist not can only at a determinate place.",
    # "Pandas are similar to koalas because they are both specialists. These two species are different from snakes since a snake is a generalist species. Snakes are generalists because they can adapt to many different locations where as pandas are stuck on China and koalas are in Australia.",
    # "Pandas in China are similar to koalas in Australia because they are both specialists. They are both different from pythons because pythons eat other species, and they are very harmful.",
    # "Panda from china and koalas from Australia are both specialists.They live eating special plants like bamboo and eucalyptus leaves while pythons are very different.They can eat almost anything and kill only animals as a source of food.They are also eaten made pets so they have a better chance of survival.",
    # "Both pandas in China and Koalas in Australia are similar because they they are specialist. This means that they would not be able to survive anywhere else because the certain food sources they need are only available in China and Australia. A python , a generalist is different because it can live almost anywhere.",
    # "Pandas in China are similar to koalas in Australia are both specialists. They eat almost nothing but one thing. They are different from pythons by how because pythons eat a lot more than just one thing, they eat a variety of things.",
    # "Pandas and koalas are specialist species because they rely on stability to live while the pythons is a generalist species that can survive in multiple places."
], distance)
clusters = cl.getlevel(1)

print(clusters)