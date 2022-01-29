package tutorial.file

object ScalaBasics extends App {
  val aBooleanVal = true
  val ifExpression = if (!aBooleanVal) 56 else 0

  def factorial(n: Int): Int =
    if (n <= 1) 1
    else n * factorial(n - 1)

  println(factorial(5))

}
