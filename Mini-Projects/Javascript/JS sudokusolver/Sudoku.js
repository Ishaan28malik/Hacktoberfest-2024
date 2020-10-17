let board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

let available = [1,2,3,4,5,6,7,8,9];


function setup(){
    canvas = createCanvas(900,900);
    canvas.parent('processing');   
    textSize(50);
    textAlign(LEFT);
    
}

function draw(){
    let h = 100;
    let w = 100;
    background("white");
    fill("black");
    for(i = 0; i < 9; i++){
        if(i % 3 == 0){
            push()      
            strokeWeight(7)
            line(w * i, 0, w* i, height);
            line(0,h*i,width,h*i);
            pop()
        }
        else{
            line(w * i, 0, w* i, height);
            line(0,h*i,width,h*i);
        }        
    }
    
    for(i = 0; i < board.length; i++){
        for(j = 0; j < board[i].length; j++){
            if(board[i][j] != 0){
               text(board[i][j].toString(),j*w + 40,i*h + 70) 
            }
            
        }
    }
}

function vakjeCheck(a){
    
    for(let p = 0; p < 3; p++){
        for(let r = 0;r < 3;r++){
          for(let z = 0; z < 9; z++){
                if(a[0] >= 0 && a[0] < 3 && a[1] >= 0 && a[1] < 3){
                    //console.log(z);
                    if(available[z] == board[p][r]){
                        available.splice(z,1);
                    }
        
                }

                if(i >= 0 && i < 3 && j >= 3 && j < 6){
                    if(available[z] == board[p][r + 3]){
                        available.splice(z,1);
                    }
        
                }

                if(i >= 0 && i < 3 && j >= 6 && j < 9){
                    if(available[z] == board[p][r + 6]){
                        available.splice(z,1);
                    }
        
                }

                if(i >= 3 && i < 6 && j >= 0 && j < 3){
                    if(available[z] == board[p + 3][r]){
                        available.splice(z,1);
                    }
        
                }

                if(i >= 3 && i < 6 && j >= 3 && j < 6){
                    if(available[z] == board[p + 3][r + 3]){
                        available.splice(z,1);
                    }
        
                }

                if(i >= 3 && i < 6 && j >= 6 && j < 9){
                    if(available[z] == board[p + 3][r + 6]){
                        available.splice(z,1);
                    }
        
                }

                if(i >= 6 && i < 9 && j >= 0 && j < 3){
                    if(available[z] == board[p + 6][r]){
                        available.splice(z,1);
                    }
        
                }

                if(i >= 6 && i < 9 && j >= 3 && j < 6){
                    if(available[z] == board[p + 6][r + 3]){
                        available.splice(z,1);
                    }
        
                }

                if(i >= 6 && i < 9 && j >= 6 && j < 9){
                    if(available[z] == board[p + 6][r + 6]){
                        available.splice(z,1);
                    }
        
                }
            }
        }
         
    }
    //console.log("vakje");




}

function invul(){
    
        for(let i = 0; i < 9; i++){
            for(let j = 0; j < 9; j++){
                let cell = [i,j];
                for(let x = 0; x < 9; x++){
                    for(let q = 0; q < 9; q++){
                        if(available[x] == board[i][q] && board[i][j] == 0){
                            available.splice(x,1);
                        }
                    
                        if(available[x] == board[q][j] && board[i][j] == 0){
                            available.splice(x,1);
                        }

                        if(board[i][j] == 0){
                            vakjeCheck(cell);
                        }
                        
                        if(available.length == 1 && board[i][j] == 0){
                            board[i][j] = available[0];
                        }
                        
                        
                        
                        //available = [1,2,3,4,5,6,7,8,9];      
                        console.log(available);
                        console.log(cell,x);
                    }

                }
                available = [1,2,3,4,5,6,7,8,9];
            }
            
        }

}

function mousePressed(){
    let mousei = floor(mouseY/100);
    let mousej = floor(mouseX/100);
    if( board[mousei][mousej] < 9){
       board[mousei][mousej] += 1; 
    }
    
    else{
        board[mousei][mousej] = 0;
    }

    
}

function keyPressed(){
    if(keyCode === ENTER){
       invul();
        
        //console.log("enter");
    }
}
