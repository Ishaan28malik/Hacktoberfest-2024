/*
 * Program to implement One Player Tic-Tac-Toe using the Minimax Algorithm
 * Swapnil mishra
 */

% Start the game
:-initialization(play).

/*
 * To start the game with the blank board, turn number 1, and move number 1
 */
play:- write('\n'),playHelp([0,0,0,0,0,0,0,0,0],1,1).

/*
 * To display the board
 */ 
% If the position being displayed is not the last in a row
bdisplay(X,I):-mod(I,3)=\=0,nth(I,X,Y),write(' '),write(Y),write(' |'),J is I+1,bdisplay(X,J).
% If the position being displayed is the last in a row, but not the last element
bdisplay(X,I):-mod(I,3)=:=0,I=\=9,nth(I,X,Y),write(' '),write(Y),write('\n---+---+---\n'),J is I+1,bdisplay(X,J).
% If the position being displayed is the last element
bdisplay(X,I):-I=:=9,nth(I,X,Y),write(' '),write(Y),write('\n\n'),!.

/*
 * To accept input from the user, and store the value Y in position (I,J) in NX, the modified
 * list of X
 */
addInputUser(X,Y,NX):-write('Enter row number:\n'),read_integer(I),write('Enter column number:\n'),read_integer(J),changeList(X,I,J,Y,NX).

/*
 * To change the (I,J)th value of the list with Y and bind it to NX
 */
changeList([_,A12,A13,A21,A22,A23,A31,A32,A33],1,1,Y,NX):-NX=[Y,A12,A13,A21,A22,A23,A31,A32,A33].
changeList([A11,_,A13,A21,A22,A23,A31,A32,A33],1,2,Y,NX):-NX=[A11,Y,A13,A21,A22,A23,A31,A32,A33].
changeList([A11,A12,_,A21,A22,A23,A31,A32,A33],1,3,Y,NX):-NX=[A11,A12,Y,A21,A22,A23,A31,A32,A33].
changeList([A11,A12,A13,_,A22,A23,A31,A32,A33],2,1,Y,NX):-NX=[A11,A12,A13,Y,A22,A23,A31,A32,A33].
changeList([A11,A12,A13,A21,_,A23,A31,A32,A33],2,2,Y,NX):-NX=[A11,A12,A13,A21,Y,A23,A31,A32,A33].
changeList([A11,A12,A13,A21,A22,_,A31,A32,A33],2,3,Y,NX):-NX=[A11,A12,A13,A21,A22,Y,A31,A32,A33].
changeList([A11,A12,A13,A21,A22,A23,_,A32,A33],3,1,Y,NX):-NX=[A11,A12,A13,A21,A22,A23,Y,A32,A33].
changeList([A11,A12,A13,A21,A22,A23,A31,_,A33],3,2,Y,NX):-NX=[A11,A12,A13,A21,A22,A23,A31,Y,A33].
changeList([A11,A12,A13,A21,A22,A23,A31,A32,_],3,3,Y,NX):-NX=[A11,A12,A13,A21,A22,A23,A31,A32,Y].

/*
 * To change the Ith value in the list with Y and bind it to NX
 */
changeOneDList([_,A2,A3,A4,A5,A6,A7,A8,A9],1,Y,NX):-NX=[Y,A2,A3,A4,A5,A6,A7,A8,A9].
changeOneDList([A1,_,A3,A4,A5,A6,A7,A8,A9],2,Y,NX):-NX=[A1,Y,A3,A4,A5,A6,A7,A8,A9].
changeOneDList([A1,A2,_,A4,A5,A6,A7,A8,A9],3,Y,NX):-NX=[A1,A2,Y,A4,A5,A6,A7,A8,A9].
changeOneDList([A1,A2,A3,_,A5,A6,A7,A8,A9],4,Y,NX):-NX=[A1,A2,A3,Y,A5,A6,A7,A8,A9].
changeOneDList([A1,A2,A3,A4,_,A6,A7,A8,A9],5,Y,NX):-NX=[A1,A2,A3,A4,Y,A6,A7,A8,A9].
changeOneDList([A1,A2,A3,A4,A5,_,A7,A8,A9],6,Y,NX):-NX=[A1,A2,A3,A4,A5,Y,A7,A8,A9].
changeOneDList([A1,A2,A3,A4,A5,A6,_,A8,A9],7,Y,NX):-NX=[A1,A2,A3,A4,A5,A6,Y,A8,A9].
changeOneDList([A1,A2,A3,A4,A5,A6,A7,_,A9],8,Y,NX):-NX=[A1,A2,A3,A4,A5,A6,A7,Y,A9].
changeOneDList([A1,A2,A3,A4,A5,A6,A7,A8,_],9,Y,NX):-NX=[A1,A2,A3,A4,A5,A6,A7,A8,Y].

