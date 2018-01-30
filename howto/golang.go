//// Format
// package name
package main
// import library
import "fmt"
//Or
import (
    "math/rand"
    "math"
    "fmt"
    "time"
)
// define a function, the main entrypoint.
func main() {
	fmt.Println("My favorite number is", rand.Intn(10))
  fmt.Println("The time is", time.Now())
  fmt.Println("The time is", math.Pi)
}

NOTE: if imported library is not used, then error happens

//// Exported names
// In Go, a name is exported if it begins with a capital letter.
// For example, Pizza is an exported name, as is Pi, which is exported from the math package. See about math.Pi

//// Function
// return single value 
func add(x int, y int) int {
	return x + y
}
// the same
func add(x, y int) int {
	return x + y
}

// Return multiple results
func swap(x, y string) (string, string) {
	return y, x
}
func main() {
	a, b := swap("hello", "world")
	fmt.Println(a, b)
}

// Return multiple named return values. Go's return values may be named. If so,
// they are treated as variables defined at the top of the function.
// These names should be used to document the meaning of the return values. 
// This is known as a "naked" return.
// A return statement without arguments returns the named return values. 

func split(sum int) (x int, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}
func main() {
	a, b := split(3)
	fmt.Println(a, b)
}

//// Variables
// The var statement declares a list of variables; as in function argument lists, the type is last.
// A var statement can be at package or function level. We see both in this example.


package main
import "fmt"

var c, python, java bool // default false

func main() {
	var i int // default 0
  // Variables with initializers. If an initializer is present, the type can be omitted; 
  // the variable will take the type of the initializer.
  var j, k int = 1, 2
	fmt.Println(i,j,k c, python, java)
}

//// Zero values
// Variables declared without an explicit initial value are given their zero value.
// The zero value is:
//    0 for numeric types,
//    false for the boolean type, and
//    "" (the empty string) for strings.

////Short variable declarations
// Inside a function, the := short assignment statement can be used in place of a var declaration with implicit type.
// Outside a function, every statement begins with a keyword (var, func, and so on) and so the := construct is
// not available.

k := 3

//// Basic data types
Go's basic types are

bool
string
int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr
byte  // alias for uint8
rune  // alias for int32 // represents a Unicode code point
float32 float64
complex64 complex128

package main

import (
	"fmt"
	"math/cmplx"
)
var (
	ToBe   bool       = false
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)

func main() {
	fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
	fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
	fmt.Printf("Type: %T Value: %v\n", z, z)
}

//// Type conversions
// The expression T(v) converts the value v to the type T.
// Some numeric conversions:
package main

import (
	"fmt"
	"math"
)

func main() {
	var x, y int = 3, 4
	var f  = math.Sqrt(float64(x*x + y*y))
	var z  = uint(f)
  // or the same.
  //var f float64 = math.Sqrt(float64(x*x + y*y))
	//var z uint = uint(f)
	fmt.Println(x, y, z)
}

//// Type inference
// When declaring a variable without specifying an explicit type (either by using the := syntax
// or var = expression syntax), the variable's type is inferred from the value on the right hand side.

//// Constants
const Pi float32 = 3.14 // float32 can be omitted

func main() {
	const World string = "世界" // string (type) is not necessary. 
	fmt.Println("Hello", World)
	fmt.Println("Happy", Pi, "Day")

	const Truth = true
	fmt.Println("Go rules?", Truth)
}

//// Numeric Constants
// Numeric constants are high-precision values.
// An untyped constant takes the type needed by its context.
// Try printing needInt(Big) too.
// (An int can store at maximum a 64-bit integer, and sometimes less.)

package main

import "fmt"

const (
	// Create a huge number by shifting a 1 bit left 100 places.
	// In other words, the binary number that is 1 followed by 100 zeroes.
	Big = 1 << 100
	// Shift it right again 99 places, so we end up with 1<<1, or 2.
	Small = Big >> 99
)

