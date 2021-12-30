int[] numbers = new int[] { 1, 2, 3, 4, 5, 6, 10, 40 };
int lastNumber = numbers.Last();
Console.WriteLine(lastNumber); // 40

string[] mountains = new string[] { "Mila", "Rila", "Rodopi", "Pirin" };
string lastMountain = mountains.Last();
Console.WriteLine(lastMountain); // Pirin

string resultWithCurrentLength = mountains.Last(x => x.Length == 4);
Console.WriteLine(resultWithCurrentLength); // Rila
