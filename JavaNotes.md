# Java Notes

## Performance

### List vs HashSet
The set will give much better performance (O(n) vs O(n^2) for the list), 
and that's normal because set membership (the contains operation) is the very purpose of a set.

Contains for a HashSet is O(1) compared to O(n) for a list, therefore you should never use a list if you often need to run contains.
```java
ArrayList<Integer> list = new ArrayList<>();
HashSet<Integer> set = new HashSet<>();
```

## String
In Java, String is *immutable*.

### String Methods

#### String and Array
```java
char[] chars = { 'A', 'B', 'C', 'D', 'E', 'F' };

String stringFromChars = String.valueOf(chars); // "ABCDEF"

char[] charsFromString = stringFromChars.toCharArray();
// { 'A', 'B', 'C', 'D', 'E', 'F' }

String theSameString = new String(charsFromString); // "ABCDEF"
```

#### Splitting the string
```java
String sentence = "a long text";
String[] words = sentence.split(" "); // {"a", "long", "text"}

String text = "Hello";
String[] parts = text.split(""); // {"H", "e", "l", "l", "o"}
```

####Sub-String
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

#### StringBuilder Constructor

```java
// create empty stringbuilder
StringBuilder sb = new StringBuilder();

// create stringbuilder with string "Hello"
StringBuilder sb = new StringBuilder("Hello");
```

#### StringBuilder Methods

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

## Exceptions and Error

### Exception Handling

```java
// try with resources
// scanner 1 and scanner 2 will be closed automatically after the try block
try (Scanner scanner1 = new Scanner(file); Scanner scanner2 = new Scanner(file2)) {
    // code that may throw exceptions
} catch (SQLException | IOException e) {
    // handling SQLException, IOException and their subclasses
    System.out.println(e.getMessage());
} catch (Exception e) {
    // handling any other exceptions
    System.out.println("Something goes wrong");
} finally {
    // code that will always be executed
}
```

#### Usage of Try with Resources
Look at the example:

```java
Reader reader = new FileReader("file.txt");
// code which may throw an exception
reader.close();
```
Suppose something goes wrong before the close invocation and an exception is thrown. 
It leads to a situation in which the method will never be called and 
system resources won't be released. It is possible to solve the problem by using the try-catch-finally construction:

```java
void readFile() throws IOException {
  Reader reader = null;
  try {
    reader = new FileReader("file.txt");
    throw new RuntimeException("Exception1");
  } finally {
    reader.close(); // throws new RuntimeException("Exception2")
  }
}
```

To ensure the code is robust and all the exceptions are handled, we can update the code in the following way:
```java
void readFile() throws IOException {
    Reader reader = null;
    try {
        reader = new FileReader("file.txt");
        throw new RuntimeException("Exception1");
    } finally {
        try {
            reader.close(); // throws new RuntimeException("Exception2")
        } catch (Exception e) {
            // handle the Exception2
        }
    }
}
```

However, the code can be more verbose and hard to read. Hence, we can use the ```try-with-resources``` construct instead:
```java
try (Reader reader1 = new FileReader("file1.txt");
     Reader reader2 = new FileReader("file2.txt")) {
    // some code
}
// reader1 and reader2 will be closed automatically after try and catch
```

### Common Exceptions

- NullPointerException
- NegativeArraySizeException
- IndexOutOfBoundsException
  - ArrayIndexOutOfBoundsException
  - StringIndexOutOfBoundsException
- NumberFormatException
- FileNotFoundException
- IOException
- InputMismatchException
- ArithmeticException

