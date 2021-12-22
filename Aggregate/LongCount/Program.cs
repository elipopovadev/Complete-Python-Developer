
Pet[] pets = { new Pet { Name="Barley", Age=8 },
                   new Pet { Name="Boots", Age=4 },
                   new Pet { Name="Whiskers", Age=1 } };

const int Age = 3;
long count = pets.LongCount(pet => pet.Age > Age); // with condition
Console.WriteLine("There are {0} animals over age {1}.", count, Age);

public class Pet
{
    public string Name { get; set; }
    public int Age { get; set; }
}

