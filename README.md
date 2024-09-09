# Python-testing-Repo
This repository focus on implementing pytest loibrary on a scratch python module

## Key topics under discussion

- Function based tests
    Function-based tests are written as standalone functions that begin with the prefix test_. Each function is 
    treated as an individual test case. This approach is straightforward and easy to understand. You simply define a function, and pytest automatically recognizes it as a test. Each function runs independently, which helps ensure that tests do not interfere with each other. This isolation is benficial for maintaining test carefully.

- Class based tests
    Class-based tests are organized within classes. Each test method within the class also starts with test_. This approach allows you to group related tests together.
    - setup_methods
        The setup method is used to prepare the necessary environment or resources required for the tests to run. This can include initializing variables, setting up database connections, or creating mock objects.
    - teardown methods
        The teardown method is used to clean up any resources or state that were created during the setup phase. This is important to ensure that tests do not interfere with each other and that the environment is reset for subsequent tests.
- Fixtures Decorators
    - confest.py 
        - Centralise Fixture Defininition: allows you to define fixtures that can be used across multiple test files without needing to import them explicitly. 
- marking and Paramterizing
    - tagging test methods
    - parameterized test methods
- Mocking