def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        print('section1,step{}'.format(n))
        move(n-1, a, c, b)
        print('section2,step{}'.format(n))
        move(1, a, b, c)
        print('section3,step{}'.format(n))
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')