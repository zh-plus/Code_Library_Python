# CodeJam
Google OJ questions.
All the questions resolved currently can be retrieved on [Kick Start](https://codingcompetitions.withgoogle.com/kickstart/archive)

The input of almost all the questions is file, thus I reload the `input` as `input = lambda: input_file.readline().rstrip('\n')`.
However, the `print` is not reloaded since I want to see the output in the console. 

There'll be other OJ involved in the future.

#### template:
The python implementation of some common algorithms.
Most of them originate from the sudo code of [Introduction to Algorithms, Third Edition](https://mitpress.mit.edu/books/introduction-algorithms-third-edition)

In order to illustrate their performance intuitively, there will be a comparison between my implementation and python implementation.

By the way, the `Timer` class from timer.py is quite convenient for me. It is worth encasing your code into `Timer`
```
with Timer():
    # your code
```
instead of 
```
start = perf_counter()
# your code
print(perf_counter() - start, 's')
```
