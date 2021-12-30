string[] countries = { "Denmark", "Sweden", "Norway" };
string[] empty = { };

string result1 = countries.FirstOrDefault();
Console.WriteLine(result1); // Denmark

string result2 = empty.FirstOrDefault();
Console.WriteLine(result2); // null
