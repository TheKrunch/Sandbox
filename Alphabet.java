/**
 * Write a description of class Alphabet here.
 * 
 * @author Matt Scalzo 
 * @version 1.0 - 12/17/15
 */
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
}
<<<<<<< HEAD

// Stuff and more and more and mormoromorormoermeormore 
=======
>>>>>>> ba88349f0dffe9fb54728138636de026aa9d2ef9
