

def isPalindrome(*args):
    return  len(list(filter(lambda x: list(reversed(x)) == list(x), args))) > 0


print(isPalindrome('kajak', 'kajak2'))
print(isPalindrome([7,8,9,8]))