# Lists

We're going to start off this set of assignments with a little teaser. What does this code do?
```
def reverse_list(x):
    for i in range(len(x) // 2):
        x[i],x[-(i+1)] = x[-(i+1)],x[i]

y = [1, 2, 3, 4, 5, 6]
reverse_list(y)
print(y)
```

If you try it, you'll see that it will reverse "y". Python actually has this inbuilt already (try `y.reverse()`).
However, something like this doesn't seem to work:
```
def square_value(x):
    x = x * x

y = 4
square_value(y)
print(y) # Why does this not print 16?
```

The answer is a little subtle, but basically, Python treats some types (like numbers) differently from other types (like lists, dicts, and "objects").

## Why?

To answer why, we should dive into the following concepts a little bit: `Reference vs. Value` and `Immutability vs. Mutability`.

### References vs. Values

In a Python program, a variable "points to" or "refers to" some value. When we write:

```
x = 3
```

You can think of it like we have two spaces: a "variable" space and a "value" space, with variables "pointing to" values. i.e.

```

                     ┌────┐
x───────────────────►│ 3  │
                     └────┘
```

When we write:
```
y = x
```
Python has to figure out what you're intending to do. The general rule is, for
"primitive" types (numbers, floats, bools), **copy** the value.

```

                     ┌────┐
x───────────────────►│ 3  │
                     └────┘
                     ┌────┐
y───────────────────►│ 3  │
                     └────┘
```

So what if instead we had a list?
```
x = [1, 2, 3]
```

```
                     ┌───────────┐
x───────────────────►│ [1, 2, 3] │
                     └───────────┘
```
Now if we do:
```
y = x # What should we do here?
```
A long time ago, the designer of Python decided that instead of **copying** the
entire list (which could be arbitrarily long and be very slow), we should just
"copy the reference". In other words, whatever value x is pointing to, y will also point to that same value:

```
                     ┌──────────┐     
x───────────────────►│ [1, 2, 3]│
                     └─▲────────┘     
                       │        
y──────────────────────┘        
```

Note that this *also* applies to when we call functions. So this is why the `square` function from above doesn't change the y value. You can think of it like when we call the function, Python is *implicitly* calling the `=` operator. In the case of the `square function`:

```
def square_value(x):
    x = x * x

y = 4
square_value(y) # This calls x = y under the hood and *copies* the value!
print(y) # Why does this not print 16?
```

### Immutability vs. Mutability

This is relatively straightforward as a concept: immutability just means that the value can't be directly mutated by the caller after it's created. Python has some immutable types (numbers, strings, floats).

For example, if we do:
```
x = "Hello"
```
there is *no* way to change the *value* of the "Hello" string. So here's a question: what is happening here?
```
x = "HELLO"
x = x.lower()
print(x) # Prints "hello"
```

So doesn't this violate the immutability of strings? Not quite! Note that I had to write out: `x = x.lower()` (not just `x.lower()`). What's actually happening here is that x.lower() is returning a **new** string (a copy!) of the old one. This may not seem particularly important, but look at this example:

```
original_string = "HI YASMINA"
lowered_string = original_string.lower()
print(original_string) # Prints "HI YASMINA"
print(lowered_string) # Prints "hi yasmina"
```

Being able to work with immutable objects is often a lot simpler to reason about regarding program behavior, so we like to use immutable objects wherever possible. The downside is sometimes that modifying immutable objects requires copies.

There's also another important point to make about immutability, namely that immutability doesn't go deeper than one level. So for example, tuples are immutable in Python, but:

```
x = (1, 2, ["hi"])
y = x[2]
y.append("there")
print(x) # Prints (1, 2, ["hi", "there"])
```
This is sometimes referred to as "interior mutability". The tuple objects forbids top-level or direct reassignment of the values, but not any deeper than that! A diagram of this might look like:

```
                       ┌──────┐              
                       │["hi"]│◄───┐        
                       └──────┘    │        
                                   │        
                                   │        
                       ┌───────────┼───────┐
                       │           │       │
x─────────────────────►│ (1, 2, list_ref)  │
                       └───────────────────┘
```

Then we do `y=x[2]`:

```
                       ┌──────┐              
                       │["hi"]│◄───┐        
                       └──────┘    │        
                                   │        
                                   │        
                       ┌───────────┼───────┐
                       │           │       │
x─────────────────────►│ (1, 2, list_ref)◄─────y 
                       └───────────────────┘
```
And we can effectively mutate a value via the `y` variable. However, note that:

```
y = [1, 2, 3] # This reassignment is totally fine.
x[2] = [1, 2, 3] # This will fail!
```
Why does this fail? Make sure this concept is clear before moving to the next assignment!

# Assignment 1: Immutable List

Python's list is completly mutable. We can set values once we've created the list, but this doesn't offer nice guarantees around immutability in situations where we don't want functions or other downstream consumers editing our list. We're going to make a new class (`Immutable List`), which will operate like a list, except that it will explicitly *forbid* adding to a list or modifying any of its elements. Here is the template of our class:

```
class ImmutableList:
    def __init__(self, input_list):
        self.backing_list = input_list
    
    def append(self, item):
        # Implement!
    
    def __getitem__(self, i):
        # Implement!
    
    def __setitem__(self, i, value):
        # Implement!
```

The way this could be used is like:
```
x = ImmutableList([1, "hello", 3])
y = x
print(x[1]) # Prints "hello"
y[0] = 5 # error!!
```
Write your implementation in `immutable_list.py`.

# Assignment 1: Copy-on-Write (CoW) List

The last assignment should have reminded you of Python's in-built "tuple" class, but now we're going to actually build something useful. Imagine we wanted to implement the following behavior: A list that *only* copies itself if it is directly modified.

So in other words, something like this:
```
x = CowList([1, 2, 3])
y = x
x = x.set_value(0, "hello")
print(x) # This should print ["hello", 2, 3]
print(y) # This should print [1, 2, 3]
```

A benefit of using this class is that we reap the benefits of passing by reference and avoiding copies, but we copy if a downstream consumer tries to change our list. This way we have safety with performance.

```
class CowList:
    def __init__(self, input_list):
        self.backing_list = input_list
    
    def __getitem__(self, i):
        # Implement!

    def append(self, item):
        # Implement!
    
    def set_value(self, i, value):
        # Implement!
```

Write your implementation in `cow_list.py`.