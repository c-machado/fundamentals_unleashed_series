
phrase_one = input('Enter the phrase one')
phrase_two = input('Enter the phrase two')

def is_an_anagram(phrase_one, phrase_two):
    phrase_one_l = []
    phrase_two_l = []
    for c in phrase_one:
        phrase_one_l.append(c)
    for char in phrase_two:
        phrase_two_l.append(char)
    for i in phrase_one_l:
        repeated_char = phrase_one_l.count(i)
        if i in phrase_two_l:
            repeated_char_l2 = phrase_two_l.count(i)
            if repeated_char == repeated_char_l2:
                flag = 1
            else:
                flag = 0
        else:
            flag = 0
    if flag == 1:
        print('is an anagram')
    else:
        print('it is not an anagram')

is_an_anagram(phrase_one,phrase_two)

# s1 = input('Enter the phrase one')
# s2 = input('Enter the phrase two')
#
#
# def is_an_anagram2(self, s1, s2):
#     s1 = s1.replace(' ', '').lower()
#     print(s1)
#     s2 = s2.replace(' ', '').lower()
#     print(s2)
#
#     if len(s1) != len(s2):
#         return False
#     count = {}
#     for letter in s1:
#         if letter in count:
#             count[letter] += 1
#         else:
#             count[letter] = 1
#     for letter in s2:
#         if letter in count:
#             count[letter] -= 1
#         else:
#             count[letter] = 1
#     for k in count:
#         if count[k] != 0:
#             print('is not an anagram')
#             return False
#     print('is an anagram')
#     return True
