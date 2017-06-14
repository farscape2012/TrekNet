// Anonymous function

object Ex16{
    def main(args:Array[String]){
        var f = () => println("Hello world") // Anonymous function.
        // how to call this function?
        f.apply()
        // Or prefer 
        f()
        var b = (x:Int, y:Int) => x+y // Anonymous function return Int value, can be string, Float, etc.
        println(b(1,2))
        var c = (x:Int, y:Int) => "value" +x+y // Anonymous function return String. Here + is used as concat
        println(c(1,2))
        var d = (x:Int, y:Int) => {"value" +(x+y)} // Anonymous function return String. Here first + is used as concat second is used as plus
        println(d(1,2))
    }
}
