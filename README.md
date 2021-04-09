## anty-if-python

Original [Gilded Rose Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata), done with Python using [Arkademy's Anty-IF Framework](https://blog.arkency.com/anti-if-framework---if-slash-else-based-on-type/) and [mutmut](https://github.com/boxed/mutmut) mutation tests.


## How to use the Gilded Rose kata? *(based on the original repo)*

The simplest way is to just clone the code and start hacking away improving the design. You'll want to look at the ["Gilded Rose Requirements"](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/master/GildedRoseRequirements.txt) which explains what the code is for. I strongly advise you that you'll also need some tests if you want to make sure you don't break the code while you refactor.

You could write some unit tests yourself, using the requirements to identify suitable test cases. I've provided a failing unit test in a popular test framework as a starting point for most languages.

Alternatively, use the "Text-Based" tests provided in this repository. (Read more about that in the next section)

Whichever testing approach you choose, the idea of the exercise is to do some deliberate practice, and improve your skills at designing test cases and refactoring. The idea is not to re-write the code from scratch, but rather to practice designing tests, taking small steps, running the tests often, and incrementally improving the design. 


### TODO

* [x] add coverage support in tox
* [ ] update Makefile
* [x] update mutmut support
* [ ] add conjured item
* [ ] refactor Pythonic stuff
* [x] add MIT licence
* [x] write a nice README file

### Resources

* [How to use the Gilded Rose kata?](https://github.com/emilybache/GildedRose-Refactoring-Kata#how-to-use-this-kata)
* [Gilded Rose requirements](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.txt)
* [Andrzej Krzywda's Arkademy](https://courses.arkademy.dev/) - it's AWESOME and it includes, among others, the [Anty-IF course](https://arkency.com/anti-ifs/)
* [mutmut](https://github.com/boxed/mutmut) - a Python mutation testing system
