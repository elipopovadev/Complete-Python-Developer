int[] numbers = new int[] { 1 };
int result = numbers.SingleOrDefault();
Console.WriteLine(result); // 1

int[] numbers2 = new int[] { 1, 2, 3 };
try
{
    int result2 = numbers2.SingleOrDefault();
    Console.WriteLine(result2);
}
catch (Exception e)
{

    Console.WriteLine(e); // System.InvalidOperationException: Sequence contains more than one element
}

int[] empty = { };
Console.WriteLine(empty.SingleOrDefault()); // 0

string[] emptyString = { };
Console.WriteLine(emptyString.SingleOrDefault()); // null


