package javaStuffs.amazingNumbers;

import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.function.LongPredicate;
import java.util.stream.Collectors;
import java.util.stream.LongStream;

public class NaturalNumber {

    final static LongPredicate notNatural = n -> n < 0;
    private static final String FIRST_ERROR = "The first parameter should be a natural number or zero.";
    private static final String SECOND_ERROR = "The second parameter should be a natural number or zero.";
    final long value;
    final List<NumberProperty> properties;


    public NaturalNumber(long value) {
        this.value = value;
        this.properties = NumberProperty.getPropertiesFor(value);
    }

    public static List<NaturalNumber> rangeFrom(long start, int count) {
        return rangeFromWithFilter(start, count, null, null);
    }

    public static List<NaturalNumber> rangeFromWithFilter(long start, int count, HashSet<NumberProperty> filters, HashSet<NumberProperty> excludeFilters) {
        if (notNatural.test(start)) throw new IllegalArgumentException(FIRST_ERROR);
        if (notNatural.test(count)) throw new IllegalArgumentException(SECOND_ERROR);
        return LongStream.iterate(start, n -> n + 1)
                .mapToObj(NaturalNumber::new)
                .filter(n -> n.propertiesFilter(filters, excludeFilters))
                .limit(count)
                .collect(Collectors.toList());
    }

    public void printProperties() {

        System.out.println("\nProperties of " + this.value);

        System.out.println("even: " + properties.contains(NumberProperty.EVEN));
        System.out.println("odd: " + properties.contains(NumberProperty.ODD));
        System.out.println("buzz: " + properties.contains(NumberProperty.BUZZ));
        System.out.println("duck: " + properties.contains(NumberProperty.DUCK));
        System.out.println("palindromic: " + properties.contains(NumberProperty.PALINDROMIC));
        System.out.println("gapful: " + properties.contains(NumberProperty.GAPFUL));
        System.out.println("spy: " + properties.contains(NumberProperty.SPY));
        System.out.println("square: " + properties.contains(NumberProperty.SQUARE));
        System.out.println("sunny: " + properties.contains(NumberProperty.SUNNY));
        System.out.println("jumping: " + properties.contains(NumberProperty.JUMPING));
        System.out.println("happy: " + properties.contains(NumberProperty.HAPPY));
        System.out.println("sad: " + properties.contains(NumberProperty.SAD));

    }

    private boolean propertiesFilter(HashSet<NumberProperty> properties, HashSet<NumberProperty> excludeProperties) {
        if (properties == null && excludeProperties == null) return true;
        HashSet<NumberProperty> propertiesSet = new HashSet<>(this.properties);

        if (properties != null && excludeProperties != null) {
            return propertiesSet.containsAll(properties) && Collections.disjoint(propertiesSet, excludeProperties);
        } else if (properties != null) {
            return propertiesSet.containsAll(properties);
        } else {
            return !Collections.disjoint(propertiesSet, excludeProperties);
        }
    }

    @Override
    public String toString() {
        StringBuilder str = new StringBuilder("\t" + this.value + " is ");
        properties.forEach(p -> {
            str.append(p.toString().toLowerCase());
            str.append(", ");
        });
        str.delete(str.length() - 2, str.length() - 1);
        return str.toString();
    }

}
