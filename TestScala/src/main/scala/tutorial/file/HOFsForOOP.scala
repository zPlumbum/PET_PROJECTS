package tutorial.file

object HOFsForOOP extends App {
  class Applicable {
    def apply(x: Int): Int = x + 1
  }

  val applicable = new Applicable
  applicable.apply(1) // 2
  applicable(1) // 2

  //function objects
  val incrementer = new Function1[Int, Int] {
    override def apply(x: Int): Int = x + 1
  }
  incrementer.apply(1) // 2
  incrementer(1) // 2

  // Syntax sugar
  val incrementerAlt = (x: Int) => x + 1 // new Function1[Int, Int] { apply = ... }
  incrementerAlt.apply(2) // 3
  incrementerAlt(2) // 3

  // HOFs
  // Example/exercise
  def nTimes(f: Int => Int, n: Int): Int => Int = {
    if (n <= 0) (x: Int) => x // identity function
    else (x: Int) => nTimes(f, n-1)(f(x))
  }

  /*
    g = nTimes(f, 4)

    nTimes(f, 4) = nTimes(f, 3)(f(x)) = f(f(f(f(x))))
    nTimes(f, 3) = nTimes(f, 2)(f(x)) = f(f(f(x)))
    nTimes(f, 2) = nTimes(f, 1)(f(x)) = f(f(x))
    nTimes(f, 1) = nTimes(f, 0)(f(x)) = f(x)

    nTimes(f, 0) = x
   */
  val func = (x: Int) => x + 1
  val f4 = nTimes(func, 4)
//  val f4Alt = (x: Int) => nTimes(func, 3)(func(x))
  val res = f4(5)

  def nTimesOriginal(f: Function1[Int, Int], n: Int): Function1[Int, Int] =
    if (n <= 0) new Function[Int, Int] { override def apply(x: Int): Int = x } // JVM object
    else new Function1[Int, Int] { override def apply(x: Int): Int = nTimesOriginal(f, n-1).apply(f(x)) }
}
