package javaStuffs;

import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;

public class BullsAndCows {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        try {
            System.out.println("Please, enter the secret code's length:");
            int numberOfDigits = scanner.nextInt();
            System.out.println("Input the number of possible symbols in the code:");
            int numberOfPossibleSymbols = scanner.nextInt();

            if (numberOfDigits > numberOfPossibleSymbols || numberOfDigits == 0) {
                throw new PossibleSymbolsTooLessException(numberOfDigits, numberOfPossibleSymbols);
            }

            if (numberOfPossibleSymbols > 36) {
                throw new PossibleSymbolsTooManyException();
            } else {

                char[] digits = new char[numberOfDigits];
                char digitChar;
                Arrays.fill(digits, ' ');

                for (int i = 0; i < numberOfDigits; i++) {
                    while (true) {

                        int digit = random.nextInt(numberOfPossibleSymbols);

                        if (digit <= 9) {
                            digitChar = (char) (digit + 48);
                        } else {
                            digitChar = (char) (digit + 87); // if digit > 9, unicode >= 97, char >= a
                        }

                        if (String.valueOf(digits).indexOf(digitChar) == -1) {
                            digits[i] = digitChar;
                            break;
                        }
                    }
                }

                String secretCode = String.valueOf(digits);

                StringBuilder sb = new StringBuilder();
                int numberOfTurns = 0;
                int numberOfBulls = 0;
                int numberOfCows;

                String symbolRange;
                if (numberOfPossibleSymbols <= 10) {
                    symbolRange = " (0-%d).".formatted(numberOfPossibleSymbols - 1);
                } else {
                    symbolRange = " (0-9, a-%c).".formatted((char) numberOfPossibleSymbols + 86);
                }
                System.out.println("The secret is prepared: " + "*".repeat(numberOfDigits) + symbolRange);
                System.out.println("Okay, let's start a game!");

                while (numberOfBulls != secretCode.length() || numberOfTurns == 0) {
                    sb.setLength(0);

                    System.out.println("Turn " + (numberOfTurns + 1) + ":");

                    String userCode = scanner.next();
                    int[] bullsAndCows = checkCode(secretCode, userCode);
                    numberOfBulls = bullsAndCows[0];
                    numberOfCows = bullsAndCows[1];

                    sb.append("Grade: ");
                    if (numberOfBulls == 0 && numberOfCows == 0) {
                        sb.append("None.");
                    } else if (numberOfBulls > 0 && numberOfCows > 0) {
                        if (numberOfBulls == 1) {
                            sb.append(numberOfBulls).append(" bull and ");
                        } else {
                            sb.append(numberOfBulls).append(" bulls and ");
                        }
                        if (numberOfCows == 1) {
                            sb.append(numberOfCows).append(" cow.");
                        } else {
                            sb.append(numberOfCows).append(" cows.");
                        }
                    } else {
                        if (numberOfBulls == 1) {
                            sb.append(numberOfBulls).append(" bull");
                        } else if (numberOfBulls > 1) {
                            sb.append(numberOfBulls).append(" bulls");
                        } else if (numberOfCows == 1) {
                            sb.append(numberOfCows).append(" cow");
                        } else if (numberOfCows > 1) {
                            sb.append(numberOfCows).append(" cows");
                        }
                    }
                    System.out.println(sb);
                    numberOfTurns++;
                }

                System.out.println("Congratulations! You guessed the secret code.");
            }

        } catch (InputMismatchException e) {
            System.out.printf("Error: \"%s\" isn't a valid number.", scanner.next());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public static int[] checkCode(String secretCode, String userCode) {

        int numberOfBulls = 0;
        int numberOfCows = 0;
        for (int i = 0; i < userCode.length(); i++) {
            if (userCode.charAt(i) == secretCode.charAt(i)) {
                numberOfBulls++;
            } else if (secretCode.contains(Character.toString(userCode.charAt(i)))) {
                numberOfCows++;
            }
        }

        return new int[]{numberOfBulls, numberOfCows};
    }
}

class PossibleSymbolsTooLessException extends RuntimeException {
    public PossibleSymbolsTooLessException(int numberOfDigits, int numberOfPossibleSymbols) {
        super("\nError: it's not possible to generate a code with a length of %d with %d unique symbols.".formatted(numberOfDigits, numberOfPossibleSymbols));
    }
}

class PossibleSymbolsTooManyException extends RuntimeException {
    public PossibleSymbolsTooManyException() {
        super("Error: maximum number of possible symbols in the code is 36 (0-9, a-z).");
    }
}
