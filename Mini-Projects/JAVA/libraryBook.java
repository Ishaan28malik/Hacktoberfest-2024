import java.util.Hashtable;
import java.util.Scanner;

public class libraryBook {
    public static void main(String[] args) {
        // insisiasi
        Hashtable<String, String> Rak1 = new Hashtable<String, String>();
        Hashtable<String, String> Rak2 = new Hashtable<String, String>();
        boolean active = false;
        int choose,rak;
        String titleBook1,codeBook1,titleBook2,codeBook2,search;
        Scanner scanner = new Scanner(System.in);

        do {
            System.out.println("----- Library List Menu -----");
            System.out.println("1. Add Book to shelf");
            System.out.println("2. View Book");
            System.out.println("3. Find Book");
            System.out.println("4. View the number of books");
            System.out.println("5. Add Book to shelf from shelf available");
            System.out.println("6. Move Book");
            System.out.println("7. Clear shelf");
            System.out.println("8. Exit");
            System.out.print("Input options : ");
            choose = scanner.nextInt();
            switch (choose){
                case 1:
                    System.out.print("Choose shelf [1/2] : ");
                    rak = scanner.nextInt();
                    scanner.nextLine();
                    if (rak == 1){
                        System.out.print("Enter a book title : ");
                        titleBook1 = scanner.nextLine();
                        System.out.print("Enter a book code : ");
                        codeBook1 = scanner.nextLine();

                        Rak1.put(titleBook1, codeBook1);
                        if (!Rak1.isEmpty()){
                            System.out.println("Book successfully added to shelf 1");
                        }
                    }else if (rak == 2){
                        System.out.print("Enter a book title : ");
                        titleBook2 = scanner.nextLine();
                        System.out.print("Enter a book code  : ");
                        codeBook2 = scanner.nextLine();

                        Rak2.put(titleBook2, codeBook2);
                        if (!Rak2.isEmpty()){
                            System.out.println("Book successfully added to shelf 2");
                        }
                    }else {
                        System.out.println("Sorry The shelf is not available!");
                    }
                    break;
                case 2:
                    System.out.print("Choose shelf [1/2] : ");
                    rak = scanner.nextInt();
                    if (rak == 1){
                        if (!Rak1.isEmpty()){
//                                Map<String, String> hash = new TreeMap<String,String>(Rak1);
                            System.out.println("List book shelf 1 : " + Rak1);
                        }else {
                            System.out.println("There are no books on the shelf 1");
                        }
                    }else if (rak == 2){
                        if (!Rak2.isEmpty()){
                            System.out.println("List book shelf 2 : " + Rak2);
                        }else {
                            System.out.println("There are no books on the shelf 2");
                        }
                    }else {
                        System.out.println("Sorry No shelf is available!");
                    }
                    break;
                case 3:
                    scanner.nextLine();
                    System.out.print("Enter a book title  : ");
                    search = scanner.nextLine();
                    String key = search;
                    if (Rak1.containsKey(key)){
                        System.out.println("Book " + search + " available on code " + Rak1.get(search));
                    }else if (Rak2.containsKey(key)){
                        System.out.println("Book " + search + " available on code " + Rak2.get(search));
                    }else{
                        System.out.println("Book not available!");
                    }
                    break;
                case 4:
                    System.out.println("Number of books on shelf 1 : " + Rak1.size());
                    System.out.println("Number of books on shelf 2 : " + Rak2.size());
                    break;
                case 5:
                    System.out.print("Choose shelf [1/2] : ");
                    rak = scanner.nextInt();
                    if (rak == 1){
                        Rak2.putAll(Rak1);
                        System.out.println("Books from shelf 1 are copied successfully to shelf 2");
                    }else if(rak == 2){
                        Rak1.putAll(Rak2);
                        System.out.println("Books from shelf 2 are copied successfully to shelf 1");
                    }else {
                        System.out.println("Sorry The shelf is not available!");
                    }
                    break;
                case 6:
                    System.out.print("Choose shelf [1/2] : ");
                    rak = scanner.nextInt();
                    scanner.nextLine();
                    if (rak == 1){
                        System.out.print("Enter the title of the Book : " );
                        titleBook1 = scanner.nextLine();
                        System.out.print("Enter the code of the Book : ");
                        codeBook1 = scanner.nextLine();
                        if (Rak1.containsKey(titleBook1)){
                            System.out.println("Successfully updated shelf 1");
                            Rak1.replace(titleBook1,codeBook1);
                        }else{
                            System.out.println("Book title not found!");
                        }
                    }else if(rak == 2){
                        System.out.print("Enter the title of the Book : " );
                        titleBook2 = scanner.nextLine();
                        System.out.print("Enter the code of the Book : ");
                        codeBook2 = scanner.nextLine();
                        if (Rak2.containsKey(titleBook2)){
                            System.out.println("Successfully updated shelf 2");
                            Rak2.replace(titleBook2,codeBook2);
                        }else{
                            System.out.println("Book title not found!");
                        }
                    }else{
                        System.out.println("Sorry The shelf is not available!");
                    }
                    break;
                case 7:
                    System.out.print("Choose shelf [1/2] : ");
                    rak = scanner.nextInt();
                    if (rak == 1){
                        Rak1.clear();
                        System.out.println("Rak 1 emptied successfully");
                    }else if (rak == 2){
                        Rak2.clear();
                        System.out.println("Rak 2 emptied successfully");
                    }else{
                        System.out.println("Sorry The shelf is not available!");
                    }
                    break;
                case 8:
                    active = true;
                    System.exit(0);
            }
        }while (!active);
    }

}
