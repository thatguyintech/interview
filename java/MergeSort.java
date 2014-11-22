import java.util.Arrays;

public class MergeSort {
	public static int level = 0;
	
	public static int[] mergesort(int[] input, int l) {
		if (input.length <= 1) {
			return input;
		}
		int[] first_half = new int[(input.length/2)];
		int[] second_half = new int[input.length-(input.length/2)];
		for (int i = 0; i < input.length/2; i++) {
			first_half[i] = input[i];
		}
		// System.out.println("first half initialized: " + Arrays.toString(first_half));
		for (int j = input.length/2; j < input.length; j++) {
			second_half[j-(input.length/2)] = input[j];
		}
		// System.out.println("second half initialized: " + Arrays.toString(second_half));
		return merge(mergesort(first_half, l+1), mergesort(second_half, l+1), l+1);
	}

	public static int[] merge(int[] first, int[] second, int l) {
		// System.out.println("current level: " + l);
		int i, j, k;
		i = j = k = 0;
		int[] merged = new int[first.length + second.length];
		// System.out.println("size of merged: " + (first.length + second.length));
		// System.out.println("empty merged array: " + Arrays.toString(merged));
		while (i < first.length && j < second.length) {
			if (first[i] >= second[j]) {
				// System.out.println("adding from second: " + second[j]);
				merged[k] = second[j];
				j++;
			} else {
				// System.out.println("adding from first: " + first[i]);
				merged[k] = first[i];
				i++;
			}
			k++;
		}
		while (i < first.length) {
			// System.out.println("left in first: " + Arrays.toString(first));
			// System.out.println("cramming: " + first[i]);
			merged[k] = first[i];
			i++;
			k++;
		}
		while (j < second.length) {
			// System.out.println("left in second: " + Arrays.toString(second));
			// System.out.println("cramming: " + second[j]); 
			merged[k] = second[j];
			j++;
			k++;
		}
		return merged;
	}

	public static void main(String args[]) {
		int[] inp = new int[] {'a', 'l', 'b', 'e', 'r', 't'};
		System.out.println(Arrays.toString(inp));
		int[] result = mergesort(inp, level);
		System.out.println(Arrays.toString(result));
	}
}