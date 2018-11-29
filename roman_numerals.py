from collections import OrderedDict

pairs = [   ('I', 'V'),
            ('X', 'L'),
            ('C', 'D'),
            ('M',)
        ]

#variations is a list of (variation, value, level) tuples
variations = []
increment = 1
for idx, pair in enumerate(pairs):
    second_value = increment * 5

    for n in range(1, 3 +1):
        variations.append((pair[0] * n, increment * n, idx))

    if pair[0] != 'M':
        variations.append((pair[0] + pair[1], second_value - increment, idx))

        variations.append((pair[1], second_value, idx))

        for n in range(1, 3+1):
            variations.append((pair[1] + pair[0] * n, (increment * n) + second_value, idx))

        variations.append((pair[0] + pairs[idx+1][0], increment * 9, idx))

    increment *= 10

variations_first_items = list(map(lambda x: x[0], variations))
variatons_value_dic = OrderedDict()

counter = 0
for n, variation in enumerate(variations_first_items, 1):
    modulo_val = n % 9
    index = modulo_val if modulo_val else 9
    variatons_value_dic[variation] = index * (10**counter)

    if not modulo_val:
        counter += 1

variatons_value_dic_reverse = {k:v for v,k in variatons_value_dic.items()}

def roman_numeral_encode(number):
    '''number must be int and it's value under 4000 and above 0.
    returns string'''

    assert type(number) == int, 'number must be int'
    #symbol M works only for numbers under 4000
    assert number > 0 and number < 4000, 'number must be greater than 0 and smaller than 4000'

    result = []
    for idx, zipped in enumerate(zip(pairs, list(str(number))[::-1])):
        pair, n = zipped
        n = int(n)
        if n in range(1,3 +1):
            result.insert(0, pair[0] * n)
        elif n == 4:
            result += pair[0] + pair[1]
        elif n in range(5,8 +1):
            result.insert(0, pair[1] + pair[0] * (n-5))
        elif n == 9:
            #get the sumbol of the next pair
            result.insert(0, pair[0] + pairs[idx + 1][0])

    return ''.join(result)

def roman_numeral_encode2(n):
    '''number must be int and it's value under 4000 and above 0.
    returns string'''

    assert type(n) == int, 'number must be int'
    #symbol M works only for numbers under 4000
    assert n > 0 and n < 4000, 'number must be greater than 0 and smaller than 4000'

    output_s = ''
    for idx, number in enumerate(str(n)):
        if number != '0':
            #how many zeroes in number
            depth = (len(str(n)) -1) - idx
            n_real_value = int(number + '0' * depth)
            output_s += variatons_value_dic_reverse[n_real_value]

    return output_s


def roman_numeral_decode(s):
    assert type(s) == str, 'input needs to be string'
    if not s:
        return None

    s = s.upper()

    number = 0
    itr = 0
    while len(s) >= 1:
        #itr is also level
        print('ccc')
        for n in range(1,4 +1)[::-1]:
            break_loop = False

            while itr < 4 or break_loop:
                try:
                    print('bb')
                    #look one letter further
                    current_variation = s[-n:]
                    for variation in variations:
                        if current_variation == variation[0] and itr == variation[2]:
                            number += variation[1]
                            break_loop = True
                            print('true')
                            break
                    else:
                        print('aa')
                        itr += 1

                except:
                    pass
                if break_loop:
                    break
            if break_loop:
                break
        else:
            return None

        s = s[:-len(current_variation):]
        itr += 1

    return number

def roman_numeral_decode2(s):
    assert type(s) == str, 'input needs to be string'
    if not s:
        return None

    modified_s = s
    output_n = 0
    #number of zeroes in last accepted variation
    depth = None
    for variation, variation_value in list(variatons_value_dic.items())[::-1]:
        variation_n_of_zeroes = list(str(variation_value)).count(str(0))
        if len(variation) <= len(modified_s) and (variation == modified_s[:len(variation)]) and  (depth == None or variation_n_of_zeroes < depth):
            #print('accepted_variation:', variation)
            depth = variation_n_of_zeroes
            output_n += variation_value
            modified_s = modified_s[len(variation):]
            if variation_n_of_zeroes == 0:
                break

    #print('leftovers:', repr(modified_s))
    #return None if there are left over letters
    return output_n if not modified_s else None


def encode_decode_test():
    for n in range(1,4000):
        print('idx:',n)
        encoded = roman_numeral_encode2(n)
        print('encoded',encoded)
        decoded = roman_numeral_decode2(encoded)
        print('decoded',decoded)
        if n != decoded:
            print('ERROR')
            break
        




if __name__ == '__main__':
    #number = 4018
    #s = 'XI'
    #result = roman_numeral_decode(s)
    #print(result)
    #encode_decode_test()
    #print(variations)

    #encode_decode_test()
    # = 'IXL'

    for x in range(1,4000):
        print(roman_numeral_encode2(x))
