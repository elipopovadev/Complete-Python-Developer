string[] names = new string[] { "Eli", "Ana", "Misho" };
IEnumerable<string> result = names.AsEnumerable();
foreach (string name in result)
{
    Console.WriteLine(name);
}

