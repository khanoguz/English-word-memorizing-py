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
    [3]Delete a Word
    [4]Random mood
    [5]See all words
    """)
    
    choice1 = input(":")

    if choice1 == "1":
        flag = True
        while flag == True:
            db = sqlite3.connect("words.db")
            word = input("Write what you wanna find:")
            word = word.lower()
            cursor.execute("SELECT * FROM words WHERE english = '{}'".format(word))
            print(cursor.fetchone())
            sec = input("Any button for new word or q for main menu:")
            os.system("clear")
            db.close()
            if sec == "q":
                flag = False

    elif choice1 == "2":
        e_word = input("Write your English word:")
        t_word = input("Write the meaning of the word:")
        insert = "INSERT INTO words(english,Turkish) VALUES (?,?);"
        a = (e_word.lower(), t_word.lower())
        cursor.execute(insert,a)
        db.commit()
        input("ADDED")
        os.system("clear")
        db.close()
    elif choice1 == "3":

        wordd = input("Please write word that you wanna delete:")
        dell = cursor.execute("DELETE FROM words WHERE english = '{}'".format(wordd.lower()))
        db.commit()
        db.close()
        input("Enter for main")

    elif choice1 == "4":
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

                        del eng_word[rast]
                    elif control == 'n':
                        pass
                    else:
                        print("Please y or n")
                elif rang != 1:
                    print("Last one..")
                    print(eng_word[0])

                    control2 = str(input("Do u remember this word ? Y/N:"))

                    if control2 == 'y':
                        print("Correct..")
                        rang = 0
                    elif control2 == 'n':
                        pass
                    else:
                        print("Please y or n")
            except:
                print("Congratulations..")
                input()
                rang = 0


    elif choice1 == "5":
        os.system("clear")
        db = sqlite3.connect("words.db")
        eng_words = []
        sql = "SELECT * FROM words"
        cursor.execute(sql)
        words = cursor.fetchall()

        for i in words:
            eng_words.append(i)


        print("-------There is {} words in the database-------".format(len(eng_words)))

        for a in eng_words:
            print(a)
        input("Enter for main menu")

    else:
        print("Please choose something!")


if __name__ == '__main__':
    while True:
        main()