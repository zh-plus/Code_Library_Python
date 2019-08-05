# Hao Zheng's Algorithm Code Library.
~~The very first reason I start this repo is preparing for google's SWE interview using Python.~~
But in order to keep my Java skills warm, I'll maintain a Java version of Code Library in [there](https://github.com/zh-plus/Code_Library_Java).
As a CS major student, I will try my best to make my implementation elegant in both of them.

Currently, there's Codeforces and CodeJam waiting for me.

## Codeforces
Well known OJ platform.

#### Tips:
In order to pass the time-limited Codeforces tests, I recommend [PyPy 3.5 (6.0.0)](https://pypy.org/) as interpreter, which is several times 
faster than origin Python interpreter nowadays(2018.12).


## CodeJam
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
