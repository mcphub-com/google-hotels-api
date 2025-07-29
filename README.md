# Aigeon AI Google Hotels API

## Project Description

The Aigeon AI Google Hotels API is a Python-based server application designed to facilitate advanced hotel search capabilities using Google's hotel search features. This application leverages the SerpApi to perform detailed and customizable searches for hotels, providing users with a wide range of parameters to tailor their search results according to specific needs and preferences.

## Features Overview

- **Advanced Hotel Search**: Perform comprehensive hotel searches using a variety of parameters.
- **Customizable Search Criteria**: Tailor search results based on location, dates, price range, amenities, and more.
- **Integration with SerpApi**: Utilizes the SerpApi for fetching and processing hotel search results.
- **Environment Configuration**: Uses environment variables for secure configuration management.

## Main Features and Functionality

The Aigeon AI Google Hotels API offers a robust set of features to perform detailed hotel searches:

- **Search Query Customization**: Specify search queries similar to regular Google Hotels searches.
- **Date Management**: Define check-in and check-out dates with precise formatting.
- **Geographical and Language Preferences**: Set country and language preferences for searches.
- **Currency and Pricing Options**: Choose currency for price display and set price range filters.
- **Occupancy Details**: Specify the number of adults and children, including children's ages.
- **Sorting and Filtering**: Sort results by price, rating, or reviews, and filter by property type, amenities, and rating.
- **Brand and Class Specification**: Focus searches on specific hotel brands or classes.
- **Additional Options**: Include options for free cancellation, special offers, eco-certification, and vacation rentals.
- **Pagination and Property Details**: Manage result pages and access detailed property information.
- **Cache Management**: Control caching behavior to optimize search performance and cost.

## Main Functions Description

### `search_hotels`

This is the core function of the application, enabling users to perform detailed hotel searches. Below are the parameters available for customization:

- **q**: Defines the search query for the hotel search.
- **check_in_date**: Specifies the check-in date in `YYYY-MM-DD` format.
- **check_out_date**: Specifies the check-out date in `YYYY-MM-DD` format.
- **gl**: Sets the country code for the search.
- **hl**: Sets the language code for the search.
- **currency**: Defines the currency for price display.
- **adults**: Specifies the number of adults.
- **children**: Specifies the number of children.
- **children_ages**: Lists the ages of children.
- **sort_by**: Determines the sorting criteria for results.
- **min_price**: Sets the minimum price for filtering results.
- **max_price**: Sets the maximum price for filtering results.
- **property_types**: Filters results by property type.
- **amenities**: Filters results by amenities offered.
- **rating**: Filters results by hotel rating.
- **brands**: Focuses search on specific hotel brands.
- **hotel_class**: Filters results by hotel class.
- **free_cancellation**: Filters results to include only those with free cancellation.
- **special_offers**: Filters results to include only those with special offers.
- **eco_certified**: Filters results to include only eco-certified hotels.
- **vacation_rentals**: Includes vacation rentals in the search.
- **bedrooms**: Sets the minimum number of bedrooms for vacation rentals.
- **bathrooms**: Sets the minimum number of bathrooms for vacation rentals.
- **next_page_token**: Retrieves the next page of results.
- **property_token**: Accesses detailed property information.
- **no_cache**: Controls caching behavior for search results.
- **aasync**: Manages asynchronous search submission.
- **zero_trace**: Enables ZeroTrace mode for enterprise users.

This function provides a comprehensive interface for users to perform highly customized hotel searches, leveraging the power of Google's hotel search capabilities through the SerpApi.