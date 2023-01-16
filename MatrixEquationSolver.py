import numpy as np

def coeffecient_extractor(eqn):
    tst = []
    for i in range(len(eqn)):
        char = eqn[i]
        if char.isdigit():
            if eqn[i-2] == '-':
                tst.append(int(char) - 2 * (int(char)))
            else:
                tst.append(int(char))
        elif char in ['x','y','z']:
            if eqn[i-1].isdigit():
                pass
            elif eqn[i-2] == '-':
                tst.append(-1)
            else:
                tst.append(1)            
    return tst

def main():
    print('Solve Equations using matrices')

    eq1 = input('Enter your first equation in the form of "ax + by + c = d":  ')
    eq2 = input('Enter your second equation in the form of "ax + by + c = d":  ')
    eq3 = input('Enter your third equation in the form of "ax + by + c = d":  ')

    r1 = coeffecient_extractor(eq1)
    r2 = coeffecient_extractor(eq2)
    r3 = coeffecient_extractor(eq3)
        
    d1,d2,d3 = r1[3],r2[3],r3[3]

    A_matrix = np.matrix([r1[0:3],r2[0:3],r3[0:3]])
    B_matrix = np.matrix([[d1],[d2],[d3]])

    
    inv_A_matrix = np.linalg.inv(A_matrix)

    var_matrix = inv_A_matrix * B_matrix



    print(f' Value of "X"  =  {int(var_matrix[0,0])}')
    print(f' Value of "Y"  =  {int(var_matrix[1,0])}')
    print(f' Value of "Z"  =  {int(var_matrix[2,0])}')

    main()

main()
