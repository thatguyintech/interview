/**
 * This is the interface that represents nested lists.
 * You should not implement it, or speculate about its implementation.
 */
public interface NestedInteger
{
    /** @return true if this NestedInteger holds a single integer, rather than a nested list */
    boolean isInteger();
 
    /** @return the single integer that this NestedInteger holds, if it holds a single integer
     * Return null if this NestedInteger holds a nested list */
    Integer getInteger();
 
    /** @return the nested list that this NestedInteger holds, if it holds a nested list
     * Return null if this NestedInteger holds a single integer */
    List<NestedInteger> getList();
}

/**
 * Given a nested list of integers, returns the sum of all integers in the list weighted by their depth
 * For example, given the list {{1,1},2,{1,1}} the function should return 10 (four 1's at depth 2, one 2 at depth 1)
 * Given the list {1,{4,{6}}} the function should return 27 (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3)
 */
public int depthSum (List<NestedInteger> input)
{
    //Implementation here
    int depth = 1;
    return sumHelper(depth, input);
}

/**
 * Recursive adder that iterates through each element in the input list; base case is if all elements in the input list
 * are integers. Recursive call to calculate sum given deeper levels if an element is a nested list.
 */
public int sumHelper (int depth, List<NestedInteger> input)
{
	int total = 0;
	for (int index=0; index < input.size(); index++) {
		if (!input.get(index).isInteger()) {
			total += sumHelper(depth+1, input.get(index).getList());
		}
		total += input.get(index).getInteger() * depth;
	}
	return total;
}
