class Account(id:Int, name:String,balence:Double) {
    def this(a:Int, n:String){
        // Constructor
        this(a, n, 0)
    }
    def this(a:Int){
        // Constructor
        this(a, "", 0)
    }
    def this(){
        // Constructor
        this(0,"", 0)
    }
    def show(){
        println("Name: " + name + " id: " + id + " Balence: " + balence)
    }
}

object Hello{
    def main(args:Array[String]){
        var account1 = new Account(12, "John", 10000)
        account1.show()
        var account2 = new Account(12, "John")
        account2.show()
        var account3 = new Account(12)
        account3.show()
    }
}