/*
 * To help play, by doing different things based on the input. X is the Board, the second argument
 * is the player whose turn it is, and the third argument is the move number in the game
 */
/*
 * If it is the player 1's turn, all moves haven't taken place, player 2 hasn't won yet, then display
 * the board, accept input, modify the board, and call play help with the modified board, player 2's turn,
 * and move number increased by 1
 */
playHelp(X,1,MoveNumber):-MoveNumber<10,\+checkWin(X,2),bdisplay(X,1),addInputUser(X,1,NX),NextMove is MoveNumber+1,playHelp(NX,2,NextMove).
/*
 * If it is player 1's turn, all moves haven't taken place, player 2 has won, then display the
 * board and declare player 2 to be the winner
 */
playHelp(X,1,MoveNumber):-MoveNumber<10,checkWin(X,2),bdisplay(X,1),giveResult(2),!.
/*
 * If it is the player 2's turn, all moves haven't taken place, it is not player 2's first move, 
 * player 1 hasn't won yet, then display the board, get the program's input, modify the board,
 * and call play help with the modified board, player 1's turn, and move number increased by 1
 */
playHelp(X,2,MoveNumber):-MoveNumber>2,MoveNumber<10,\+checkWin(X,1),bdisplay(X,1),computerPlay(X,NX),NextMove is MoveNumber+1,playHelp(NX,1,NextMove).
/*
 * If it is player 2's turn, all moves haven't taken place, player 1 has won, then display the
 * board and declare player 1 to be the winner
 */
playHelp(X,2,MoveNumber):-MoveNumber>2,MoveNumber<10,checkWin(X,1),bdisplay(X,1),giveResult(1),!.
/*
 * If it is player 2's turn, the computer's turn, it is its first move, the center cell is empty,
 * then play in the center cell
 */
playHelp(X,2,MoveNumber):-MoveNumber=:=2,nth(5,X,Value),Value=:=0,changeOneDList(X,5,2,NX),bdisplay(X,1),NextMove is MoveNumber+1,playHelp(NX,1,NextMove).
/*
 * If it is player 2's turn, the computer's turn, it is its first move, the center cell is not empty,
 * then play in the first cell
 */
playHelp(X,2,MoveNumber):-MoveNumber=:=2,nth(1,X,Value),Value=:=0,changeOneDList(X,1,2,NX),bdisplay(X,1),NextMove is MoveNumber+1,playHelp(NX,1,NextMove).
/*
 * If the board is full, and player 1 has won, then declare it to be the winner
 */
playHelp(X,_,10):-checkWin(X,1),giveResult(1),!.
/*
 * If the board is full, and player 1 has not won, then it must be a draw, so declare a draw
 */
playHelp(X,_,10):- \+checkWin(X,1),giveResult(0),!.

/*
 * List of all victory conditions in Tic-Tac-Toe
 */
