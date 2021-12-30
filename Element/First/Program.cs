string[] towns = new string[] { "Varna", "Plovdiv", "Sofia" };
string firstTowns = towns.First();
Console.WriteLine(firstTowns); // Varna

string[] mountains = new string[] { "Rila", "Pirin", "Rodopi" };
string firstMountain = mountains.First();
Console.WriteLine(firstMountain); // Rila

string resultWithCurrentLength = towns.First(x => x.Length == 5);
Console.WriteLine(resultWithCurrentLength); // Varna
