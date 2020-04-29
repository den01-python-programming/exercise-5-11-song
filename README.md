# Exercise 5.11 Song

In the exercise base there is a class called `Song` that can be used to create new objects that represent songs. Add to that class the `__eq__` method so that the similarity of songs can be examined.

```python
jack_sparrow = Song("The Lonely Island", "Jack Sparrow", 196)
another_sparrow = Song("The Lonely Island", "Jack Sparrow", 196)

if (jack_sparrow == another_sparrow):
    print("Songs are equal.")

if (jack_sparrow == "Another object"):
    print("Strange things are afoot.")
```

```plaintext
Songs are equal
```
