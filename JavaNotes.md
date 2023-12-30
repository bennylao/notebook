# Java Notes

## String
In Java, String is *immutable*.

### String Methods

- String and Array
```java
char[] chars = { 'A', 'B', 'C', 'D', 'E', 'F' };

String stringFromChars = String.valueOf(chars); // "ABCDEF"

char[] charsFromString = stringFromChars.toCharArray();
// { 'A', 'B', 'C', 'D', 'E', 'F' }

String theSameString = new String(charsFromString); // "ABCDEF"
```

- Splitting the string
```java
String sentence = "a long text";
String[] words = sentence.split(" "); // {"a", "long", "text"}

String text = "Hello";
String[] parts = text.split(""); // {"H", "e", "l", "l", "o"}
```

- Sub-String
```java
String str = "Hello World!";

System.out.println(str.substring(2)); // llo World!
System.out.println(str.substring(2, 5)); // llo
System.out.println(str.substring(0, 5)); // Hello
```

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