checkWin([A11,A12,A13,_,_,_,_,_,_],I):-A11=I,A11=A12,A12=A13.
checkWin([_,_,_,A21,A22,A23,_,_,_],I):-A21=I,A21=A22,A22=A23.
checkWin([_,_,_,_,_,_,A31,A32,A33],I):-A31=I,A31=A32,A32=A33.
checkWin([A11,_,_,A21,_,_,A31,_,_],I):-A11=I,A11=A21,A21=A31.
checkWin([_,A12,_,_,A22,_,_,A32,_],I):-A12=I,A12=A22,A22=A32.
checkWin([_,_,A13,_,_,A23,_,_,A33],I):-A13=I,A13=A23,A23=A33.
checkWin([A11,_,_,_,A22,_,_,_,A33],I):-A11=I,A11=A22,A22=A33.
checkWin([_,_,A13,_,A22,_,A31,_,_],I):-A31=I,A31=A22,A22=A13.

/*
 * To display the result based on who wins
 */
giveResult(0):-write('Draw!\n').
giveResult(1):-write('You win!\n').
giveResult(2):-write('I win!\n').

/*
 * For taking the board X, and modifying it with the computer's move and binding it to NX
 */
computerPlay(X,NX):-findBestMove(X,NewPos),changeOneDList(X,NewPos,2,NX).

/*
 * To check if any moves are left in the game
 */
/*
 * Call the isMovesHelper, with 1 to aid recursion
 */
isMovesLeft(X):- \+isMovesLeftHelper(X,1).
/*
 * If I<10, i.e., recursion is to continue, then check if the Ith position is non-zero, and
 * recurse with I+1
 */
isMovesLeftHelper(X,I):-I<10,nth(I,X,Value),Value=\=0,NextI is I+1,isMovesLeftHelper(X,NextI).
/*
 * If I is 10, then stop recursing
 */
isMovesLeftHelper(_,I):-I=:=10.

/*
 * To evaluate the score, based on the state of the board
 */
% If player 2 has won, then the score is 10
evaluate(X,Score):-checkWin(X,2),Score is 10.
% If player 1 has won, then the score is -10
evaluate(X,Score):-checkWin(X,1),Score is (-10).
% If no one has one, then the score is 0
evaluate(X,Score):- \+checkWin(X,1),\+checkWin(X,2),Score is 0.

/*
 * For finding the minimax value
 */
/*
 * If the score is 10, i.e., player 2 is winning, then result is the score
 */
minimax(X,Depth,_,Result):-evaluate(X,Score),Score=:=10,Result=Score-Depth,!.
/*
 * If the score is -10, i.e., player 1 is winning, then result is the score
 */
minimax(X,Depth,_,Result):-evaluate(X,Score),Score=:=(-10),Result=Score+Depth,!.
/*
 * If no moves are left, then result is 0
 */
minimax(X,_,_,Result):- \+isMovesLeft(X),Result=0,!.
/*
 * If player 2's turn is being simulated, then find the best move for player 2 from this stage
 */
minimax(X,Depth,IsMax,Result):-isMovesLeft(X),IsMax = 1,Best is (-1000),
NewDepth is Depth+1,
(
((nth(1,X,Value1),Value1=:=0,changeOneDList(X,1,2,NX1),minimax(NX1,NewDepth,0,Result1));Result1 is Best),
((nth(2,X,Value2),Value2=:=0,changeOneDList(X,2,2,NX2),minimax(NX2,NewDepth,0,Result2));Result2 is Best),
((nth(3,X,Value3),Value3=:=0,changeOneDList(X,3,2,NX3),minimax(NX3,NewDepth,0,Result3));Result3 is Best),
((nth(4,X,Value4),Value4=:=0,changeOneDList(X,4,2,NX4),minimax(NX4,NewDepth,0,Result4));Result4 is Best),
((nth(5,X,Value5),Value5=:=0,changeOneDList(X,5,2,NX5),minimax(NX5,NewDepth,0,Result5));Result5 is Best),
((nth(6,X,Value6),Value6=:=0,changeOneDList(X,6,2,NX6),minimax(NX6,NewDepth,0,Result6));Result6 is Best),
((nth(7,X,Value7),Value7=:=0,changeOneDList(X,7,2,NX7),minimax(NX7,NewDepth,0,Result7));Result7 is Best),
((nth(8,X,Value8),Value8=:=0,changeOneDList(X,8,2,NX8),minimax(NX8,NewDepth,0,Result8));Result8 is Best),
((nth(9,X,Value9),Value9=:=0,changeOneDList(X,9,2,NX9),minimax(NX9,NewDepth,0,Result9));Result9 is (-1000))),
FindMaxFrom = [Result1,Result2,Result3,Result4,Result5,Result6,Result7,Result8,Result9],
max_list(FindMaxFrom,Result).

