int[] numbers = new int[] { 1 };
int result = numbers.Single();
Console.WriteLine(result); // 1

int[] numbers2 = new int[] { 1, 2, 3 };
try
{
    int result2 = numbers2.Single();
    Console.WriteLine(result2);
}
catch (Exception e)
{

    Console.WriteLine(e); // System.InvalidOperationException: Sequence contains more than one element
}

int[] empty = new int[] { };
try
{
    Console.WriteLine(empty.Single());
}
catch (Exception e)
{

    Console.WriteLine(e); // System.InvalidOperationException: Sequence contains no elements
}


