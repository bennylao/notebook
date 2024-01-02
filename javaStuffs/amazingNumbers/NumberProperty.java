package javaStuffs.amazingNumbers;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

public enum NumberProperty {
    EVEN {
        @Override
        boolean hasProperty(long n) {
            return n % 2 == 0;
        }
    },
    ODD {
        @Override
        boolean hasProperty(long n) {
            return n % 2 != 0;
        }
    },
    BUZZ {
        @Override
        boolean hasProperty(long n) {
            return n % 7 == 0 || n % 10 == 7;
        }
    },
    DUCK {
        @Override
        boolean hasProperty(long n) {
            return String.valueOf(n).matches("\\d+0\\d*");
        }
    },
    PALINDROMIC {
        @Override
        boolean hasProperty(long n) {
            return new StringBuilder(String.valueOf(n))
                    .reverse()
                    .toString()
                    .equals(String.valueOf(n));
        }
    },
    GAPFUL {
        @Override
        boolean hasProperty(long n) {
            if (n <= 99) return false;
            String numStr = String.valueOf(n);
            long concat =
                    Long.parseLong(numStr.charAt(0) + numStr.substring(numStr.length() - 1));
            return n % concat == 0;
        }
    },
    SPY {
        @Override
        boolean hasProperty(long n) {
            String numStr = String.valueOf(n);
            int sum = Arrays.stream(numStr.split(""))
                    .mapToInt(Integer::parseInt)
                    .sum();
            int product = Arrays.stream(numStr.split(""))
                    .mapToInt(Integer::parseInt)
                    .reduce(1, (a, b) -> a * b);
            // 'i' is identity element (served as an initial value)
            // here the first value of 'a' is the initial value a = i = 1 while b is the first integer of numStr
            // the first product = 1 * b1 = b1
            // the second value of a = b1 where b2 is the second integer of numStr
            // hence the second product = b1 * b2

            return sum == product;
        }
    },
    SQUARE {
        @Override
        boolean hasProperty(long n) {
            return Math.sqrt(n) % 1 == 0;
        }
    },
    SUNNY {
        @Override
        boolean hasProperty(long n) {
            return Math.sqrt(n + 1) % 1 == 0;
        }
    },
    JUMPING {
        @Override
        boolean hasProperty(long n) {
            String numStr = String.valueOf(n);
            for (int i = 0; i < numStr.length() - 1; i++) {
                if (Math.abs(Character.getNumericValue(numStr.charAt(i)) - Character.getNumericValue(numStr.charAt(i + 1))) != 1) {
                    return false;
                }
            }
            return true;
        }
    },
    HAPPY {
        @Override
        boolean hasProperty(long n) {
            HashSet<Long> history = new HashSet<>();
            history.add(n);
            while (n != 1) {
                String numStr = String.valueOf(n);
                n = Arrays.stream(numStr.split("")).mapToInt(Integer::parseInt).reduce(0, (a, b) -> a + b * b);
                if (history.contains(n)) {
                    return false;
                }
                history.add(n);
            }
            return true;
        }
    },
    SAD {
        @Override
        boolean hasProperty(long n) {
            HashSet<Long> history = new HashSet<>();
            history.add(n);
            while (n != 1) {
                String numStr = String.valueOf(n);
                n = Arrays.stream(numStr.split("")).mapToInt(Integer::parseInt).reduce(0, (a, b) -> a + b * b);
                if (history.contains(n)) {
                    return true;
                }
                history.add(n);
            }
            return false;
        }
    };

    public static List<NumberProperty> getPropertiesFor(final long n) {
        return Arrays.stream(NumberProperty.values())
                .filter(p -> p.hasProperty(n)).collect(Collectors.toList());
    }

    public static Optional<NumberProperty> getProperty(String search) {
        return Arrays.stream(NumberProperty.values())
                .filter(v -> v.toString().equalsIgnoreCase(search))
                .findAny();
    }

    public static String[] mutuallyExclusive(HashSet<NumberProperty> properties, HashSet<NumberProperty> excludeProperties) {
        if (properties.containsAll(Arrays.asList(EVEN, ODD))) {
            return new String[]{"EVEN", "ODD"};
        } else if (properties.containsAll(Arrays.asList(DUCK, SPY))) {
            return new String[]{"DUCK", "SPY"};
        } else if (properties.containsAll(Arrays.asList(SQUARE, SUNNY))) {
            return new String[]{"SQUARE", "SUNNY"};
        } else if (excludeProperties.containsAll(Arrays.asList(EVEN, ODD))) {
            return new String[]{"-EVEN", "-ODD"};
        } else if (excludeProperties.containsAll(Arrays.asList(DUCK, SPY))) {
            return new String[]{"-DUCK", "-SPY"};
        } else if (excludeProperties.containsAll(Arrays.asList(SQUARE, SUNNY))) {
            return new String[]{"-SQUARE", "-SUNNY"};
        } else if (findCommonProperty(properties, excludeProperties).length > 0) {
            return findCommonProperty(properties, excludeProperties);
        } else {
                return new String[0];
            }
        }

        private static String[] findCommonProperty(HashSet<NumberProperty> properties, HashSet<NumberProperty> excludeProperties) {
            for (NumberProperty property : properties) {
                if (excludeProperties.contains(property)) {
                    String str = property.toString().toUpperCase();
                    return new String[] {str, "-" + str};
                }
            }
            return new String[0];
        }


    abstract boolean hasProperty(long n);
}