func needInt(x int) int { return x*10 + 1 }
func needFloat(x float64) float64 {
	return x * 0.1
}

func main() {
	fmt.Println(needInt(Small))
	fmt.Println(needFloat(Small))
	fmt.Println(needFloat(Big))
}

//// for loop
// Go has only one looping construct, the for loop.
// The basic for loop has three components separated by semicolons:
//  the init statement: executed before the first iteration
//  the condition expression: evaluated before every iteration
//  the post statement: executed at the end of every iteration
//  the braces { } are always required.
//  the init and post statement are optional.
//  the expression need not be surrounded by parentheses ( ), but can have them. But the braces { } are required.

package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)
  // The init and post statement are optional.
  sum := 1
	for ; sum < 1000; {
  // or 
  // for sum < 1000 { // The same. semicolon can be dropped.
		sum += sum
	}
	fmt.Println(sum)
  
  // forever
  for {
	}
}

// The range form of the for loop iterates over a slice or map.
// When ranging over a slice, two values are returned for each iteration.
// The first is the index, and the second is a copy of the element at that index.
// You can skip the index or value by assigning to _.
var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}

func main() {
	for i, v := range pow {
	// for _, value := range pow
		fmt.Printf("2**%d = %d\n", i, v)
	}
}


//// if
//  the expression need not be surrounded by parentheses ( ), but can have them. But the braces { } are required.
if( x < 0 ){
		return sqrt(-x) + "i"
}

// If with a short statement
// Like for, the if statement can start with a short statement to execute before the condition.
// Variables declared by the statement are only in scope until the end of the if.
// Variables declared inside an if short statement are also available inside any of the else blocks.


package main
import (
	"fmt"
	"math"
)

func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	} else {
		fmt.Printf("%g >= %g\n", v, lim)
	}
  // can't use v here, though
	return lim
}

//// Switch
// Go's switch is like the one in C, C++, Java, JavaScript, and PHP, except that Go only runs the selected 
// case, not all the cases that follow. In effect, the break statement that is needed at the end of each case
// in those languages is provided automatically in Go. Another important difference is that Go's switch cases 
// need not be constants, and the values involved need not be integers.
//
// Switch cases evaluate cases from top to bottom, stopping when a case succeeds.
package main
import (
	"fmt"
	"runtime"
  "time"
)

func main() {
	fmt.Print("Go runs on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.", os)
	}
  
  fmt.Println("When's Saturday?")
	today := time.Now().Weekday()
	switch time.Saturday {
	case today + 0:
		fmt.Println("Today.")
	case today + 1:
		fmt.Println("Tomorrow.")
	case today + 2:
		fmt.Println("In two days.")
	default:
		fmt.Println("Too far away.")
	}
  // Switch with no condition
  t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon.")
	default:
		fmt.Println("Good evening.")
	}
}

//// Defer
// A defer statement defers the execution of a function until the surrounding function returns.
// The deferred call's arguments are evaluated immediately, but the function call is not executed
// until the surrounding function returns.
package main

import "fmt"

func main() {
	fmt.Println("Hi,")
	defer fmt.Println("world") // This function executes in the end after 'hello'
    fmt.Println("My dear")
	fmt.Println("Hif,")
	a := 1
	fmt.Println(a)
	fmt.Println("hello")
}

//// Stacking defers
// Deferred function calls are pushed onto a stack. When a function returns, its deferred calls are executed 
// in last-in-first-out order. The deferred functions are stacked into a list. To learn more about defer statements
// read this blog post (https://blog.golang.org/defer-panic-and-recover).
//    Defer is commonly used to simplify functions that perform various clean-up actions.

package main

import "fmt"

func main() {
	fmt.Println("Hi,")
	defer fmt.Println("world")
	defer fmt.Println("Hello   33")
    fmt.Println("My dear")
	fmt.Println("Hif,")
	a := 1
	fmt.Println(a)
	fmt.Println("hello")
}
// output
Hi,
My dear
Hif,
1
hello
Hello   33
world


