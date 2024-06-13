# Django Microservices Project

This Django project implements two microservices:

1. **Average Calculator Microservice**:
    - Calculates the average of numbers fetched from a test server based on specific criteria (prime, Fibonacci, even, random).
    - Exposes a REST API to fetch numbers and their average.
    - Implements sliding window functionality to store a limited number of recent numbers.
    - Ensures quick responses and handles errors gracefully.
    
2. **E-commerce Microservice**:
    - Fetches top products and product details from an external e-commerce API.
    - Implements endpoints to fetch top products based on category and retrieve product details by ID.
    - Provides options to filter and sort products.
    
## Problem-1: Average Calculator Microservice

### Features:
- Fetches numbers from the test server based on specific criteria: prime, Fibonacci, even, random.
- Stores fetched numbers in a sliding window, ensuring uniqueness and limited window size.
- Calculates the average of numbers in the current window.
- Handles errors gracefully and ensures quick responses.
  
### Endpoints:
- **GET /numbers/{numberid}**: Fetches numbers from the test server based on the specified criteria.
    - Parameters: 
        - `numberid`: Identifier for the type of numbers to fetch ('p' for prime, 'f' for Fibonacci, 'e' for even, 'r' for random).
    - Returns:
        - JSON response containing fetched numbers, previous and current window state, and the average.
        
## Problem-2: E-commerce Microservice

### Features:
- Fetches top products and product details from an external e-commerce API.
- Provides options to filter and sort products based on price and other attributes.
- Retrieves product details by ID and category.

### Endpoints:
- **GET /categories/{category_name}/products**: Fetches top products from the e-commerce API based on the specified category.
    - Parameters:
        - `category_name`: Name of the product category.
        - Query Parameters:
            - `product_count`: Number of products to fetch (default: 10).
            - `min_cost`: Minimum product price (default: 0).
            - `max_cost`: Maximum product price (default: 1000000).
            - `sort_attribute`: Attribute to sort products by (default: 'price').
            - `sort_order`: Sort order ('asc' for ascending, 'desc' for descending, default: 'asc').
    - Returns:
        - JSON response containing top products based on the provided criteria.

- **GET /categories/{category_name}/products/{product_id}**: Fetches details of a specific product by its ID and category.
    - Parameters:
        - `category_name`: Name of the product category.
        - `product_id`: ID of the product in the format "{company_identifier}_{product_name}" (e.g., "AMZ_iPhone13").
    - Returns:
        - JSON response containing details of the specified product.

## Screenshots:
Problem-1: Average Calculator Microservice
![image](https://github.com/2100030898-manideep/2100030898/assets/110282076/fb7e9fb7-8b0c-4157-bc73-d6deb9563340)
![image](https://github.com/2100030898-manideep/2100030898/assets/110282076/70991eb3-b402-4c93-af2f-d1b35b635b6e)
![image](https://github.com/2100030898-manideep/2100030898/assets/110282076/6013ba2c-778f-4d28-a9bb-6cd0f6895331)
![image](https://github.com/2100030898-manideep/2100030898/assets/110282076/173575d2-2b39-4f17-9c76-890d5dc14b58)
![image](https://github.com/2100030898-manideep/2100030898/assets/110282076/326040cd-4cba-404f-a805-4a5c2fbc3b47)
![image](https://github.com/2100030898-manideep/2100030898/assets/110282076/d3ee24f4-8f2a-402c-a18b-9c51290416a4)
![image](https://github.com/2100030898-manideep/2100030898/assets/110282076/d8c268b3-47dc-4daa-93ad-c5a6ac633d51)
![image](https://github.com/2100030898-manideep/2100030898/assets/110282076/c47f522d-fb90-4db4-bdd4-7cb74f5d763b)

Problem-2: E-commerce Microservice
![image](https://github.com/2100030898-manideep/2100030898/assets/110282076/70dfdced-530f-410e-81b9-fcd6a7382c98)
![image](https://github.com/2100030898-manideep/2100030898/assets/110282076/64f558a7-0367-4342-a131-45f1f316a7e4)
![image](https://github.com/2100030898-manideep/2100030898/assets/110282076/3845525b-f1be-44d2-a05a-d198c1c349d7)
![image](https://github.com/2100030898-manideep/2100030898/assets/110282076/363059aa-a07c-43de-8c00-ff8a4a845d82)

## Dependencies:
- Django
- Requests

## Setup:
1. Clone the repository: `git clone https://github.com/your_username/your_repository.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

## Contribution:
Contributions are welcome! Please create a pull request for any enhancements or bug fixes.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
