package Ds.Hashmaps;

import java.util.*;

public class HashCodeandEqual {

	public static void main(String[] args) {
	  pen  pen1 = new pen(10,"blue");	
	  pen  pen2 = new pen(10,"blue");	
	  
//	  System.out.println(pen1.equals(pen2));
	  Set<pen> pens = new HashSet<>();
	  pens.add(pen1);
	  pens.add(pen2);
	  System.out.println(pens);
	}
	
}
class pen{
	int price;
	String color;
	public pen(int price , String color) {
		this.price = price;
		this.color = color;
	}
//	@Override
//	public boolean equals(Object obj) {
//		pen that = (pen) obj;
//		boolean isEqual = this.price == that.price && this.color.equals(that.color);
//		return isEqual;
//	}
//	@Override
//	public int hashCode() {
//		return price + color.hashCode();
//	}
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((color == null) ? 0 : color.hashCode());
		result = prime * result + price;
		return result;
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		pen other = (pen) obj;
		if (color == null) {
			if (other.color != null)
				return false;
		} else if (!color.equals(other.color))
			return false;
		if (price != other.price)
			return false;
		return true;
	}
}