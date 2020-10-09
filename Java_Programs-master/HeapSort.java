import java.util.Arrays;

public class HeapSort{
    public static void swap(int[] array, int i, int j){
        int tmp = array[i];
        array[i] = array[j];
        array[j] = tmp;
    }

    static void buildHeap(int[] array){
        int root = (array.length / 2) -1;
        while(root >= 0){
            maxHeapify(array, array.length, root);
            root--;
        }
    }

    static void maxHeapify(int[] array, int heapSize, int root){
        int left = (2 * root) + 1;
        int right = left + 1;
        int max = root;
        if(left < heapSize && array[left] > array[max]){
            max = left;
        }
        if(right < heapSize && array[right] > array[max]){
            max = right;
        }
        if(max != root){
            swap(array, root, max);
            maxHeapify(array, heapSize, max);
        }
    }

    static void heapsort(int[] array){
        buildHeap(array);
        for(int heapSize = array.length -1; heapSize >=1 ; heapSize--){
            swap(array, 0, heapSize);
            maxHeapify(array, heapSize, 0);
        }
    }
    public static void main(String[] args){
       /* final int N = 1000_000;
        int[] array = Sesion1.randomArray(N, -N, N);
        long start = System.currentTimeMillis();
        heapsort(array);
        long end = System.currentTimeMillis();
        System.out.printf("HeapSort %.2f\n",(end-start)/1000.0);

        array = Sesion1.randomArray(N, -N, N);
        start = System.currentTimeMillis();
        ShellSort.shell(array);
        end = System.currentTimeMillis();
        System.out.printf("ShellSort %.2f\n",(end-start)/1000.0);
        
        array = Sesion1.randomArray(N, -N, N);
        start = System.currentTimeMillis();
        insertionMethod.insertion(array);
        end = System.currentTimeMillis();
        System.out.printf("Insertion %.2f\n",(end-start)/1000.0);
        */
        int[] array = {4,7,2,8,10,5,9,6,3,1,7,10,9,5};
        buildHeap(array);
        System.out.println(Arrays.toString(array));
    }
}