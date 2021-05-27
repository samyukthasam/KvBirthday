import sys
import time
from time import sleep
import itertools
import threading


print("")
print("")
print("")
print("                                                             *                            *   ")
sleep(0.30)
print('             *                             *                 |               *                                      *                   ')
sleep(0.30)
print('                          *                                 |||          *                  *             * ')
sleep(0.30)
print('                                   *                       |||||                    *                                              * ')

sleep(0.30)
print('                 *                                        |||||||          *                            * ')
sleep(0.30)
print('                            *                             $$$$$$$                 *   ')
sleep(0.30)
print('                                           *              |||||||                                                    * ')
sleep(0.45)
print('                       *            *                     $$$$$$$          *          ')
sleep(0.45)
print('                   *                                      |||||||                       *       ')
sleep(1)
print('                                                          $$$$$$$               *     ')
sleep(0.30)
print('                                  *                       $$$$$$$      *                      *  ')
sleep(0.30)
print('                                              *           |||||||                  *  ')
sleep(0.30)
print('               *                        |#.=$.$.=$.=$.$.=$.=$.$.=$.=$.$.=$.=$.$.=$.#|')
sleep(0.30)
print('                        *               ||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$||        *')
print('                                        |||||||| SAM  |||||||||||||||||||||||||||||||                    *  ')
sleep(0.45)
print('         *                              ||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$||      *                                     * ')
sleep(0.45)
print('                       *                ||||||||||||| WISHES ||||||||||||||||||||||||             *')
sleep(0.45)
print('                                        ||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$||       *                             *')
sleep(0.45)
print('                                        ||||||||||||||||   KARAN❤    |||||||||||||||                          *')
sleep(0.45)
print('             *                          ||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$||          *                           *')
sleep(1)
print('                                        ||||||||||||   HAPPY BIRTHDAY  ||||||||||||||       *')
sleep(0.45)
print('                       *                ||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%$$$$$$$$||                         *            ')
sleep(0.45)
print('                                        ||||||||||| ENTRPRENEUR  ||||||||||||||||||||        *')
sleep(1)
print('                                        ||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$||')
sleep(1)
print("")
def main():
    a = 0
    for x in range (0,8):
        a = a + 1
        b = ("Loading" + "." * a)
        # \r prints a carriage return first, so `b` is printed on top of the previous line.
        sys.stdout.write('\r'+b)

        time.sleep(0.5)
main()
sleep(1)
main()
print("")

print("")
sleep(2)
print("              I wish you many more happiest of birthdays!\n  ")
sleep(2)
print("              Live your life with smiles, not tears. ")
sleep(2)
print("")
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rHEY!! FightingCock😂, U are always my fav and best prsn forever🤝 \n\n\n   ')


t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(10)
done = True

#print (a)



# second code

import sys
import time
from time import sleep
import itertools
import threading
import emoji

love=emoji.emojize("HAPPY BIRTHDAY :red_heart:")
love1 = emoji.emojize(" :red_heart:")

print("")
print("")
print("")
print("                                                             *                            *   ")
sleep(0.30)
print(f'             *                              *                |               *        {love1}                              *                   ')
sleep(0.30)
print(f'                          *                   {love1}            |||          *                  *             * ')
sleep(0.30)
print('                                   *                       |||||                    *                                              * ')
sleep(0.30)
print(love                      ,'     *                     *             |||||||          *                            * ')
sleep(0.30)
print('                            *                             $$$$$$$                 *   ')
sleep(0.30)
print('                                           *              |||||||                                                    * ',love1)
sleep(0.45)
print('                       *            *                     $$$$$$$          *          ')
sleep(0.45)
print(love1,'                   *                                   |||||||                       *       ')
sleep(1)
print(f'*       {love1}.                                               $$$$$$$               *     ')
sleep(0.30)
print('                                  *                       $$$$$$$      *                      *  ',love1)
sleep(0.30)
print('                                              *           |||||||                  *  ')
sleep(0.30)
print('               *                        |#.=$.$.=$.=$.$.=$.=$.$.=$.=$.$.=$.=$.$.=$.#|')
sleep(0.30)
print('                        *               ||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$||        *')
print('                                        |||||||| JERY |||||||||||||||||||||||||||||||                 *  ')
sleep(0.45)
print('         *                              ||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$||      *                                     * ')
sleep(0.45)
print('                       *                ||||||||||| WISHES ||||||||||||||||||||||||||              *')
sleep(0.45)
print('                                        ||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$||       *                             *')
sleep(0.45)
print('                                        ||||||||||||||   HER TOM ||||||||||||||||||||                         *')
sleep(0.45)
print('             *                          ||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$||          *                           *')
sleep(1)
print('                                        ||||||||||||||||||||| KARAN KV ||||||||||||||       *',love1)
sleep(0.45)
print(love1,  '               *                     ||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%$$$$$$$$||                         * ',love1)
sleep(0.45)
print('                                        |||||||||||||HAPPY B DAY ||||||||||||||||||||        *')
sleep(1)
print('                                        ||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$||')
sleep(1)
print("")
print("")
def main():
    a = 0
    for x in range (0,8):
        a = a + 1
        b = ("Loading" + "." * a)
        # \r prints a carriage return first, so `b` is printed on top of the previous line.
        sys.stdout.write('\r'+b)

        time.sleep(0.5)
main()
sleep(1)
main()
print("")

print("")
sleep(2)
print("              Cheers to do lots of fi8 🥂  Ipolam andha force ae ilaye karan😂!\n  ",love1)
sleep(2)
print("              LIVE YOUR LIFE WITH SMILES, NOT TEARS. ",love1)
sleep(2)
print("")
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(f'\rGodbless You ✨{love1} \n\n\n  ')


t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(10)
done = True

print("Stay happy da and motivate, irritate and finaly fi8 with me Karan 😂")

from gtts import gTTS
import os

myText = "Hey Karan Happy BirthDay. We are always like Tom and Jerry only cause we always make fight, I want our friendship to be like Aurum and Argentum .Like it should be constant and not a variable as how we declare something in maths, For these many years we were so nice Friends but to understand you it took me a very long time , But I like the way how you behave with me and one thing which is static in you is you always irritate me but still I like that too since I had experienced a lot from you. Your Probability and Logic made us to talk after a very big fight. I always want my Entrepreneur Sir to be Happy and have a nice smile in your face. I like you so much as the best boy and the best person forever with lot of soft and humble character towards me, and raising my bp level especialy during exams,atleast from now give respect for me, With lots of love from me Stay happy and  be blessed  and I wish You should get everything You want in your life, aim for great heights and I am sure that you will become as the famous entrepreneur soon. Let us be Tom and Jerry always.Cheers to do more fight. Once again Sam wishes her tom Karan K V a very happy birthday Legend.How much ever we fight You are always the best for me. Have a smile now and party hard.... Be Happy Karan"

language = 'en'

speech = gTTS(text=myText, lang=language, slow=False)

speech.save("myText.mp3")

os.system("start myText.mp3")

