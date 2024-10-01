package Ds.Queue;

public class Runner {

	public static void main(String[] args) {
		arrayQueue q = new arrayQueue();
		q.enQueue(5);
		q.enQueue(4);
		q.enQueue(3);
		q.enQueue(7);
		q.enQueue(6);
		q.enQueue(1);
//		q.enQueue(0);

		q.deQueue();
		q.show();
		System.out.println("size is "+ q.getSize());
	}

}
