string[] colors = { "Red", "Green", "Blue" };
string result = colors.ElementAtOrDefault(0);
string result2 = colors.ElementAtOrDefault(10);
string result3 = colors.ElementAtOrDefault(1);
Console.WriteLine(result); // Red
Console.WriteLine(result2); // NULL
Console.WriteLine(result3); // Green