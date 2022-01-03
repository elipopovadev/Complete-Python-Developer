List<Pet> pets = new List<Pet> { { new Pet("Eli", 10) }, { new Pet("Gosho", 5) } };

foreach (Pet pet in pets.DefaultIfEmpty())
{
    if (pet != null)
    {
        Console.WriteLine(pet.Name); // Eli, Gosho
    }
    else
    {
        throw new Exception("Pet is null");
    }
}


public class Pet
{
    public Pet(string Name, int Age)
    {
        this.Name = Name;
        this.Age = Age;
    }
    public string Name { get; set; }
    public int Age { get; set; }
}
