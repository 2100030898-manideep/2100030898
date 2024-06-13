from django.http import JsonResponse
import requests
from django.views.decorators.http import require_http_methods
from .config import API_BEARER_TOKEN, ECOMMERCE_API_BASE_URL

@require_http_methods(["GET"])
def fetch_top_products(request, category_name):
    product_count = int(request.GET.get('product_count', 10))
    page_number = int(request.GET.get('page_number', 1))
    min_cost = request.GET.get('min_cost', 0)
    max_cost = request.GET.get('max_cost', 1000000)
    sort_attribute = request.GET.get('sort_attribute', 'price')
    sort_order = request.GET.get('sort_order', 'asc')

    company_list = ["AMZ", "FLP", "SNP", "MYN", "AZO"]
    all_products = []

    for company in company_list:
        request_url = f'{ECOMMERCE_API_BASE_URL}/{company}/categories/{category_name}/products'
        request_params = {
            'top': product_count,
            'minPrice': min_cost,
            'maxPrice': max_cost
        }
        request_headers = {
            'Authorization': f'Bearer {API_BEARER_TOKEN}',
        }

        response = requests.get(request_url, params=request_params, headers=request_headers)
        if response.status_code == 200:
            company_products = response.json()
            for product in company_products:
                product['company'] = company
                product['category'] = category_name
            all_products.extend(company_products)
        else:
            return JsonResponse({'error': f'Failed to fetch products from company {company}'}, status=response.status_code)

    is_reverse_order = sort_order == 'desc'
    all_products = sorted(all_products, key=lambda x: x.get(sort_attribute, 0), reverse=is_reverse_order)

    start_idx = (page_number - 1) * product_count
    end_idx = start_idx + product_count
    paginated_products = all_products[start_idx:end_idx]

    response_payload = {
        'total_products': len(all_products),
        'total_pages': (len(all_products) + product_count - 1) // product_count,
        'current_page': page_number,
        'products': paginated_products
    }

    return JsonResponse(response_payload)

@require_http_methods(["GET"])
def fetch_product_details(request, category_name, product_id):
    company_identifier, product_name = product_id.split('_')

    request_url = f'{ECOMMERCE_API_BASE_URL}/{company_identifier}/categories/{category_name}/products'
    request_headers = {
        'Authorization': f'Bearer {API_BEARER_TOKEN}',
    }

    response = requests.get(request_url, headers=request_headers)
    if response.status_code == 200:
        company_products = response.json()
        for product in company_products:
            if product['productName'] == product_name:
                product['company'] = company_identifier
                product['category'] = category_name
                return JsonResponse(product)
        return JsonResponse({'error': 'Product not found'}, status=404)
    else:
        return JsonResponse({'error': f'Failed to fetch products from company {company_identifier}'}, status=response.status_code)
