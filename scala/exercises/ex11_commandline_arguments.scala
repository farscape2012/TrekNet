/*  This example demonstrates how to get arguments from command line and pass to main function
    run from console:
                scala Ex05 1 2 3 4 fdjaslkfdjasl ./ex05_commandline_arguments.scala
 */
object Ex11{
    def main(args:Array[String]){
        if(args.length > 1){
            for (ar <- args){
                println(ar)
            }
        }else{
            println("Please specify some arguments")
        }
    }
}
