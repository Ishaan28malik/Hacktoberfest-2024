package Ds.Heaps;

import java.util.ArrayList;

public class pqHeap {
    public static class PriorityQueue{
    	ArrayList<Integer> data;
    	
    public void PriorityQueue(){
    	data = new ArrayList<>();
    }
    public void add(int val) {
    	data.add(val);
    	upheapfiy(data.size()-1);	
    }
    private void upheapfiy(int i) {
    	if(i==0) {
    		return;
    	}
    	int p1= (i-1)/2;
    	if(data.get(i) < data.get(p1)) {
    		swap(i ,p1);
    		upheapfiy(p1);
    	}
    }
    private void swap(int i , int j) {
    	int ith = data.get(i);
    	int jth = data.get(j);
    	data.set(i, jth);
    	data.set(j, ith);
    }
    public int remove() {
    	if(this.size()==0) {
    		System.out.println("Underflow");
    		return -1;
    	}
    	swap(0,data.size()-1);
    	int val = data.remove(data.size()-1);
    	downheapify(0);
    	return val;
    }
    private void downheapify(int i) {
    	int min = i;
    	int li = 2*i+1;
    	if(li< data.size() && data.get(li)< data.get(min)) {
    		min = li;
    	}
    	int ri = 2*i+2;
    	if(ri< data.size() && data.get(ri)< data.get(min)) {
    		min = ri;
    	}
    	if(min != i) {
    		swap( i , min);
    		downheapify(min);
    	}
    }
    public int peek() {
    	if(this.size()==0) {
    		System.out.println("Underflow");
    		return -1;
    	}
    	return data.get(0);
    }
    public int size() {
    	 return data.size();
    }
    
    }
	public static void main(String[] args) {
		

	}

}
