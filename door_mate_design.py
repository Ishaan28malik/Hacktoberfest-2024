def door_mat(row,column):
    # for i in range(1, 2*row+1, 2):
    #     if i==((2*row)//2):
    #         print('WELCOME'.center(column,'-'))
    #     elif i<((2*row)//2):    
    #         print(((i)*'.|.').center(column,'-'))
    #     else:
    #         print(((2*row-i)*'.|.').center(column,'-'))
    
            
    pattern = [('.|.'*(2*i + 1)).center(column, '-') for i in range(row//2)]
    print('\n'.join(pattern + ['WELCOME'.center(column, '-')] + pattern[::-1]))        
    
if __name__=='__main__':
    x,y = input().split()

    door_mat(int(x),int(y))
