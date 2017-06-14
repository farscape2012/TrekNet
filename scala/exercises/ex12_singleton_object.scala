/*
    Singleton and companion objects are covered in this example
        1. properties, such as both can access private members of each other
        2. They have the same name

 */

object Companion{
    /*
        This object is singleton. Singleton object can not be instantiated in the execution time. It is a single use class.
        main function is singleton. Singleton object can be used to access to the properties of the object from outside.
    */
    private var m:Int = 10 // this member can be accessible from outside (i.e., Ex06.m)
    def show(){
        var aa:Companion = new Companion // Companion object can access private memebers of companion class
        println("Value: " + aa.aa)
    }
}
class Companion{
    /* In Scala, you can create a class that has the same name as singleton object, in this case, Ex06 class. 
            This class is known as a companion class and the object is known as a companion object.
            These two object and class can get access to private members of each other.
     */
    private var aa:Int = 20
    def show(){
        println("Value: " + Companion.m) 
        // or 
        import Companion._; println("Value: " + m) 
    }
}

object Ex12{
    def main(args:Array[String]){
        var ob:Companion = new Companion
        ob.show()

        Companion.show()
    }

}
