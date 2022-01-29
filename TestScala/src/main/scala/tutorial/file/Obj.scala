package tutorial.file

object Obj extends App {
  class Student(val name: String, age: Int) {
    def sayHello(userName: String): Unit = {
      println(s"Hello, $userName")
    }

    def sayHello(): String = {
      val answer = "You were greeted!"
      answer
    }
  }

  val student = new Student("Alex", 18)
  println(student.name)
}
