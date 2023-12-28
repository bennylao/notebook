# Java Notes

## String
In Java, String is *immutable*.

### Formatted Output
To format output or strings, use ```System.out.printf()``` or ```String.format()``` methods.

```java

// format print
System.out.printf("My name is %s and I am %d years old.", "Benny", 21);

// format string
String s = String.format("My name is %s and I am %d years old.", "Benny", 21);
System.out.println(s);

/*format spcifier*/

// %d - integer
System.out.printf("\nInteger: %d", 10);
// %f - float
System.out.printf("\nFloat: %.2f", 123.4567);
// %s - string
System.out.printf("\nString: %s", "Hello");
// %c - character
System.out.printf("\nCharacter: %c", 'A');
```


### StringBuilder
In order to construct a String, ```StringBuilder``` is used.

- StringBuilder Constructor

```java
// create empty stringbuilder
StringBuilder sb = new StringBuilder();

// create stringbuilder with string "Hello"
StringBuilder sb = new StringBuilder("Hello");
```

- StringBuilder Methods

```java
// create empty stringbuilder
StringBuilder sb = new StringBuilder();

// length of stringbuilder
sb.length();

// capacity of stringbuilder
sb.capacity();

// append string to stringbuilder
sb.append("Hello");

// reverse the string
sb.reverse();

// insert string at index i
sb.insert(i, "Hello");

// replace string
sb.replace(i, j, "Hello");

// return character at index i
sb.charAt(i);

// replace character at index i
sb.setCharAt(i, 'a');

// delete character at index i
sb.deleteCharAt(i);

// delete from index i to index j
sb.delete(i, j);
```
