package sb.codebreakers.domain;

public enum Month {
    JANUARY("January", "This is January"),
    FEBRUARY("February", "This is February"),
    MARCH("March", "This is March"),
    APRIL("April", "This is April"),
    MAY("May", "This is May"),
    JUNE("June", "This is June"),
    JULY("July", "This is July"),
    AUGUST("August", "This is August"),
    SEPTEMBER("September", "This is September"),
    OCTOBER("October", "This is October"),
    NOVEMBER("November", "This is November"),
    DECEMBER("December", "This is December");

    private final String value;
    private final String description;

    Month(String value, String description) {
        this.value = value;
        this.description = description;
    }

    public String getValue() {
        return description;
    }
}
