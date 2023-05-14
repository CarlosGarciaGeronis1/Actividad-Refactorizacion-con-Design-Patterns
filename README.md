# Actividad-Refactorizacion-con-Design-Patterns

The code was refactored using the following design patterns:

Inheritance: The PrintReport class derives from the WebReport class through inheritance. This allows the PrintReport class to reuse code from the WebReport class and add new functionality to format the report for printing.

Overriding: The PrintReport class overrides the format_report() method from the WebReport class. This enables the PrintReport class to modify the report's formatting specifically for printing.

The refactoring of the code was done using the following SOLID principles:

Single Responsibility Principle: The PrintReport class has a single responsibility, which is to format the report for printing. This adheres to the principle of having classes with a single purpose, making the code easier to read and maintain.

Open/Closed Principle: The PrintReport class is open for extension but closed for modification. This means that new features can be added to the class without modifying the existing code. This promotes code reusability and minimizes the risk of introducing bugs.
