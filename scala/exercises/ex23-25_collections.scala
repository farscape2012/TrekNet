// Ex23 - Ex -- Collection: List
//          Usage: range, tabulate, fill, merging list

object Ex23{
    
    def list_print(list:List[Int]):Unit = {
        for(i <- list){
            print(i + " ")
        }
        println
        // or
        //list.foreach{
        //    // temporary variable _
        //    print(_)
        //}
        //println("")
    }
    def even(x:Int):Boolean = {
        if (x % 2 == 0){
            return true
        }else{
            return false
        }
    }

    def main(args:Array[String]){
        var a = List(1,2,3,4)
        var b = 21 :: Nil // create a new List from scratch. prepend items
        var c = 20 :: 21 :: Nil // create a new List from scratch. 21 first is added to list and then 20. prepend items
        // var b = 21 :: a // add 21 to List a
        list_print(a)
        list_print(b)
        list_print(c)
        
        // Range
        a = List.range(1, 10, 2) // last right bound is not included. The last parameter step can be missing
        a.foreach{
            print(_)
        }
        println("")
        // Tabulate
        // have to provide logic. creates a new List whose elements are created according to the function you supply. 
        // b = = List.tabulate(10) (_ *_) //  error: missing parameter type for expanded function
        // b = = List.tabulate(10) (_ * 2) //  OK
        b = List.tabulate(10){_ + 2} // have to provide logic. creates a new List whose elements are created according to the function you supply. 
        list_print(b)

        // Merge two Lists
        c = a ::: b  //O(n) 
        // c = List.concat(a, b)
        list_print(c)
        var sum = 0
        c.foreach(sum += _)
        println(sum)
        // Filter
        var d = c.filter(even) // provide logic
        list_print(d)
        // or
        d = c.filter(x=> x %2 == 0) // provide logic
        // or 
        d = c.filter(_%2 == 0) // provide logic
        list_print(d)
    }

}
