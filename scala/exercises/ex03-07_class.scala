/* Ex03 - 07, it is demonstrated that how to 
    1. craete a class,
    2. set/get members by using . operation
    3. create multiple constructors
    4. default arguments
    5. overwrite methods which have been builtin, such as toString, equals and hashCode.
        Takes toString as an example

*/
class Point {
    // there is only one default constructor
    private var _x = 0
    private var _y = 0
    private val bound = 100

    def x = _x // getter function
    def x_= (newValue: Int): Unit = { // setter function with verification
        if (newValue < bound) 
            _x = newValue 
        else 
            printWarning
    }
    def y = _y // getter function
    def y_= (newValue: Int): Unit = { // setter function with verification
      if (newValue < bound) _y = newValue else printWarning
    }
    private def printWarning = println("WARNING: Out of bounds")
    override def toString = "(" + _x + "," + _y + ")"
}

class PointMultiConstructors(input1:Int, input2:Int, bound:Int) {
    // Create multi-constructors
    private var _x = input1
    private var _y = input2
    private val _bound = bound

    def this(){
        this(0,0,100)
    }
    def this(x:Int, y:Int){
        this(x,y,100)
    }
    def this(y:Int){
        this(0,y,100)
    }
    def x = _x // getter function
    def x_= (newValue: Int): Unit = { // setter function with verification
        if (newValue < bound) 
            _x = newValue 
        else 
            printWarning
    }
    def y = _y // getter function
    def y_= (newValue: Int): Unit = { // setter function with verification
      if (newValue < bound) _y = newValue else printWarning
    }
    private def printWarning = println("WARNING: Out of bounds")
    override def toString = "(" + _x + "," + _y + ")"
}
class PointMultiConstructorsWithArgument(input1:Int=10, input2:Int=10, bound:Int=10) {
    // Create multi-constructors with default arguments
    private var _x = input1
    private var _y = input2
    private val _bound = bound

    def this(x:Int, y:Int){
        this(x,y,100)
    }
    def this(y:Int){
        this(0,y,100)
    }
    def x = _x // getter function
    def x_= (newValue: Int): Unit = { // setter function with verification
        if (newValue < bound) 
            _x = newValue 
        else 
            printWarning
    }
    def y = _y // getter function
    def y_= (newValue: Int): Unit = { // setter function with verification
      if (newValue < bound) _y = newValue else printWarning
    }
    private def printWarning = println("WARNING: Out of bounds")
    override def toString = "(" + _x + "," + _y + ")"
}
object Ex02{
    def main(args:Array[String]){
        var point = new Point
        // get values
        println(point.x)
        println(point.y)
        // set new values
        point.x = 10
        point.y = 20
        println(point.x)
        println(point.y)

        // toString
        println(point)
        // multiconstrucors
        var pointmulti1 = new PointMultiConstructors()
        println(pointmulti1.x)
        println(pointmulti1.y)

        pointmulti1 = new PointMultiConstructors(1,2)
        println(pointmulti1.x)
        println(pointmulti1.y)

        pointmulti1 = new PointMultiConstructors(10)
        println(pointmulti1.x)
        println(pointmulti1.y)
        // multiconstrucors
        var pointmultiwithargument = new PointMultiConstructorsWithArgument()
        println(pointmultiwithargument.x)
        println(pointmultiwithargument.y)
    }
}
