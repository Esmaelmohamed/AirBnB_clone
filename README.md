# Algorithm for BaseModel Operations:

1. **Create a class named BaseModel:**

    ```python
    class BaseModel:
    ```

    - Define the `__init__` method:
        
        ```python
        def __init__(self):
        ```

        - Initialize instance attributes:
            - `id`: a unique identifier generated using `uuid.uuid4()`
            - `created_at`: current datetime
            - `updated_at`: current datetime
        - Set `id`, `created_at`, and `updated_at` attributes.

    - Define the `__str__` method:
        
        ```python
        def __str__(self):
        ```

        - Return a string representation of the instance
