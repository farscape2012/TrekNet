/* In this exercise, it is demonstrated that how to 
    1. use loops (for, while, do-while)
        a. 
    2. 
    3. 
    4. 
    5. 

*/
object Ex08{
    def main(args:Array[String]){

        for (i <- 1 to 5) // equivalent val j:Int = 1 to 5; "<-" is a generator creating a immutable variable.
            println(i)    // the scope of i is only valid in this for loop. it is a tempolary variable.
                          // other tips: 1 to 10; 1 until 10 (10 not included in this case)
        var i:Int = 0
        while (i < 5){
            println(i)
            i += 1
        }

        do{
            println(i)
            i -= 1
        }while(i>0)
    }
}
