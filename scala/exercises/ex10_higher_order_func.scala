// Higher order function -- Passing anonymous function as parameter
// With higher order function, you can change logic but have the same input and output interface

object Ex17{
    def perform(func:(Int, Int)=> Int ){
        // ()=> "Hello world" // return String, No data type
        // Unit  => String // No parameters, then use Unit (None)
        // (x:Int, y:Int) => "value" +x+y 
        // (Int, Int) => String
        println(func(1,2))
    }
    def main(args:Array[String]){
        
        perform((x:Int,y:Int)=>x*y)
    }
}
