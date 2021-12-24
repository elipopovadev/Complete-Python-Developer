object[] objects = { "Thomas", 31, 5.02, null, "Joey" };
var result = objects.OfType<string>();
foreach (var item in result)
{
    Console.WriteLine(item);
}
