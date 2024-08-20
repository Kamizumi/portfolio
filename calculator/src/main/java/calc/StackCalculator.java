package calc;
import java.util.Scanner;
import java.util.Stack;

public class StackCalculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String expression;
        
        while (true) {
            System.out.print("Enter an arithmetic expression (or 'exit' to quit): ");
            expression = scanner.nextLine();
            
            if (expression.equalsIgnoreCase("exit") || expression.equalsIgnoreCase("e")) {
                System.out.println("Exiting the program.");
                break;
            }

            try {
                double result = evaluateExpression(expression);
                System.out.println("The result is: " + result);
            } catch (Exception e) {
                System.out.println("Invalid expression: " + e.getMessage());
            }
        }

        scanner.close();
    }

    public static double evaluateExpression(String expression) {
        Stack<Double> values = new Stack<>();
        Stack<Character> operators = new Stack<>();

        for (int i = 0; i < expression.length(); i++) {
            char ch = expression.charAt(i);

            if (Character.isWhitespace(ch)) {
                continue; // Skip whitespaces
            }

            if (Character.isDigit(ch) || ch == '.') {
                StringBuilder sb = new StringBuilder();
                while (i < expression.length() && (Character.isDigit(expression.charAt(i)) || expression.charAt(i) == '.')) {
                    sb.append(expression.charAt(i++));
                }
                i--; // Decrease the index by 1 because it will be incremented in the next iteration of the loop
                values.push(Double.parseDouble(sb.toString()));
            } else if (ch == '(') {
                operators.push(ch);
            } else if (ch == ')') {
                while (!operators.isEmpty() && operators.peek() != '(') {
                    values.push(applyOperation(operators.pop(), values.pop(), values.pop()));
                }
                operators.pop();
            } else if (isOperator(ch)) {
                while (!operators.isEmpty() && hasPrecedence(ch, operators.peek())) {
                    values.push(applyOperation(operators.pop(), values.pop(), values.pop()));
                }
                operators.push(ch);
            } else {
                throw new IllegalArgumentException("Unsupported character in expression: " + ch);
            }
        }

        while (!operators.isEmpty()) {
            values.push(applyOperation(operators.pop(), values.pop(), values.pop()));
        }

        return values.pop();
    }

    public static boolean isOperator(char ch) {
        return ch == '+' || ch == '-' || ch == '*' || ch == '/';
    }

    public static boolean hasPrecedence(char op1, char op2) {
        if (op2 == '(' || op2 == ')') {
            return false;
        }
        if ((op1 == '*' || op1 == '/') && (op2 == '+' || op2 == '-')) {
            return false;
        }
        return true;
    }

    public static double applyOperation(char operator, double b, double a) {
        switch (operator) {
            case '+':
                return a + b;
            case '-':
                return a - b;
            case '*':
                return a * b;
            case '/':
                if (b == 0) {
                    throw new UnsupportedOperationException("Cannot divide by zero");
                }
                return a / b;
            default:
                throw new UnsupportedOperationException("Unsupported operator: " + operator);
        }
    }
}
