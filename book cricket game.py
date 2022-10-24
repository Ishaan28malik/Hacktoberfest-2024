for overs in range(1, numOvers + 1): 

  if endGame: #.........set to true from inner loop when breaking
            break

    print()
    print("---------------------------")
    print("Enter runs for over ", overs)
    print("---------------------------")

    #inner loop for number of balls in the over 
    for _runs in range(1, BALLS_IN_OVER + 1): 

      #calculate the number of overs and remainding balls
      totalBallsFaced += 1 
      totalOversFaced = (totalBallsFaced // BALLS_IN_OVER)    
      partOverFaced = (totalBallsFaced % BALLS_IN_OVER) 

      #print()
      runs = int(input("> ")) #...........prompt user for runs

      if runs < 0:#.......................if negative number, add to 1 to wicket
        wicket += 1
        print("Batter out...")

        if wicket >= 10:#...............if batter out and if all batters out then team out
          print("Batters all out")
          endGame = 1 #..............set to true
          break #.......................break to outer loop
      else: 
        total += runs #..................if input >= 0 , add to total
