
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class abc {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        String[] availableProperties = {"even", "odd", "buzz", "duck", "palindromic", "gapful", "spy"};

        System.out.println(
                """
                        Welcome to Amazing Numbers!
                                           
                        Supported requests:
                        - enter a natural number to know its properties;
                        - enter two natural numbers to obtain the properties of the list:
                          * the first parameter represents a starting number;
                          * the second parameters show how many consecutive numbers are to be processed;
                        - two natural numbers and a property to search for;
                        - separate the parameters with one space;
                        - enter 0 to exit."""
        );

        while (true) {

            System.out.print("\nEnter a request: ");
            String userInput = scanner.nextLine();

            if (userInput.isEmpty()) {

                System.out.println(
                        """
                                Supported requests:
                                - enter a natural number to know its properties;
                                - enter two natural numbers to obtain the properties of the list:
                                  * the first parameter represents a starting number;
                                  * the second parameters show how many consecutive numbers are to be processed;
                                - two natural numbers and a property to search for;
                                - separate the parameters with one space;
                                - enter 0 to exit."""
                );
                continue;
            }

            String[] arguments = userInput.split(" ");

            long firstNumber;


            try {
                firstNumber = Long.parseLong(arguments[0]);
                if (firstNumber < 0) {
                    System.out.print("The first parameter should be a natural number or zero.");
                    continue;
                } else if (firstNumber == 0) {
                    break;
                }
            } catch (NumberFormatException e) {

                continue;
            }

            if (arguments.length == 1) {
                numberProperties(firstNumber);
            } else {

                long secondNumber;
                try {
                    secondNumber = Long.parseLong(arguments[1]);
                    if (secondNumber < 1) {
                        System.out.println("The second parameter should be a natural number or zero.");
                        continue;
                    }
                } catch (NumberFormatException e) {

                    continue;
                }
                if (arguments.length == 2) {
                    System.out.println();
                    for (int i = 0; i < secondNumber; i++) {
                        System.out.println(multipleNumberProperties(firstNumber + i));
                    }
                } else if (arguments.length == 3) {
                    String arg = arguments[2].toLowerCase();
                    if (Arrays.asList(availableProperties).contains(arg)) {
                        numberProperties(firstNumber, secondNumber, arg);
                    } else {
                        System.out.printf("\nThe property [%s] is wrong.\nAvailable properties: [EVEN, ODD, BUZZ, DUCK, PALINDROMIC, GAPFUL, SPY]", arg.toUpperCase());
                    }
                }
            }
        }

        System.out.println("\nGoodbye!");
    }



    private static String multipleNumberProperties(long number) {
        List<String> properties = new ArrayList<>();

        if (buzz(number)) {
            properties.add("buzz");
        }
        if (duck(number)) {
            properties.add("duck");
        }
        if (palindromic(number)) {
            properties.add("palindromic");
        }
        if (gapful(number)) {
            properties.add("gapful");
        }
        if (spy(number)) {
            properties.add("spy");
        }
        if (number % 2 == 0) {
            properties.add("even");
        } else {
            properties.add("odd");
        }

        return number + " is " + String.join(", ", properties);
    }

    private static void numberProperties(long firstNumber, long secondNumber, String arg) {

        long count = 0;
        long number = firstNumber;

        if (arg.contentEquals("buzz")) {
            while (count < secondNumber) {
                String str = multipleNumberProperties(number);
                if (str.contains("buzz")) {
                    System.out.println(str);
                    count++;
                }
                number++;
            }
        } else if (arg.contentEquals("duck")) {
            while (count < secondNumber) {
                String str = multipleNumberProperties(number);
                if (str.contains("duck")) {
                    System.out.println(str);
                    count++;
                }
                number++;
            }
        } else if (arg.contentEquals("palindromic")) {
            while (count < secondNumber) {
                String str = multipleNumberProperties(number);
                if (str.contains("palindromic")) {
                    System.out.println(str);
                    count++;
                }
                number++;
            }
        } else if (arg.contentEquals("gapful")) {
            while (count < secondNumber) {
                String str = multipleNumberProperties(number);
                if (str.contains("gapful")) {
                    System.out.println(str);
                    count++;
                }
                number++;
            }
        } else if (arg.contentEquals("spy")) {
            while (count < secondNumber) {
                String str = multipleNumberProperties(number);
                if (str.contains("spy")) {
                    System.out.println(str);
                    count++;
                }
                number++;
            }
        } else if (arg.contentEquals("even")) {
            while (count < secondNumber) {
                String str = multipleNumberProperties(number);
                if (str.contains("even")) {
                    System.out.println(str);
                    count++;
                }
                number++;
            }
        } else if (arg.contentEquals("odd")) {
            while (count < secondNumber) {
                String str = multipleNumberProperties(number);
                if (str.contains("odd")) {
                    System.out.println(str);
                    count++;
                }
                number++;
            }
        }

    }



}
