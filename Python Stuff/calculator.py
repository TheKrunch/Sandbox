contin = True;
accum = 0.0;
import math;

while contin:
    print("***");
    print("Accumulator = " + str(accum));
    print("Please choose one of the following options:");
    print("1) Addition");
    print("2) Subtraction");
    print("3) Multiplication");
    print("4) Division");
    print("5) Square root");
    print("6) Clear");
    print("0) Exit");

    opt = int(input("What is your option? "));

    if opt == 0:
        contin = False;

    elif opt == 1:
        add = float(input("Enter a number: "));
        accum = accum + add;

    elif opt == 2:
        sub = float(input("Enter a number: "));
        accum = accum - sub;

    elif opt == 3:
        mult = float(input("Enter a number: "));
        accum = accum * mult;

    elif opt == 4:
        div = float(input("Enter a number: "));
        accum = accum / div;

    elif opt == 5:
        accum = math.sqrt(accum);

    elif opt == 6:
        accum = 0.0;

    else:
        print("Illegal option: " + str(opt));


print("Program finished");
