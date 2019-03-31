# non-determenistic-finite-automaton

@Sources
https://en.wikipedia.org/wiki/Regular_expression
<br/>
https://swtch.com/~rsc/regexp/regexp1.html
<br/>
https://en.wikipedia.org/wiki/Shunting-yard_algorithm
<br/>
The following youtube video helped me understand NFA
https://www.youtube.com/watch?v=X8nlQPyHsp4
<br/>
Huge amount of knowledge acquired on this subject was attained following the professors video tutorials which he posted online
on our college website.
(unsure if sourcing these videos is allowed)

The python script starts off with the Shunting algorythm which converts a regular expression from infix notation to postfix
notation so that the computer can read it quickly and efficiantly from left to right in one parse.

After that there is the Thomsons construction, with a state class with two edges and a class for NFA, this is where the 
postfix notation is read and based on the character or operator a chunk of code is executed and then it is pushed to the stack.

After that there is a helper function which is named followes, it returns the set of states that can be reached
from state following e arrow.
Finally a maching function which compares an infix expressions with a few strings returning true or false.
