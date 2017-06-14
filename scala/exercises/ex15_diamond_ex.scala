/*  Diamond problem
 */

trait One{
    def show(){
        println("Show function in One trait")
    }
}
trait Two extends One{
    override def show(){
        println("Show function in Two trait")
    }
}
trait Three extends One{
    override def show(){
        println("Show function in Three trait")
    }
}

class Four extends Two with Three 
// Here Four inherits show function from the last one (Three). 
// If Two comes last, then get show  trait from Two.
object Ex15{
    def main(args:Array[String]){
        var ob:Four = new Four
        ob.show()
    }
}
