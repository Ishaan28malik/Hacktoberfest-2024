fun main() {
    //Converting my NumberGame.java from Nov 2018 to Kotlin

    //In this program, the computer randomly selects a number between 1 and 100 and saves it
    //Then the player is to correctly guess the number
    val msg =
        "I have chosen a random number between 1 and 100. Try guessing it to win the game. Select difficulty to know your number of retries \nLet's Start!"
    println(msg)
    println("Select Difficulty: \n 1 = Guesser\n 2 = Mind Reader\n 3 = Telepath")

    try {
        val difficulty: Int = readLine()!!.toInt()
        val retries: Int
        if (difficulty in 1..3) {
            retries = when (difficulty) {
                1 -> {
                    println("Let's get to it!")
                    10
                }
                2 -> {
                    println("Mind Reader, right?? Let's see what you can do!")
                    6
                }
                else -> {
                    println("Telepath, Uh- ho")
                    3
                }
            }
            game(retries)
        } else {
            println("Please, Restart the Game and Select a Valid Option.")
        }
    } catch (e: Exception) {
        println("Please, Restart the Game and Select a Valid Option.")
    }
}

fun game(retries: Int) {
    var hasWon = false
    val number: Double = (Math.random() * 100) + 1
    val guess: Int = number.toInt()
    try {
        loop@ for (i in retries downTo 1) {
            if (i == 1)
                println("LAST GUESS")
            else
                println("You have $i retries left")
            val usersGuess = readLine()!!.toInt()
            when {
                usersGuess < guess -> println("$usersGuess is less than the answer")
                usersGuess > guess -> println("$usersGuess is greater than the answer")
                else -> {
                    hasWon = true
                    break@loop
                }
            }
        }
        if (hasWon) {
            println("Correct! You Have Won!!")
        } else {
            println("You Are Out of Tries\nThe Correct Answer is $guess. Better Luck Next Time...")
        }
    } catch (e: Exception) {
        println("Only Integer Inputs Are Allowed")
    }
}

