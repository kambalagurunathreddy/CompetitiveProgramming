import java.util.*;
class temperature{
	private int minTemp=Integer.MAX_VALUE;
	private int maxTemp=Integer.MIN_VALUE;
	private int numberOfReadings;
	private long totalSum;
	private double mean;
	private int[] occurrences = new int[111];
	private int maxOccurrences;
	private int mode;
	public void insert(int temp){
		occurrences[temp]++;
		if (occurrences[temp] > maxOccurrences) {
			mode = temp;
			maxOccurrences = occurrences[temp];
		}
		minTemp=Math.min(minTemp,temp);
		maxTemp=Math.max(maxTemp,temp);
		numberOfReadings++;
		totalSum += temp;
		mean = (double) totalSum/numberOfReadings;
	}
	public int getMax() {
		return maxTemp;
	}
	public int getMin() {
		return minTemp;
	}
	public double getMean() {
		return mean;
	}
	public int getMode() {
		return mode;
	}

	public static void main(String[] args){
		temperature t = new temperature();
		t.insert(60);
		System.out.println(t.getMax());
		System.out.println(t.getMin());
		System.out.println(t.getMean());
		System.out.println(t.getMode());
		System.out.println("######################");
		t.insert(90);
		System.out.println(t.getMax());
		System.out.println(t.getMin());
		System.out.println(t.getMean());
		System.out.println(t.getMode());
		System.out.println("######################");
		t.insert(60);
		System.out.println(t.getMax());
		System.out.println(t.getMin());
		System.out.println(t.getMean());
		System.out.println(t.getMode());
		System.out.println("######################");
		t.insert(60);
		System.out.println(t.getMax());
		System.out.println(t.getMin());
		System.out.println(t.getMean());
		System.out.println(t.getMode());
		System.out.println("######################");

	}
}


