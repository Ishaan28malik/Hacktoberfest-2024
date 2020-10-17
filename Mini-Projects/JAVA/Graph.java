package com.company;
import java.util.LinkedList;

public class Graph {
    LinkedList<String> adjancency[];

    public Graph() {
        adjancency = new LinkedList[9];
        for (int i = 0; i < adjancency.length; i++) {
            adjancency[i] = new LinkedList<>();
        }
    }

    public void add(char vertex, String edge) {
        int index = 0;
        for (char i = 'a'; i < 'z'; ++i) {
            if (i == vertex) {
                adjancency[index].add(edge);
                index = 0;
            }
            index++;
        }
    }

    public void print() {
        char vertex = 'a';
        for (int i = 0; i < adjancency.length; i++) {
            System.out.print(vertex + " -> ");
            System.out.println(adjancency[i].toString().replaceAll("\\[", "")
                    .replaceAll("\\]", "").replaceAll(",","->"));
            vertex++;
        }
    }
}
package com.company;

public class Main {

    public static void main(String[] args) {
        Graph a = new Graph();
        a.add('a', "b");
        a.add('a', "e");
        a.add('a',"d");
        a.add('b',"e");
        a.add('c',"b");
        a.add('d',"g");
        a.add('e',"f");
        a.add('e',"h");
        a.add('f',"c");
        a.add('f',"h");
        a.add('g',"h");
        a.add('h',"i");
        a.add('i',"f");
        a.print();
    }


}

