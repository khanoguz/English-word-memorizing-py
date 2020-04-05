import os,sqlite3
import time,random



def main():
    os.system("clear")
    db = sqlite3.connect("words.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS words(english,Turkish)")
    print("""
    Welcome, please select your choice
    [1]Find a word
    [2]Add a word
    [3]Random mood
    """)
    
    choice1 = input(":")
    if choice1 == "1":
        word = input("Write what you wanna find:")
        cursor.execute("SELECT * FROM words WHERE english = '{}'".format(word))
        print(cursor.fetchone())
        input("Found")
        os.system("clear")
        db.close()
    elif choice1 == "2":
        e_word = input("Write your English word:")
        t_word = input("Write the meaning of the word:")
        insert = "INSERT INTO words(english,Turkish) VALUES (?,?);"
        a = (e_word, t_word)
        cursor.execute(insert,a)
        db.commit()
        input("ADDED")
        os.system("clear")
        db.close()
    elif choice1 == "3":
        eng_word = []
        sql = "SELECT * FROM words"
        cursor.execute(sql)
        word = cursor.fetchall()
        for i in word:
            eng_word.append(i)

        rang = len(eng_word)

        while rang != 0:
            try:
                os.system("clear")
                rast = random.randint(0, len(eng_word)-1)
                print(eng_word[rast])
                control = str(input("Do u remember this word ? Y/N:"))

                if rang != 1:
                    if control == 'y':
                        print(control,"bildin")
                        del eng_word[rast]
                    elif control == 'n':
                        print(control,"Bilemedin")
                    else:
                        print("adam akili bisey gir!")
                elif:
                    print("1 kaldiiiiiiiiiiiiiiii")
                    print(eng_word[0])

                    control2 = str(input("Do u remember this word ? Y/N:"))

                    if control2 == 'y':
                        print("bildinnn")
                        rang = 0
                    elif control2 == 'n':
                        pass
                    else:
                        print("adammm akilli bisy girr")
            except:
                print("bittii")
                input()
                rang = 0







if __name__ == '__main__':
    while True:
        main()