package tutorial.file

object Advanced extends App {
  lazy val aLazyVal = 2
  lazy val aSecondLazyVal = aLazyVal + 4

  def nullMethod(): String = "Hello, Scala!"

  val anOption = Option(nullMethod())
  val optionResult = anOption match {
    case Some(string) => s"I got a normal result $string"
    case None => "I got a null result"
  }

  def implicitMethod(implicit arg: Int): Int = arg + 1
  implicit val myArg: Int = 5
  print(implicitMethod)
}
