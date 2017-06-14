/* In this example, usage of Array is covered, including multidimensional array creation and access
*/
object Ex09{
    def main(args:Array[String]){
        // Single dimensional array
        var myArray:Array[Int] = new Array[Int](5)  // Type: Array[Int], it saves Int array in the array. Array[Int](5): 5 int values. If String/Float is needed, then just change Int to String or Float
        myArray(0) = 0
        myArray(1) = 1
        myArray(2) = 2
        myArray(3) = 3
        for(i <- 0 to 4){
            println(myArray(i))
        }

        for(i <- myArray){
            println(i)
        }


        // Multi-dimensional array
        var bArray = Array.ofDim[String](2,3)      // two dimensions, two rows and three columns
        bArray(0)(0) = "00"
        bArray(0)(1) = "01"
        bArray(0)(2) = "02"
        bArray(1)(0) = "10"
        bArray(1)(1) = "11"
        bArray(1)(2) = "12"
        for(i<-0 to 1; j <- 0 to 2){
            println(bArray(i)(j))
        }

        // Three dimensional array
        var cArray = Array.ofDim[String](2,3,4)      // three dimensionss
        for(i<-0 to 1; j <- 0 to 2; k<-0 to 3){
            cArray(i)(j)(k) = i + " " + j + " " + k 
        }
        for(i<-0 to 1; j <- 0 to 2; k<-0 to 3){
            println(cArray(i)(j)(k)) 
        }
    }
}
