entree(salade).
entree(avocat).
entree(soupe).
entree(huitre).

dessert(raisin).
dessert(melon).

viande(steak).
viande(escalope).

poisson(truitre).
poisson(daurade).

calories(salade,15).
calories(raisin,70).
calories(avocat,220).
calories(melon,27).
calories(huitre,70).
calories(soupe,70).
calories(steak,203).
calories(truitre,98).
calories(escalope,105).
calories(daurade,90).

plat(V):- viande(V).
plat(V):- poisson(V).

repas(E,P,D):- entree(E),plat(P),dessert(D).
calculcal(E,P,D,V):- repas(E,P,D),calories(E,X),calories(P,Y),calories(D,Z),V is X+Y+Z.

min([X],X).
min([X,Y|L],M):- calories(X,A),calories(Y,B), min([X|L],M),A=<B.
min([X,Y|L],M):- calories(X,A),calories(Y,B), min([Y|L],M),A>B.
minRepas(Me,Mp,Md):- min([salade,avocat,soupe,huitre],Me),min([steak,escalope,truitre,daurade],Mp),min([raisin,melon],Md).
