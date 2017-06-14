// Ex 22 -- Curring
//      The idea of currying is to partially apply function and return a function.

object Ex22{
   
    def add(x:Int, y:Int):Int={x + y}

    // This concept says that if a function has multiple parameters, this concept converts that function
    // into a form which will take only a single parameter. What will hapen to second parameter ?
    // Return data type of that function will be a closure (or anonymous) function which will take the remaining parameter
    // Three ways of defining currying function
    def add_currying1(x:Int)={(y:Int)=> x + y} 
    def add_currying2(x: Int)(y: Int) = x + y  // clean definition
    def add_currying3(x: Int): Int => Int = y => x + y 
    
    def main(args:Array[String]){
        println(add(1,2))
        println(add_currying1(1)(2))
        println(add_currying2(1)(2))
        println(add_currying3(1)) // return a function
        println(add_currying3(1)(2)) // return a value
        
        val plus5 = add_currying3(5)
        println(plus5(10))
        val plus3 = add_currying2(3)_
        println(plus3(3))
    }
}

