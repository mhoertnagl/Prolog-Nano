```prolog
human(socrates).
human(aristotle).
human(plato).
god(zeus).
god(apollo).
mortal(X) :- human(X).

?- human(socrates)
```

```bnf
program : rule+ query+

query : '?-' term '.'

rule : term '.'
     | term :- terms '.'

terms : term
      | term ',' terms

term : PREDICATE '(' terms ')'
     | PREDICATE
     | VARIABLE
```

This grammar is rather simplistic and allows non-sensical input like A :- a. Or a :- A.

* https://en.wikipedia.org/wiki/Twelve_Olympians
* List support
* Numbers?
* Strings
* Extensive example - greek pantheon
* other examples from Prolog books
* https://github.com/maldoinc/mamba/blob/master/setup.py

# Ressources

* [Prol](https://gist.github.com/brunokim/0a737a8642b756a5d0dcc3a07ec1ef81)
* [py4fun](http://www.openbookproject.net/py4fun/)
* [Python-Prolog-Interpreter](https://github.com/photonlines/Python-Prolog-Interpreter)
* [Prolo Examples](http://www.cs.toronto.edu/~sheila/384/w11/simple-prolog-examples.html)

* [Twelve Olympians](https://en.wikipedia.org/wiki/Twelve_Olympians)
* [Family Tree Of The Greek Gods](https://en.wikipedia.org/wiki/Family_tree_of_the_Greek_gods)
