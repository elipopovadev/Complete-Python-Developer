int[] numbers = new int[] { 1, 2, 3, 4 };
int result = numbers.Aggregate(10, (a, b) => a + b);
Console.WriteLine(result); // 20

int[] numbers2 = new int[] { 1, 2, 3 };
int result2 = numbers2.Aggregate(10, (a, b) => a * b);
Console.WriteLine(result2); // 60

