// Ex 20 -- Exception handling

object Ex20{
    def main(args:Array[String]){
        var a:Int = 12
        var b:Int = 0
        try{
            println(a/b) // exception, How to handle ?
        }catch{
            case ex:ArithmeticException => println("Exception is generated"); println(ex)
        }

    }
}
