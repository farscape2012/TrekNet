// Ex26 - 27 -- Map class
//      - the same as dict in python
//      - Immutable / mutable
//      - 

object Ex26{
    def main(args:Array[String]){
        // immutable map
        var marks = Map("john"->123, "ram"->234) // key->value
        // add to map
        marks += ("andy"->88)

        println(marks("john"))
        println(marks("andy"))
        for((k,v)<- marks){
            printf("Key:%s Value:%s\n", k,v)
        }
        // delete from map
        marks -= "john"
        for((k,v)<- marks){
            printf("Key:%s Value:%s\n", k,v)
        }

        // change value of key. This throw an error
        //marks("john") = 100
        //marks -= "john"
        //for((k,v)<- marks){
        //    printf("Key:%s Value:%s\n", k,v)
        //}
        
        // mutable map
        val a = scala.collection.mutable.Map("john"->123, "ram"->234)
        // error. It should be the same data type
        //a("john") = "JOHN"
        a("john") = 321 
        for((k,v)<- a){
            printf("Key:%s Value:%s\n", k,v)
        }
        var b = a + ("pan"->34)
        for((k,v)<- b){
            printf("Key:%s Value:%s\n", k,v)
        }
    }
}
