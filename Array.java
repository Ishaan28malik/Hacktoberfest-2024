import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;
 
public class ArrayListExample {
public static void main(String[] args) {
List<String> programmingLanguages = new ArrayList<>();
programmingLanguages.add("C");
programmingLanguages.add("C++");
programmingLanguages.add("Java");
programmingLanguages.add("Kotlin");
programmingLanguages.add("Python");
programmingLanguages.add("Perl");
programmingLanguages.add("Ruby");
 
System.out.println("Initial List: " + programmingLanguages);
 
// Remove the element at index `5`
programmingLanguages.remove(5);
System.out.println("After remove(5): " + programmingLanguages);
 
// Remove the first occurrence of the given element from the ArrayList
// (The remove() method returns false if the element does not exist in the ArrayList)
boolean isRemoved = programmingLanguages.remove("Kotlin");
System.out.println("After remove(\"Kotlin\"): " + programmingLanguages);
 
// Remove all the elements that exist in a given collection
List<String> scriptingLanguages = new ArrayList<>();
scriptingLanguages.add("Python");
scriptingLanguages.add("Ruby");
scriptingLanguages.add("Perl");
 
programmingLanguages.removeAll(scriptingLanguages);
System.out.println("After removeAll(scriptingLanguages): " + programmingLanguages);
 
// Remove all the elements that satisfy the given predicate
programmingLanguages.removeIf(new Predicate<String>() {
@Override
public boolean test(String s) {
return s.startsWith("C");
}
});
 
System.out.println("After Removing all elements that start with \"C\": " + programmingLanguages);
 
// Remove all elements from the ArrayList
programmingLanguages.clear();
System.out.println("After clear(): " + programmingLanguages);
}
}
Output on execution of the program looks like:

1
2
3
4
5
6
Initial List: [C, C++, Java, Kotlin, Python, Perl, Ruby]
After remove(5): [C, C++, Java, Kotlin, Python, Ruby]
After remove("Kotlin"): [C, C++, Java, Python, Ruby]
After removeAll(scriptingLanguages): [C, C++, Java]
After Removing all elements that start with "C": [Java]
After clear(): []
