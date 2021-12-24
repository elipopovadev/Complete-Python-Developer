int[] numbers = { 1, 2, 3, 4 };
int[] result = numbers.ToArray(); // the result is a new array
foreach (var item in result)
{
    Console.WriteLine(item);
}