//// Pointers
// A pointer holds the memory address of a value. The type *T is a pointer to a T value. Its zero value is nil.
// Go has no pointer arithmetic.
var p *int
i := 42
p = &i
fmt.Println(*p) // read i through the pointer p
*p = 21         // set i through the pointer p

//// Structs
// A struct is a collection of fields.
// Struct fields are accessed using a dot.
// Struct fields can be accessed through a struct pointer.

package main
import "fmt"

type Vertex struct {
	X int
	Y int
}
var (
	v1 = Vertex{1, 2}  // has type Vertex
	v2 = Vertex{X: 1}  // Y:0 is implicit
	v3 = Vertex{}      // X:0 and Y:0
	q  = &Vertex{1, 2} // has type *Vertex
)
func main() {
  v := Vertex{1, 2}
	v.X = 4
	fmt.Println(v.X)
  p := &v
	p.Y = 1e9
  fmt.Println(v.Y)
  fmt.Println(p.Y)
 
  fmt.Println(v1)
  fmt.Println(v2)
  fmt.Println(v3)
  fmt.Println(*q)

}

//// Arrays
// The type [n]T is an array of n values of type T.
// An array has a fixed size. A slice, on the other hand, is a dynamically-sized, flexible view into the
// elements of an array. In practice, slices are much more common than arrays.
// Slices: left closed, and right open
//   The type []T is a slice with elements of type T. var s []int = primes[1:4]
//   A slice does not store any data, it just describes a section of an underlying array.
//   Changing the elements of a slice modifies the corresponding elements of its underlying array.
//   Other slices that share the same underlying array will see those changes.
//  
// Slice length and capacity
//   A slice has both a length and a capacity.
//   The zero value of a slice is nil.
package main

import "fmt"

func main() {
	var a [2]string
	a[0] = "Hello"
	a[1] = "World"
	fmt.Println(a[0], a[1])
	fmt.Println(a)

	primes := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println(primes)
  b := [2]string{"hello", "world"}
  //or
  //b := [2] string {"hello", "world"}
  fmt.Println(b[1:2])
  // slice
  var s []int = primes[1:4]
  fmt.Println(s)
  fmt.Println(s[0:10])
  fmt.Println(s[:10])
  fmt.Println(s[0:])
  fmt.Println(s[:])
  fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
  var d []int
  fmt.Println(d, len(d), cap(d))
  if d == nil {
  fmt.Println("nil!")
	}
}

package main

import "fmt"

func main() {
	q := []int{2, 3, 5, 7, 11, 13}
	fmt.Println(q)

	r := []bool{true, false, true, true, false, true}
	fmt.Println(r)

	s := []struct {
		i int
		b bool
	}{
		{2, true},
		{3, false},
		{5, true},
		{7, true},
		{11, false},
		{13, true},
	}
	fmt.Println(s)
}

// Creating a slice with make
// Slices can be created with the built-in make function; this is how you create dynamically-sized arrays.
// The make function allocates a zeroed array and returns a slice that refers to that array:
a := make([]int, 5)  // len(a)=5
//To specify a capacity, pass a third argument to make:

b := make([]int, 0, 5) // len(b)=0, cap(b)=5

b = b[:cap(b)] // len(b)=5, cap(b)=5
b = b[1:]      // len(b)=4, cap(b)=4

func main() {
	// Create a tic-tac-toe board.
	board := [][]string{
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
	}

	// The players take turns.
	board[0][0] = "X"
	board[2][2] = "O"
	board[1][2] = "X"
	board[1][0] = "O"
	board[0][2] = "X"

	for i := 0; i < len(board); i++ {
		fmt.Printf("%s\n", strings.Join(board[i], " "))
	}
}

// slice append
func append(s []T, vs ...T) []T

