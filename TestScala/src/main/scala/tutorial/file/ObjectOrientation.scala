package tutorial.file

object ObjectOrientation extends App {
  trait Animal{
    def voice(): Unit
  }

  case class MyDinasour(name: String)

  class Dinosaur(val dinoType: String) extends Animal {
    def eat(): Unit = println("I'll eat you!")
    override def voice(): Unit = println("Argrgr!!!")
  }

  val dino = new Dinosaur("Rex")
  println(s"The type of this dino is ${dino.dinoType}")
  dino.eat()
  dino.voice()

  val dino2 = MyDinasour("Ret")

  dino2 match {
    case MyDinasour("Rex") => println("Ok")
    case _ => println("Not ok")
  }

  println(dino.dinoType)

  trait LightDinosaur{
    def sayHi(): Unit
  }

  case class MyNewDinosaur() extends Dinosaur(dinoType = "Bob") with LightDinosaur{
    override def sayHi(): Unit = println("Hi")
  }

  val dino3 = MyNewDinosaur()
  dino3.sayHi()
}
