import java.util.*;
import java.io.*;

public class Tries {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    int t = Integer.parseInt(br.readLine());
    
    while (t-->0) {
      String[] words = br.readLine().split(" ");
      Trie trie = new Trie();
      for (String word: words) trie.insertRecursive(word);
      trie.printTrie(trie.root);
      System.out.println("abc present: " + trie.searchWord("abc"));
      System.out.println("abd present: " + trie.searchWord("abd"));
      System.out.println("ab present: " + trie.searchPrefix("ab"));
      System.out.println("ac present: " + trie.searchPrefix("ac"));
      trie.delete("abe");
      trie.printTrie(trie.root);
      trie.delete("lmn");
      trie.printTrie(trie.root);
      trie.delete("abe");
      trie.printTrie(trie.root);
    }
  }
}

class Trie {
  private class TrieNode {
	Map<Character, TrieNode> children;
    boolean endOfWord;
    
    TrieNode() {
      this.children = new HashMap<>();
      this.endOfWord = false;
    }
  }
  
  protected final TrieNode root;
  
  Trie() {
    this.root = new TrieNode();
  }
  
  public void insert(String word) {
    TrieNode curr = this.root;
    for (int i=0; i<word.length(); i++) {
      char ch = word.charAt(i);
      if (!curr.children.containsKey(ch)) {
        curr.children.put(ch, new TrieNode()); // if character isn't present in the map, put a new TrieNode corresponding to it in the map
      }
      curr = curr.children.get(ch);
    }
    curr.endOfWord = true;
  }
  
  public void insertRecursive(String word) {
    insertHelper(word, this.root, 0);
  }
  
  private void insertHelper(String word, TrieNode node, int ind) {
    if (ind == word.length()) {
      node.endOfWord = true;
      return;
    }
    
    char ch = word.charAt(ind);
	if (!node.children.containsKey(ch)) {
      node.children.put(ch, new TrieNode());
    }
    insertHelper(word, node.children.get(ch), ind+1);
  }
  
  public boolean searchWord(String word) {
    TrieNode curr = this.root;
    for (int i=0; i<word.length(); i++) {
      char ch = word.charAt(i);
      if (!curr.children.containsKey(ch)) return false; // if word doesn't exist, return false
      curr = curr.children.get(ch);
    }
    return curr.endOfWord;
  }
  
  public boolean searchPrefix(String pre) {
    TrieNode curr = this.root;
    for (int i=0; i<pre.length(); i++) {
      char ch = pre.charAt(i);
      if (!curr.children.containsKey(ch)) return false;
      curr = curr.children.get(ch);
    }
    return true; // prefix exists
  }
  
  public void delete(String word) {
    deleteHelper(word, this.root, 0);
  }
  
  private boolean deleteHelper(String word, TrieNode curr, int ind) {
    if (word.length() == ind) {
      if (!curr.endOfWord) return false; // if word doesn't exist, return false
      curr.endOfWord = false;
      return curr.children.size() == 0; // checks if the word is terminating at this point, we can delete the node, else just mark endOfWord as false
    }
    
    char ch = word.charAt(ind);
    TrieNode node = curr.children.get(ch);
    
    if (node == null) return false; // if word doesn't exist, return false;
    boolean shouldDeleteCurr = this.deleteHelper(word, node, ind + 1);
    
    if (shouldDeleteCurr) {
      curr.children.remove(ch); // if no children exist for this character, delete it from its parent's map, and recursion will ensure all such nodes get removed in bottom-up approach
      return curr.children.size() == 0;
    }
    
    return false;
  }
  
  public void printTrie(TrieNode node) {
	if (node.children.isEmpty()) {
      System.out.println(node.children.keySet() + " " + node.endOfWord);
      return;
    }
    for (char c: node.children.keySet()) {
      System.out.println(c + ": " + node.children.get(c).children.keySet() + " " + node.endOfWord);
      printTrie(node.children.get(c));
    }
  }
}