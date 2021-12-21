int[] numbers = new int[] { 1, 2, 3, 4 };
int result = numbers.Aggregate((a, b) => a + b);
Console.WriteLine(result); // 10

int[] numbers2 = new int[] { 1, 2, 3, 4 };
int result2 = numbers2.Aggregate((a, b) => a * b);
Console.WriteLine(result2); //24