```java
int[] numbers = null;
int size = numbers.length; // It throws a NullPointerException

int[] numbers = new int[negSize]; // It throws a NegativeArraySizeException

List<Integer> numbers = new ArrayList<>();
numbers.add(1);
int number = numbers.get(numbers.size()); // It throws an IndexOutOfBoundsException

int[] array = { 1, 2, 3 }; // an array of ints
int n2 = array[array.length]; // It throws an ArrayIndexOutOfBoundsException

String str = "Hello";
char c = str.charAt(str.length()); // It throws a StringIndexOutOfBoundsException

int invalidNumber = Integer.parseInt("abc"); // It throws a NumberFormatException 

Scanner scanner = new Scanner(new File("file.txt")); // It throws a FileNotFoundException

FileReader fileReader = new FileReader("Test.txt");
System.out.println(fileReader.read()); // It throws an IOException
fileReader.close(); // It throws an IOException

Scanner scanner = new Scanner(System.in);
int number = scanner.nextInt(); // It throws an InputMismatchException if user input is string

int result = 10 / 0; // It throws an ArithmeticException
```

### Hierarchy of Exceptions
![hierarchy of exceptions](docs/assets/hierarchy_of_exceptions.jpg)

- The Throwable class has two direct subclasses: **java.lang.Error** and **java.lang.Exception**.

- subclasses of the Error class represent low-level exceptions in the JVM,
  for example: OutOfMemoryError, StackOverflowError;

- subclasses of the Exception class deal with exceptional events inside applications,
  such as: RuntimeException, IOException;

- the RuntimeException class is a rather special subclass of Exception.
  It represents so-called unchecked exceptions, including: ArithmeticException, NumberFormatException, NullPointerException.

#### Throwable Methods
```java
// returns the detailed string message of this exception object
e.getMessage();

// get the cause of this exception or null 
//if the cause is nonexistent or unknown
e.getCause();

// get stack trace
e.getStackTrace();

// print stack trace
e.printStackTrace();
```

#### Checked and unchecked exceptions

##### Checked exceptions

Checked exceptions are represented by the Exception class, excluding the RuntimeException subclass. 
The compiler checks whether the programmer expects the occurrence of such exceptions in a program or not.

```java
public static String readLineFromFile() throws FileNotFoundException {
    Scanner scanner = new Scanner(new File("file.txt")); // throws FileNotFoundException
    return scanner.nextLine();
}
```

FileNotFoundException is a standard checked exception. This constructor of Scanner declares that it may throw the 
FileNotFoundException exception if the specified file does not exist. To ensure that this method can be compiled 
successfully, we must include the throws keyword in the method declaration to indicate that the method may throw the 
FileNotFoundException exception. As a result, the caller of this method will need to decide 
whether to either handle the exception internally or throw it further to its caller method.

##### Unchecked exceptions

Unchecked exceptions are represented by the RuntimeException class and all its subclasses. 
The compiler does not check whether the programmer expects the occurrence of such exceptions in a program.

```java
public static Long convertStringToLong(String str) {
    return Long.parseLong(str); // It may throw a NumberFormatException
}
```


## enum

### Defining an enum

#### Declaring an enum in a new file
```java
public enum Direction {
    NORTH, SOUTH, EAST, WEST
}
```

#### Declaring an enum inside a class
```java
enum Direction {
    NORTH, SOUTH, EAST, WEST
}
```

### Methods for processing enums

```java
Direction north = Direction.NORTH;

System.out.println(north.name()); // "NORTH"
System.out.println(north.ordinal()); // 0

Direction west = Direction.valueOf("WEST");
System.out.println(west.name()); // "WEST"
System.out.println(west.ordinal()); // 3

Direction wrongNorth = Direction.valueOf("north"); // IllegalArgumentException

Direction[] directions = Direction.values();
```

### Enumerations in a switch statement

```java
switch (direction) {
    case NORTH:
        // do something
        break;
    case SOUTH:
        // do something
        break;
    case EAST:
        // do something
        break;
    case WEST:
        // do something
        break;
}
```

### Iteration with enums

```java
for (Direction direction : Direction.values()) {
    System.out.println(direction);
}
/*
NORTH
SOUTH
EAST
WEST
```

### Fields and Methods in enums

Note that the constructor of an enum must not be public, which avoids the creation of new enum objects 
by ```new Direction(5, "color")```.

