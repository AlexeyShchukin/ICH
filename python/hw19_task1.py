def anagrams(words: list[str]) -> list:
    my_set = set()
    groups = []  # groups with anagrams
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in my_set:
            my_set.add(sorted_word)
            groups.append([word])  # create group of words in groups
        else:
            for group in groups:
                if ''.join(sorted(group[0])) == sorted_word:  # check which group the next word belongs to
                    group.append(word)
                    break
    return [group for group in groups if len(group) > 1]  # filter out groups of one word


print(*anagrams(input('Enter words separated by spaces: ').split()), sep=', ')
