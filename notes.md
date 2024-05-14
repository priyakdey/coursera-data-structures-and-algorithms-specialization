### Runtimes:

**Asymptotic Notation**

An estimation of a function, sequence as the input reaches a certain value.
Simply put, we do not care about constants involved in the computation, but
rather study the growth of time against the input size.

|                    |   n   | n _log_ n | n<sup>2</sup> |      2<sup>n</sup>       |
| :----------------: | :---: | :-------: | :-----------: | :----------------------: |
|       n = 20       | 1 sec |   1 sec   |     1 sec     |          1 sec           |
|       n = 50       | 1 sec |   1 sec   |     1 sec     |          13 day          |
| n = 10<sup>2</sup> | 1 sec |   1 sec   |     1 sec     | 4 \* 10<sup>3</sup> year |
| n = 10<sup>6</sup> | 1 sec |   1 sec   |    17 min     |                          |
| n = 10<sup>9</sup> | 1 sec |  30 sec   |    30 year    |                          |

These are rough estimations but gives us a good understanding of what time
complexity we should try and target for come complex algorithms and its input
size. This will allow us to decide for trade offs we make for different input
sizes.

**<u>Maximum values are</u>:**

|     Big O     |      Max n       |
| :-----------: | :--------------: |
|       n       |  10<sup>9</sup>  |
|   n _log_ n   | 10<sup>7.5</sup> |
| n<sup>2</sup> | 10<sup>4.5</sup> |
| 2<sup>n</sup> |        30        |

**<u>Big O comparison</u>:**

> _log_ n < n<sup>0.5</sup> < n < n _log_ n < n<sup>2</sup> < 2<sup>n</sup>

### Big-O Notation

Some function bounded by ........ (boring maths). Simply put, how does the
runtime scale according to input size' if sufficiently large input size is
considered how does the growth of the runtime is related to input size.

Big-O is a notation to define the performance or asymptotic runtime of the
function in terms of worst cases possible.


### Greedy Algorithms


