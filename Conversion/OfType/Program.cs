object[] objects = { "Thomas", 31, 5.02, null, "Joey" };
var result = objects.OfType<string>();
foreach (var item in result)
{
    Console.WriteLine(item); // Thomas, Joey
}

object[] objects2 = { "Thomas", 31, 5.02, null, "Joey" };
var result2 = objects2.OfType<int>();
foreach (var item in result2)
{
    Console.WriteLine(item); // 31
}
