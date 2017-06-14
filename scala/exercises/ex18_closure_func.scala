// Ex 18 -- Closure function whose return value depends on some variables which are declared outside the function.
//          In this example, func is a closure
//          

object Ex18{
    def main(args:Array[String]){
        var y:Int = 120 // declare a variable
        // anonymous function which uses a variable declared outside, out of scope.
        // If variables defined inside and outside of function have the same name, how to refer them?
        val func = (x:Int) => x * y // anonymous function which uses a variable declared outside, out of scope (If variables defined inside and outside of function have the same name, how to refer them?)
        println(func(10))
    }
}
