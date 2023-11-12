# Country Details API
This API is used to get the Details of a country.

## Prerequisites
 You should have installed [python3](https://www.python.org/downloads/) and [Git](https://www.git-scm.com/downloads)

## Installation
1. Clone the project from GitHub
    ```git
    git clone https://github.com/koushikromel/fluvi-task3.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```py
    uvicorn main:app --host 0.0.0.0 --port 3000
    ```

## Endpoints
1. Get the Country Data
    Get the Country Details by country_code
    -   Method: GET
    -   Endpoint: http://0.0.0.0:3000/country/{country_code}
    -   Parameters:
        - country_code: str
    -   Request: GET /country/in
    -   Response: 
        ```json
            {
                "top_level_domain": [
                    ".in"
                ],
                "alpha2_code": "IN",
                "alpha3_code": "IND",
                "currencies": [
                    {
                    "code": "INR",
                    "name": "Indian rupee",
                    "symbol": "₹"
                    }
                ],
                "capital": "New Delhi",
                "calling_codes": [
                    "91"
                ],
                .
                .
                .
                .
                "regional_blocs": [
                    {
                    "acronym": "SAARC",
                    "name": "South Asian Association for Regional Cooperation"
                    }
                ],
                "cioc": "IND"
            }
        ```

## License
This Project is licensed under the MIT License - see the [License](https://choosealicense.com/licenses/mit/) file for details.