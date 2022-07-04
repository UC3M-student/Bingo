def del_item_list_of_lists(given_list, n):
    asdf = []
    for i in people:
        try:
            b = list(given_list[i - 1])
            b.remove(n)
            asdf.append(b)
        except:
            c = list(given_list[i - 1])
            asdf.append(c)
            continue
    return asdf
