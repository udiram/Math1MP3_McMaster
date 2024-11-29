tol = 0.01

def pseries(p, max_t, tol):
    next_term = 1
    iter = 1
    sn = 0
    while next_term >= tol and iter <= max_t:
        sn += next_term
        iter += 1
        next_term = 1 / iter ** p # next term

    return sn



def convert_list_to_dict_len(L):
    D = {}
    for word in L:
        D[word] = len(word)

    return D

D = convert_list_to_dict_len(['Apple', 'Banana'])
print(D)


def combine_two(D1, D2):
    D3 = {}
    for word in D1:
        if word in D2:
            D3[word] = D1[word] + D2[word]
        else:
            D3[word] = D1[word]

    for word in D2:
        if word not in D3:
            D3[word] = D2[word]

    return D3

D3 = combine_two({'Apple': 5, 'Banana': 6}, {'Apple': 4, 'Kiwi': 6})
print('D3_Me {}'.format(D3))
def combine_two_izzy(D1, D2):
    D3 = D2
    for word in D1:
        if word in D3:
            D3[word] += D1[word]
        else:
            D3[word] = D1[word]

    return D3

D3_iz = combine_two_izzy({'Apple': 5, 'Banana': 6}, {'Apple': 4, 'Kiwi': 6})
print(f'D3_Iz {D3_iz}')


def check_subset(A, S):
    for i in A:
        if i not in S:
            break
    print(f'{i} not in superset, therefore A not subset of S')


check_subset({1, 4},{1,2,3})


def remove(A,d):
    filtered = []
    for num in A:
        parseable_num = str(num)
        if str(d) not in parseable_num:
            filtered.append(int(parseable_num))

    print(filtered)
    return filtered


A = {13, 17, 100, 772}
d = 7

remove(A, d)

def create_dict(L):
    info_dict = {}
    for info in L:
        surname = info[0]
        hometown = info[1]
        info_dict[surname] = hometown

    print(info_dict)
    return info_dict

L=[['clements','oshawa', '1980'], ['cousins', 'hamilton', '1990']]

create_dict(L)
print(set(create_dict(L).values()))

def inverse(D):
    D_inverse = {}
    for key, values in D.items():
        D_inverse[values] = key

    print(f'Dinverse {D_inverse}')
    return D_inverse


inverse(create_dict(L))
