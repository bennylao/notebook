package javaStuffs.amazingNumbers;

import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        String INSTRUCTION = """
                
                Supported requests:
                - enter a natural number to know its properties;
                - enter two natural numbers to obtain the properties of the list:
                  * the first parameter represents a starting number;
                  * the second parameter shows how many consecutive numbers are to be printed;
                - two natural numbers and properties to search for;
                - a property preceded by minus must not be present in numbers;
                - separate the parameters with one space;
                - enter 0 to exit.""";

        System.out.println("Welcome to Amazing Numbers!");
        System.out.println(INSTRUCTION);

        inputLoop:
        while (true) {

            System.out.print("\nEnter a request: ");
            String[] userInput = scanner.nextLine().split(" ");

            long firstNumber;
            int secondNumber;

            switch (userInput.length) {
                case 0:
                    System.out.println(INSTRUCTION);
                    throw new NullPointerException();
                case 1:
                    try {
                        firstNumber = Long.parseLong(userInput[0]);

                        if (firstNumber == 0) {
                            break inputLoop;
                        } else if (firstNumber < 0) {
                            throw new NumberFormatException();
                        }
                        NaturalNumber number = new NaturalNumber(firstNumber);
                        number.printProperties();
                    } catch (NullPointerException e) {
                        System.out.println(INSTRUCTION);
                    } catch (NumberFormatException e) {
                        System.out.print("The first parameter should be a natural number or zero.");
                    }
                    break;

                case 2:
                    try {
                        firstNumber = Long.parseLong(userInput[0]);
                    } catch (NumberFormatException e) {
                        System.out.print("The first parameter should be a natural number.");
                        break;
                    }
                    try {
                        secondNumber = Integer.parseInt(userInput[1]);
                    } catch (NumberFormatException e) {
                        System.out.print("The second parameter should be a natural number.");
                        break;
                    }

                    try {
                        List<NaturalNumber> numbers = NaturalNumber.rangeFrom(firstNumber, secondNumber);
                        numbers.forEach(System.out::println);
                    } catch (IllegalArgumentException e) {
                        System.out.println(e.getMessage());
                    }
                    break;
                default: {
                    HashSet<NumberProperty> requiredProperties = new HashSet<>();
                    HashSet<NumberProperty> excludedProperties = new HashSet<>();
                    List<String> wrongProperties = new ArrayList<>();
                    try {
                        firstNumber = Long.parseLong(userInput[0]);
                    } catch (NumberFormatException e) {
                        System.out.print("The first parameter should be a natural number.");
                        break;
                    }
                    try {
                        secondNumber = Integer.parseInt(userInput[1]);
                    } catch (NumberFormatException e) {
                        System.out.print("The second parameter should be a natural number.");
                        break;
                    }

                    for (int i = 2; i < userInput.length; i++) {
                        searchProperty(requiredProperties, excludedProperties, wrongProperties, userInput[i]);
                    }

                    if (wrongProperties.isEmpty()) {
                        String[] mutuallyExclusiveProperties = NumberProperty.mutuallyExclusive(requiredProperties, excludedProperties);
                        if (mutuallyExclusiveProperties.length > 0) {
                            System.out.printf("""

                                    The request contains mutually exclusive properties: [%s, %s]
                                    There are no numbers with these properties.""", mutuallyExclusiveProperties[0], mutuallyExclusiveProperties[1]);
                        } else {
                            List<NaturalNumber> numbers = NaturalNumber.rangeFromWithFilter(firstNumber, secondNumber, requiredProperties, excludedProperties);
                            numbers.forEach(System.out::println);
                        }
                    } else {
                        boolean multipleProperties = wrongProperties.size() > 1;
                        String str = multipleProperties ?
                                "The properties [" + String.join(", ", wrongProperties) + "] are wrong.\nAvailable properties: %s".formatted(Arrays.toString(NumberProperty.values())) :
                                "The property [" + String.join(", ", wrongProperties) + "] is wrong.\nAvailable properties: %s".formatted(Arrays.toString(NumberProperty.values()));
                        System.out.println(str);
                    }
                    break;
                }

            }

        }
        // when the program is terminating
        System.out.println("\nGoodbye!");
    }

    private static void searchProperty(HashSet<NumberProperty> requiredProperties, HashSet<NumberProperty> excludedProperties, List<String> wrongProperties, String propertyStr) {

        if (propertyStr.charAt(0) == '-' && NumberProperty.getProperty(propertyStr.substring(1)).isPresent()) {
            excludedProperties.add(NumberProperty.getProperty(propertyStr.substring(1)).get());
        } else if (NumberProperty.getProperty(propertyStr).isPresent()) {
            requiredProperties.add(NumberProperty.getProperty(propertyStr).get());
        } else {
            wrongProperties.add(propertyStr);
        }
    }

}
