% https://en.wikipedia.org/wiki/Twelve_Olympians

deity(uranus).
male(uranus).

deity(gaia).
female(gaia).

deity(chronos).
male(chronos).
parent(chronos, uranus).
parent(chronos, gaia).

deity(rhea).
female(rhea).
parent(rhea, uranus).
parent(rhea, gaia).

deity(zeus).
male(zeus).
parent(zeus, chronos).
parent(zeus, rhea).

deity(hera).
female(hera).
parent(hera, chronos).
parent(hera, rhea).

deity(poseidon).
male(poseidon).
parent(poseidon, chronos).
parent(poseidon, rhea).

deity(hades).
male(hades).
parent(hades, chronos).
parent(hades, rhea).

deity(demeter).
female(demeter).
parent(demeter, chronos).
parent(demeter, rhea).

deity(hestia).
female(hestia).
parent(hestia, chronos).
parent(hestia, rhea).

deity(ares).
male(ares).
parent(ares, zeus).
parent(ares, hera).

deity(hephaestos).
male(hephaestos).
parent(hephaestos, zeus).
parent(hephaestos, hera).

deity(metis).
female(metis).

deity(athena).
female(athena).
parent(athena, zeus).
parent(athena, metis).

deity(leto).
female(leto).

deity(apollo).
male(apollo).
parent(apollo, zeus).
parent(apollo, leto).

deity(artemis).
female(artemis).
parent(artemis, zeus).
parent(artemis, leto).

deity(maia).
female(maia).

deity(hermes).
male(hermes).
parent(hermes, zeus).
parent(hermes, maia).

deity(semele).
female(semele).

deity(dionysos).
male(dionysos).
parent(dionysos, zeus).
parent(dionysos, semele).

god(X) :- male(X), deity(X).
goddess(X) :- female(X), deity(X).

% Father of X is Y
father(X, Y) :- parent(X, Y), male(Y).
% Mother of X is Y
mother(X, Y) :- parent(X, Y), female(Y).
% Grandfather of X is Y
% grandfather(X, Y) :- parent(X, Z), parent(Z, Y), male(Y).
grandfather(X, Y) :- parent(X, Z), father(Z, Y).

?- grandfather(X, Y).