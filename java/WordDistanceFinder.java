/* This class will be given a list of words (such as might be tokenized
 * from a paragraph of text), and will provide a method that takes two
 * words and returns the shortest distance (in words) between those two
 * words in the provided text. 
 * Example:
 *   WordDistanceFinder finder = new WordDistanceFinder(Arrays.asList("the", "quick", "brown", "fox", "quick"));
 *   assert(finder.distance("fox","the") == 3);
 *   assert(finder.distance("quick", "fox") == 1);
 
 */
public class WordDistanceFinder {
    
    List<String> input;
    
    public WordDistanceFinder (List<String> words) {
        // implementation here
        input = words;
    }
    public int distance (String wordOne, String wordTwo) {
        // implementation here
        // these lists hold indices where wordOne and wordTwo show up
        List<int> wordOneIndices = new List();
        List<int> wordTwoIndices = new List();

        for index in input.size():
            if wordOne.equals(word):
                wordOneIndices.add(index);
            if wordTwo.equals(word):
                wordTwoIndices.add(index);

        for (int index=0; index < input.size(); index++) {
            if (wordOne.equals(word)) {
                wordOneIndices.add(index);
            }
            if (wordTwo.equals(word)) {
                wordTwoIndices.add(index);
            }
        }

        int currMinDist = maxint();
        int j, k;
        j = k = 0;

        while (j < wordOneIndices.size() && k < wordTwoIndices.size()) {
            if (abs(wordOneIndices.get(j) - wordTwoIndices.get(k)) < currMinDist) {
                currMinDist = abs(wordOneIndices.get(j) - wordTwoIndices.get(k)); 
            }
            if (wordOneIndices.get(j) < wordTwoIndices.get(k)) {
                j++;
            } else {
                k++;
            }
        }

        return currMinDist;

    }
}