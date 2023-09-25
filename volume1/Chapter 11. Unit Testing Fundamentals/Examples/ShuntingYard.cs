using System.Linq;

namespace BookOneExamples;

public static class ShuntingYard
{
    private static readonly Dictionary<string, (string symbol, int precedence, bool rightAssociative)> operators
        = new (string symbol, int precedence, bool rightAssociative)[] {
        ("^", 4, true),
        ("*", 3, false),
        ("/", 3, false),
        ("+", 2, false),
        ("-", 2, false)
    }.ToDictionary(op => op.symbol);

    public static string ToPostfix(this string infix)
    {
        string[] tokens = infix.Split(' ');
        var stack = new Stack<string>();
        var output = new List<string>();
        foreach (string token in tokens)
        {
            if (int.TryParse(token, out _))
            {
                output.Add(token);
                Print(token);
            }
            else if (operators.TryGetValue(token, out var op1))
            {
                while (stack.Count > 0 && operators.TryGetValue(stack.Peek(), out var op2))
                {
                    int c = op1.precedence.CompareTo(op2.precedence);
                    if (c < 0 || !op1.rightAssociative && c <= 0)
                    {
                        output.Add(stack.Pop());
                    }
                    else
                    {
                        break;
                    }
                }
                stack.Push(token);
                Print(token);
            }
            else if (token == "(")
            {
                stack.Push(token);
                Print(token);
            }
            else if (token == ")")
            {
                string top = "";
                while (stack.Count > 0 && (top = stack.Pop()) != "(")
                {
                    output.Add(top);
                }
                if (top != "(")
                {
                    throw new ArgumentException("No matching left parenthesis.");
                }

                Print(token);
            }
        }
        while (stack.Count > 0)
        {
            var top = stack.Pop();
            if (!operators.ContainsKey(top))
            {
                throw new ArgumentException("No matching right parenthesis.");
            }

            output.Add(top);
        }
        Print("pop");
        return string.Join(" ", output);

        void Print(string action)
        {
            Console.WriteLine("{0,-4} {1,-18} {2}", action + ":", $"stack[ {string.Join(" ", stack.Reverse())} ]", $"out[ {string.Join(" ", output)} ]");
        }
    }
}
