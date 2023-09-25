namespace BookOneExamples;
public class Calculator
{
    public decimal Calculate(string expression)
    {
        return RPNEvaluator.CalculateRPN(expression.ToPostfix());
    }
}