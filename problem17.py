'''
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example,
342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters. The use of "and" when
writing out numbers is in compliance with British usage.
'''

nums = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tys = {0: '', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty',
       7:'seventy', 8:'eighty', 9:'ninety'}

def num_to_words(n):
    if n == 1000: return 'onethousand'
    
    ans = ''
    a = n // 100 #百の位
    b = (n - a * 100) // 10 #十の位
    c = n - a * 100 - b * 10 #一の位
    if a > 0:
        ans = ans + nums[a] + 'hundred'
        if b > 0 or c > 0: ans += 'and'
    if b == 1:
        ans = ans + teens[c]
    else:
        ans = ans + tys[b] + nums[c]
    return ans

if __name__ == '__main__':
    print(sum((len(num_to_words(n)) for n in range(1, 1001))))
    