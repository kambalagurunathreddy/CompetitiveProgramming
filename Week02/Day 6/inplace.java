import java.util.Arrays;
import java.util.Random;

public class Solution 
{
private static Random rand = new Random();

    private static int getRandom(int floor, int ceiling) 
    {
        return rand.nextInt((ceiling - floor) + 1) + floor;
    }

    

    public static void shuffle(int[] arr) 
    {

   
        for (int i= 0; i< arr.length;i++) 
        {

        
            int j= getRandom(i,arr.length - 1);

       
            if (j!=i) 
            {
                
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

    }

    public static void main(String[] args) 
    {
        final int[] initial = {8,3,4,5,9,2};
        final int[] shuffled = Arrays.copyOf(initial, initial.length);
        shuffle(shuffled);
        System.out.printf("initial array: %s\n", Arrays.toString(initial));
        System.out.printf("shuffled array: %s\n", Arrays.toString(shuffled));
    }
}