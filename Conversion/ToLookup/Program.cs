List <Employee> employees = new List<Employee>();
Employee first = new Employee(1, 20, "Gosho", 'M');
Employee second = new Employee(2, 24, "Pesho", 'M');
Employee third = new Employee(3, 25, "Andrei", 'M');
Employee fourth = new Employee(4, 30, "Mina", 'F');

employees.Add(first);
employees.Add(second);
employees.Add(third);   
employees.Add(fourth);

var details = employees.ToLookup(x => x.Gender);
foreach (var detail in details)
{
    Console.WriteLine(detail.Key);
    foreach (var employee in detail)
    {
        Console.WriteLine(employee.Name);
    }
}



public class Employee
{
    public Employee(int ID, int Age, string Name, char Gender)
    {
        this.ID = ID;
        this.Age = Age;
        this.Name = Name;
        this.Gender = Gender;
    }

    public int ID { get; set; }
    public int Age { get; set; }
    public string Name { get; set; }
    public char Gender { get; set; }

}