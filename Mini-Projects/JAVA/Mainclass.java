import java.util.Scanner;
import java.util.ArrayList;

abstract class User{
	String name;
	String nickname;
	int age;
	String gender;
	int user_id;
	final String community;
	abstract void user_contact();
	User(){
		community = "IIITG";
		name = "Virat";
		nickname = "Chiku";
	}
	public void print_name(String name){
		System.out.println("Name of the user is : "+ name);
	}
	// method overloading
	public void print_name(String name,String nickname){
		System.out.println("Name of the user is - "+ name + " but popularly known as - "+ nickname);
	}
	public void set_details(){
		Scanner input = new Scanner(System.in);
		System.out.print("Enter your name : ");
		name = input.nextLine();
		System.out.print("Enter your age : ");
		age = input.nextInt();
		input.nextLine();
		System.out.print("Enter your gender : ");
		gender = input.nextLine();
		System.out.print("Enter your User_id : ");
		user_id = input.nextInt();
	}
	public void getDetails(int id){
		System.out.println("Name : "+ name);
		System.out.println("Age : "+ age);
		System.out.println("Gender : "+ gender);
		System.out.println("Member of community : "+ community);
	}
	public int getId(int id){
		return id;
	}
}

class Student extends User{
	Scanner input = new Scanner(System.in);
	String current_year;
	float cpi;
	float semester_cpi;
	Student(){
		cpi = 8.79f;
		semester_cpi = 8.77f;
	}
	public void getCPI(float cpi){
		System.out.println("Total CPI of student is "+ cpi);
	}
	// method overloading
	public void getCPI(float cpi,float semester_cpi){
		System.out.println("Total CPI of student is "+ cpi);
		System.out.println("CPI of current semester is "+ semester_cpi);
	}
	public void user_contact(){
		int number;
		System.out.print("Enter your contact number : ");
		number = input.nextInt();

	}
	// method overriding
	public void set_details(){
		super.set_details();
		System.out.print("Enter your present graduation year : ");
		current_year = input.nextLine();
		System.out.print("Enter your CPI : ");
		cpi = input.nextFloat();
	}
	// method overriding
	public void getDetails(int id){
		super.getDetails(id);
		System.out.println("Present year of studing : "+ current_year);
		System.out.println("CPI till now : "+ cpi);
		user_contact();
	}
}
class Faculty extends User{
	Scanner input = new Scanner(System.in);
	int salary;
	int extraSalary;
	int noOfPublication;
	String placeOfGraduation;
	void user_contact(){
		int number;
		System.out.print("Enter your contact number : ");
		number = input.nextInt();
	}
	Faculty(){
		salary = 100000;
		extraSalary = 50000;
	}
	public void getSalary(int salary){
		System.out.println("Salary of faculty member is : "+salary);
	}
	// method overloading
	public void getSalary(int salary,int extraSalary){
		System.out.println("Salary of faculty member is : "+salary);
		System.out.println("Extra salary from other activities of faculty : "+extraSalary);
	}
	// method overriding
	public void set_details(){
		super.set_details();
		System.out.print("Enter salary of faculty : ");
		salary = input.nextInt();
		System.out.print("Enter total number of publications under his/her name : ");
		noOfPublication = input.nextInt();
		input.nextLine();
		System.out.print("Enter place from where you graduated : ");
		placeOfGraduation = input.nextLine();
	}
	// method overriding
	public void getDetails(int id){
		super.getDetails(id);
		System.out.println("Total number of Publications : "+ noOfPublication);
		System.out.println("Graduated from : "+ placeOfGraduation);
	}
}

