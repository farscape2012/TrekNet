// Higher order function -- Passing anonymous function as parameter

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
