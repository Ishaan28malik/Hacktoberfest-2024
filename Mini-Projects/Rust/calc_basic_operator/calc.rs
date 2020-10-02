use std::io;

fn main() {
    println!("===== Simple Calculator =====");

    let mut number1:String = String::new();
    let mut number2:String = String::new();
    let mut operation:String = String::new();

    //Input Operation
    println!("Select Operator :\na. + \nb. - \nc. * \nd. /");
    io::stdin().read_line(&mut operation).expect("FAILED");

    //Input Numbers
    println!("Input Number 1 ");
    io::stdin().read_line(&mut number1).expect("FAILED");
    
    println!("Input Number 2 ");
    io::stdin().read_line(&mut number2).expect("FAILER");

    // Parsing Type
    let operation:&str = operation.trim();
    let number1:f32 = number1.trim().parse().expect("ERROR PARSING TO INTEGER"); 
    let number2:f32 = number2.trim().parse().expect("ERROR PARSING TO INTEGER");
    
    let result = match operation {
        "a" => number1+number2,
        "b" => number1-number2,
        "c" => number1*number2,
        "d" => number1/number2,
        _ => 0.0,
    };

    println!("Result {}", result);

}