def game():
       player1=input("Enter the name of player1:")
       player2=input("Player2 name:")
       sticks=16
       print("Game started")
       remaining=sticks
       while (remaining>0):
            play1=int(input("Enter the choice of first player:"))
            if play1>3 or play1==0:
                print("invalid")
                break
            remaining=remaining-play1
            print("Remaining=", remaining)
            if remaining==0:
                     print("Player 1 Loses")
            else:("Win1")
            play2=int(input("Enter the choice of player2:"))
            remaining=remaining-play2
            print("Remaining=",remaining)
            if remaining==0:
                  print(" Player 2 loses")
            else:("win2")


game()
