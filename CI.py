import random
import matplotlib.pyplot as plt
import math

def sphere(arr,no_of_variables,no_of_candidates):
    sphere = []
    for i in range(no_of_candidates):
        temp = 0
        for j in range(no_of_variables):
            temp = temp + (arr[i][j])**2
        sphere.append(temp)
    # print(sphere)
    return sphere

def beale(arr,no_of_variables,no_of_candidates):
    beale = []
    for i in range(no_of_candidates):
        temp = ((arr[i][0] + (2*arr[i][1]) - 7)**2 + ((2*arr[i][0]) + arr[i][1] - 5)**2)
        beale.append(temp)
    # print(beale)
    return beale

def booth(arr,no_of_variables,no_of_candidates):
    booth = []
    for i in range(no_of_candidates):
        temp = ((1.5-arr[i][0]+(arr[i][0]*arr[i][1]))**2 + (2.25-arr[i][0]+(arr[i][0]*(arr[i][1])**2))**2 + (2.625-arr[i][0]+(arr[i][0]*(arr[i][1])**3))**2)
        booth.append(temp)
    # print(booth)
    return booth

def shubert(arr,no_of_variables,no_of_candidates):
    shubert = []
    for  j in range(no_of_candidates):
        temp1 = 0
        temp2 = 0 
        for i in range(1,5):
            temp1 = temp1 + (i*math.cos(((i+1)*arr[j][0])+i))
            temp2 = temp2 + (i*math.cos(((i+1)*arr[j][1])+i))
        temp3 = temp1*temp2
        shubert.append(temp3)
    print(shubert)
    return shubert

def inverse_add_probab(lst):
    temp = []
    probab = []
    divisor = 0
    for x in lst:
        x = 1/x
        divisor += x
        temp.append(x)
    for x in temp:
        x = x/divisor
        probab.append(x)
    # print(probab)
    return probab

def roulette(probab,main_list):
    temp = []
    rand = []
    follow = []
    new_list = []
    rand_val = 0
    tot = 0
    for x in probab:
        tot +=x
        rand_val = random.randrange(0,100) / 100
        temp.append(tot)
        rand.append(rand_val)
    # print(temp)
    # print(rand)
    for y in range(len(probab)):
        flag = 0
        for j in range(len(probab)):
            if rand[y]<temp[j]:
                flag = j
                break
            else:
                pass
        follow.append(flag)

    for y in range(len(probab)):
        new_list.append(main_list[follow[y]])
    # print(follow)
    # print(new_list)
    return new_list

def range_reduc(upper,lower,rf):
    temp = upper-lower
    sampling = temp*rf
    sampling = sampling/2
    upper = sampling
    lower = -sampling
    print(upper,lower)
    return upper,lower

def new_boundary(upper_bound,lower_bound,main_arr,no_of_candidates,no_of_variables,original_upper,original_lower):
    new = []

    for candidates in range(no_of_candidates):
        temp = []
        for variables in range(no_of_variables):
            temp2 = []
            upper = main_arr[candidates][variables] + upper_bound
            lower =main_arr[candidates][variables] + lower_bound
            if lower < original_lower:
                lower=original_lower
            if upper > original_upper:
                upper = original_upper
            temp2.append(lower)
            temp2.append(upper)
            temp.append(temp2)
        new.append(temp)
    # print(temp)
    # print("new bounds ",new)
    return new

def new_matrix(new_bounds,no_of_candidates,no_of_variables):
    new = []
    for candidates in range(no_of_candidates):
        temp = []
        for variables in range(no_of_variables):
            temp.append(random.uniform(new_bounds[candidates][variables][0], new_bounds[candidates][variables][1]))
        new.append(temp)   
    # print("new matrix ",new)   
    print("--------------------------")  
    return new



            

if __name__ == "__main__":
    # upper_bound=float(input("Enter Upper Bound:"))
    # lower_bound=float(input("Enter Lower Bound:"))
    
    #sphere bounds
    # upper_bound=5.12
    # lower_bound=-5.12

    # #beale bounds
    # upper_bound=4.5
    # lower_bound=-4.5

    # #booth bounds
    # upper_bound=10
    # lower_bound=-10

    #shubert bounds
    upper_bound=10
    lower_bound=-10

    original_upper = upper_bound
    original_lower = lower_bound
    # print(upper_bound,lower_bound)
    no_of_variables=int(input("Enter Number of Variables:"))
    no_of_candidates=int(input("Enter Number of Candidates:"))
    reduction_factor=0.9
    main_arr=[]
    for candidates in range(no_of_candidates):
        temp = []
        for variables in range(no_of_variables):
            # temp.append(float(input("Enter value of candidate "+str(candidates)+", variable "+str(variables)+":")))
            temp.append(random.uniform(upper_bound, lower_bound))
        main_arr.append(temp)
                
        # print(candidates,variables)
    print("main array",main_arr)
    # list_from_fn = sphere(main_arr,no_of_variables,no_of_candidates)
    
    # list_from_fn = beale(main_arr,no_of_variables,no_of_candidates)
    
    # list_from_fn = booth(main_arr,no_of_variables,no_of_candidates)

    list_from_fn = shubert(main_arr,no_of_variables,no_of_candidates)

    probab = inverse_add_probab(list_from_fn)
    main_arr = roulette(probab,main_arr)
    upper_bound,lower_bound=range_reduc(upper_bound,lower_bound,reduction_factor)
    new_bounds = new_boundary(upper_bound,lower_bound,main_arr,no_of_candidates,no_of_variables,original_upper,original_lower)
    main_arr = new_matrix(new_bounds,no_of_candidates,no_of_variables)

    x=[]
    y=[]
    for i in range(100): 
        y.append(list_from_fn)
        x.append([i]*no_of_candidates) 
        # list_from_fn = sphere(main_arr,no_of_variables,no_of_candidates)
        
        # list_from_fn = beale(main_arr,no_of_variables,no_of_candidates)

        # list_from_fn = booth(main_arr,no_of_variables,no_of_candidates)

        list_from_fn = shubert(main_arr,no_of_variables,no_of_candidates)
        probab = inverse_add_probab(list_from_fn)
        main_arr = roulette(probab,main_arr)
        upper_bound,lower_bound=range_reduc(upper_bound,lower_bound,reduction_factor)
        new_bounds = new_boundary(upper_bound,lower_bound,main_arr,no_of_candidates,no_of_variables,original_upper,original_lower)
        main_arr = new_matrix(new_bounds,no_of_candidates,no_of_variables)
    
    plt.figure("Shubert")
    plt.plot(x,y)
    plt.show()


    # print(arr)