func main() {
	var s []int
	printSlice(s)

	// append works on nil slices.
	s = append(s, 0)
	printSlice(s)

	// The slice grows as needed.
	s = append(s, 1)
	printSlice(s)

	// We can add more than one element at a time.
	s = append(s, 2, 3, 4)
	printSlice(s)
}

func printSlice(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

//// Maps
// A map maps keys to values.
// The zero value of a map is nil. A nil map has no keys, nor can keys be added.
// The make function returns a map of the given type, initialized and ready for use.
// the keys can be string, int, float32.

type Vertex struct {
	Lat, Long float64
}

var m map[string]Vertex

var n = map[string]Vertex{
	"Bell Labs": Vertex{
		40.68433, -74.39967,
	},
	"Google": Vertex{
		37.42202, -122.08408,
	},
}

func main() {
	m = make(map[string]Vertex)
	m["Bell Labs"] = Vertex{
		40.68433, -74.39967,
	}
	fmt.Println(m["Bell Labs"])
	fmt.Println(n)
}

// Mutating Maps
//   Insert or update an element in map m:
m[key] = elem

//   Retrieve an element:
elem = m[key]

//   Delete an element:
delete(m, key)

//   Test that a key is present with a two-value assignment:
elem, ok = m[key]

//   If key is in m, ok is true. If not, ok is false.
//   If key is not in the map, then elem is the zero value for the map's element type.
//   Note: if elem or ok have not yet been declared you could use a short declaration form:
elem, ok := m[key]

//// Function values
// Functions are values too. They can be passed around just like other values.
// Function values may be used as function arguments and return values.

func compute(fn func(float64, float64) float64) float64 {
	//         [    type             ][ return ]
	return fn(3, 4)
}

func main() {
	hypot := func(x, y float64) float64 {
		return math.Sqrt(x*x + y*y)
	}
	fmt.Println(hypot(5, 12))

	fmt.Println(compute(hypot))
	fmt.Println(compute(math.Pow))
}

//// Methods
// Go does not have classes. However, you can define methods on types.
// A method is a function with a special receiver argument.
// The receiver appears in its own argument list between the func keyword and the method name.
// In this example, the Abs method has a receiver of type Vertex named v.
// Remember: a method is just a function with a receiver argument.

type Vertex struct {
	X, Y float64
}

func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
// Here's Abs written as a regular function with no change in functionality.
func Abs(v Vertex) float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v := Vertex{3, 4}
	fmt.Println(v.Abs())
	fmt.Println(Abs(v))
}
// You can declare a method on non-struct types, too.
// In this example we see a numeric type MyFloat with an Abs method. 
// You can only declare a method with a receiver whose type is defined in the same package as the method. 
// You cannot declare a method with a receiver whose type is defined in another package (which includes
// the built-in types such as int).

import (
	"fmt"
	"math"
)

type MyFloat float64

func (f MyFloat) Abs() float64 {
	if f < 0 {
		return float64(-f)
	}
	return float64(f)
}

func main() {
	f := MyFloat(-math.Sqrt2)
	fmt.Println(f.Abs())
}

// another example
package main
import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}
// or 
//func (v Vertex) Scale(f float64) Vertex {
//	v.X = v.X * f
//	v.Y = v.Y * f
//	return v
//}

func main() {
	v := Vertex{3, 4}
	v.Scale(10)
	fmt.Println(v.Abs())
}

//
// Similar functionality with normal way
//
package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

func Abs(v Vertex) float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func Scale(v *Vertex, f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func main() {
	v := Vertex{3, 4}
	Scale(&v, 10)
	fmt.Println(Abs(v))
}

// Another example
package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func (v *Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v := &Vertex{3, 4}
	fmt.Printf("Before scaling: %+v, Abs: %v\n", v, v.Abs())
	v.Scale(5)
	fmt.Printf("After scaling: %+v, Abs: %v\n", v, v.Abs())
}






























