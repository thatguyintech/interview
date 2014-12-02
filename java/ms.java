import java.util.Arrays;
import java.util.ArrayList;

public class ms {
	public static ArrayList<Integer> mergesort(ArrayList<Integer> a) {
		int size = a.size();
		int midpt = size/2;
		if (size <= 1) {
			return a;
		}
		ArrayList<Integer> left = new ArrayList<Integer>();
		ArrayList<Integer> right = new ArrayList<Integer>();
		for (int index=0; index < size; index++) {
			if (index < midpt) {
				left.add(a.get(index));
			} else {
				right.add(a.get(index));
			}
		}
		return merge(mergesort(left), mergesort(right));
	}

	public static ArrayList<Integer> merge(ArrayList<Integer> a, ArrayList<Integer> b) {
		ArrayList<Integer> result;	
		int i, j;

		if (a.size() == 0) {
			return b;
		}
		if (b.size() == 0) {
			return a;
		}

		result = new ArrayList<Integer>();

		while (a.size() > 0 && b.size() > 0) {
			if (a.get(0) <= b.get(0)) {
				result.add(a.remove(0));
			} else {
				result.add(b.remove(0));
			}
		}

		if (a.size() == 0) {
			result.addAll(b);
		} if (b.size() == 0) {
			result.addAll(a);
		}
		return result;
	}


	public static void main(String[] args) {
		ArrayList<Integer> foo = new ArrayList<Integer>();
		foo.add(1);
		foo.add(6);
		foo.add(-9);
		foo.add(3);
		foo.add(2);
		foo.add(23);
		foo.add(11);
		// 1, 2, 3, 5, 9, 23
		ArrayList<Integer> bar = mergesort(foo);
		for (int i : bar) {
			System.out.println(i);
		}
	}
}