/*
 * If player 1's turn is being simulated, then find the best move for player 1 from this stage
 */
minimax(X,Depth,IsMax,Result):-isMovesLeft(X),IsMax = 0,Best is 1000,
NewDepth is Depth+1,
(
((nth(1,X,Value1),Value1=:=0,changeOneDList(X,1,1,NX1),minimax(NX1,NewDepth,1,Result1));Result1 is Best),
((nth(2,X,Value2),Value2=:=0,changeOneDList(X,2,1,NX2),minimax(NX2,NewDepth,1,Result2));Result2 is Best),
((nth(3,X,Value3),Value3=:=0,changeOneDList(X,3,1,NX3),minimax(NX3,NewDepth,1,Result3));Result3 is Best),
((nth(4,X,Value4),Value4=:=0,changeOneDList(X,4,1,NX4),minimax(NX4,NewDepth,1,Result4));Result4 is Best),
((nth(5,X,Value5),Value5=:=0,changeOneDList(X,5,1,NX5),minimax(NX5,NewDepth,1,Result5));Result5 is Best),
((nth(6,X,Value6),Value6=:=0,changeOneDList(X,6,1,NX6),minimax(NX6,NewDepth,1,Result6));Result6 is Best),
((nth(7,X,Value7),Value7=:=0,changeOneDList(X,7,1,NX7),minimax(NX7,NewDepth,1,Result7));Result7 is Best),
((nth(8,X,Value8),Value8=:=0,changeOneDList(X,8,1,NX8),minimax(NX8,NewDepth,1,Result8));Result8 is Best),
((nth(9,X,Value9),Value9=:=0,changeOneDList(X,9,1,NX9),minimax(NX9,NewDepth,1,Result9));Result9 is Best)),
FindMinFrom = [Result1,Result2,Result3,Result4,Result5,Result6,Result7,Result8,Result9],
min_list(FindMinFrom,Result).

/*
 * Find the best move to be played at this point
 */
findBestMove(X,NewPos):-Best is (-1000),
(
((nth(1,X,Value1),Value1=:=0,changeOneDList(X,1,2,NX1),minimax(NX1,0,0,Result1));Result1 is Best),
((nth(2,X,Value2),Value2=:=0,changeOneDList(X,2,2,NX2),minimax(NX2,0,0,Result2));Result2 is Best),
((nth(3,X,Value3),Value3=:=0,changeOneDList(X,3,2,NX3),minimax(NX3,0,0,Result3));Result3 is Best),
((nth(4,X,Value4),Value4=:=0,changeOneDList(X,4,2,NX4),minimax(NX4,0,0,Result4));Result4 is Best),
((nth(5,X,Value5),Value5=:=0,changeOneDList(X,5,2,NX5),minimax(NX5,0,0,Result5));Result5 is Best),
((nth(6,X,Value6),Value6=:=0,changeOneDList(X,6,2,NX6),minimax(NX6,0,0,Result6));Result6 is Best),
((nth(7,X,Value7),Value7=:=0,changeOneDList(X,7,2,NX7),minimax(NX7,0,0,Result7));Result7 is Best),
((nth(8,X,Value8),Value8=:=0,changeOneDList(X,8,2,NX8),minimax(NX8,0,0,Result8));Result8 is Best),
((nth(9,X,Value9),Value9=:=0,changeOneDList(X,9,2,NX9),minimax(NX9,0,0,Result9));Result9 is Best)),
FindMinFrom = [Result1,Result2,Result3,Result4,Result5,Result6,Result7,Result8,Result9],
max_list(FindMinFrom,Value),
nth(NewPos,FindMinFrom,Value).
