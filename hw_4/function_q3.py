import random as r

#find the idx of the first appearance
def find_first_idx(let, name_lst)->int:
    idx=0
    for i in range(len(name_lst)):
        if let==name_lst[i]:
            idx=i
            break
    return idx

def hangman_game():
    list_words=["game","drink","jym","bartender"]
    len_lst=len(list_words)

    program_pick=r.randint(0,len_lst-1)

    chosen_word=list(list_words[program_pick])
    const_chosen_word=chosen_word.copy()
    usr_guess=list("_"*(len(chosen_word)))

    count=0
    print(f"My word has {len(chosen_word)} lettres")
    while 1:
        if count==5:
            print("Game over:(")
            break
        elif const_chosen_word==usr_guess:
            print()
            print()
            print(f"Congratulations! ---> {''.join(const_chosen_word)} <--- is the right word!")
            break
        guess=input("Enter a letter: ")
        if guess not in chosen_word:
            count+=1
            print("Wrong letter :(")
            print(f"{5-count} tries to go")
            for v in usr_guess:
                print(v,end='')
            print()
        elif guess in chosen_word:
            idx=find_first_idx(guess, chosen_word)
            usr_guess[idx]=guess
            chosen_word[idx]=''

            if '_' in usr_guess:
                print("correct!")
                for v in usr_guess:
                    print(v,end='')
                print()
