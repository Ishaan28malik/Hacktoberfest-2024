process.stdin.resume();
process.stdin.setEncoding('utf8');
// your code goes here

    comparison(2);
    

function comparison(fruits) {

    // console.log((this===window).toString());
    // var fruits = "banana";
    switch(fruits) {
     case "1": {
         var dap = "block";
         console.log("String Value");
         console.log(dap);
         break;
     }
         
     case 2: {
       let dap = "ok bhai";
         console.log(dap);
         break;  
     }
         
     case '1':
         console.log("Char Value");
         break;
     case 1:
         console.log("Integer Value");
         break;
     case "banana":
         console.log("good");
         break;
     case "apple":
         console.log("try again please");
         break;
     case "banana":
         console.log("not again banana");
         break;
     default:
         console.log("your such a pathetic");
    }
    

    // let list = [1,2,3,4,5];
    
    // for(const ele in list) {
    //     console.log(ele);
    // }
    
    // for(const ele of list) {
    //     console.log(ele);
    // }
    
    let product  =  {
         0 : 2,
        "2" : 3,
        "3" : 4,
        "4" : 5,
        // calculate : function() {
        //     return this.product[0] - this.product[3];
        // }
    };
    
    let anotherProduct = [
        { "name" : "Lakshya", "age" : 22 , "hobby" : "cricket" },
        { "name" : "Harshit", "age" : 24 , "hobby" : "mentoring" , "strength" : "good" }
    ];
    
    for(const key in product) {
        console.log(key + " " + product[key]);
    }
    
    // for(const item of product) {
    //     console.log(item);
    //     // console.log(JSON.stringify(item));
    // }
    
    
    console.log(100+ (+"200"));  // converts "200" -> 200  // 300
    console.log("200"+100);
    console.log("200"+"100");
    console.log(100+200);
    console.log('222'+'1233');
    
    price = '10';
    
    console.log(price!=10);
    console.log(price!==10);
    console.log(price!="10");
    console.log(price!=="10");
    console.log(price!='10');
    console.log(price!=='10');
    console.log(Boolean(34/"Lakshya")); // false
    console.log(Boolean(NaN),Boolean(null),Boolean(""),Boolean(''),Boolean(undefined), Boolean(false));
    console.log(typeof(undefined),typeof(null),
    typeof(comparison),typeof(anotherProduct),typeof(product),typeof(new String()));
    div = 0;
    divi = 18;
    let result;

    try {
        result = divi/div;
    } catch (error) {
        console.log("Divide by zero exception");
        console.log(error.message);
    }

    // SPREAD OPERATOR

    // 1. string to array
    let productNumber = "4234-5345=54325";
    let duplicate = [...productNumber];
    console.log(duplicate);

    // 2. copy array
    let arr = [1,2,3,4,5]
    let duplicate_arr = [...arr];
    let _arr = [5,4,3,2,1]
    let _duplicate_arr = [...arr,...duplicate_arr,..._arr];
    console.log(duplicate_arr,duplicate_arr);

    console.log(eval('2 + 2'));

    let foo = () => {
        console.log("User1");
        return false;
    }
    let bar = () => {
        console.log("User2");
        return true;
    }
    let x = false || bar() || foo();

    console.log(Boolean({}));

    return 0;
    // truthy values -> values not mentioned in falsy, boolean true or variable that has some value
    // falsy values -> NaN, null, "", '', undefined, false
}
