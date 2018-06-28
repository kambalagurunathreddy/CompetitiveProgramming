import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Trie {

    // implement a trie and use it to efficiently store string
    


        private Node root;   

     static class Node {
        private char c;                        
        private Node left, mid, right;  
        private Integer val;                     
    }


    public boolean contains(String key) {
        if (key == "") {
            key="\0";
        }
        return get(key) != null;
    }


    public Integer get(String key) {
        if (key == "") {
            key="\0";
        }
        if (key == null) {
            key="\0";
        }
        //if (key.length() == 0) throw new IllegalArgumentException("key must have length >= 1");
        Node x = get(root, key, 0);
        if (x == null) return null;
        return x.val;
    }

    
    private Node get(Node x, String key, int d) {
        if (x == null) return null;
        //if (key.length() == 0) throw new IllegalArgumentException("key must have length >= 1");
        char c = key.charAt(d);
        if      (c < x.c)              return get(x.left,  key, d);
        else if (c > x.c)              return get(x.right, key, d);
        else if (d < key.length() - 1) return get(x.mid,   key, d+1);
        else                           return x;
    }


    public void put(String key, int val) {
        if (key == null || key=="") {
            key="\0";
        }
        root = put(root, key, val, 0);
    }

    private Node put(Node x, String key, int val, int d) {
        char c = key.charAt(d);
        if (x == null) {
            x = new Node();
            x.c = c;
        }
        if      (c < x.c)               x.left  = put(x.left,  key, val, d);
        else if (c > x.c)               x.right = put(x.right, key, val, d);
        else if (d < key.length() - 1)  x.mid   = put(x.mid,   key, val, d+1);
        else                            x.val   = val;
        return x;
    }


        public boolean addWord(String word) {
            if (contains(word)){
                return false;
            }
            put(word,1);
            return true;
        }
    
















    // tests

    @Test
    public void trieTest() {
        final Trie trie = new Trie();

        boolean result = trie.addWord("catch");
        // System.out.println(1);
        assertTrue(result);

        result = trie.addWord("cakes");
        // System.out.println(2);
        assertTrue(result);

        result = trie.addWord("cake");
        // System.out.println(3);
        assertTrue(result);

        result = trie.addWord("cake");
        // System.out.println(4);
        assertFalse(result);

        result = trie.addWord("caked");
        // System.out.println(5);
        assertTrue(result);

        result = trie.addWord("catch");
        // System.out.println(6);
        assertFalse(result);

        result = trie.addWord("");
        // System.out.println(7);

        assertTrue(result);

        result = trie.addWord("");
        // System.out.println(8);
        assertFalse(result);
    }

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(Trie.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("All tests passed.");
        }
    }
}