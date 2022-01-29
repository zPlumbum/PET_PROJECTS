import tutorial.file.Obj._

object Example extends App {

  class Ex[T](name: String, value: T){
    def printNameAndValue: T = value
  }

  val ex = new Ex[Int]("Интовка", 5)

  def abc(illig: Int): Int = {
    val newInt = illig
    newInt
  }
  println(abc(7))

  val student = new Student("Jerry", 19)

  student.sayHello("Alex")

}
