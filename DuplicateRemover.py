from random import choice


while True:
    user_inp = input("Enter a set of characters: ").replace(" ", "").replace("\t", "").replace("\n", "")
    if user_inp.isalpha():
        if len(user_inp) % 2 == 0:
            break
        else:
            waste = choice(user_inp)
            user_inp = user_inp.replace(waste, "")
            print("Odd number of characters used. \nPurging a random character...")
            break
    else:
        print("Invalid input")



def sample_creator(given_string):
    index_init = 2
    work_list = list(given_string)
    for _ in range(int(len(given_string)/2)-1):
        work_list.insert(index_init + _ , ",")
        index_init += 2
    
    crt_sample = "".join(work_list).split(",")
    
    return crt_sample


sample = sample_creator(user_inp)


new_sample = []

for gene in sample:
    new_sample.append(tuple(gene))

new_sample = set(new_sample)

new_sample = list(new_sample)

print(new_sample)