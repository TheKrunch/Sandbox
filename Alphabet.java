/**
 * This program creates a caesar cipher shifted alphabet.
 * 
 * @author Matt Scalzo 
 * @version 2.0 - 1/17/20
 */

import java.util.Scanner;

public class Alphabet
{
    private String plain;
    private String shifted;
   
    public Alphabet(int shift)
    {
        plain = "abcdefghijklmnopqrstuvwxyz ";
        shifted = getShifted(shift);
    }
    
    public String getShifted(int shift)
    {
        int n = 27;//this is the length of the alphabet
        int s = shift;//this is how much you are shifting the alphabet
        
        return plain.substring(s,n) + plain.substring(0,s);//this is the shifted alphabet
    }


public static void main(String[] args)
{
    Scanner input = new Scanner(System.in);
    System.out.print("Enter how much you want to shift by: ");
    
    int number = input.nextInt();
    input.close();
    Alphabet alph = new Alphabet(number);

    System.out.println("Your new alphabet is: " + alph.shifted);
}
}
