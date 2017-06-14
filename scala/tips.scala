// From youtube vidoe https://www.youtube.com/watch?v=DzFt0YkZo8M&list=PLrPC0_h8PkNMGtX3Dz6FJZ_il41rg0yTq
// usefull data type
Byte
Boolean
Char
Short
Int
Long
Float
Double // has 15 digit precision

// Create a big integer
var bigint = BigInt("12312312312321312312312312312312312312321")
bigint + 1
val bigdecimal = BigDecimal("3.1415918238219830921830921809382109830921")

// tab function
var randInt = 100
randInt. // click tab, it will show all methods (object)

// mathematical operations
+,-,/,*, %

// Scala does not support ++ nor --, but
randInt += 1
randInt -= 1
randInt *= 1
randInt /= 1

// import a library
import scala.math._ // import all the libraries in the math.
abs, cbrt, ceil, round, floor, exp, pow(2,3), sqrt(2,3), hypot(2,3), log10(1000), log(2,7182),min(1,2), max(1,2), 
random // it generates random value between (random * (11 - 1)).toInt

toRadians(90) // convert degree to dadian
toDegrees(toRadians(90))

////////////////////////////
// Conditional  ==, &&, ||, !, >, <, >=, <=, !=
var age = 20
val canVote = if (age >=18) "yes" else "no"

////////////////////////////
// loop
while() {}
do{} while()
for(){}

for(i <- 0 to 10) // equal to for(i<-0 until 11)
{}
var letter = "fdasjrewuiofjdslakf"
letter.length // or click tab to see all methods supported.

var evenList = for{ i <- 1 to 20 if (i %2) == 0 } yield i // equal to [if i %2 == 0: i for i in 1:20]
// for( i <- 1 to 20) if ((i %2) == 0)  yield i : Error
var evenList = for( i <- 1 to 20 if i %2 == 0 ) yield i // Correct
// iterate multiple variables
for(i <- 1 to 10; j <- 1 to 10){
  println("i: " + i + " j:" + j)
}

///////////////////////////////
// input and output
import scala.io.StdIn.{readLine,readInt} // import only readLine and readInt
import scala.math._ // import all functions in the math library
import java.io.PrintWriter 
import scala.io.Source // allow us to read from and and write to a file
var x = 0 // must initialize variable
do{
  print("give a number ")
  x = readInt
  println(x)
}while(x != 10)

// Formatted print
val name = "Eric"
val weight = 73.2
val age = 20
println(s"Hello $name") 
println(f"I am $age old and weigh $weight%.2f") 
// %c: character, %d : integer, %f: float %s: string
printf("%05d\n", 5) // 5 space, 0 fills, right alignment
printf("'%-5d'\n", 5) // 5 space, cannot fill 0s, left alignment
printf("%.5f", 3.14) // 5 digit decimals, 0 fills

///////////////////////////////////////
// String

var s = "I saw a dragon fly by"
println("3rd index: " + s(3))
println(s.length)
println(s.concat(" and explode"))
// .equals(string), .concat, .indexOf(pattern), .toArray()
for(v <- s){
  println(v)
}

////////////////////////////////////////
// define a function
//def funcName(param1:dataType, param2:dataType):returyType ={
//    body
//    return valueToReturn // it can be omitted. The last line will be considered as return value
//}
def getSum(num1:Int=1, num2:Int=2):Int={
    return num1 + num2
}
println("1 + 2 = " + getSum(1,num=2))
def getSum(args:Int*): Int = {
    var sum:Int = 0
    for(num<- args){
        sum += num
    }
    sum
}

//////////////////////////////////////////
// Array
var favNums = new Array[Int](20) //size of 20
// Array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
for(i <- 0 to (favNums.length - 1)){
    favNums(i) = i
    println(favNums(i))
}
var favNums2 = for(i <- favNums) yield 2 * i // var favNums2 = for(i <- favNums) {yield 2 * i} : Error. Can not have {}
favNums.foreach(println)
var favNumsDiv4 = for(num <- favNums if num%4 == 0 ) yield num

var friends = Array[String]("Bob", "Tom") // new Array[String]("Bob", "Tom"), new Array("Bob", "Tom") :  ERROR
friends(0) = "Sue"
for (f <- friends){
    println(f)
}

// ArrayBuffer
import scala.collection.mutable.ArrayBuffer
var friends2= ArrayBuffer[String]() // the array size can change.
friends2.insert(0, "Bill")
friends2 += "Mike"
friends2 ++= Array("Mike", "Paul")
friends2.insert(2, "Sam","Marry", "Sally")
friends2.remove(1,2)

//////////////////////////////////////////////////////
// multi-dim array
var multTable = Array.ofDim[Int](3,4)
for(i<-0 until 3; j <- 0 until 4){
  multTable(i)(j) = i * j
}

Array.sum, .max, , min, sortWith(_>_) // or sortWith(_<_)
// Return index sequence
Array.deep.mkString(",")

///////////////////////////////////////////////////////
// map  
// http://docs.scala-lang.org/overviews/collections/maps.html

var employees = Map("Manager"->"Bob", "Secretary"-> "John") // immutable
println(employees("Manager"))
var customers = collection.mutable.Map(100-> "Paul", 101-> "Sally")
customers(100) = "Ffdsae"
customers(101) = "fdjka"
customers(101) = 100 // Error
customers("100") = "Ffdsae
// add/update new maps
customers = customers + (102-> "102", 103->"103") 
customers = customers + (102-> "102", 103->"104")  // if keys exist, update values
customers = customers + (102-> 102)  // Error. It somehow needs the same datatype.
// remove
customers = customers - 102
customers = customers - (102,103,100) // If a key does not exist, it will be skipped. 

////////////////////////////////////////////////////
// tuple
var tuple = (103, "John", 10.24)
printf("%s owes us $%.2f", tuple._2, tuple._3)
