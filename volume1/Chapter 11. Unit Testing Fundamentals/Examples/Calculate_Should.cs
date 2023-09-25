using NUnit.Framework;

namespace BookOneExamples;

[TestFixture]
public class Calculate_Should
{
    [Test]
    public void ExpressionCalculatedCorrectly_When_ContainsAllOperations()
    {
        // Arrange
        string expression = "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3";
        var calculator = new Calculator();

        // Act
        decimal actualResult = calculator.Calculate(expression);

        // Assert
        Assert.AreEqual(3.0001220703125, actualResult);
    }

    [Test]
    public void ExpressionCalculatedCorrectly_When_ContainsOnlyAdditionTwoSingleNumberedOperands()
    {
        // Arrange
        string expression = "5 + 4";
        var calculator = new Calculator();

        // Act
        decimal actualResult = calculator.Calculate(expression);

        // Assert
        Assert.AreEqual(9, actualResult);
    }

    [Test]
    public void ExpressionCalculatedCorrectly_When_ContainsOnlyAdditionTwoMultipleNumberedOperands()
    {
        // Arrange
        string expression = "51 + 489";
        var calculator = new Calculator();

        // Act
        decimal actualResult = calculator.Calculate(expression);

        // Assert
        Assert.AreEqual(540, actualResult);
    }
}