"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 3
        expected = 7

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_and_negative(self):
        """Test subtracting negative from positive."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_and_positive(self):
        """Test subtracting positive from negative."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_with_zero(self):
        """Test subtracting zero from a number."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_from_zero(self):
        """Test subtracting a number from zero."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = -5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 5.5
        b = 2.3
        expected = 3.2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        # Arrange
        calc = Calculator()
        a = 4
        b = 5
        expected = 20

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -4
        b = -5
        expected = 20

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_positive_and_negative(self):
        """Test multiplying positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 4
        b = -5
        expected = -20

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_and_positive(self):
        """Test multiplying negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -4
        b = 5
        expected = -20

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_with_zero(self):
        """Test multiplying a number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_zero_with_number(self):
        """Test multiplying zero with a number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 4.0
        expected = 10.0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 2
        expected = 5.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negative_numbers(self):
        """Test dividing two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -10
        b = -2
        expected = 5.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_positive_by_negative(self):
        """Test dividing positive by negative."""
        # Arrange
        calc = Calculator()
        a = 10
        b = -2
        expected = -5.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negative_by_positive(self):
        """Test dividing negative by positive."""
        # Arrange
        calc = Calculator()
        a = -10
        b = 2
        expected = -5.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 0.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 0

        # Act & Assert
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(a, b)

    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 7.5
        b = 2.5
        expected = 3.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestInvalidInputException:
    """Tests for InvalidInputException when values exceed allowed range."""

    # Too large value tests (> 1,000,000)
    def test_add_with_too_large_first_argument(self):
        """Test that add raises InvalidInputException when first argument is too large."""
        # Arrange
        calc = Calculator()
        a = 1000001  # Exceeds MAX_VALUE
        b = 1

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_with_too_large_second_argument(self):
        """Test that add raises InvalidInputException when second argument is too large."""
        # Arrange
        calc = Calculator()
        a = 1
        b = 1000001  # Exceeds MAX_VALUE

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_subtract_with_too_large_value(self):
        """Test that subtract raises InvalidInputException when value is too large."""
        # Arrange
        calc = Calculator()
        a = 1000001  # Exceeds MAX_VALUE
        b = 1

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.subtract(a, b)

    def test_multiply_with_too_large_value(self):
        """Test that multiply raises InvalidInputException when value is too large."""
        # Arrange
        calc = Calculator()
        a = 1000001  # Exceeds MAX_VALUE
        b = 1

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.multiply(a, b)

    def test_divide_with_too_large_value(self):
        """Test that divide raises InvalidInputException when value is too large."""
        # Arrange
        calc = Calculator()
        a = 1000001  # Exceeds MAX_VALUE
        b = 1

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.divide(a, b)

    # Too small value tests (< -1,000,000)
    def test_add_with_too_small_first_argument(self):
        """Test that add raises InvalidInputException when first argument is too small."""
        # Arrange
        calc = Calculator()
        a = -1000001  # Below MIN_VALUE
        b = 1

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_with_too_small_second_argument(self):
        """Test that add raises InvalidInputException when second argument is too small."""
        # Arrange
        calc = Calculator()
        a = 1
        b = -1000001  # Below MIN_VALUE

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_subtract_with_too_small_value(self):
        """Test that subtract raises InvalidInputException when value is too small."""
        # Arrange
        calc = Calculator()
        a = -1000001  # Below MIN_VALUE
        b = 1

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.subtract(a, b)

    def test_multiply_with_too_small_value(self):
        """Test that multiply raises InvalidInputException when value is too small."""
        # Arrange
        calc = Calculator()
        a = -1000001  # Below MIN_VALUE
        b = 1

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.multiply(a, b)

    def test_divide_with_too_small_value(self):
        """Test that divide raises InvalidInputException when value is too small."""
        # Arrange
        calc = Calculator()
        a = -1000001  # Below MIN_VALUE
        b = 1

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.divide(a, b)

    # Boundary value tests (exactly at the limit should be valid)
    def test_add_with_max_value(self):
        """Test that add works with exactly MAX_VALUE."""
        # Arrange
        calc = Calculator()
        a = 1000000  # Exactly MAX_VALUE
        b = 0

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == 1000000

    def test_add_with_min_value(self):
        """Test that add works with exactly MIN_VALUE."""
        # Arrange
        calc = Calculator()
        a = -1000000  # Exactly MIN_VALUE
        b = 0

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == -1000000
