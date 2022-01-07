var empty = Enumerable.Empty<Student>();
Console.WriteLine(empty.Count()); // 0
Console.WriteLine(empty.GetType().Name); //EmptyPartition`1

public class Student
{
    public int ID { get; set; }
    public string Name { get; set; }
}
