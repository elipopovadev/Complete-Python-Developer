int[] numbers = { 1, 2, 3, 4, };
var result = numbers.ToDictionary(k => k, v => (v % 2) == 1 ? "Odd" : "Even");
foreach (var (k, v) in result)
{
    Console.WriteLine($"{k} is {v}");
}