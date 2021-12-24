List<string> vegetables = new List<string> { "Cucumber", "Tomato", "Broccoli" };

var result = vegetables.Cast<string>();
foreach (var item in result)
{
    Console.WriteLine(item); // Cucumber, Tomato, Broccoli
}
