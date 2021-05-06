import random 

answer_list = ["pig", "nut", "net","her"]
name = random.randint(0, len(answer_list)-1)

def hangman(word):
    num_wrong = 0
    Hangman = ["",
               "_________    ",
               "|      |     ",
               "|      O     ",
               "|     /|\    ",
               "|     / \    ",
               "|________    "]
    win = False
    num = ["_"] * len(word)
    key = list(word)
    while num_wrong < len(Hangman) - 1:
        print("\n")
        answer = input("文字を入力してください >> ")
        if answer in key:
            id = key.index(answer)
            num[id] = answer
            key[id] = "$"
        else:
            num_wrong += 1
            print("\n".join(Hangman[0:num_wrong+1]))
        print(" ".join(num))
        if "_" not in num:
            print("あなたの勝利です！")
            print(" ".join(num))
            win = True
    if not win:
        print("あなたの負けです!")
        print("答えは{}です！".format(word))
hangman(answer_list[name])


