import os, requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP('serp-hotels')


serp_url = "https://serpapi.com/search"
serp_api_key = os.getenv("SERP_API_KEY")

@mcp.tool()
def search_hotels(q: Annotated[str, Field(description='Parameter defines the search query. You can use anything that you would use in a regular Google Hotels search.')],
                 check_in_date: Annotated[str, Field(description='Parameter defines the check-in date. The format is YYYY-MM-DD. e.g. 2025-06-26')],
                 check_out_date: Annotated[str, Field(description='Parameter defines the check-out date. The format is YYYY-MM-DD. e.g. 2025-06-27')],
                 currency: Annotated[Union[str, None], Field(description="Parameter defines the currency of the returned prices. Default to USD. Head to the Google Travel Currencies page for a full list of supported currency codes.")] = None,
                 adults: Annotated[Union[int, None], Field(description="Parameter defines the number of adults. Default to 2.")] = None,
                 children: Annotated[Union[int, None], Field(description="Parameter defines the number of children. Default to 0.")] = None,
                 children_ages: Annotated[Union[str, None], Field(description="Parameter defines the ages of children. The age range is from 1 to 17, with children who haven't reached 1 year old being considered as 1. Example for single child only: 5. Example for multiple children (seperated by comma ,): 5,8,10. The number of children's ages specified must match the children.")] = None,
                 sort_by: Annotated[Union[int, None], Field(description="Parameter is used for sorting the results. Default is sort by Relevance. Available options: 3 - Lowest price, 8 - Highest rating, 13 - Most reviewed")] = None,
                 min_price: Annotated[Union[float, None], Field(description="Parameter defines the lower bound of price range.")] = None,
                 max_price: Annotated[Union[float, None], Field(description="Parameter defines the upper bound of price range.")] = None,
                 property_types: Annotated[Union[str, None], Field(description="Parameter defines to include only certain type of property in the results. Head to the Google Hotels Property Types page for a full list of supported Hotels property types. For Vacation Rentals, please refer to the Google Vacation Rentals Property Types page for a full list of supported Vacation Rentals property types. Example for single property type only: 17. Example for multiple property types (seperated by comma ,): 17,12,18")] = None,
                 amenities: Annotated[Union[str, None], Field(description="Parameter defines to include only results that offer specified amenities. Head to the Google Hotels Amenities page for a full list of supported Hotels amenities. For Vacation Rentals, please refer to the Google Vacation Rentals Amenities page for a full list of supported Vacation Rentals amenities. Example for single amenity only: 35. Example for multiple amenities (seperated by comma ,): 35,9,19")] = None,
                 rating: Annotated[Union[int, None], Field(description="Parameter is used for filtering the results to certain rating. Available options: 7 - 3.5+, 8 - 4.0+, 9 - 4.5+")] = None,
                 brands: Annotated[Union[str, None], Field(description="Parameter defines the brands where you want your search to be concentrated. ID values are accessible inside brands array, located in our JSON output (e.g. brands[0].id). Example for single brand only: 33. Example for multiple brands (seperated by comma ,): 33,67,101. This parameter isn't available for Vacation Rentals.")] = None,
                 hotel_class: Annotated[Union[str, None], Field(description="Parameter defines to include only certain hotel class in the results. Available options: 2 - 2-star, 3 - 3-star, 4 - 4-star, 5 - 5-star. Example for single hotel class only: 2. Example for multiple hotel class (seperated by comma ,): 2,3,4. This parameter isn't available for Vacation Rentals.")] = None,
                 free_cancellation: Annotated[Union[bool, None], Field(description="Parameter defines to show results that offer free cancellation. This parameter isn't available for Vacation Rentals.")] = None,
                 special_offers: Annotated[Union[bool, None], Field(description="Parameter defines to show results that have special offers. This parameter isn't available for Vacation Rentals.")] = None,
                 eco_certified: Annotated[Union[bool, None], Field(description="Parameter defines to show results that are eco certified. This parameter isn't available for Vacation Rentals.")] = None,
                 vacation_rentals: Annotated[Union[bool, None], Field(description="Parameter defines to search for Vacation Rentals results. Default search is for Hotels.")] = None,
                 bedrooms: Annotated[Union[int, None], Field(description="Parameter defines the minimum number of bedrooms. Default to 0. This parameter only available for Vacation Rentals.")] = None,
                 bathrooms: Annotated[Union[int, None], Field(description="Parameter defines the minimum number of bathrooms. Default to 0. This parameter only available for Vacation Rentals.")] = None,
                 next_page_token: Annotated[Union[str, None], Field(description="Parameter defines the next page token. It is used for retrieving the next page results.")] = None,
                 property_token: Annotated[Union[str, None], Field(description="Parameter is used to get property details which consists of name, address, phone, prices, nearby places, and etc. You can find property_token from Google Hotels Properties API.")] = None,
                 no_cache: Annotated[Union[bool, None], Field(description="Parameter will force SerpApi to fetch the Google Hotels results even if a cached version is already present. A cache is served only if the query and all parameters are exactly the same. Cache expires after 1h. Cached searches are free, and are not counted towards your searches per month. It can be set to false (default) to allow results from the cache, or true to disallow results from the cache. no_cache and async parameters should not be used together.")] = None,
                 aasync: Annotated[Union[bool, None], Field(description="Parameter defines the way you want to submit your search to SerpApi. It can be set to false (default) to open an HTTP connection and keep it open until you got your search results, or true to just submit your search to SerpApi and retrieve them later. In this case, you'll need to use our Searches Archive API to retrieve your results. async and no_cache parameters should not be used together.")] = None,
                 zero_trace: Annotated[Union[bool, None], Field(description="Enterprise only. Parameter enables ZeroTrace mode. It can be set to false (default) or true. Enable this mode to skip storing search parameters, search files, and search metadata on our servers. This may make debugging more difficult.")] = None
            ):
    '''Use this tool to search for hotels and vacation rentals with Google Hotels search engine.'''
    payload = {
        'q': q,
        'engine': "google_hotels",
        'api_key': serp_api_key,
        'check_in_date': check_in_date,
        'check_out_date': check_out_date,
        'currency': currency,
        'adults': adults,
        'children': children,
        'children_ages': children_ages,
        'sort_by': sort_by,
        'min_price': min_price,
        'max_price': max_price,
        'property_types': property_types,
        'amenities': amenities,
        'rating': rating,
        'brands': brands,
        'hotel_class': hotel_class,
        'free_cancellation': free_cancellation,
        'special_offers': special_offers,
        'eco_certified': eco_certified,
        'vacation_rentals': vacation_rentals,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'next_page_token': next_page_token,
        'property_token': property_token,
        'no_cache': no_cache,
        'async': aasync,
        'zero_trace': zero_trace
    }
    payload = {k: v for k, v in payload.items() if v is not None}

    response = requests.get(serp_url, params=payload)
    print(response)
    return response.json()

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9998
    mcp.run(transport="stdio")
