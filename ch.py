class Hangman:
    def __init__(self, word):
        self.stage = ["",
                      "_________",
                      "|    |   ",
                      "|    o   ",
                      "|   /|\  ",
                      "|   / \  ",
                      "|________" ]
        self.ko = list(word)
        self.word = list(word)
        self.wrong = 0
        self.win = False
        self.ans = ["_"]*len(self.word)
    def Set(self):
        while self.wrong < len(self.stage) - 1:
            kotae = input("文字を入力してください.")
            if kotae in self.word:
                id = self.word.index(kotae)
                self.ans[id] = kotae
                self.word[id] = "$"
            else:
                self.wrong += 1
                #e = self.wrong + 1 
            print(" ".join(self.ans))
            print("\n")
            print("\n".join(self.stage[0:self.wrong+1]))

            if "_" not in self.ans:
                print("あなたの勝利です！")
                print(" ".join(self.ans))
                self.win = True
                break
        if not self.win:
            print("あなたの負けです")
            print("答えは{}".format(" ".join(self.ko)))
        

s = Hangman("takasaki genki")
s.Set()
        