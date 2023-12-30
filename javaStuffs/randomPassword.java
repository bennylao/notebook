package javaStuffs;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 *
 * Generating passwords
 * A password is hard to crack if it contains at least A uppercase letters, at least B lowercase letters,
 * at least C digits and consists of exactly N symbols.
 * Also, a password cannot contain two or more of the same characters in a row.
 * For the given numbers A, B, C, and N, you should output a password that matches these requirements.
 * It is guaranteed that A, B, C, and N are non-negative integers, and A + B + C <= N.
 * Keep in mind that any parameter can be equal to zero.
 * It means that it's ok if the password doesn't contain symbols of such type.
 * Sample Input 1:
 * 3 2 3 10
 * Sample Output 1:
 * ABAab121AB
 *
 */

public class randomPassword {
    public static void main(String[] args) {
        // write your code here
        StringBuilder sb = new StringBuilder();
        Random random = new Random();

        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        int N = scanner.nextInt();

        int numberOfMissingCharacters = N - (a + b + c);
        for (int i = 0; i < numberOfMissingCharacters; i++) {
            int randomNumber = random.nextInt(3);
            switch(randomNumber) {
                case 0:
                    a++;
                    break;
                case 1:
                    b++;
                    break;
                case 2:
                    c++;
                    break;
            }
        }

        IntStream uppercaseLetterCodes = random.ints(a, 65, 91);
        IntStream lowercaseLetterCodes = random.ints(b, 97, 123);
        IntStream digits = random.ints(c, 0, 10);

        int[] uppercaseLetterCodesArray = appendCharacterIntoString(uppercaseLetterCodes, 65, 91);
        int[] lowercaseLetterCodesArray = appendCharacterIntoString(lowercaseLetterCodes, 97, 123);
        int[] digitsArray = appendCharacterIntoString(digits, 0, 10);

        sb.append(Arrays.stream(uppercaseLetterCodesArray).mapToObj(i -> String.valueOf((char) i)).collect(Collectors.joining()));
        sb.append(Arrays.stream(lowercaseLetterCodesArray).mapToObj(i -> String.valueOf((char) i)).collect(Collectors.joining()));
        sb.append(Arrays.stream(digitsArray).mapToObj(String::valueOf).collect(Collectors.joining()));

        System.out.println(sb);
    }

    public static int[] appendCharacterIntoString(IntStream codeStream, int origin, int bound) {
        Random random = new Random();
        int[] codes = codeStream.toArray();
        for (int i = 1; i < codes.length; i++) {
            while (codes[i] == codes[i - 1]) {
                codes[i] = random.nextInt(bound - origin) + origin;
            }
        }

        return codes;
    }
}