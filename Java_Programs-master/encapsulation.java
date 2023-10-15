class human{
    private String name;
    private int age;
    public int getage(){
        return age;
    }
    public void setage(int a){
        age=a;
    }
    public void setname(String b){
        name= b;
    }
    public String getname(){
        return name ;
    }
}
public class encapsulation{
    public static void main(String[] args){ 
        human obj=new human();
        obj.setname("Gopi");
        obj.setage(20);
        System.out.println(obj.getname()+":"+obj.getage());    
    }
}
