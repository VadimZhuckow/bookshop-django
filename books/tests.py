from django.test import TestCase

# Create your tests here.
games = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']
def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        print(res)
        if res[0] > res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count


a = games[0].split(':')
print(a)

print(a[0] > a[1])
