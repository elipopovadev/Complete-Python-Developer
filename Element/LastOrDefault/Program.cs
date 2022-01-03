int[] numbers = new int[] {10, 9, 30,40,50,60};
int lastNumber = numbers.LastOrDefault();
Console.WriteLine(lastNumber); // 60

int[] numbers2 = new int[4];
int lastNumber2 = numbers2.LastOrDefault();

int result = numbers.LastOrDefault( x => x <= 10); 
Console.WriteLine(result); // 9