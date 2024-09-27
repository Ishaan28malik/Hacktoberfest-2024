public class BubbleSort {
    static void bubbleSort(int[] list) {
        int n = list.length;
        int temp = 0;
        for(int i=0; i < n; i++){
            for(int j=1; j < (n-i); j++){
                if(list[j-1] > list[j]){
                    temp = list[j-1];
                    list[j-1] = list[j];
                    list[j] = temp;
                }
            }
        }

    }
    public static void main(String[] args) {
        int list[] ={1,10,500,3,55,301,12,45,23,32,100};

        System.out.println("Unsorted Array");
        for(int i=0; i < list.length; i++){
            System.out.print(list[i] + " ");
        }
        System.out.println();

        bubbleSort(list);

        System.out.println("Sorted Array");
        for(int i=0; i < list.length; i++){
            System.out.print(list[i] + " ");
        }

    }
}