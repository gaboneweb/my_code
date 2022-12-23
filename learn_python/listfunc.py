def move_list(list_,is_positive= True,index = 0):
    if index == len(list_) - 1:
        index = -1
        print("hi")
    elif index == -len(list_):
        index = 0
    if is_positive:
        index += 1
        print("Change")
    else:
        index -= 1

    return index
    
def multiple_move_list(list_,number,index = 0):
    is_positive = False
    if number > 0:
        is_positive = True
    for i in range(abs(number)):
        index = move_list(list_,is_positive,index)

    return index


if __name__ == "__main__":
    num_list = [1, 2,3,4]
    index_= 3
    index = move_list(num_list,True,index_)
    print(f"index is {index}")

    index = multiple_move_list(num_list,5)
    print(f"index is {index}")

    index = num_list[multiple_move_list(num_list,-5)]
    print(f"index is {index}")
    


    