```java
public enum ChargeLevel {
    FULL(4, "green"), 
    HIGH(3, "green"),
    MEDIUM(2, "yellow"),
    LOW(1, "red");

    private final int sections;
    private final String color;
    
    // the constructor must not be public
    // This means we cannot create enum objects by new ChargeLevel(5, "black")
    ChargeLevel(int sections, String color) {
        this.sections = sections;
        this.color = color;
    }
    
    // static methods can also be declared in enums
    public static ChargeLevel findByNumberOfSections(int sections) {
        for (ChargeLevel value: values()) {
            if (value.sections == sections) {
                return value;
            }
        }
        return null;
    }

    public int getSections() {
        return sections;
    }

    public String getColor() {
        return color;
    }
}
```

## Input and Output

To read data from standard input, use ```Scanner```.

```java
import java.util.Scanner;

Scanner scanner = new Scanner(System.in);

String line = scanner.nextLine() // read a whole line, e.g., "Hello, Kotlin"
int num = scanner.nextInt()   // read a number, e.g., 123
long longNum = scanner.nextLong()   // read a number, e.g., 12345678900987654321
String string = scanner.next()   // read a string, e.g., "Hello"

// to close the scanner
scanner.close();
```

### Methods

```java
import java.util.Scanner;

Scanner scanner = new Scanner(System.in);

// to assert whether the scanner has next data
while (scanner.hasNext()) {
    System.out.println(scanner.next());
}
```

### Custom Delimiter
We can input data directly in ```Scanner```.
```java
import java.util.Scanner;

Scanner scanner = new Scanner("123_456_789");
scanner.useDelimiter("_");

println(scanner.nextInt()) // 123
println(scanner.nextInt()) // 456
println(scanner.nextInt()) // 789

// to close the scanner
scanner.close();
```

## Files

### Relative path and absolute path
It is generally a good practice to use relative path so that the code is portable.

```java
File fileOnUnix = new File("./images/picture.jpg");
File fileOnWin = new File(".\\images\\picture.jpg");
```
To access the parent directory, just write ```..``` (double dot).
So, ```../picture.jpg``` is a file placed in the parent directory of the working directory.

### Reading Files
To read a file, we use the ```File``` class.
```java
import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;

File fileOnUnix = new File("/home/username/Documents");    // a directory on a UNIX-like system
File fileOnWin = new File("D:\\Materials\\java-materials.pdf"); // a file on Windows

try (Scanner scanner = new Scanner(file)) {
    while (scanner.hasNext()) {
        System.out.print(scanner.nextLine() + " ");
    }
} catch (FileNotFoundException e) {
    System.out.println("No file found: " + pathToFile);
}
```

Also, the scanner will throw ```NoSuchElementException``` if the file does not contain data of the certain type.
```java
int nextInt = scanner.nextInt(); // throws NoSuchElementException if there is no next int
String nextLine = scanner.nextLine(); // throws NoSuchElementException if there is no next line
```

### Reading Files with newer versions of Java

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

// The following method returns all text from a specified file
public static String readFileAsString(String fileName) throws IOException {
  return new String(Files.readAllBytes(Paths.get(fileName)));
}

// To read source code from a java file
// the following methods will print out the source code from a java file

public static String readFileAsString(String fileName) throws IOException {
  return new String(Files.readAllBytes(Paths.get(fileName)));
}

public static void main(String[] args) {
  String pathToHelloWorldJava = "./HelloWorld.java";
  try {
    System.out.println(readFileAsString(pathToHelloWorldJava));
  } catch (IOException e) {
    System.out.println("Cannot read file: " + e.getMessage());
  }
}
```

### File Methods

```java
File file = new File("/home/username/Documents/javamaterials.pdf");

System.out.println("File name: " + file.getName()); // javamaterials.pdf
System.out.println("File path: " + file.getPath()); // /home/username/Documents/javamaterials.pdf
System.out.println("Is file: " + file.isFile()); // true
System.out.println("Is directory: " + file.isDirectory()); // false
System.out.println("Exists: " + file.exists()); // true
System.out.println("Parent path: " + file.getParent()); // /home/username/Documents
```