class Staff extends User{
	final int salary;
	int extraSalary;
	String areaOfWorking;
	Scanner input = new Scanner(System.in);
	void user_contact(){
		int number;
		System.out.print("Enter your contact number : ");
		number = input.nextInt();
	}
	Staff(){
		salary = 5000;
		extraSalary = 1500;
	}
	// method overriding
	public void set_details(){
		super.set_details();
		//salary = input.nextInt();
		System.out.print("Enter your region of your work : ");
		areaOfWorking = input.nextLine();
	}
	// method overriding
	public void getDetails(int id){
		super.getDetails(id);
		System.out.println("Monthly salary : "+ salary);
		System.out.println("Place of working : "+ areaOfWorking);
	}
	final void annualSalary(int salary){
		System.out.println("Annual income of the member is : "+ salary * 12);
	}
	public void getSalary(int salary){
		System.out.println("Salary of staff member is : "+salary);
	}
	// method overloading
	public void getSalary(int salary,int extraSalary){
		System.out.println("Salary of staff member is : "+salary);
		System.out.println("Extra salary from other activities of staff : "+extraSalary);
	}
}

public class Mainclass{
	public static void main(String[] args){
		ArrayList<Student> student = new ArrayList<>();
		ArrayList<Faculty> faculty = new ArrayList<>();
		ArrayList<Staff> staff = new ArrayList<>();
		ArrayList<User> common = new ArrayList<>();
		int choice;
		int opt;
		int option;
		while(true){
			System.out.println("Enter as : 1. Admin 2. Non-admin 3. Exit portal");
			Scanner input = new Scanner(System.in);
			choice = input.nextInt();
			switch(choice){
				case 1: {
					System.out.println("Length of student arraylist : "+student.size());
					System.out.println("Length of faculty arraylist : "+faculty.size());
					System.out.println("Length of staff arraylist : "+staff.size());
					System.out.println("Length of common arraylist : "+common.size());
					System.out.println("Enter the operation : 1. Create object 2. Delete Object");
					opt = input.nextInt();
					switch(opt){
						case 1: {
							System.out.println("Choose the class for object creation : 1. Student 2. Faculty 3. Staff");
							option = input.nextInt();
							switch(option){
								case 1: {
									System.out.println("Going for object insertion..................");
									Student studentObj = new Student();
									studentObj.set_details();
									student.add(studentObj);
									common.add(studentObj);
									break;
								}
								case 2: {
									System.out.println("Going for object insertion..................");
									Faculty facultyObj = new Faculty();
									facultyObj.set_details();
									faculty.add(facultyObj);
									common.add(facultyObj);
									break;
								}
								case 3: {
									System.out.println("Going for object insertion..................");
									Staff staffObj = new Staff();
									staffObj.set_details();
									staff.add(staffObj);
									common.add(staffObj);
									break;
								}
							}
							break;
						}
						case 2: {
							System.out.println("Choose the class for object deletion : 1. Student 2. Faculty 3. Staff");
							option = input.nextInt();
							switch(option){
								case 1: {
									if(student.size() >= 1){
										System.out.println("Number of objects in student arraylist is "+ student.size());
										System.out.println("Proceed for deletion...........");
										student.remove(0);
										System.out.println("Object deleted successfully.");
									}
									else
										System.out.println("No objects in student arraylist.");
									break;
								}
								case 2: {
									if(faculty.size() >= 1){
										System.out.println("Number of objects in faculty arraylist is "+ faculty.size());
										System.out.println("Proceed for deletion...........");
										faculty.remove(0);
										System.out.println("Object deleted successfully.");
									}
									else
										System.out.println("No objects in faculty arraylist.");
									break;
								}
								case 3: {
									if(staff.size() >= 1){
										System.out.println("Number of objects in staff arraylist is "+ staff.size());
										System.out.println("Proceed for deletion...........");
										staff.remove(0);
										System.out.println("Object deleted successfully.");
									}
									else
										System.out.println("No objects in staff arraylist.");
									break;
								}
							}
						}
					}
					break;
				}
				case 2: {
					input.nextLine();
					System.out.print("Enter user name for information : ");
					String name = input.nextLine();
					for(int i=0;i<common.size();i++){
						if(common.get(i).name.equals(name)){
							common.get(i).getDetails(common.get(i).user_id);
							break;
						}
					}
					break;
				}
				case 3: {
					return;
				}
			}
		}
	}
}