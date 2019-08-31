#!/usr/bin/env python3
def func_tri_check(l1,l2,l3):
    if (l1>l2+l3) or (l2>l1+l3) or (l3>l1+l2):
        print('nop')
    elif (l1==l2+l3) or (l2==l1+l3) or (l3==l1+l2):
        print('yes')
    else:
        print('yes')
side1 = int(input('enter side 1\n'))
side2 = int(input('enter side 2\n'))
side3 = int(input('enter side 3\n'))
func_tri_check(side1,side2,side3)