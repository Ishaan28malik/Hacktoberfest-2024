package Lec5;

public class GasStation {
    public static void main(String[] args) {
        int[] gas = {1,2,3,4,5};
        int[] cost = {3,4,5,1,2};
        System.out.println(canCompleteCircuit(gas,cost));
    }
    public static int canCompleteCircuit(int[] gas, int[] cost){
        int total = 0;
        int current = 0;
        int start = 0;
        for(int i=0;i<gas.length;i++) {
            total += (gas[i] - cost[i]);
            current = current + (gas[i]-cost[i]);
            if(current<0){
                current = 0;
                start = i+1;
            }
        }
        if(total<0){
            return -1;
        }
        return start;
    }
}
