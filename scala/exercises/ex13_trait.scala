/*
    1. Trait
        a. Trait is similar to interface, declare methods and members (with or without definition and instantiation). Some functions can be defined. Trait can not be instantiated.
        b. Traits are used to define object types by specifying the signature of the supported methods.
        c. Scala allows traits to be partially implemented; i.e. it is possible to define default implementations for some methods. 
        d. In contrast to classes, traits may not have constructor parameters.
    
    Abstract class

    Multi-traits
*/

trait One{
    var x:Int   // abstract field
    var y:Int = 1 // concrete field
    def show()
}

trait Two{
    def show()
}
class Three extends One with Two{
    /* this class has to define all functions declared in the trait.
        If this class does not define all functions, this class is becoming abstract class that can not create objects or can not be instantiated.
        When declared methods/members are not defined/implemented/initialized, you will get errors while compling it (class Three needs to be abstract, since method show in trait One of type ()Unit is not defined). 
        To solve this, add abstrct keyword before class Three extends One with Two.... Or initialize all members and define all methods.

        If there are more traits, then continue use with TraitA with TraitB......
     */
    var x = 12;
    def show(){
        println("show function in the trait is called")
    }
    def display(){
        println("display function")
    }
}
object Ex13{
    def main(args:Array[String]){
        var ob:Three = new Three
        ob.show()
        ob.display()
    }
}
